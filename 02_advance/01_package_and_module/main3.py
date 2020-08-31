import reader_package.reader

r = reader_package.reader.Reader('test.bz2')
print(r.read())
r.close()

gr = reader_package.reader.Reader('test.gz')
print(gr.read())
gr.close()
