#######################################################
# Implement a program to check, given two strings     #
# if they are one edit (or zero edits) away.          #
# EXAMPLE                                             #
# pale, ple -> true                                   #
# pales, pale -> true                                 #
# pale, bake -> false                                 #
#                                                     #
#######################################################


def oneAway(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    if (abs(length1-length2) > 1):
        return False

    count = 0

    i = 0
    j = 0

    while(i < length1 and j < length2):
        if string1[i] != string2[j]:
            if count == 1:
                return False

            if length1 > length2:
                i += 1
            elif length1 < length2:
                j += 1
            else:                           # If lengths of both strings is same
                i += 1
                j += 1

            count += 1

        else:                               # if current characters match
            i += 1
            j += 1

    if i < length1 or j < length2:          # if last character is extra in any string
        count += 1

    return count == 1


def main():
    string1 = input("Enter the string 1: ")
    string2 = input("Enter the string 2: ")

    if oneAway(string1, string2):
        print('True')
    else:
        print("False")

if __name__ == '__main__':
    main()
