# Purpose

This repo is the code used by our self hosted github runners to allow users from the github actions workflows to tag a checkmarx project with a platform tag. This code uses the [CheckmarxPythonSDK](https://github.com/checkmarx-ts/checkmarx-python-sdk) library in order to interact with our checkmarx server and run api calls pythonically.

## Prerequisites
* Python3
* Pip (for python3)

## Installation
As mentioned, the purpose of this is to be used with our aws self hosted runners. It is currently being used in our user-data.sh script in the [code to deploy aws scalable ec2 instances](https://github.com/asurion-private/github-actions-secure-pipeline-byos/blob/main/configuration_files/userdata.sh)
```
curl -kL 'https://raw.githubusercontent.com/csravelar/checkmarx_tag/main/install.sh' | bash -sl
```
The line above grabs the install.sh script text in this repo and then pipes that to bash to be run as commands. The install.sh script runs the commands in order necessary to install the program and ensure its dependencies are available.

Note:
> This install script assumes Amazon Linux based AMI is being used. If you're using a different image you may need to make minor tweaks like checking python3 is installed and replacing yum with whatever package manager is being used

## How it works
First run the install script. It will place this repo in the /usr/local/bin/checkmarx_tag folder and an alias is created for executing entrypoint.sh as checkmarx_tag 

This should allow users running github actions on the runners with this installed repo to simply enter
```
checkmarx_tag
```
in the command line to run the program and tag the project with the platform tag.

However, you will need to specify the following environment variables to the environment

```
CHECKMARX_SERVER
CHECKMARX_USERNAME
CHECKMARX_PASSWORD
PROJECT_NAME
TEAM_NAME
PLATFORM_TAG
```
You can use githubs secrets settings in the repo to securely store this info and then pass it to github workflows env section for this step. More information on those can be found here:

[How to pass environment variables in github actions](https://docs.github.com/en/actions/reference/environment-variables#about-environment-variables)

[How to create secrets in github](https://docs.github.com/en/actions/reference/encrypted-secrets)
