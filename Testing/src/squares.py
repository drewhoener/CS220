import math


def squares(area):
    numbers = []
    while area > 3:
        for i in range(area, 2, -1):
            sqrt = int(math.sqrt(i))
            if sqrt * sqrt == i:
                area -= i
                numbers.append(i)
                break
    for i in range(area):
        numbers.append(1)
    return numbers


if __name__ == '__main__':
    print(squares(12))
