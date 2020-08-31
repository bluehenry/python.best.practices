# Moduels
* Python's basic tool for organizing code
* Normally a single Python source file
* Load models with import
* Represented by module objects

### Importing models
```python
import x
from x import y
from x import y as z
```

# Packages
* A package is just a special type of module, that can contain other modules or packages.
* A package is a directory containing \__init__.py
* Packages are generally directories. Modules are generally files,
* Packages have \__path__, but modules don't.
* In the following case urllib is a package, and urllib.request is a module.
```python
>>> import urllib
>>> import urllib.request
>>> type(urllib)
<class 'module'>
>>> type(urllib.request)
<class 'module'>
```
* import sub-module
```python
from urllib import request
```


# Locating Modules
## sys.path
* sys.path is a list of directories, that controls module search
* It is initialized from PYTHONPATH
* Searched in order im import
* First match provides module
* ImportError when there is no match
```python
import sys
sys.path
```

## PYTHONPATH
* Environment variable
* List of paths added to sys.path
* Windows
```bash
set PYTHONPATH=path1;path2;path3
```
*Linux/macOS
```bash
export PYTHONPATH=path1:path2:path3
```
# MultReader
```bash
python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
python -m demo_reader.compressed.gzipped test.gz data compressed with gzip

```
```python
from demo_reader.multireader import MultiReader
r = MultiReader('test.bz2')
r.read()
r.close()

r = MultiReader('test.gz')
r.read()
r.close()
```

# Relative Imports
* Relative imports can only be used to import modules within the current top-level package
* Can reduce typing in deeply nested package structures
* Promote a certain form of modifiability
* In general, prefer absolute imports
```python
from ..module_name import name
```

# \__all__
* Module-level attribute
* Controls from module import * behavior
* If not specified, import all public names
* Must be a list of strings. Each entry is a name to import.
* We recommended avoiding import * in general
```python
from pprint import pprint
from demo_reader.compressed import *
pprint(locals())

```

# Namespace packages
[PEP 420 -- Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)
* Namespace packages are a mechanism for splitting a single Python package across multiple directories on disk. 
* Namespace packages may not have \__init__.py

## Namespace package Discovery Algrithm
* Scan each directory in sys.path
* Import standard package if found
* import standard module if found
* Otherwise, all matching directories contribute to a namespace package

```python
import sys
sys.path.extend(['./path1', './path2'])
import demo_reader
demo_reader.__path__
import demo_reader.util
import demo_reader.compressed
demo_reader.util.__path__

```

## Executable Directories
* You can execute a directory if it contains \__main__.py
* \__main__.py will be executed
```bash
python multi-reader-program test.bz2
```

## Executable Zip Files
* The zip file contains the same contents as the directory, not the directory itself
```bash
python -m zipfile -c ../multi-reader-program.zip *
python multi-reader-program.zip test.bz2
```

## Executable Packages
* Using \__main__.py in Packages
* The -m tells Python to treat it as a module
* \__main__.py is a submodule of the directory package
```bash
python -m demo_reader test.bz2
```

# Recommended Python Project Layouts
* README.rst should be in project root. Often refers to docs directory.
* THe src directory ensures that you develop against installed versions of your packages.
* Usually don't want tests installed with package 

## Extending Packages with Plugins
* Packages define extension points
* Extensions are implemented outside the package
* Extensions are discovered at runtime
* Two methods
    * Namespace packages and [pkgutil](https://docs.python.org/3/library/pkgutil.html) 
    * setuptools entry points

### Implementing Plugins with setuptools Entry Points
* Define extension points using setuptools
* Plugins add to extension points in setup.py
* Core package iterates over plugins added to extension points


# Distributing Packages
* Archive of package contents
* Easy to install
* Various formats
    * Zip files
    * Tarballs
    * [Wheels](https://pythonwheels.com/)
    
## Built Packages
* Placed directly into installation directory
* Build results are included in the package
* Can be platform-specific
* Use the wheel format defined in PEP 427
```bash
pip install wheel
python setup.py bdist_wheel
pip install dist/demo_reader-1.0.0-py3-none-any.whl

```

## Source Packages
* Contains everything needed to build the package
* Cannot be placed directly into installation directory
* It is necessary to build the package before installing it
```bash
python setup.py sdist
pip install demo_reader-1.0.0.tar.gz
```


## Uploading Packages to a Package Server
* [PyPi.org](https://pypi.org/)
* Use [twine](https://pypi.org/project/twine/) to upload packages
```bash
twine upload dist/demo_reader-1.0.0-py3-none-any.whl
```