import os
from PyPDF2 import PdfReader
import pprint
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print(f"Usage {sys.argv[0]} <pdf-filename>")
    sys.exit(-1)
if not os.path.isfile(filename):
    print(f"**** Error: file does not exist {filename}")
    os.exit(-1)

reader = PdfReader(filename)

meta = reader.metadata

pprint.pprint(meta)
