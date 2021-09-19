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
    if linkedlist is None:
    	return None
    elem_l = []
    node = linkedlist.head
    while node:
        elem_l.append(node.value)
        node = node.next
    return sorted(set(elem_l))


def append_to_linked_list(list_):
    """Appends list element to linked list
    Args:
    	list_ (list): list with elements
    Returns:
    	class: linked list class Node
    """
    if list_ is None:
    	return None
    linked_list = LinkedList()
    for element in list_:
        linked_list.append(element)
    return linked_list


def intersect(element_1, element_2):
    """ Appends intersecting values to new linked list node
    Args:
        linked_list_1 (class): node class with values
        linked_list_2 (class): node class with values
    Returns:
        class: node class with intersecting values
    """
    if element_1 is None or element_2 is None:
    	return None
    linked_list_1 = append_to_linked_list(element_1)
    linked_list_2 = append_to_linked_list(element_2)
    
    array_1 = linkedlistToArray(linked_list_1)
    array_2 = linkedlistToArray(linked_list_2)
    intersecting_linked_list = LinkedList()

    for i in array_1:
        for j in array_1:
            if i == j:
                intersecting_linked_list.append(i)
    
    return intersecting_linked_list


def union(element_1, element_2):
    """ Appends Unioned values to new Linked list
    Args:
    	linked_list_1 (class): class Node with values
    	linked_list_2 (class): class Node with values
    Returns:
    	class: class Node with values
    """
    if element_1 is None or element_2 is None:
    	return None
    elif type(element_1) != list or type(element_2) != list:
    	print("Not list")
    	return None
    linked_list_1 = append_to_linked_list(element_1)
    linked_list_2 = append_to_linked_list(element_2)
    
    array_1 = linkedlistToArray(linked_list_1)
    array_2 = linkedlistToArray(linked_list_2)
    
    union_linked_list = LinkedList()
    combined_list = sorted(set(array_1 + array_2))
    
    for element in combined_list:
    	union_linked_list.append(element)
    	return union_linked_list


def printOutLinkedList(linked_list):
    if linked_list is None:
    	print("\nNoneType values input elements\n")
    	return None
    node = linked_list.head
    print("\n")
    while node:
        if node is None:
        	break
        print("-{}->".format(node.value), end='')
        node = node.next


# Unit Test 1
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

intersect_ll = intersect(element_1, element_2)
union_ll = union(element_1, element_2)

#printOutLinkedList(intersect_ll)
#printOutLinkedList(union_ll)



# Unit Test 2
element_1 = None
element_2 = None

intersect_ll = intersect(element_1, element_2)
union_ll = union(element_1, element_2)

#printOutLinkedList(intersect_ll)
#printOutLinkedList(union_ll)




# Unit Test 2
element_1 = "A"
element_2 = "B"

intersect_ll = intersect(element_1, element_2)
union_ll = union(element_1, element_2)

printOutLinkedList(intersect_ll)
printOutLinkedList(union_ll)
