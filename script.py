import os
import sys
from github import Github
from helper_classes import MissingRepoNameException

ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']

g = Github(ACCESS_TOKEN)

if len(sys.argv) < 2:
    raise MissingRepoNameException()

# create a github repo with the given name

user = g.get_user()

try:
    repo = user.create_repo(sys.argv[1])
except:
    print('Repo creation failed.')
    quit()
else:
    print(f"Repo with name {sys.argv[1]} created!")

# make a README.md
repo.create_file('README.md', "initial commit", f"# {sys.argv[1].title()}")
print('README CREATED')

# cd to the right folder
# print(f'CURRENT DIR: {os.}')
# clone the repo
# initialize a git repo
