import multiprocessing
import time


def cal_pi(value: int):
    pi = 0
    i = 1
    while i <= value:
        deno = ((i - 0.5) / value * (i - 0.5) / value) + 1
        pi += 1 / deno
        i += 1
    pi = 4 / value * pi

    print(pi)
    return None


def cal_time_processing(value: int):
    start = time.time()
    p1 = multiprocessing.Process(target=cal_pi, args=(value,))
    p1.start()
    p1.join()
    end = time.time()
    print("Времени работы с multiprocessing", end - start)
    return None


if __name__ == '__main__':
    print('Вычисления приближенния числа pi')
    print('Введите номер, чем большее чем точнее')
    a = int(input())
    cal_time_processing(a)

    print("Использовать функцию")
    start_def = time.time()
    cal_pi(a)
    end_def = time.time()
    print("Времени работы с фукцией", end_def - start_def)
