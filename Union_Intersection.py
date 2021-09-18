class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n_entries = 0
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.n_entries += 1 
            return

        self.tail.next = new_node
        self.tail = self.tail.next
        self.n_entries += 1

    def pop(self):
        value = self.head
        self.head = self.head.next
        self.n_entries -= 1
        return value

    def size(self):
        return self.n_entries



def linkedlistToArray(linkedlist):
    """ Appends a linked list to sorted array
    Args:
        linked_list (class): node class with values
    Returns:
        list: sorted array of values
    """
    elem_l = []
    node = linkedlist.head
    while node:
        elem_l.append(node.value)
        node = node.next
    return sorted(set(elem_l))

def intersect(linked_list_1, linked_list_2):
    """ Appends intersecting values to new linked list node
    Args:
        linked_list_1 (class): node class with values
        linked_list_2 (class): node class with values
    Returns:
        class: node class with intersecting values
    """
    
    array_1 = linkedlistToArray(linked_list_1)
    array_1 = linkedlistToArray(linked_list_2)
    intersecting_linked_list = LinkedList()

    for i in array_1:
        for j in array_1:
            if i == j:
                intersecting_linked_list.append(i)
    
    return intersecting_linked_list


def union(linked_list_1, linked_list_2):
    elem_set1 = linkedlistToArray(linked_list_1)
    elem_set2 = linkedlistToArray(linked_list_2)
    ll = LinkedList()
    comb_l = sorted(set(elem_set1 + elem_set2))
    for i in comb_l:
        ll.append(i)
    return ll


element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

def append_to_linked_list(list_):
    linked_list = LinkedList()
    for element in list_:
        linked_list.append(element)
    return linked_list


linked_list_1 = append_to_linked_list(element_1)
linked_list_2 = append_to_linked_list(element_2)

intersect_ll = intersect(linked_list_1, linked_list_2)
union_ll = union(linked_list_1, linked_list_2)




def printOutLinkedList(linked_list):
    node = linked_list.head
    print("\n")
    while node:
        print("-{}->".format(node.value), end='')
        node = node.next\

printOutLinkedList(intersect_ll)
printOutLinkedList(union_ll)
