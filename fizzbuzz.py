# -*- coding:utf-8 -*-
def main():
    for i in range(1, 31):
        print(f"{i}:", (i % 3 == 0) * "Fizz" + (i % 5 == 0) * "Buzz" or i)


if __name__ == "__main__":
    main()
