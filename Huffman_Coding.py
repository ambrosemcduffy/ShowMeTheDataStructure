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


def get_frequency(message):
	""" This function gets the frequency of character per message
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
	if node_list is None:
		return None
	node_list.sort(key=operator.attrgetter('freq'))
	return node_list


def get_parent_node(node_list):
	""" Gets parent node with left, and right child
	Args:
	    node_list: list of nodes
	Returns:
	    class: parent node of left, and right child
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
	""" Gets frequency of characters to Node in message and appends to list
	Args:
	    message (str): string message
	Returns:
	    list: list of node values with frequency and character
	"""
	if message is None:
		return None
	freq_dict = get_frequency(message)
	# Appending the key, and values to node, and appending node to list
	node_list = []
	for k, v in freq_dict.items():
		node = Node(k, v)
		node_list.append(node)
	return node_list


def getHuffTree(message):
	""" Creates a Huffman Tree recursively
	Args:
	    node_list (list): list of sorted nodes
	Returns:
	    class: huffman trees
	"""

	node_list = get_append_node_list(message)
	sorted_node_list = sort_list(node_list)
	def MakeHuffmanTree(node_list):
		if node_list is None:
			return None
		if len(node_list) == 1:
			return node_list
		new_node = get_parent_node(node_list)
		node_list.append(new_node)
		node_list = sort_list(node_list)
		MakeHuffmanTree(node_list)
	MakeHuffmanTree(sorted_node_list)
	if node_list is None:
		return None
	else:
		return node_list[0]



def dfs(node, char):
	""" Traverses tree and gets encoded value of character
	Args:
	    node (class): class node containing, char, freq, left, and right child
	    char (str): string character
	Returns:
	    class: parent root node
	"""
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
	""" encodes messages to bits
	Args:
	    message (str): string message
	Returns:
	    str: bit string message
	"""
	# Getting parent of node tree
	parent_node = getHuffTree(message)
	
	# Getting encoding of message
	encoding = ""
	if message is None:
		return None
	for char in message:
		encoding += dfs(parent_node, char)
	return encoding


def decoder(encoded_message, message):
	""" Decodes our encoded bit message
	Args:
	    encoded_message (str): string encoded message
	    message (str): string message
	Returns:
	    str: string decode message
	"""
	# Getting parent of node tree
	parent_node = getHuffTree(message)
	if message is None:
		return None
	node = parent_node
	decoded_string = ""
	if parent_node.get_left_child() is None or parent_node.get_left_child() is None:
	        for bit in encoded_message:
	            decoded_string = decoded_string + parent_node.char
	else:
	    for bit in encoded_message:
	        if bit == '0':
	            node = node.get_left_child()
	        else:
	            node = node.get_right_child()
	        if node.has_char():
	            decoded_string = decoded_string + node.char
	            #Start from tree root
	            node = parent_node
	return decoded_string

# Unit test 1
# Expecting encoded and decoded message
message = "It's possible to commit no mistake and still lose."
encoded_message = encode(message)
decoded_message = decoder(encoded_message, message)

print("encoded message: {}".format(encoded_message))
print("decoded message: {}\n".format(decoded_message))

# Unit test 2
# Expecting None
message = None
encoded_message = encode(message)
decoded_message = decoder(encoded_message, message)

print("encoded message: {}".format(encoded_message))
print("decoded message: {}\n".format(decoded_message))

# Unit test 3
# Expecting empty string
message = " "
encoded_message = encode(message)
decoded_message = decoder(encoded_message, message)

print("encoded message: {}".format(encoded_message))
print("decoded message: {}\n".format(decoded_message))

# Unit test 4
# Expecting encoded and decoded message

message = "Coding is Fun."
encoded_message = encode(message)
decoded_message = decoder(encoded_message, message)


print("encoded message: {}".format(encoded_message))
print("decoded message: {}\n".format(decoded_message))