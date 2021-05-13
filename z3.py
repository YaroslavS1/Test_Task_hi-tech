from typing import List, Tuple
import copy as cp
from collections import defaultdict

# 1----------------------------
class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

def to_linked_list(array: List[int]) -> Node:
    if len(array) == 0:
        return None
    return Node(array[0], to_linked_list(array[1:]))

# head = to_linked_list([1, 2, 3, 4])

# print(head.val)
# print(head.next.val)
# print(head.next.next.val)
# print(head.next.next.next.val)
# --------------------------------
# 2-------------------------------
def linked_list_to_str(head: Node) -> str:
    strng = ""
    tmp = cp.deepcopy(head)
    while True:
        strng += str(tmp.val)
        tmp = cp.deepcopy(tmp.next)
        if tmp == None:
            break
        strng += " -> "         
    return strng

# print(linked_list_to_str(to_linked_list([1, 2, 3])))
# print(linked_list_to_str(to_linked_list(range(10))))
# --------------------------------
def remove_n_th_node(head: Node, n: int) -> Node:
    if not head.next:
        return None
    front=head
    back = head
    counter = 0
    flag = False
    while counter<=n:
        if(not front):
            flag = True
            break
        front = front.next
        counter+=1
    while front:
        front = front.next
        back = back.next
    if not flag:
        temp = back.next
        back.next = temp.next
        temp.next = None
    else:
        head = head.next
    return head

head = to_linked_list(range(10))
print(linked_list_to_str(head))

new_head = remove_n_th_node(head, 3)
print(linked_list_to_str(head))

