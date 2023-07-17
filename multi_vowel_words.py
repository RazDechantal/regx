"""
The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

The regular expression r"\b\w*[aeiou]{3,}\w*\b" consists of the following components:

\b is a word boundary to match the start or end of a word.
\w* matches zero or more word characters (letters, digits, or underscores).
[aeiou]{3,} matches 3 or more consecutive vowels (a, e, i, o, u) in a case-insensitive manner.
\w* matches zero or more word characters (letters, digits, or underscores).
\b is another word boundary to ensure the matched substring is a separate word.
re.IGNORECASE is used as a flag in re.findall() to perform a case-insensitive match.

"""

import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []