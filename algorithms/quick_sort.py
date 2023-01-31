import random
import bisect


def main():
    # входные параметры
    n, m = map(int, input().split())
    # создаем списки для левых и правых границ отрезков
    lst_left = list()
    lst_right = list()
    # проходим по всем границам отрезков
    for i in range(n):
        # вводим n отрезков
        l, r = map(int, input().split())
        # добавляем левую и правую границу отрезков в соответствующие списки
        lst_left.append(l)
        lst_right.append(r)
    # создаем список с искомыми точками
    points = [int(q) for q in input().split()]
    # cортируем списки границ
    lst_left.sort()
    lst_right.sort()
    # проходимся по всем искомым точкам
    for p in points:
        # добавляем точку в список с левыми границами как можно правее
        index_left = bisect.bisect(lst_left, p)
        # добавляем точку в список с правыми границами как можно левее
        index_right = bisect.bisect_left(lst_right, p)
        # с помощью разности индексов находим количество отрезков, к которым принадлежит точка
        print(abs(index_left - index_right), end = " ")


if __name__ == "__main__":
    main()