PYTHON ?= python3
SPHINXBUILD ?= sphinx-build
DOCS_SOURCE := docs
DOCS_BUILD := build

.PHONY: docs docs-check docs-clean docs-linkcheck docs-pdf registry manifest

docs: registry
	$(SPHINXBUILD) -b html $(DOCS_SOURCE) $(DOCS_BUILD)/html
	$(PYTHON) tools/write_build_manifest.py --output $(DOCS_BUILD)/build-manifest.json

docs-check: registry
	$(PYTHON) tools/validate_documentation.py
	$(SPHINXBUILD) -W --keep-going -b html $(DOCS_SOURCE) $(DOCS_BUILD)/html
	$(PYTHON) tools/write_build_manifest.py --output $(DOCS_BUILD)/build-manifest.json

docs-linkcheck: registry
	$(SPHINXBUILD) -b linkcheck $(DOCS_SOURCE) $(DOCS_BUILD)/linkcheck

docs-pdf: registry
	$(SPHINXBUILD) -M latexpdf $(DOCS_SOURCE) $(DOCS_BUILD)

registry:
	$(PYTHON) tools/render_source_registry.py

manifest:
	$(PYTHON) tools/write_build_manifest.py --output $(DOCS_BUILD)/build-manifest.json

docs-clean:
	$(SPHINXBUILD) -M clean $(DOCS_SOURCE) $(DOCS_BUILD)

