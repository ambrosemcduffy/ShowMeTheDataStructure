from collections import deque
import operator


class Node:
	def __init__(self, char=None, freq=None):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None
		self.bit = None

	def has_char(self):
		return self.char != None

	def get_bit(self):
		return self.bit

	def set_bit(self, value):
		self.bit = value
	
	def set_right_child(self, value):
		self.right = value
	
	def set_left_child(self, value):
		self.left = value

	def get_left_child(self):
		self.bit = 0
		return self.left
	
	def get_right_child(self):
		self.bit = 1
		return self.right
	
	def has_left_child(self):
		return self.left!= None
	
	def has_right_child(self):
		return self.right != None


class Container:
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.n_entries = 0
	
	def enq(self, value):
		new_node = container(value)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
			self.n_entries += 1
			return
		self.tail.next = new_node
		self.tail = self.tail.next
		self.n_entries += 1
	
	def deq(self):
		node_value = self.head
		self.head = self.head.next
		self.n_entries -= 1
		return node_value.value
	
	def __len__(self):
		return self.n_entries


def get_frequency(message):
	""" This function gets the frequency
	of character per message
	
	Args:
		message (str): string message
	Returns:
		dict: frequency dictionary.
		
	"""
	freq_dict = {}
	cnt = 1
	for char in message:
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1
	return freq_dict


def sort_list(node_list):
	""" Sorts nodes in list
	Args:
	    node_list (list): list of nodes
	Returns:
	    list: sorted node list    
	"""

	node_list.sort(key=operator.attrgetter('freq'))
	return node_list


def get_parent_node(node_list):
	""" Gets parent node with left, and right child
	Args:
	    node_list: list of nodes
	Returns:
	    class: node of left, and right child
	"""
	pop_values = []
	for i in range(2):
		pop_values.append(node_list.pop(0))
	value_sum = pop_values[0].freq + pop_values[1].freq
	
	node_1 = pop_values[1]
	node_2 = pop_values[0]

	node_1.set_bit(1)	
	node_2.set_bit(0)
	
	parent_node = Node(char=None, freq=value_sum)

	parent_node.set_left_child(node_2)
	parent_node.set_right_child(node_1)
	
	return parent_node


def get_append_node_list(message):
	freq_dict = get_frequency(message)
	# Appending the key, and values to node, and appending node to list
	node_list = []
	for k, v in freq_dict.items():
		node = Node(k, v)
		node_list.append(node)
	return node_list


def getHuffTree(message):
	""" Creates a Huffman Tree
	Args:
	    node_list (list): list of sorted nodes
	Returns:
	    class: huffman trees
	"""

	node_list = get_append_node_list(message)
	sorted_node_list = sort_list(node_list)
	def MakeHuffmanTree(node_list):
		if len(node_list) == 1:
			return node_list
		new_node = get_parent_node(node_list)
		node_list.append(new_node)
		node_list = sort_list(node_list)
		MakeHuffmanTree(node_list)
	MakeHuffmanTree(sorted_node_list)
	return node_list[0]



def dfs(node, char):
 	visit_order = []
 	bit = ""
 	def traverse(node, bit=""):
 		if node != None:
 			if node.char == char:
 				visit_order.append(bit)
 			traverse(node.get_left_child(),bit+ "0")
 			traverse(node.get_right_child(), bit + "1")
 	traverse(node)
 	return visit_order[0]


def encode(message):
	# Getting parent of node tree
	parent_node = getHuffTree(message)
	
	# Getting encoding of message
	encoding = ""
	for char in message:

		encoding += dfs(parent_node, char)
	return encoding


def decoder(encoded_message, message):
	# Getting parent of node tree
	parent_node = getHuffTree(message)
	
	node = parent_node
	decoded_string = ""
	if parent_node.get_left_child() is None or parent_node.get_left_child() is None:
	        for bit in encoded_message:
	            decoded_string = decoded_string + parent_node.char
	else:
	    for bit in encoded_message:
	        if bit is '0':
	            node = node.get_left_child()
	        else:
	            node = node.get_right_child()
	        if node.has_char():
	            decoded_string = decoded_string + node.char
	            #Start from tree root
	            node = parent_node
	return decoded_string

# Getting the Frequency of message
message = "Coding will forever be fun"

print(encode(message))
print(decoder(encode(message), message))

message = "Star Trek is the best series ever"

print(encode(message))
print(decoder("10100110110101011111101100110010111111010110011111011100000111110010010011011111000001101010010011100010000011"
, message))
