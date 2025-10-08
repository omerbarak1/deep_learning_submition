# Auto-generated driver that executes split notebook cells in order.
# Runs **operational** cells only, preserving logic & sequence via a shared context.
import importlib, pkgutil
from pathlib import Path

def main():
    ctx = {}
    # Dynamically import all nb_cells modules in lexical order (cell_001, cell_002, ...)
    import nb_cells as cells_pkg
    pkg_path = Path(cells_pkg.__file__).parent
    modules = sorted([m.name for m in pkgutil.iter_modules([str(pkg_path)]) if m.name.startswith("cell_")])
    for name in modules:
        mod = importlib.import_module(f"nb_cells." + name)
        if hasattr(mod, "run"):
            ctx = mod.run(ctx)
    return ctx

if __name__ == "__main__":
    main()
