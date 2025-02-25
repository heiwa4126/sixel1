import sys

from sixel import converter

c = converter.SixelConverter("foo.png")
c.write(sys.stdout)
