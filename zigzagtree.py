class Tree():

    def __init__(self, head):
        self.head = head

    def __repr__(self):
        return f"head: {self.head}, children1: {self.head.children}"

class Node():
    
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __repr__(self):
        return f"{self.data}"


def zigzag(tree):
    """
    
    >>> four, five, six, seven = Node(4), Node(5), Node(6), Node(7)
    >>> two, three = Node(2, [four, five]), Node(3, [six, seven])
    >>> one = Node(1, [two, three])
    >>> tree = Tree(one)
    >>> zigzag(tree)
    [[1], [3, 2], [4, 5, 6, 7]]
    """

    current_lvl = [tree.head]
    left_to_right = True
    output = []
    
    def add_children(level):

        level = level[:]
        next_level = []
        while level:        
            next_level.extend(level.pop(0).children)

        return next_level
        
    to_see = add_children(current_lvl) 

    while current_lvl:
        if left_to_right == True:
            output.append(current_lvl)
            left_to_right = False
        elif left_to_right == False:
            output.append(current_lvl[-1::-1])
            left_to_right = True
        
        current_lvl = to_see
        to_see = add_children(current_lvl)
    
    return output

