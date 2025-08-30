set shell := ["powershell.exe", "-c"]

create-venv:
    uv venv .venv
    .venv/Scripts/activate

update-deps:
    bazelisk run //requirements:requirements_3_13.update
    uv pip install -r requirements/requirements_lock_3_13.txt

install: create-venv update-deps

build-all:
    bazelisk build //...
    
build-all-with-update: update-deps build-all