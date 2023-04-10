from collections import deque
from re import S

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def list2binary_tree(node_list):
    if(len(node_list) == 0):
        return None
    root = TreeNode(node_list[0])
    q = deque()
    q.append(root)
    idx = 1
    while(len(q) != 0):
        cur = q.popleft()
        if(idx >= len(node_list)):
            left = None
        else:
            if(node_list[idx] is None):
                left = None
            else:
                left = TreeNode(node_list[idx])
                q.append(left)
        idx+=1
        if(idx >= len(node_list)):
            right = None
        else:
            if(node_list[idx] is None):
                right = None
            else:
                right = TreeNode(node_list[idx])
                q.append(right)
        if(cur):
            cur.left = left
            cur.right = right
        idx+=1
        
    return root

    
# if __name__ == "__main__":
#     null = None
#     root = [3,2,3,null,3,null,1]
#     list2binary_tree(root)