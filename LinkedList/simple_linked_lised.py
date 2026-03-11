class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next


# Create nodes
list1 = LinkedList()

list1.head = Node(10)
second = Node(20)
third = Node(30)

# Connect nodes
list1.head.next = second
second.next = third

# Print list
list1.print_list()
