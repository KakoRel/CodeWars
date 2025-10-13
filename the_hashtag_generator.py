"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
-It must start with a hashtag (#).
-All words must have their first letter capitalized.
-If the final result is longer than 140 chars it must return false.
-If the input or the result is an empty string it must return false.
"""

def generate_hashtag(s):
    m = []
    m = str(s).split()
    hashtag_str = '#'
    
    if len(m) == 0 or (sum(len(i) for i in m)) + 1 > 140:
        return False
    
    for word in m:
        hashtag_str += word[0].replace(word[0], word[0].upper()) + word[1:len(word)].lower()
        print(word[0])
    
    return hashtag_str

print(generate_hashtag("" ))