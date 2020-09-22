# Organizing Larger Program
Run the following command under module_demo directory

# sys.path and PYTHONPATH environment variable
list of directories Python searches for modules
```
print(sys.path)
sys.path.append(module_directory)
```

# Packages
* Packages are modules that contain other modules
* Packages are generally implemented as directories containing a special \_\_init__.py file 

import package
```python
import reader_package
```
reader_package/\_\_init__.py should be executed


import reader.py from reader_package
```python
import reader_package.reader
r = reader_package.reader.Reader('main.py')
r.read()
r.close()
```

Uncompress file
```python
import reader_package.reader
r = reader_package.reader.Reader('test.bz2')
r.read()
r.close()
```

# Subpackages
compressed is a subpackage/directory
```python
import reader_package.compressed
import reader_package.compressed.bzipped

```

run in command line
```bash
python3 -m reader_package.compressed.bzipped test.bz2 data compressed with bz2
```


# Relative imports
* Relative can reduce typing in deeply nested package structures
* Can aid package renaming and refactoring
 
```python
from .b import B
```

# \_\_file__
\_\_file__ is the pathname of the file from which the module was loaded


# \_\_all__
\_\_all__ is a list of public objects of that module, as interpreted by import *. 

It overrides the default of hiding everything that begins with an underscore.

# Namespace packages 
* Split packages across several directories
* Namespace package have on \_\_init__.py
* This avoids complex initialization ordering problems
```python
import sys
sys.path.extend(['path1'],['path2'])
import split_package
split_package.__path__

```

# Executable Directories
## \_\_main.py__
## executable zip file
zip file containing an entry point for Python execution