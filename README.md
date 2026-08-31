# GOOD

General Open Orbital Dynamics platform project.

This repository contains the source of the internal GOOD Developer Portal. The
portal is a living Development Plan and Developer User Manual assembled from
version-controlled project documentation, source-code reference, and approved
project documents.

## Build the documentation

Python 3.11 or newer is required.

```console
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/requirements.txt
make docs
```

Open `build/html/index.html` after the build. Before proposing a change, run:

```console
make docs-check
```

The documentation sources, contributor guidance, source registries, and
governance rules are under [`docs/`](docs/index.md). Documentation-agent rules
are in [`AGENTS.md`](AGENTS.md).
