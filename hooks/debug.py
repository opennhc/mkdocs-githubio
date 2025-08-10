import sys
import os

for path in sys.path:
    print("sys path:", path)

import material
print("material file:", os.path.abspath(material.__file__))

import material.extensions
print("extensions file:", os.path.abspath(material.extensions.__file__))