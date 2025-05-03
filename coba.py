def solution(str):
    return str[::-1]


def digitize(n):
    hasil1 = str(n)
    hasil2 = solution(hasil1)
    guesses = []
    for i in hasil2:
        guesses.append(int(i), )
    print(guesses)

digitize(35231)


# def digitize(n):
#     guesses = []
#     while n > 0:
#         hasil = n % 10
#         n //= 10
#         guesses.append(hasil)
#
#     print(guesses)
#
# digitize(13425)