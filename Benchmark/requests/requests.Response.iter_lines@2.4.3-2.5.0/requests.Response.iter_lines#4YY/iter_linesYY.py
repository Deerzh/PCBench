import requests
url = 'https://example.com/data'
response = requests.get(url, stream=True)
lst = response.iter_lines(512,  False)
for line in lst:
    if line:
        print(line)
