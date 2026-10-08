words = ['Communication', 'transportation', 'lateness', 'come', 'prosperity', 'call']
def longest_word(words):
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest, len(longest)
    
print(longest_word(words))
