#!/bin/bash

CORE_DIR=$(echo $0 | sed -u "s/wipe.sh//g")
VENV_PATH=$(echo "${CORE_DIR}../../../venv/bin/python3")
MNG_PATH=$(echo "${CORE_DIR}../../manage.py")

function wipe_database() {
    $VENV_PATH $MNG_PATH shell -c "\
from app.models import \
Division, Category, Position;\
Division.objects.all().delete();\
Category.objects.all().delete();\
Position.objects.all().delete();"
}

wipe_database
