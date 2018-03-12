###########################################################
# Assume you have a method is Substring which checks if   #
# one word is a substring of another. Given two strings,  #
# sl and s2, write code to check if s2 is a rotation of   #
# sl using only one call to isSubstring                   #
# (e.g.,"waterbottle" is a rotation of"erbottlewat").     #
#                                                         #
###########################################################

#you can use any of the two methods

def method1(string1, string2):
    for i in range(len(string1)-1):
        if string1[i] == string2[0] and string1[i+1] == string2[1]:
            if string2.endswith(string1[:i]):
                return True


def method2(string1, string2):

    string3 = string2 + string2
    if string1 not in string3:
        return False
    else:
        return True


def main():
    string1 = input("Enter the string 1: ")
    string2 = input("Enter the string 2: ")

    if method2(string1,string2):
        print("The string 2 is substring rotation of string 1")
    else:
        print("The string 2 is not substring rotation of string 1")

if __name__=="__main__":
    main()


