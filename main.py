import multiprocessing


def cal_pi(value: int):
    pi = 0
    i = 1
    while i <= value:
        deno = ((i - 0.5) / value * (i - 0.5) / value) + 1
        pi += 1 / deno
        i += 1
    pi = 4/value * pi
    print(pi)
    return None


if __name__ == '__main__':
    print('Вычисления приближенния числа pi')
    print('Введите номер, чем большее чем точнее')
    a = int(input())
    p1 = multiprocessing.Process(target=cal_pi, args=(a, ))
    p1.start()
    p1.join()
    print("Done!")
