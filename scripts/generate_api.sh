#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

apt install curl wget default-jre -y

MOST_RECENT_VERSION=$(curl -s  https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/maven-metadata.xml 2>&1 |  sed -En "s/<version>([0-9]*\.[0-9]*\.[0-9]*)<\/version>/\1/pm" | tail -n 1 | xargs echo -n)

echo $MOST_RECENT_VERSION
DOWNLOAD_PATH=https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/$MOST_RECENT_VERSION/swagger-codegen-cli-$MOST_RECENT_VERSION.jar
echo "Downloading $DOWNLOAD_PATH..."
wget -O swagger-codegen-cli.jar $DOWNLOAD_PATH

rm -rf ./strava_python;
rm setup.py requirements.txt;
java -jar swagger-codegen-cli.jar generate --input-spec https://developers.strava.com/swagger/swagger.json --lang python
python3 ./scripts/finalize_package.py
rm swagger-codegen-cli.jar
cp scripts/auth.py strava_python/
OWNER=${SUDO_USER:-$(whoami)}
chown -R $OWNER:$OWNER strava_python
cat scripts/.gitignore >> .gitignore
cp scripts/README.md README.md
rm git_push.sh 
