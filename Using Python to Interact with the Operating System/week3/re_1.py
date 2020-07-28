import re

result = re.search(r"aza",  "plaza")
print(result)

result_1 = re.search(r"aza", "bazaar")
print(result_1)
result_2 = re.search(r"aza", "maze")
print(result_2)

print("---------------------------------")

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))


print("---------------------------------")

print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))


print("Match the word cat either dog ")

print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I like dog"))
print(re.search(r"cat|dog", "I like dog and cats"))
print(re.findall(r"cat|dog", "I like both dogs and cats"))

