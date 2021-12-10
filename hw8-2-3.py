# Author: SMR 12/10/21
def three_letter_words(lst):
    leng = 0
    for word in lst:
        if(len(word) == 3):
            leng += 1
        else:
            continue
    return leng
print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)