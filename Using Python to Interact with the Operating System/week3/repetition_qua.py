import re

# We are looking for a letter that reapeted 5 times

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))


# To find all mactches

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost apeared"))
