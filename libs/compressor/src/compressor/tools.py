def compress(data: str) -> str:
    """Compress the input string by removing whitespace."""
    return "".join(data.split())


def get_np_version() -> str:
    """Return the version of numpy installed."""
    import numpy as np

    return np.__version__
