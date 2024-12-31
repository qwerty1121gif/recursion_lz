def add_large_numbers(num1, num2, carry=0):
    if not num1 and not num2 and not carry:
        return ""

    digit1 = int(num1[-1]) if num1 else 0
    digit2 = int(num2[-1]) if num2 else 0

    sum_digits = digit1 + digit2 + carry
    current_digit = str(sum_digits % 10)
    next_carry = sum_digits // 10

    return add_large_numbers(num1[:-1], num2[:-1], next_carry) + current_digit


if __name__ == "__main__":
    while True:
        try:
            num1 = input("Введите первое большое число: ")
            num2 = input("Введите второе большое число: ")
            result = add_large_numbers(num1, num2)
            print(f"Сумма чисел {num1} и {num2}: {result}")
            
            continue_input = input("Хотите продолжить? (y/n): ")
            if continue_input.lower() != "y":
                break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
