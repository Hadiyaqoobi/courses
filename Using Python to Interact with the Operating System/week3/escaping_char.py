import re

#\ is used for escaping characters

print(re.search(r".come" , "welcome"))

print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "mydomain.com"))
