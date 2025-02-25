import sys

from sixel import converter


def main():
    c = converter.SixelConverter("example/foo.png")
    c.write(sys.stdout)


if __name__ == "__main__":
    main()
