#################################################################
# Implement an algorithm to delete a node in the middle         #
# (i.e., any node but the first and last node, not necessarily  #
# the exact middle) of a singly linked list, given only         #
# access to that node. Do not print anything                    #
#                                                               #
#################################################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def add(self, value):           # function to add nodes in a list
        temp = self.head
        new_node = Node(value)
        if temp == None:
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def deleteNode(self, value):      # function to remove duplicates
        current = self.head
        while(current != None):
            if current.data == value:
                current.data = current.next.data
                current.next = current.next.next

            current = current.next

def main():

    ll = linkedlist()

    nodeCount = int(input("Enter the number of nodes: "))

    for i in range(nodeCount):
        value = input("Enter the element in the linkedlist:")
        ll.add(value)

    value = input("Enter the element to be deleted: ")

    ll.deleteNode(value)

if __name__=="__main__":
    main()