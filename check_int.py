def check_int_number(number): # verify that the number is an integer
    try:
        return (False, int(number))
    except:
        print("Invalid input! !")
        return (True, None)

def main():
        make_selection = True
        while make_selection:
            selection = input("select a whole number from:")
            make_selection,selextion = check_int_number(selection) 
        print("Good job",selection, "is a whole number !!!")

if __name__ == "__main__":
     main()
