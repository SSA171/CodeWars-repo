def square_digits(num):
    y = [x for x in str(num)]
    answer = []
    for i in y:
        g = int(i)**2
        answer += str(g)
    return int("".join(answer))

print(square_digits(9119))


