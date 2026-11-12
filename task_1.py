class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        assert prev is not None
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


def reverse_linked_list(head: Node | None) -> Node | None:
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev


def insertion_sort(head: Node | None) -> Node | None:
    sorted_head = None
    cur = head

    while cur:
        next_node = cur.next
        if sorted_head is None or cur.data < sorted_head.data: # type: ignore
            cur.next = sorted_head
            sorted_head = cur
        else:
            pivot = sorted_head
            while pivot.next and pivot.next.data <= cur.data: # type: ignore
                pivot = pivot.next
            cur.next = pivot.next
            pivot.next = cur
        cur = next_node

    return sorted_head


def merge_sorted_lists(first: Node | None, second: Node | None) -> Node | None:
    temp = Node()
    tail = temp

    while first and second:
        if first.data <= second.data: # type: ignore
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next

    tail.next = first or second
    return temp.next


def main():
    unsorted_list = LinkedList()
    for value in [4, 2, 7, 1, 3]:
        unsorted_list.insert_at_end(value)

    print("Початковий список:")
    unsorted_list.print_list()

    unsorted_list.head = insertion_sort(unsorted_list.head)
    print("Відсортований список:")
    unsorted_list.print_list()

    unsorted_list.head = reverse_linked_list(unsorted_list.head)
    print("Реверсований список:")
    unsorted_list.print_list()

    first_sorted_list = LinkedList()
    second_sorted_list = LinkedList()
    for value in [1, 3, 5]:
        first_sorted_list.insert_at_end(value)
    for value in [2, 4, 6]:
        second_sorted_list.insert_at_end(value)

    merged_head = merge_sorted_lists(
        first_sorted_list.head,
        second_sorted_list.head,
    )
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Об'єднаний відсортований список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()

