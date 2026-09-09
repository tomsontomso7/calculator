from operations import add, subtract, multiply, divide


def main():
    a = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    try:
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Неизвестная операция")
            return

        print("Результат:", result)

    except ValueError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
