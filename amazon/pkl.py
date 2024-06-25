import pickle
import os

save = True
base_dir = 'agi'

# random seed
seed = 2023
data_path = 'amazon'

# def save_pkl(path, map_dict):
#     full_path = path.format(base_dir, data_path)
#     if not os.path.exists(full_path):
#         os.makedirs(full_path)
#     with open(full_path, 'wb') as fs:
#         pickle.dump(map_dict, fs)

user_org2remap_dict = {}
user_org2remap_dict_inv = {}
item_org2remap_dict = {}
item_org2remap_dict_inv = {}

# if save:
#     save_pkl("{}/{}/remap_dict/user_org2remap_dict.pkl", user_org2remap_dict)
#     save_pkl("{}/{}/remap_dict/user_org2remap_dict_inv.pkl", user_org2remap_dict_inv)
#     save_pkl("{}/{}/remap_dict/item_org2remap_dict.pkl", item_org2remap_dict)
#     save_pkl("{}/{}/remap_dict/item_org2remap_dict_inv.pkl", item_org2remap_dict_inv)

import os

# save as pickle file
## remap_dict
# if save:
#     full_path = "{}/{}/remap_dict".format(base_dir, data_path)
#     if not os.path.exists(full_path):
#         os.makedirs(full_path)

# with open("{}/{}/remap_dict/user_org2remap_dict.pkl".format(base_dir, data_path), 'wb') as fs:
#     pickle.dump(user_org2remap_dict, fs)
# with open("{}/{}/remap_dict/user_org2remap_dict_inv.pkl".format(base_dir, data_path), 'wb') as fs:
#     pickle.dump(user_org2remap_dict_inv, fs)

# with open("{}/{}/remap_dict/item_org2remap_dict.pkl".format(base_dir, data_path), 'wb') as fs:
#     pickle.dump(item_org2remap_dict, fs)
# with open("{}/{}/remap_dict/item_org2remap_dict_inv.pkl".format(base_dir, data_path), 'wb') as fs:
#     pickle.dump(item_org2remap_dict_inv, fs)

if save:
    full_path = "{}/{}/data".format(base_dir, data_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)