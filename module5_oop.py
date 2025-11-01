class NumberList:
    def __init__(self):
        self.data = []

    def insert_number(self, num):
        self.data.append(num)

    def find_number(self, x):
        for i in range(len(self.data)):
            if self.data[i] == x:
                return i + 1
        return -1


def main():

    n = int(input("Enter N (positive integer): "))

    numbers = NumberList()

    for i in range(n):
        value = int(input(f"Enter number #{i+1}: "))
        numbers.insert_number(value)

    x = int(input("Enter X (integer to search): "))

    result = numbers.find_number(x)
    print(result)


main()
