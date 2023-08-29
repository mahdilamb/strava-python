#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

apt install curl wget default-jre nodejs npm -y
apt install npm -y

npm install @openapitools/openapi-generator-cli

rm -rf ./strava_python;
rm setup.py requirements.txt;
npx openapi-generator-cli generate -i https://developers.strava.com/swagger/swagger.json -g python -o . --skip-validate-spec --enable-post-process-file --package-name strava_python
python3 ./scripts/finalize_package.py

cp scripts/auth.py strava_python/
OWNER=${SUDO_USER:-$(whoami)}
chown -R $OWNER:$OWNER .
cat scripts/.gitignore >> .gitignore
cp scripts/README.md README.md
rm git_push.sh 
