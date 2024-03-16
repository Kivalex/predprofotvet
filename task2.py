def insertion_sort(sp):
    """
    Сортировка вставками по второму элементу внутренних списков.

    Args:
        arr (list): Список списков длиной в 7 элементов, который нужно отсортировать.

    Returns:
        list: Отсортированный список.
    """


    for i in range(1, len(sp)):
        key = sp[i]
        j = i - 1
        while j >= 0 and key[1][0] < sp[j][1]:
            sp[j + 1] = sp[j]
            j -= 1
        sp[j + 1] = key

    return sp

def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    with open('monster_game.csv', encoding='UTF-8') as file:
        lines = file.read().split('\n')
        filik = [line.split(',') for line in lines]

    data = insertion_sort(filik)

    print(f'{data[1][0]} имеет возможность: {data[1][1]}, вероятность использования возможноси равна {data[1][2]}')
    print(f'{data[2][0]} имеет возможность: {data[2][1]}, вероятность использования возможноси равна {data[2][2]}')
    print(f'{data[3][0]} имеет возможность: {data[3][1]}, вероятность использования возможноси равна {data[3][2]}')

if __name__ == "__main__":
    main()