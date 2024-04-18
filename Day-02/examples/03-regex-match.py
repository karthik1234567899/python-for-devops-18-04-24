# In this it just search for the word quick in the text, if the quick is io the 1st line of the text, then it pass otherwise it will show as no match"
import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
