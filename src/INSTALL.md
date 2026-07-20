# Installation & dependency patches

This project needs Python 3.12+ and the following packages:

- `gymnasium` ≥ 1.0
- `numpy` ≥ 1.26
- `torch` ≥ 2.1
- `torch-geometric` ≥ 2.5
- `brevitas` ≥ 0.12

## Standard install (via `uv`)

```bash
cd Policy4FONDRL2BNN
uv venv
uv pip install -e .
```

## Known issue: Brevitas vs the `_dependencies` package on Python 3.14

Brevitas 0.12.x depends (transitively) on the `_dependencies` injector package.
The newest `_dependencies` releases reject class names that start and end with
double underscores, but Brevitas builds several internal classes with dunder
names.  Until upstream Brevitas resolves this, apply the following one-line
patch to the installed file.

The error you would otherwise see is:

```
_dependencies.exceptions.DependencyError: Magic methods are not allowed
```

### Patch (apply once after install)

Edit the file
`/path/to/your-venv/lib/python3.X/site-packages/_dependencies/checks/injector.py`
and rewrite the `_check_dunder_name` body to a no-op:

```python
def _check_dunder_name(name):
    # Patched locally for Brevitas 0.12.x compatibility.
    return
```

This file is included in this repo for reference: `_patches/injector.py`.

## Quick verification

```bash
python -c "from brevitas.nn import QuantLinear; import torch; \
  m = QuantLinear(4, 4, weight_bit_width=1); \
  print(m(torch.zeros(1, 4)).shape)"
```

You should see `(torch.Size([1, 4]))` and no `DependencyError`.
