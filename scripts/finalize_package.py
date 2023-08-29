import functools
import glob
import re
import shutil

ADDITIONAL_REQUIREMENTS = [
    "oauthlib @ git+https://github.com/oauthlib/oauthlib.git",
    "python-dotenv",
    "requests",
]
PACKAGE_NAME = "strava_python"

def update_requirements():
    requirements = str(ADDITIONAL_REQUIREMENTS)[1:-1].replace("'","\"")
    with open("setup.py", "r") as r_fp:
        replacement = re.sub(r"((?:\n|.)*REQUIRES.*?=.*?\[(?:\n|.)*?)(?:\s*,\s*)?(\](?:\n|.)*)", fr'\1, {requirements}\2', r_fp.read(),flags=re.M)
        with open("setup.py", "+w") as w_fp:
            w_fp.write(replacement)
    with open("requirements.txt" ,"a") as fp:
        for requirement in ADDITIONAL_REQUIREMENTS:
            fp.write(requirement + "\n")

update_requirements()
