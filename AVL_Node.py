NB_ROT = 0


def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0


class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def rot_left(self):
        global NB_ROT
        self._right._left = self
        self._right = None
        NB_ROT += 1
        return self._right, 0

    def rot_right(self):
        global NB_ROT
        self._left._right = self
        self._left = None
        NB_ROT += 1
        return self._left, 0

    def insert_(self, value):
        if self._left is None and self._value > value:
            self._left = AVL_Node(value)
            self._balance += 1
            return self, 1

        elif self._right is None and value > self._value:
            self._right = AVL_Node(value)
            self._balance -= 1
            return self, -1

        elif self._right is None and self._right is None:
            if self._value > value:
                self._left = AVL_Node(value)
                return self, 1
            else:
                self._right = AVL_Node(value)
                return self, -1


        elif self._value == value:
            return self, 0

        if self._value > value:
            self._left, balance = self._left.insert_(value)
            self._balance += balance

        else:
            self._right, balance = self._right.insert_(value)
            self._balance += balance

        if self._balance <= -2:
            return self.rot_left()

        elif self._balance >= 2:
            return self.rot_right()

        return self, balance

    def insert(self, value):
        return self.insert_(value)[0]

    def tree_print(self):
        if self._left is not None:
            self._left.tree_print()
        print(self._value, self._balance)

        if self._right is not None:
            self._right.tree_print()

bst = AVL_Node(42)
bst = bst.insert(69)
bst = bst.insert(20)
bst = bst.insert(53)
bst = bst.insert(80)
bst = bst.insert(30)
bst = bst.insert(10)
bst = bst.insert(1)
bst = bst.insert(800)

bst = bst.rot_left()

bst.tree_print()

