#################################################
# Implement a program to determine if a string  #
# has all unique characters. Also, you are not  #
# allowed to use new data structure.            #
#                                               #
#################################################

def main():
    string= input("Enter the string: ")

    newString = str()

    for char in string:
        if (char in newString and char!=" "):
            print("Character repeated")
            break
        else:
            newString = newString + char                     #appending the char in the string b

    if (newString == string):
        print("String contains all unique characters")

if __name__=="__main__":
    main()