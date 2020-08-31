# absolute imports
from reader_package.reader import Reader

r = Reader('test.bz2')
print(r.read())
r.close()

gr = Reader('test.gz')
print(gr.read())
gr.close()
