# Author: SMR 12/10/21
def letter_counter(word, letter):

    amount = 0 
    for x in list(word):
        if(x == letter):
            amount += 1
        else:
            continue
    return amount
print(letter_counter("cat", "t") == 1)
print(letter_counter("apple", "p") == 2)
print(letter_counter("supercalifragilisticexpialidocious", "i") == 7)