from compressor.tools import compress, get_np_version


def main():
    print(f"Compressed string: '{compress('  Hello   World  ')}'")
    print(f"Numpy version: {get_np_version()}")


if __name__ in {"__main__", "__mp_main__"}:
    main()
