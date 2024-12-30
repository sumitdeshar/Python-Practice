#remove vowel from string(sentence).
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

#tip
def smash(words):
    return " ".join(words)
#tip is that join can iterate over a list if you pass a list and ' ' blackspace here is applied after each iteration. 