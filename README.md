# Gisli Monorepo

## Update Requirements Lock Files

Per Python Version if it's different

`bazelisk run //requirements:requirements_3_13.update`

## Build Targets

For all targets:

`bazelisk build //...`

## Running Targets

`bazelist run //<target>`

Targets are also compiled to `bazel-bin/` folder