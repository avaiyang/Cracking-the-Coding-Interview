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

    def print_linkedList(self):     # function to print the nodes of the linked list
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

    def removeDuplicate(self):      # function to remove duplicates
        current = self.head
        second = current
        while(current!=None):
            while(second.next !=None):
                if (current.data == second.next.data):
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next

def main():

    ll = linkedlist()

    nodeCount = int(input("Enter the number of nodes: "))

    for i in range(nodeCount):
        value = input("Enter the element in the linkedlist:")
        ll.add(value)

    ll.removeDuplicate()
    ll.print_linkedList()

if __name__=="__main__":
    main()