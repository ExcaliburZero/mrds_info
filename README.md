# mrds_info

## Development
```bash
uv venv --python 3.13
uv pip install .

cd docs
make html
```

### Auto-update html on changes
```bash
uv run sphinx-autobuild docs docs/_build/html
```