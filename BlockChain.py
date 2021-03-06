
import hashlib
import time


class Block(object):
    def __init__(self, timestamp, value, prev_hash):
        self.value = value
        self.next = None
        self.previous = None
        self.hash = self.calc_hash(value)
        self.timestamp = timestamp
        self.prev_hash = prev_hash

    def calc_hash(self, value):
        value = str(value)
        sha = hashlib.sha256()
        hash_str = value.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def get_timestamp(self):
        return "GMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

    def append(self, value):
        if type(value) != int:
            return None

        if self.head is None:
            self.head = Block(self.get_timestamp(), "$"+str(value), 0)
            self.tail = self.head
            return None

        self.tail.next = Block(self.get_timestamp(), "$"+str(value), self.head.hash)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def __str__(self):
        if self.head is None:
            print("--No values please enter interger--")
            return " "
        s = ""
        node = self.head
        index = 0
        while node:
            s += "\n______________________________\n"
            s += f"Timestamp: {node.timestamp}"
            s += f"\nData: {node.value}"
            s += f"\nSHA256 Hash: {node.hash}"
            s += f"\nPrev_Hash: {node.prev_hash}"
            s += f"\n      Block: {index}"
            index += 1
            node = node.next
        return s


# Unit Test 1
# blockchain data should show $500 dollars
bc = BlockChain()
bc.append(500)
print(bc)

# Unit Test 2
# blockchain data should return None
bc = BlockChain()
bc.append(" ")
print(bc)


# Unit Test 3
# blockchain data should return None
bc = BlockChain()
bc.append(None)
print(bc)

# Unit Test 4
# blockchain data should return None
bc = BlockChain()
bc.append("ambrose")
print(bc)


# Unit Test 5
# blockchain data should return all values linked
# blockchain time data should be different
for i in range(10):
    bc.append(i*i)
    time.sleep(.7)
print(bc)

