# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

ace_of_spades = "Ace of Spades"
In [33]: ace_of_spades[::-1]
Out[33]: 'sedapS fo ecA'
_______________________________________

my_str = input('Enter a string: ')
temp = ''
for char in my_str:
    temp = char + temp
print(temp)


string = input('Type something in to have it reversed: ' )
​_______________________________________
def reverse(string):
    reversed_string = ''
    for i in reversed(string):
        reversed_string += i
    print ('Your string, reversed: ', reversed_string)
reverse(string)
​
def reverse_again(string):
    # using range with (start index, end index, step )
    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    print(result)
reverse_again(string)
