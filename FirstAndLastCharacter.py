text = "Generation"
def first_last(text):
    if len(text) < 2:
        return ""

    return text[0:2] + text[-2:]

print(first_last(text))
