#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') -> 'eodc'
#front_back('a') -> 'a'
#front_back('ab') -> 'ba'

def front_back(str):
    if len(str) <= 1:
        return str
    if len(str) == 2:
        first = str[0]
        second = str[1]
        return second + first
    else:
        first = str[0]
        num = len(str)-1
        last = str[num]
        return last + str[1:num] + first

print front_back('code')
print front_back('a')
print front_back('ab')
