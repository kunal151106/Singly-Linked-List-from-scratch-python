class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
            self._length = 1
        else:
            self.head = None
            self._length = 0
    
    
    # Adds a new node with the given value to the very end of the linke list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1
    
    
    # Removes the very last node from the end of the linked list
    def pop(self):
        if self.head is None:
            raise ValueError("Index is out of bounds")
        else:
            current =  self.head
            if current.next is None:
                self.head = None
            else:
                while current.next.next:
                    current = current.next
                current.next = None
            self._length -= 1
    
    
    # Adds a new node with given value to the very front of the linked list 
    def prepend(self, value):
        current = self.head
        self.head = Node(value)
        self.head.next = current
        self._length += 1
    
    
    # Finds and removes the first node that matches the given value from the linked list
    def remove(self, value):
        current = self.head
        if current is None:
            raise ValueError("Index out of bounds")
        elif current.value == value:
            self.head = current.next
            self._length -= 1
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    self._length -= 1
                    break
                current = current.next
            else:
                raise ValueError("Value not found")
    
    
    # Inserts a new node with given value at a specific index position
    def insert(self, index, value):
        if index >= 0 and index <= self._length:
            if index == 0:
                self.prepend(value)
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                self._length += 1
        else:
            raise ValueError("Index out of bounds")
    
    
    # Removes the node at a specific index position
    def delete(self, index):
        if index >= 0 and index < self._length:
            if index == 0:
                self.head = self.head.next
                self._length -= 1
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                current.next = current.next.next
                self._length -= 1
        else:
            raise ValueError("Index out of bounds")
    
    
    # Overwrites the value of a node at a specific index position
    def replace(self, index, value):
        if index >= 0 and index < self._length:
            current = self.head
            for i in range(index):
                current = current.next
            current.value = value
        else:
            raise ValueError("Index out of bounds")
    
    
    # Checks if a specific value exists anywhere in the linked list
    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    
    # Checks whether the linked list as zero elements in it
    def is_empty(self):
        return self.head is None
    
    
    # Finds the index position of the first node that matches the given value
    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return "Value not found"
    
    
    # Returns the total number of nodes currently inside the linked list
    def length(self):
        return self._length
    
    
    # Counts the total number of times a specific value appears in the linked list
    def count(self, value):
        current = self.head
        counter = 0
        while current:
            if current.value == value:
                counter += 1
            current = current.next
        return counter
    
    
    # Finds and returns the highest value stored anywhere in the linked list
    def maximum(self):
        if self.head is None:
            return "List is empty"
        else:
            current = self.head
            maximum_value = current.value
            while current.next:
                if maximum_value < current.next.value:
                    maximum_value = current.next.value
                current = current.next
            return maximum_value
    
    
    # Finds and returns the lowest value stored anywhere in the linked list
    def minimum(self):
        if self.head is None:
            return "List is empty"
        else:
            current = self.head
            minimum_value = current.value
            while current.next:
                if minimum_value > current.next.value:
                    minimum_value = current.next.value
                current = current.next
            return minimum_value
    
    
    # Wipes the entire linked list clean by removing all nodes
    def clear(self):
        self.head = None
        self._length = 0
    
    
    # Reverses the direction of entire linked list in place
    def reverse(self):
        if self._length == 0:
            return "List is empty"
        elif self._length == 1:
            self.return_list()
        else:
            prev = None
            current = self.head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev
            self.return_list()
    
    
    # Converts the linked list into a formatted string representation resembling a list
    def return_list(self):
        if self.head is None:
            return "[]"
        else:
            current = self.head
            output = '['
            while current.next:
                output += f'{current.value}, '
                current = current.next
            return output + f'{current.value}]'
    
    
    # Prints the string representation of the linked list directly to the console
    def disaplay(self):
        print(self.return_list())


if __name__ == '__main__':
    # Initialize a new Linked List instance
    ll = LinkedList()

    # =========================================================================
    # write your own custom testing logic here!
    # =========================================================================

    # Display the final state of the linked list
    ll.display()