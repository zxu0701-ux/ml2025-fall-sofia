from module5_mod import PublicNumberList
def main():

    n = int(input("Enter N (positive integer): "))

    numbers = PublicNumberList()

    for i in range(n):
        value = int(input(f"Enter number #{i+1}: "))
        numbers.insert_number(value)

    x = int(input("Enter X (integer to search): "))

    result = numbers.find_number(x)
    print(result)


main()