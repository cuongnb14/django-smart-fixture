
#! /bin/bash

PROJECT_NAME=smart_fixture

echo "Downloading project ${PROJECT_NAME}..."
git clone --depth 1 https://github.com/cuongnb14/django-smart-fixture.git /tmp/smart_fixture
mv -f /tmp/smart_fixture/${PROJECT_NAME} .
rm -rf /tmp/smart_fixture