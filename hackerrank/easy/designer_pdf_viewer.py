
def designerPdfViewer(h, word): 
    wordIndexDictionary = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24, 
        'y': 25,
        'z': 26,
    }

    wordList = list(word)
    wordHeights = [0] * len(wordList) 
    i = 0
    for x in wordList:
        wordHeights[i] = h[wordIndexDictionary[x] - 1]
        i += 1

    maxHeight = wordHeights[0]
    for i in range(len(wordHeights)):
        if wordHeights[i] > maxHeight:
            maxHeight = wordHeights[i]
    
    return maxHeight * len(wordList)



definedHeights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(designerPdfViewer(definedHeights, 'zxc'))