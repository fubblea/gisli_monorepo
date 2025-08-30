import numpy as np
from compressor.tools import compress
from nicegui import ui


def main():
    arr = np.array([1, 2, 3, 4, 5])
    ui.label(f"Numpy array: {arr}")
    ui.label(f"Array mean: {np.mean(arr)}")
    ui.label(f"Compressed string: '{compress('  Hello   World  ')}'")


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(native=True)
