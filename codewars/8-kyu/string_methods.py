def remove_exclamation_marks(s):
    # Replace all exclamation marks in the string with an empty string
    return s.replace('!', '')

input_string = "Hello! This is an example string with some exclamation marks!"
output_string = remove_exclamation_marks(input_string)
print(output_string)  # Output: Hello This is an example string with some exclamation marks


#use of split method
#syntax
#string.split(separator, maxsplit)
sentence = "This is a sentence"
words = sentence.split()  # Split the sentence by whitespace
print(words)  # Output: ['This', 'is', 'a', 'sentence']

#When using method like split that generates two output and we pass a var it automatically becomes a list
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
