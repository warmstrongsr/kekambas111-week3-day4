class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def _get_node(self, value_to_get):
        check = self.head
        while check is not None:
            if check.value == value_to_get:
                return check
            check = check.next
        return None
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def insert_after(self, prev_value, new_value):
        prev_node = self._get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
            return
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def traverse_list(self):
        node = self.head
        while node:
            print(node) 
            node = node.next
    # From lecture I know that you should "point" Tuesday to Thursday but I have no clue how to do that.  
    # I mostly tried to copy what we did in class to figure it out
    
    # def remove(self, value_to_remove):
    #     # If empty print empty
    #     if self.head is None:
    #         print("List is empty")
    #         return
    #     # if value to remove is head value
    #     if self.head.value == value_to_remove:
    #         self.head == self.head.next
    #         return
    #     # set previous and current variables
    #     prev = None
    #     current = self.head
    #     # while loop 
    #     while current is not None:
    #         if current == value_to_remove:
    #             prev.next = current
    #             return
    #         prev = current
    #         current = current.next
                
    def remove(self, value_to_remove):
        if self.head is None:
            print("Linked list is empty.")
            return
        
        if self.head.value == value_to_remove:
            self.head = self.head.next
            return
        
        prev_node = None
        curr_node = self.head
        
        while curr_node is not None:
            if curr_node.value == value_to_remove:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next
        
        print(f"{value_to_remove} not found in linked list.")          
            
            
weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

weekdays.remove('Wednesday')

weekdays.traverse_list()


'''I asked Chat GPT to help me fix my code and run do of how this works.  THe commented out section is as far as I got.  

Me:
Could you explain what you have done?

ChatGpt:
Certainly! Here's a step-by-step explanation of the changes made to add the .remove() method to the LinkedList class:

Define the .remove() method signature: The method should take a single argument - the value to be removed from the linked list.

Check if the linked list is empty: If the linked list is empty, there is nothing to remove. Therefore, we add an if statement to check if the self.head is None. If it is, we print a message indicating that the linked list is empty, and then return from the method.

Handle the case where the head node matches the value to remove: If the self.head node matches the value to remove, then we simply update the self.head to the next node. We add an if statement to check if the self.head.value matches the value_to_remove. If it does, we set the self.head to the next node (i.e., self.head = self.head.next) and then return from the method.

Iterate through the linked list to find the node to remove: If the node to remove is not the head node, we need to iterate through the linked list to find it. We create two variables: prev_node and curr_node, which point to the previous node and current node in the iteration, respectively. Initially, prev_node is set to None and curr_node is set to self.head.

Check each node in the linked list: We use a while loop to iterate through each node in the linked list until we either find the node to remove or reach the end of the list. Within the loop, we add an if statement to check if the curr_node.value matches the value_to_remove. If it does, we set prev_node.next to curr_node.next (i.e., we skip the curr_node), and then we return from the method.

Update the variables for the next iteration: If we haven't found the node to remove yet, we update the prev_node and curr_node variables for the next iteration. We set prev_node to curr_node and curr_node to curr_node.next.

Handle the case where the value to remove is not in the linked list: If we have iterated through the entire linked list and not found the node to remove, then we print a message indicating that the value_to_remove was not found in the linked list.

Testing: We can test the LinkedList.remove() method by creating a linked list and adding some nodes to it using the push_on() and append() methods. We can then call the remove() method with different values to ensure that it correctly removes nodes from the linked list.


'''