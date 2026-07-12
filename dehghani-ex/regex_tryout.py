import re

str = "start regex"

print(f'the regex pattern is=[{re.search('start', str).span()}]')

text = "Python is great 123434"
text1 = "12w3434"
result = re.search(r"\s", text)
print(result.start())

print(re.fullmatch(r"\d+", text1))