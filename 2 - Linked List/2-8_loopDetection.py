#############################################################
# Given a circular linked list, implement an algorithm      #
# that returns the node at the beginning of the loop.       #
# EXAMPLE                                                   #
# Input: A -> B -> C -> D -> E -> C [the same C as earlier] #
# Output: C                                                 #
#                                                           #
#############################################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def loopDetect(self):
        new = set()
        temp = self.head

        while(temp != None):
            if temp.data in new:
                return temp.data
            else:
                new.add(temp.data)
                temp = temp.next
        return ("No loop detected")


def main():

    ll = linkedlist()

    print(ll.loopDetect())

if __name__=="__main__":
    main()