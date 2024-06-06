import requests
url = 'https://example.com/data'
response = requests.get(url, stream=True)
lst = response.iter_lines(chunk_size=512, decode_unicode=False)
for line in lst:
    if line:
        print(line)
