import os

from jinja2 import Environment, FileSystemLoader

url = os.environ.get("CHECKMARX_SERVER")
username = os.environ.get("CHECKMARX_USERNAME")
password = os.environ.get("CHECKMARX_PASSWORD")

loader = FileSystemLoader("/")
jinja_env = Environment(loader=loader)
template = jinja_env.get_template("config_template.txt")

config_path = f"{os.getcwd()}/config.ini"
os.environ["checkmarx_config_path"] = config_path

with open(config_path, "w") as config:
    config.write(template.render(base_url=url, username=username, password=password))
