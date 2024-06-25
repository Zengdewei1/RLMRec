import pickle

# 打开.pkl文件
def load(pkl):
    with open(pkl, 'rb') as file:
        # 使用pickle.load()函数加载对象
        data = pickle.load(file)
    return data

# data = load('data/amazon/itm_emb_np.pkl')
# print(data.shape)
# (9332, 1536)

# data = load('data/amazon/usr_emb_np.pkl')
# print(data.shape)
# (11000, 1536)

# data = load('data/amazon/usr_prf.pkl')
# print(len(data.keys()))
# print(data[0])
# 11000
# {'profile': 'This user enjoys reading heart-warming romance novels with relatable characters, sweet storylines, and family dynamics. They seem to like stories about second-chances, rebuilding trust, and starting over in relationships. They prefer books with well-developed characters, witty dialogue, and unexpected turns. However, they may not enjoy books with far-fetched ideas.', 'reasoning': "Based on the user's reviews of the purchased books, they provided positive feedback on the heart-warming romance novels they read and enjoyed. They also mentioned enjoying the relatable characters and family dynamics. Additionally, they mentioned Bernadette's writing style and Brenda Jackson's ability to tell a story. Based on their reviews and book descriptions, it is evident that they prefer books with themes of second-chances, rebuilding trust, and family bonds. However, they may not enjoy books with far-fetched ideas and unrealistic plots."}

# data = load('data/amazon/itm_prf.pkl')
# print(len(data.keys()))
# print(data[0])
"""
9332
{'profile': 'Romance novel enthusiasts who enjoy tales of rebuilding trust and starting over in relationships would enjoy this book. Those who have a fascination with the concept of family dynamics and internal struggles would also be intrigued by What a Westmoreland Wants. The book explores themes of trust, deceit, forgiveness, and family bonds, which can appeal to readers who have experienced similar situations in their own lives or seek to witness it in a fictional setting.', 'reasoning': "The book's plot revolves around Gemma Westmoreland who is struggling to rebuild trust with her new administrative assistant after discovering the latter embezzled $20,000 from her business. Additionally, Callum, her brother's friend, is trying to convince Gemma of his love but must overcome the barrier of Ramsey's protectiveness over his younger sister. The book details Gemma's internal struggles and family dynamics, providing an interesting and relatable narrative for readers with similar experiences or interests in these themes. Moreover, the book can appeal to romance enthusiasts as it explores the matters of the heart, including forgiveness and starting over in relationships."}
"""

# data = load('data/amazon/trn_mat.pkl')
# print(data.shape)
"""
(11000, 9332)
(10999, 1270) 1.0
(10999, 8544) 1.0
"""

# data = load('data/amazon/tst_mat.pkl')
# print(data.shape)
# print(data)
"""
(11000, 9332)
(10999, 1223) 1.0
(10999, 6335) 1.0
"""

data = load('data/amazon/val_mat.pkl')
print(data.shape)
print(data)
"""
(11000, 9332)
(10998, 2680) 1.0
(10999, 4052) 1.0
(10999, 3019) 1.0
"""

"""
amazon_item.json
{"iid": 9330, "asin": "1400073480"}
{"iid": 9331, "asin": "0849947251"}
"""

"""
amazon_user.json
{"uid": 10998, "reviewerID": "A37ES8MT922M6L"}
{"uid": 10999, "reviewerID": "A1PI91NSG468T8"}
"""

