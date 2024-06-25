import gzip
import json

input_file = './data.json'  # 输入的JSON文件名
output_file = './data.json.gz'  # 输出的压缩文件名

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)

