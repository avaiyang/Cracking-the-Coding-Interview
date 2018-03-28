#############################################################
# You have two numbers represented by a linked list,        #
# where each node contains a single digit. The digits       #
# are stored in reverse order,such that the 1's digit       #
# is at the head of the list. Write a function that adds    #
# the two numbers and returns the sum as a linked list.     #
# EXAMPLE                                                   #
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.    #
# Output:2 -> 1 -> 9.That is, 912.                          #
#                                                           #
#############################################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def printLinkedList(self):         # function to print the nodes of the linked list
        a = self.head
        while (a != None):
            print(a.data)
            a = a.next

    def insert(self, value):            # function to add nodes in a list
        temp = self.head
        new_node = Node(value)
        if temp == None:
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def addLinkedlist(self,p,q):
        x = []
        while p and q:
            a = int(p.data) + int(q.data)
            x.append(a)
            p = p.next
            q = q.next
        x.append(0)                         # for carry

        for i in range(len(x)):
            if x[i] >9:
                x[i+1] += int(x[i]/10)
                x[i] %=10
        return(x)

def main():

    ll1 = linkedlist()
    nodeCount1 = int(input("Enter the number of nodes: "))

    for i in range(nodeCount1):
        value = input("Enter the element in the linkedlist1: ")
        ll1.insert(value)

    ll2 = linkedlist()
    nodeCount2 = int(input("Enter the number of nodes: "))

    for i in range(nodeCount2):
        value = input("Enter the element in the linkedlist2: ")
        ll2.insert(value)

    ll3 = linkedlist()                          # creating linkedlist for the output of the addition
    x = ll3.addLinkedlist(ll1.head, ll2.head)

    for i in x:
        ll3.insert(i)

    ll3.printLinkedList()


if __name__=="__main__":
    main()