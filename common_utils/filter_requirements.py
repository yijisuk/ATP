import sys

for line in sys.stdin:
    package = line.split(" @")[0]
    print(package)