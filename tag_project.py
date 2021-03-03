import json
import os
import sys

import requests
from CheckmarxPythonSDK.CxRestAPISDK import ProjectsAPI
from CheckmarxPythonSDK.CxRestAPISDK.sast.projects.dto.customFields import CxCustomField


def check_valid_platform_tag(platform_tag):
    """Check the user supplied platform tag against cloudgov tags to ensure validity"""
    response = json.loads(
        requests.get("https://cloudgov.asurion.com/api/1/tags", verify=False).text
    )
    # Sanity check against any possible changes to the cloudgov platform that the second element
    # in the response json is still a list of platform values
    if response[1]["Key"].lower() == "platform":
        valid_platform_tags = response[1]["Values"]
    # All platform tags in cloudgov are complete uppercase which lends itself to straight comparison
    if not platform_tag.strip().upper() in valid_platform_tags:
        return False
    return True


def main():
    project_name = os.environ["cxProject"]
    team_name = os.environ["cxTeam"]
    platform_tag = os.environ["cxPlatformTag"]

    project_api = ProjectsAPI()
    project_id = project_api.get_project_id_by_project_name_and_team_full_name(
        project_name, team_name
    )
    if not project_id:
        sys.exit(
            f"Your project {project_name} with team name {team_name} does not exist in checkmarx"
        )

    if not check_valid_platform_tag(platform_tag):
        sys.exit(f"You're platform tag {platform_tag} doesn't exist in cloudgov")

    # Get all the project details to update the project along with the new custom field
    project_details = project_api.get_project_details_by_id(project_id)
    # Get a custom field object to update project with.
    # In the object we set the custom_field_id to 1 to let it know we are referring to platform_tag
    # And we set the name to the platform_tag name we want to give it
    custom_fields = [CxCustomField.CxCustomField(custom_field_id=1, name=platform_tag)]
    # Update the project with the project attributes and platform tag custom_field
    project_api.update_project_by_id(
        project_id=project_details.project_id,
        project_name=project_details.name,
        team_id=project_details.team_id,
        custom_fields=custom_fields[0],
    )


if __name__ == "__main__":
    main()
