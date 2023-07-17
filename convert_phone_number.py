"""
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a 
dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Write the function "convert_phone_number" to 
complete this task.

The regular expression r"\b(\d{3})-(\d{3})-(\d{4})\b" consists of the following components:

\b is a word boundary to ensure the phone number is a separate word.
(\d{3}) captures the first three digits.
- matches the dash.
(\d{3}) captures the next three digits.
- matches the dash.
(\d{4}) captures the last four digits.
\b is another word boundary to ensure the matched substring is a separate word.
In re.sub(), the first argument is the regular expression pattern, the second argument r"(\1) \2-\3" is the replacement string. 
Here, \1, \2, and \3 refer to the content matched by the capturing groups, representing the three sets of digits.

"""

import re
def convert_phone_number(phone):
  regex = r"\b(\d{3})-(\d{3})-(\d{4})\b"
  result = re.sub(regex, r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300