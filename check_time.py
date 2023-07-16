""" 
The check_time function takes a time string as input and uses a regular expression to match the time against 
the specified pattern. If the time matches the pattern, the function returns True; otherwise, it returns False.
"""

import re
def check_time(text):
  #pattern = r"^([1-9]|0?[1-9]):([0-5][0-9])([ap]m|AM|PM)$"
  pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])\s*([ap]m|AM|PM)$"
  #pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])\s*(AM|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False