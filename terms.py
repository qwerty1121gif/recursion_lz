def partitions(n, max_val=None):
    if max_val is None:
        max_val = n

    if n == 0:
        return [[]]

    result = []
    for i in range(min(n, max_val), 0, -1):
        for partition in partitions(n - i, i):
            result.append([i] + partition)

    return result


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите число для разбиения: "))
            if n < 0:
                print("Число должно быть неотрицательным")
                continue
            result = partitions(n)
            print(f"Разбиения числа {n}: {result}")

            continue_input = input("Хотите продолжить? (y/n): ")
            if continue_input.lower() != "y":
                break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

