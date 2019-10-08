import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')

print(r.status_code)
print("---")
print(r.headers)
print("---")
for item in r.json():
    print(item)