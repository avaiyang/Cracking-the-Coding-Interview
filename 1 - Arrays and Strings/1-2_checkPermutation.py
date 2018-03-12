#####################################################
# Implement a program to determine if one string    #
# is permutation of other. The input is case        #
# sensitive and spaces are taken into consideration #
#                                                   #
#####################################################

def permutation(string1, string2):
    ASCIsum1 = 0
    ASCIsum2 = 0

    if len(string1) != len(string1):
        return False

    for char in string1:
        ASCIsum1 += ord(char)

    for char in string2:
        ASCIsum2 += ord(char)

    if ASCIsum1 == ASCIsum2:
        return True

def main():
    string1 = input("Enter the string 1: ")
    string2 = input("Enter the string 2: ")

    if permutation(string1, string2):
        print('The two strings are permutation of one another')

    else:
        print('The two strings are not permutation of one another')

if __name__=="__main__":
    main()