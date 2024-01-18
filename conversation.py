def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes":
        print("that's good - the United states need more coders! !")
    elif answer == "no":
        print("perhaps you will change your mind ")
        print ("Goodbye")
    else:
        print("i dont understand what do you mean")

def main():
    print("welcome to my conversation program")
    conversation()
    print("Thank for chatting with me")

if __name__ == "__main__":
  main()
