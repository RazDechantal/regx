"""
The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins 
with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, 
we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also 
want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). 
Write a function called "transform_comments" for that. 

The transform_comments function uses the replace() method to perform the required replacements on the given comment.

comment.replace("###", "//") replaces occurrences of "###" with "//".
comment.replace("##", "//") replaces occurrences of "##" with "//".
comment.replace("#", "//", 1) replaces the first occurrence of "#" with "//". The 1 argument limits the replacement to only the first occurrence.

"""

import re
def transform_comments(comment):
  result = comment.replace("###", "//").replace("##", "//").replace("#", "//", 1)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"