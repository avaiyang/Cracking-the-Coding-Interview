##############################################################
# Implement a program to perform basic string compression    #
# using counts of repeated characters.                       #
# Example: aabccccaaa would become a2b1c4a3                  #
#                                                            #
##############################################################

def stringCompression(a):

    count = 1
    newString = str()

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
        else:
            if count == 1:  # only one character
                newString += a[i] + str(count)
            else:
                newString += a[i - 1] + str(count)
            count = 1

    newString += a[-1] + str(count)

    if len(a) <= len(newString):
        return a

    return newString

def main():
    string = input("Enter the string: ")
    print(stringCompression(string))

if __name__=="__main__":
    main()