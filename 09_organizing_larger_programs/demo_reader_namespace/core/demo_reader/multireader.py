# demo_reader/multireader.py

import importlib
import os
import pkgutil

import demo_reader.compressed


# Namespace package argument ns_pkg
# Finds all sub packages
# Ensure absolute package names
def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(
        ns_pkg.__path__,
        ns_pkg.__name__ + ".")


# Build set of module objects
# Import them with importlib
# Find modules to import with iter_namespace
compression_plugins = {
    importlib.import_module(module_name)
    for _, module_name, _ in iter_namespace(demo_reader.compressed)
}


# Build extension_map dict comprehension
# Look for module-level attributes
# Get modules from compression_plugins
extension_map = {
    module.extension: module.opener
    for module in compression_plugins
}


class MultiReader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()