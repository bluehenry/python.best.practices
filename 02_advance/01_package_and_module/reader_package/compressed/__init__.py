# append module_demo folder into sys.path() or add it in PYTHONPATH
from reader_package.compressed.bzipped import opener as bz2_opener
from reader_package.compressed.gzipped import opener as gzip_opener

print('reader_package/compressed subpackage is imported')

__all__ = ['bz2_opener', 'gzip_opener']
