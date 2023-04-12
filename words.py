def print_upper_words(list):
    """Search for e in each word of the list, print out the proper words in uppercase"""
    for word in list:
       if "e" in word:
           print(word.upper())


print_upper_words(['hello', 'meowmix', 'kittens', 'go', 'chicken'])
