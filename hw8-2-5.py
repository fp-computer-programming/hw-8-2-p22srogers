# Author: SMR 12/10/21
def sum_odds_exclusive(numbers):
    num = 0
    for number in numbers:
        if(number % 2 == 0):
            num += number
            continue
        else:
            break
    return num

print(sum_odds_exclusive([2, 4, 6, 8, 9]) == 20)
print(sum_odds_exclusive([13, 12, 10]) == 0)
print(sum_odds_exclusive([14, 16, 32]) == 62)