# Gisli Monorepo

## Setup

- Install bazelisk
- Install uv
- Install just

## Commands

### Create a Python venv

`just install`

Run all bazelisk commands in this venv

### Update Requirements Lock Files

`just update-deps`

### Build Targets

`just build-all`

Build all with update reqs:

`just build-all-with-update`

### Running Targets

`bazelist run //<target>`

Targets are compiled to `bazel-bin/` folder