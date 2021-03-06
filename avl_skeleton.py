# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


def main():
    print("aa")


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = AVLNode()
        self.right = AVLNode()
        self.parent = None
        self.height = 0
        self.size = 1
        self.balanceFactor = 0

    """Constructor for virtual Node

        
    """
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.balanceFactor = 0

    """returns Node size
        @rtype: AVLNode
        @returns: size
        """
    def getSize(self):
        return self.size
    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """update balance factor
    
    """
    def updateBalanceFactor(self):
        self.balanceFactor = self.getLeft().getHeight() - self.getRight().getHeight()

    """return balance factor
    @rtype: int
    @return: balanceFactor
        """

    def getBalanceFactor(self):
        return self.balanceFactor

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height


    """sets size

        @type node: int
        @param node: a node
        """

    def setSize(self, i):
        self.size = i

    """Increase Size by 1
        @param node: a node
        """
    def increaseSizeByOne(self):
        self.size = self.size + 1

    """sets left child

        @type node: AVLNode
        @param node: a node
        """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        if self.isRealNode():
            self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        if self.height == -1:
            return False
        return True


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.first = None
        self.last = None
        self.length = 0

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.root is None

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return None

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        if not (0 <= i <= self.length):
            return 0
        self.length = self.length + 1
        nodeToInsert = AVLNode(val)
        if i == 0 and self.root is None:
            self.root = nodeToInsert
            return 0
        if i == 0:
            self.first = nodeToInsert
        if i == self.getRoot().getSize - 1:
            self.last = nodeToInsert

        self.insertRec(i, self.getRoot(), nodeToInsert)
        parentNode = nodeToInsert.getParent()

        rotateCounter = 0

        while parentNode is not None:
            parentLastHeight = parentNode.getHeight()
            parentNode.updateHeight()
            parentNode.updateBalanceFactor()
            bf = parentNode.getBalanceFactor()
            if abs(bf) <= 1 and parentNode.getHeight() == parentLastHeight:
                return rotateCounter
            elif abs(bf) <= 1 and parentNode.getHeight() != parentLastHeight:
                parentNode = nodeToInsert.getParent()
                continue
            elif abs(bf) == 2:
                return
            return 0


    def insertRec(self, i, root, nodeToInsert):
        if i == 0 and not root.getLeft().isRealNode():
            root.SetLeft(nodeToInsert)
            nodeToInsert.setParent(root)
            return
        if i == 1 and not root.getRight().isRealNode():
            root.setRight(nodeToInsert)
            nodeToInsert.setParent(root)
            return
        leftTreeSize = root.getLeft().getSize()
        if i <= leftTreeSize:
            root.increaseSizeByOne()
            self.insertRec(i, root.getLeft, nodeToInsert)
        else:
            root.increaseSizeByOne()
            self.insertRec(i - (leftTreeSize + 1), root.getRight(), nodeToInsert)
        return
    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        return -1

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.last

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return self.listToArrayRec(self.getRoot())

    def listToArrayRec(self , node):
        if not node.isRealNode():
            return []
        return self.listToArrayRec(node.getLeft()) + [node.getValue()] + self.listToArrayRec(node.getRight)
    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return None

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


