#!/bin/bash

CORE_DIR=$(echo $0 | sed -u "s/reload.sh//g")
VENV_PATH=$(echo "${CORE_DIR}../../venv/bin/python3")
MNG_PATH=$(echo "${CORE_DIR}../manage.py")
FIXT_PATH=$(echo "${CORE_DIR}cache/fixtures/all.json")

function reload_fixtures() {
    $VENV_PATH $MNG_PATH loaddata $FIXT_PATH
    $VENV_PATH $MNG_PATH makemigrations
    $VENV_PATH $MNG_PATH migrate
}

reload_fixtures
