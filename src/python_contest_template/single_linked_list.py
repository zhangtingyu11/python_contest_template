class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2single_linked_list(node_list):
    if (len(node_list) != 0):
        root = ListNode(node_list[0])
        curNode = root
    else:
        return None
    for i in range(1, len(node_list)):
        addNode = ListNode(node_list[i])
        curNode.next = addNode
        curNode = addNode
    return root

def print_list(head):
    if(head is None):
        print(None)
    else:
        while(head is not None):
            print(head.val)
            head = head.next
