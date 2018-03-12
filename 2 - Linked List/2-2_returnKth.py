#####################################
# Write code to remove duplicates   #
# from an unsorted linked list. Do  #
# not use any buffer space          #
#                                   #
#####################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def print(self, position):     # function to print the kth postion of linkedlist
        a = self.head
        count = 1
        while(count !=position):
            a = a.next
            count +=1
        print(a.data)

    def add(self, value):           # function to add nodes in a linkedlist
        temp = self.head
        new_node = Node(value)
        if temp == None:
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def size(self):             # function to calculate the size of linkedlist
        temp = self.head
        count = 0
        while (temp != None):
            count += 1
            temp = temp.next
        return count

def main():

    ll = linkedlist()

    nodeCount = int(input("Enter the number of nodes: "))

    for i in range(nodeCount):
        value = input("Enter the element in the linkedlist:")
        ll.add(value)

    length = ll.size()

    k = int(input("Enter the kth position to be printed from the last: "))

    m = length - k + 1

    ll.print(m)

if __name__=="__main__":
    main()