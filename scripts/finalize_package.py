import glob
import re
import shutil

ADDITIONAL_REQUIREMENTS = [
    "oauthlib @ git+https://github.com/oauthlib/oauthlib.git",
    "python-dotenv",
    "requests",
    "pydantic"
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

def rename_package():
    with open("setup.py", "r") as r_fp:
        replacement = re.sub(r"^NAME\s*=\s*(.*?)$", fr'NAME = "{PACKAGE_NAME}"', r_fp.read(),flags=re.M)
        with open("setup.py", "+w") as w_fp:
            w_fp.write(replacement)
    
    pattern = re.compile(r"(.*?import\s*|.*?from\s*|.*?getattr\(\s*)(swagger_client)", re.MULTILINE)
    for file in glob.glob("swagger_client/**/*.py", recursive=True):

        with open(file,"r") as fp:
            updated  =pattern.sub(rf"\1{PACKAGE_NAME}", fp.read())
            with open(file, "+w") as w_fp:
                w_fp.write(updated)
    shutil.move("swagger_client", PACKAGE_NAME)

update_requirements()
rename_package()
