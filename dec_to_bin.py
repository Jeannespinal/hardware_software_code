def decimal_to_binary(number):
    try:
        result = ""
        number=int(number)
        while number > 0:                #keep dividing until at 0
            remainder = number % 2
            number = number // 2
            result = str(remainder) + result #place string in reverse order
        return result
    except ValueError:
        num = ("Enter a decimal number")
    print("Invalid number please enter decimal number")


def main():
    num = input("Enter Binary Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__== "__main__":
    main()
