# learn-flyte

 Repository to record Flyte Learning journey

## Setup

```bash
poetry install
poetry shell
```

## Hello World

```bash
cd workflows
pyflyte run hello_world.py hello_world_wf
pyflyte run hello_world.py hello_world_wf --name Ming
```

## Standard Scale

```bash
python standard_scale.py
```

or

```bash
pyflyte run standard_scale.py standard_scale_workflow --values '[1.0,2.0,3.0,4.0]'
```

## Standard Scale with Submodule

```bash
pyflyte run standard_scale_with_subworkflow.py workflow_with_subworkflow --num_samples 10 --seed 3
```

## Standard Scale with Launch Plan

At ./learn-flyte root:

```bash
python -m workflows.standard_scale_launchplan
```

or

At ./learn-flyte/workflows:

```bash
pyflyte run standard_scale_launchplan.py workflow_with_launchplan --num_samples 10 --seed 3
```

## Local Cluster

Works only on Linux:

```bash
curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
export FLYTECTL_CONFIG=~/.flyte/config-sandbox.yaml
flytectl demo start
flytectl create project \
      --id "my-project" \
      --labels "my-label=my-project" \
      --description "My Flyte project" \
      --name "My project"

pyflyte run --remote -p my-project -d development example.py wf --name Ada
```

### Register workflows

For single workflow, local testing:

```bash
pyflyte register workflows
```

Production setting:

```bash
pyflyte --pkgs workflows package

flytectl register files \
    --project my-project \
    --domain development \
    --archive flyte-package.tgz \
    --version "$(git rev-parse HEAD)"
```
