#!/usr/bin/env bash
set -e
set -x

python3 -m venv dist/venv
source dist/venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install -r build_requirements.txt
shiv --site-packages venv/lib/python3.10/site-packages \
        --compressed \
        -o caffeine \
        -e caffeine.__main__:main src/ \
        --upgrade