# Tutorial dari https://youtu.be/9N6a-VLBa2I

import json
from urllib.request import urlopen

webApi = 'https://jsonplaceholder.typicode.com/todos'

with urlopen(webApi) as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))