"""
Run this program to create your config.ini file that checkmarxpythonsdk
needs to use to authenticate with the api
"""
import os
import pathlib

from jinja2 import Environment, FileSystemLoader


def main():
    base_url = os.environ["cxServer"]
    username = os.environ["cxUsername"]
    password = os.environ["cxPassword"]

    # Tell jinja where in the filesytem we are going to read a file from
    cwd_path = str(pathlib.Path(__file__).parent.absolute())
    loader = FileSystemLoader(cwd_path)
    jinja_env = Environment(loader=loader)
    template = jinja_env.get_template("config_template.txt")

    with open("config.ini", "w") as config:
        config.write(
            template.render(base_url=base_url, username=username, password=password)
        )


if __name__ == "__main__":
    main()
