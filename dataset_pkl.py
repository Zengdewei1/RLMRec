import pickle

# 打开.pkl文件
def load(pkl):
    with open(pkl, 'rb') as file:
        # 使用pickle.load()函数加载对象
        data = pickle.load(file)
    return data


# data = load('agi/amazon/data/dataset.pkl')
# print(data.keys())
# print(data['train'].shape)
# print(len(data['reviews'].keys()))
# print(len(data['item_description'].keys()))
# print(data['n_user'])
# print(data['n_item'])
"""
(11056, 13338)
11056
12177
11056
13338
dict_keys(['n_user', 'n_item', 'train', 'test', 'val', 'reviews', 'item_description'])
"""

# data = load('agi/amazon/remap_dict/item_org2remap_dict.pkl')
# print(len(data.keys()))
# print(list(data.keys())[:20])
# print(data['0345803493'])
"""
13338
['0345803493', '0345803507', '0373039549', '0373730489', '0373795424', '0615824404', '0985334541', '0985817003', '1477502378', '1612187145', 'B008YA0A30', '1484067894', '1484068769', '1484068963', '0988191237', '1477588779', '1493569724', '149607923X', 'B004SBO41S', 'B005S1XTEA']
0
"""

data = load('agi/amazon/remap_dict/item_org2remap_dict_inv.pkl')
print(len(data.keys()))
print(list(data.keys())[:10])
print(data[0])
"""
13338
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0345803493
"""

