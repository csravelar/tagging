import json
import pathlib
import os
import sys

import requests

os.environ["checkmarx_config_path"] = f"{str(pathlib.Path(__file__).parent.absolute())}/config.ini"

from CheckmarxPythonSDK.CxRestAPISDK import ProjectsAPI
from CheckmarxPythonSDK.CxRestAPISDK.sast.projects.dto.customFields import CxCustomField


def check_valid_platform_tag(platform_tag):
    """Check the user supplied platform tag against cloudgov tags to ensure validity"""
    response = json.loads(requests.get("https://cloudgov.asurion.com/api/1/tags", verify=False).text)
    # Sanity check against any possible changes to the cloudgov platform that the second element
    # in the response json is still a list of platform values
    if response[1]["Key"].lower() == "platform":
        valid_platform_tags = response[1]["Values"]
    # All platform tags in cloudgov are complete uppercase which lends itself to straight comparison
    if not platform_tag.strip().upper() in valid_platform_tags:
        return False
    return True


def get_project_info(project_name):
    """Get all projects that exist in checkmarx confirm we can match the user input."""
    projects = get_all_projects_id_name()
    for project in projects:
        # Compare strings after we set them both to lowercase and strip user input of spaces
        if project["ProjectName"].lower() == project_name.strip().lower():
            return project
    return None


def main():
    project_name = os.environ["PROJECT_NAME"]
    platform_tag = os.environ["PLATFORM_TAG"]

    project = get_project_info(project_name)
    if not project:
        sys.exit(f"Your project {project} does not exist in checkmarx")

    if not check_valid_platform_tag(platform_tag):
        sys.exit(f"You're platform tag {platform_tag} doesn't exist in cloudgov")

    projects_api = ProjectsAPI()
    # Get all the project details to update the project along with the new custom field
    project_details = projects_api.get_project_details_by_id(project["ProjectId"])
    # Get a custom field object to update project with.
    # In the object we set the custom_field_id to 1 to let it know we are referring to platform_tag
    # And we set the name to the platform_tag name we want to give it
    custom_fields = [CxCustomField.CxCustomField(custom_field_id=1, name=platform_tag)]
    # Update the project with the project attributes and platform tag custom_field
    projects_api.update_project_by_id(
        project_id=project_details.project_id,
        project_name=project_details.name,
        team_id=project_details.team_id,
        custom_fields=custom_fields[0],
    )

if __name__ == '__main__':
    main()
