##############################################################
# Write a program such that if an element in an MxN matrix   #
# is 0, its entire row and column are set to 0.              #
#                                                            #
##############################################################

def main():
    m = int(input("Enter the number of rows: "))  # rows
    n = int(input("Enter the number of columns: "))        # columns
    row = 0
    column = 0

    matrix = []
    print("\nEnter the elements of matrix:")
    for i in range(0, m):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(0)
            matrix[i][j] = int(input())
    print(matrix)

    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j] == 0:
                row = i+1
                column = j+1
                matrix[i][j] = 0

    if row != 0:
        print("The 0 element is present in row {} and column {}\n".format(row, column))
        for i in range(0, m):
            for j in range(0,n):
                matrix[row-1][j]=0
                matrix[i][column-1]=0
        print("The zero matrix is given as:\n", matrix)
    else:
        print("There is no zero matrix")

if __name__=="__main__":
    main()