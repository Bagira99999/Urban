
def calculate (a, b, operation):
    try:
        if operation == "+":
            return a+b
        elif operation == "-":
            return a-b
        elif operation == "*":
            return a*b
        elif operation == "/":
            try:
                return a/b
            except ZeroDivisionError:
                return "Деление на ноль запрещено"
    except Exception as error:
        return ("Вычисление не удалось. Попробуйте еще раз. Ошибка:", error)

print(calculate(int(input()), int(input()), input()))


