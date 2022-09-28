class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        self.head = new_node
        new_node.next = cur_node

    def insert_after(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                new_node.next = nxt
                cur.next = new_node
            cur = cur.next

        if cur is None:
            print("Previous Node is not present in the list")
            return

    def delete_node(self, key):

        # Case 1
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case 2
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print("The Node is not present in the list")
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            count += 1
            cur_node = cur_node.next

        if cur_node is None:
            print("The Node is not present in the list")
            return

        prev.next = cur_node.next
        cur_node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    
if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    llist.insert_after("D", "S")

    llist.prepend("E")

    llist.delete_node("A")
    llist.delete_node_at_pos(1)

    llist.print_list()
