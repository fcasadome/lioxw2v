import os


# recursively find files with a given extension
def get_files(path, extension):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith(extension):
                yield os.path.join(root, f)
