import json

def install_sort(package):
    return package['analytics']['30d']

with open('packages_info.json', 'r') as f:
    data = json.load(f)
    
# menggunakan list comprehension
data = [item for item in data if 'video' in item['desc']] # list semua item yang ada video didalam deskripsi

data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data, indent=2)

print(data_str)