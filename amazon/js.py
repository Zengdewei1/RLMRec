import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)

for l in parse('./data.json.gz'):
  print(l)