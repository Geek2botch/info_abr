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
        NB_ROT += 1
        head = self._right
        temp = head._left
        head._left = self
        self._right = temp
        head._left._balance = 0
        head._balance = 0
        return head

    def rot_right(self):
        global NB_ROT
        NB_ROT += 1
        head = self._left
        temp = head._right
        head._right = self
        self._left = temp
        head._right._balance = 0
        head._balance = 0
        return head

    def node_balance(self):
        if self._balance > 1:
            if self._left._balance <= -1:
                self._left = self._left.rot_left()
            return self.rot_right()
        else:
            if self._right._balance >= 1:
                self._right = self._right.rot_right()
            return self.rot_left()


    def new_balance(self, delta):
        self._balance += delta
        if 1 >= self._balance >= -1:
            return self
        else:
            return self.node_balance()

    def insert_(self, value):
        if self._value == value:
            return None

        if value < self._value:
            if self._left is None:
                self._left = AVL_Node(value)
                return self.new_balance(1)
            else:
                old_bal = self._left._balance
                node = self._left.insert_(value)
                if node is None:
                    return None
                else:
                    self._left = node
                    if old_bal == 0 and old_bal != node._balance:
                        node = self.new_balance(1)
                    else:
                        node = self
                return node
        else:
            if self._right is None:
                self._right = AVL_Node(value)
                return self.new_balance(-1)
            else:
                old_bal = self._right._balance
                node = self._right.insert_(value)
                if node is None:
                    return None
                else:
                    self._right = node
                    if old_bal == 0 and old_bal != node._balance:
                        node = self.new_balance(-1)
                    else:
                        node = self
                    return node

    def insert(self, value):
        node = self.insert_(value)
        return self if node is None else node


