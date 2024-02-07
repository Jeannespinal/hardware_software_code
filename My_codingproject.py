

def binary_to_decimal(binary):
    result = 0
    power = 0
    while binary > 0
        decimal += (binary % 10) * (2 ** power)
        binary = binary // 10
        power += 1
    return result

def decimal_to_binary(binary):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary



def main():
    print("Convert Decimal to Binary or Binary to Decimal")
    while True:
        print("\nPlease select an option:")
        print("A. Convert binary to decimal")
        Print("B. Convert Decimal to binary")
        Print("C. Quit")
        choice = input("Enter your choice(A, B, or C): ")

        if choice == 'A':
            try:
                Binary = input("Enter in a binary number: ")
                decimal = binary_to_decimal(int(binary))
                print("Binary {} to Decimal: {}".format(binary, decimal))
            except ValueError:
                print("Invalid input! Please enter a valid binary number.")
        elif choice == 'B':
            decimal 


if __name__ == "__main__":
    main()
