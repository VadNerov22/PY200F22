class Calculator:
    @staticmethod
    def add(val_1, val_2):
        return val_1 + val_2

    @staticmethod
    def mul(val_1, val_2):
        return val_1 * val_2


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
