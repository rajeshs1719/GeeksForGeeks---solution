#User function Template for python3

# design the class in the most optimal way

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        # Cache capacity
        self.capacity = cap
        
        # HashMap to store key -> node reference for fast access
        self.cache = {}
        
        # Doubly Linked List to maintain the LRU order (head is most recent, tail is least recent)
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        # Remove node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node):
        # Add node right after the head (most recent)
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    #Function for storing key-value pair.   
    
    def get(self, key):
        # If the key exists, move the corresponding node to the front (most recent)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1
    
    def put(self, key, value):
        # If the key exists, update the value and move the node to the front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # If the key doesn't exist, create a new node
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used (tail's prev)
                tail_node = self.tail.prev
                self._remove(tail_node)
                del self.cache[tail_node.key]
            
            # Create new node and add it to the front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends