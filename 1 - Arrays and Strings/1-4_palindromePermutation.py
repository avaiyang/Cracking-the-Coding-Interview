#######################################################
# Implement a program to check if a string is         #
# permutation of a palindrome                         #
# Example: INPUT: Tact Coa                            #
# OUTPUT: True (permutations: "taco cat", "atco cta") #
#                                                     #
#######################################################

def main():
    string = input("Enter the string: ")
    string = string.lower().replace(" ","")         #to remove all the space characters, and convert the chars to lowercase

    length = int(len(string))

    stringSet = set(string)
    setLength = int(len(stringSet))

    a = int(length/2)

    if length%2 == 1:
        if ((a +1) == setLength):
            print("True")
    else:
        if (a == setLength):
            print("True")

if __name__=="__main__":
    main()