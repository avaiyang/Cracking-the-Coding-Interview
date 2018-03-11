#########################################################
# Implement a program to replace all spaces in a string #
# with '%20'. You are given the true length of the      #
# string                                                #
# Example: INPUT: "Mr john Smith           ", 13        #
# OUTPUT: "Mr%20John%20Smith"                           #
#                                                       #
#########################################################

def URL(string, length):
    return string[:int(length)].replace(" ", "%20")

def main():

    string = input('Enter the string: ')
    length = input('Enter the string length: ')

    URL_string = URL(string, length)

    print(URL_string)

if __name__=="__main__":
    main()