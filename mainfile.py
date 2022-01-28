def printmine(name):
    return f"You're name is {name}"

def add(num1, num2):
    return num1 + num2 + 5


def main():
    print(printmine("Ahmad"))
    print(add(6, 4))

if __name__ == "__main__":
    main()    


class ABC:
    @staticmethod
    def printABC():
        print("ABCDEFG")