#####################################################################
# Write code to partition a linked list around a value x, such      #
# that all nodes less than x come before all nodes greater than     #
# or equal to x. If x is contained within the list the values of    #
# x only need to be a er the elements less than x (see below).      #
# The partition element x can appear anywhere in the "right         #
# partition"; it does not need to appear between the left and       #
# right partitions.                                                 #
# EXAMPLE                                                           #
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]              #
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8                          #
#                                                                   #
#####################################################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def print_linkedList(self):  # function to print the nodes of the linked list
        a = self.head
        while (a != None):
            print(a.data)
            a = a.next

    def add(self, value):           # function to add nodes in a list
        temp = self.head
        new_node = Node(value)
        if temp == None:
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def partitionss(self, x):
        dummySmaller = Node(-1)
        dummyGreater = Node(-1)

        greater = dummyGreater
        smaller = dummySmaller

        temp = self.head

        while temp != None:
            if temp.data < x:
                smaller.next = temp
                smaller = smaller.next
            else:
                greater.next = temp
                greater = greater.next
            temp = temp.next

        smaller.next = dummyGreater.next
        greater.next = None

        return dummySmaller.next

def main():

    ll = linkedlist()

    nodeCount = int(input("Enter the number of nodes: "))

    for i in range(nodeCount):
        value = input("Enter the element in the linkedlist:")
        ll.add(value)

    value = input("Enter the value of partition: ")

    ll.partitionss(value)
    ll.print_linkedList()

if __name__=="__main__":
    main()