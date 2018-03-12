##############################################################
# Given an image represented by an NxN matrix, where each    #
# pixel in the image is 4 bytes, write a program to rotate   #
# the image by 90 degrees.                                   #
#                                                            #
##############################################################

def main():

    m = int(input("Enter the number of rows: "))  # rows
    n = int(input("Enter the number of columns: "))        # columns

    matrix = []
    print("\nEnter the elements of matrix:")
    for i in range(0, m):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(0)
            matrix[i][j] = int(input())
    print(matrix)

    reverseMatrix = matrix[::-1]        #reversing the matrix

    rotated = zip(*reverseMatrix)       #unzipping the elements of matrix and zipping them to tuple
    print("\nThe rotated matrix is:")

    for row in list(rotated):
        print(row)

if __name__=="__main__":
    main()

