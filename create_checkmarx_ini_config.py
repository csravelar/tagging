import os
import pathlib

from jinja2 import Environment, FileSystemLoader

url = os.environ["CHECKMARX_SERVER"]
username = os.environ["CHECKMARX_USERNAME"]
password = os.environ["CHECKMARX_PASSWORD"]

cwd_path = str(pathlib.Path(__file__).parent.absolute())
loader = FileSystemLoader(cwd_path)
jinja_env = Environment(loader=loader)
template = jinja_env.get_template("config_template.txt")

with open("config.ini", "w") as config:
    config.write(template.render(base_url=url, username=username, password=password))
