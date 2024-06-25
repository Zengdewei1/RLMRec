
from tqdm import tqdm
import json
import gzip

data_path = 'amazon'
review_data_path = data_path + '/origin/reviews_Books.json.gz'
meta_data_path = data_path + '/origin/meta_Books.json.gz'

def parse_meta(path):
  with gzip.open(path, 'r') as g:
    for l in g:
        yield eval(l.replace(b'\n', b''))


metas = []
for l in tqdm(parse_meta(meta_data_path), desc='读取meta文件'):
    metas.append(l)

# load meta data
cnt = 0
item_description = {}
for i in tqdm(range(len(metas)), desc='处理meta数据'):
    # data = json.loads(json.dumps(eval(metas[i].replace('\n', ''))))
    data = metas[i]
print(metas[0])