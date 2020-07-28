'''Add to the regular expression used in the extract_pid function, to return the uppercase message in
parenthesis, after the process id.'''

import re
def extract_pid(log_line):
    x = re.search(r"\[(\d+)\]: ([A-Z]*)", log_line)
    if x is None:
        return None
    return "{} ({})".format(x[1], x[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# REGEX EXPLANATION
# find the number that is inside the square brackets:
# \d finds numbers from 0-9
# \d+ finds repetition of \d, if there is one or more occurrences in the text
# [\d+] I need the number inside []
# \[\d+\] I need the litteral meaning of square brackets, so I use \ before each bracket

# find the uppercase word after :whitespace
# : [A-Z]
# : [A-Z]* , the star repetition qualifier finds zero or more occurrences in the text
# whole regex is \[\d+\]: [A-Z]*
# if I try to print here i get the match '[12345]: ERROR' from 1st text, which I do not want

# now I will create 2 capturing groups by placing parentheses
# I place 1st () around \d+ to eventually retrieve only the number and not the square brackets!
# I place 2nd () around [A-Z]* to eventually retrieve only the uppercase word and not the : and the whitespace
# later I will use x[1] to retrieve \d+ match
# and I will use x[2] to retrieve [A-Z]* match