import os

from jinja2 import Environment, FileSystemLoader

url = os.environ.get("CHECKMARX_SERVER")
username = os.environ.get("CHECKMARX_USERNAME")
password = os.environ.get("CHECKMARX_PASSWORD")

loader = FileSystemLoader(".")
jinja_env = Environment(loader=loader)
template = jinja_env.get_template("config_template.txt")

with open("/root/.Checkmarx/config.ini", "w") as config:
    config.write(template.render(base_url=url, username=username, password=password))