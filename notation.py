def convert_to_base(number, base):
    if not 2 <= base <= 16:
        raise ValueError("Основание системы счисления должно быть от 2 до 16")
    
    if number == 0:
      return "0"

    digits = "0123456789ABCDEF"

    if number < 0:
        return "-" + convert_to_base(-number, base)
        
    if number < base:
        return digits[number]
    else:
        return convert_to_base(number // base, base) + digits[number % base]


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Введите десятичное число: "))
            base = int(input("Введите основание системы счисления (2-16): "))
            result = convert_to_base(number, base)
            print(f"Число {number} в системе счисления с основанием {base}: {result}")
            
            continue_input = input("Хотите продолжить? (y/n): ")
            if continue_input.lower() != "y":
                break
        except ValueError as e:
            print(f"Ошибка ввода: {e}.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

