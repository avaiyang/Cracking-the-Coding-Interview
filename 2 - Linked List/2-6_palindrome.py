###############################################
# Implement a function to check if a linked  #
# list is a palindrome.                       #
#                                             #
###############################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def insert(self, value):                    # function to add nodes in a list
        temp = self.head
        new_node = Node(value)
        if temp == None:
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def isPalindrome(self, head):
        fast = slow = head
                                                # to find the mid of the node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
                                                # reverse the second half of the linkedlist
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
                                                # compare the first and second half of the nodes
        while node:  # while node and head:
            if node.data != head.data:
                return False
            node = node.next
            head = head.next
        return True

def main():

    ll = linkedlist()
    nodeCount = int(input("Enter the number of nodes: "))

    for i in range(nodeCount):
        value = input("Enter the element in the linkedlist: ")
        ll.insert(value)

    print(ll.isPalindrome(ll.head))

if __name__=="__main__":
    main()