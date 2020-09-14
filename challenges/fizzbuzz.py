def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            tuple_one = (f'{i} % 15 == 0', 'FizzBuzz')
            print(tuple_one)
        elif i % 5 == 0:
            tuple_two = (f'{i} % 5 == 0', 'Buzz')
            print(tuple_two)
        elif i % 3 == 0:
            tuple_three = (f'{i} % 3 == 0', 'Fizz')
            print(tuple_three)
        else:
            print(i)
​
fizzbuzz(100)