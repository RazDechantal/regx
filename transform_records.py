"""
We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role 
field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the 
phone number. Write a function called "transform_record" in which the regular expression, uses groups to do that.

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))

Should print "Sabrina Green,+1-802-867-5309,System Administrator"

The transform_record function uses re.sub() to substitute the matched phone number pattern with the modified format.

The regular expression (\b\d{3}-\d{3}-\d{4}\b) consists of the following components:

(\b\d{3}-\d{3}-\d{4}\b) defines a capturing group with parentheses that matches the pattern of a phone number in the format "###-###-####" 
where '#' represents a digit.
\b is a word boundary to ensure the phone number is a separate word.
In re.sub(), the first argument is the regular expression pattern, the second argument r"+1-\1" is the replacement string. Here, \1 refers 
to the content matched by the capturing group, representing the phone number.
"""
import re
def transform_record(record):
  regex = r"(\b\d{3}-\d{3}-\d{4}\b)"
  new_record = re.sub(regex, r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer