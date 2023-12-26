# Задание №2
# Банк предлагает ряд вкладов для физических лиц:
# Срочный вклад: расчет прибыли осуществляется по формуле простых процентов;
# Бонусный вклад: бонус начисляется в конце периода как % от прибыли, если вклад
# больше определенной суммы;
# Вклад с капитализацией процентов.
# Реализуйте приложение, которое бы позволило подобрать клиенту вклад по заданным
# параметрам.
# Опишите все исключения, возможные в программе. (Например, неверный вод, ошибка
# деления на 0 и т.д.).

class InvalidInputError(Exception):
    pass

class Deposit:
    def __init__(self, principal, interest_rate, time):
        self.principal = principal
        self.interest_rate = interest_rate
        self.time = time

    def calculate_simple_interest(self):
        return self.principal * self.interest_rate * self.time

    def calculate_capitalized_interest(self, times_compounded):
        return self.principal * ((1 + self.interest_rate / times_compounded) ** (times_compounded * self.time))

def select_deposit_type():
    print("Выберите тип вклада:")
    print("1. Срочный вклад")
    print("2. Бонусный вклад")
    print("3. Вклад с капитализацией процентов")
    choice = int(input("Введите номер: "))
    return choice

def main():
    try:
        principal = float(input("Введите начальную сумму вклада: "))
        interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
        time = float(input("Введите срок вклада (в годах): "))

        deposit_type = select_deposit_type()

        if deposit_type == 1:
            deposit = Deposit(principal, interest_rate, time)
            interest = deposit.calculate_simple_interest()
            print(f"Прибыль по срочному вкладу: {interest}")

        elif deposit_type == 2:  # Бонусный вклад
            bonus_threshold = 1000
            if principal >= bonus_threshold:
                deposit = Deposit(principal, interest_rate, time)
                interest = deposit.calculate_simple_interest()
                bonus = interest * interest_rate
                print(f"Прибыль по бонусному вкладу: {interest}")
                print(f"Бонус: {bonus}")
            else:
                print("Сумма вклада ниже минимальной для начисления бонуса")

        elif deposit_type == 3:
            times_compounded = int(input("Введите количество раз, когда проценты капитализируются за год: "))
            deposit = Deposit(principal, interest_rate, time)
            interest = deposit.calculate_capitalized_interest(times_compounded)
            print(f"Прибыль по вкладу с капитализацией процентов: {interest}")

        else:
            raise InvalidInputError("Неверный выбор типа вклада")

    except ValueError:
        print("Ошибка ввода. Введите числовое значение.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except InvalidInputError as e:
        print(e)

if __name__ == "__main__":
    main()
