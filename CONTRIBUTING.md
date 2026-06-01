# Contributing to SNIN

Thank you for considering contributing to SNIN V5 Mesh Fabric! We welcome
contributions of all kinds — code, documentation, bug reports, feature requests.

## How to Contribute

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/snin.git
cd snin
pip install -e .
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

### 3. Run Tests
```bash
python -m pytest tests/ -v
```
All tests must pass before submitting.

### 4. Lint
```bash
pip install ruff
python -m ruff check src/snin/
```

### 5. Commit & Push
Use clear commit messages:
- `feat: add DHT bootstrap from seed nodes`
- `fix: handle orjson bytes in nostr_bridge`
- `docs: update CHANGELOG for v5.0.0`

### 6. Open a Pull Request
Against the `main` branch. Describe what changed and why.

## Code Style
- Python 3.10+ type hints encouraged
- 100 char line limit
- No `sys.path.insert` hacks — use proper imports
- All configuration via `SNIN_*` environment variables
- No secrets in code

## Reporting Issues
Open a GitHub issue with:
- SNIN version (`python -c "from snin import __version__; print(__version__)"`)
- Python version
- Full traceback if applicable
- Steps to reproduce
