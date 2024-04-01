def esolution(text, ending):
    return text.endswith(ending)

def ssolution(text, starting):
    return text.startswith(starting)

print(ssolution('sumit', 's'))