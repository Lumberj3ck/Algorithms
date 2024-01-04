from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = None, neighbors = None):
       self.val = val 
       self.neighbors = neighbors if neighbors else None

# travers through graph
# get the first element create new node with Node(val=el.val, neighbours=el.val)
# put new node to the list and put this node to dict visited with val as the key and node as the value
# then add childrens to the queue and iterate over this queue 
# check if this node is visited[el.val) if yes skip 
# Wow you can actually can check presense of key in dict just like this
# key in dict(key: value)


def clone_graph(node: Node) -> Optional[Node]:
    '''
    this function creates deep copy of the graph
    so for every node have to create new ones 
    
    Iterate over every neighbour for curent node
    create new node for every neighbour
    every iteration add this new neighbour we just created
    to the neighbours of current node

    It is like we got this node and immediately add it to cur_node

    And the most important step is to store this new created node
    so we can access it 

    The process is pretty straight forward
    1. Got new node from queue
    2. Create neighbour nodes 
    3. Add every neighbour node to the main
    4. Lastly we return node with start value

    We do not create cur node, because it have been already created when 
    we stored neighbour values of first node

    '''
    clones = {node.val: Node(node.val, [])}
    queue = [node] 
    
    if not node:
        return node

    while queue:
        cur = queue.pop(0) 
        cur_node = clones[cur.val] 

        for neighbor in cur.neighbors:
            if neighbor.val not in clones:
                clones[neighbor.val] = Node(val=neighbor.val, neighbors=[])  
                queue.append(neighbor)

            cur_node.neighbors.append(clones[neighbor.val])

    return clones[node.val]

