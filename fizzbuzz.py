# -*- coding:utf-8 -*-
def main():
    for i in range(1, 31):
        print(f'{i}:', int(not (i % 3)) * 'Fizz' + int(not (i % 5)) * 'Buzz' or i)


if __name__ == '__main__':
    main()
