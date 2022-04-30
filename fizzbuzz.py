# -*- coding:utf-8 -*-
def fizzbuzz(n):
    for i in range(1, n):
        print(f"{i}:", (i % 3 == 0) * "Fizz" + (i % 5 == 0) * "Buzz" or i)
