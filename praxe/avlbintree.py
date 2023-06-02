import sys

sys.setrecursionlimit(1_000_000)


class Node:
    def __init__(
        self, key, data, par_ref=None, my_side=None, left=None, right=None
    ) -> None:
        self.key = key
        self.data = data
        self.my_side = my_side  # 0 left, 1 right
        self.par_ref = par_ref
        self.left = left
        self.right = right

    def bf_ld(self) -> int:
        if isinstance(self.left, Node):
            return self.left.bf_max() + 1
        else:
            return 0

    def bf_rd(self) -> int:
        if isinstance(self.right, Node):
            return self.right.bf_max() + 1
        else:
            return 0

    def bf(self) -> int:
        return self.bf_ld() - self.bf_rd()

    def bf_max(self) -> int:
        return max(self.bf_ld(), self.bf_rd())


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key, data):
        if isinstance(self.root, Node):
            self._insert(key, data, self.root)
        else:
            self.root = Node(key, data)

    def _insert(self, key, data, node: Node):
        if key < node.key:
            if isinstance(node.left, Node):
                self._insert(key, data, node.left)
            else:
                node.left = Node(key, data, node, 0)
        elif key > node.key:
            if isinstance(node.right, Node):
                self._insert(key, data, node.right)
            else:
                node.right = Node(key, data, node, 1)
        balance = node.bf()

        if isinstance(node.left, Node) and isinstance(node.right, Node):
            if balance > 1 and key < node.left.key:
                return self.rotate_right(node)

            elif balance < -1 and key > node.right.key:
                return self.rotate_left(node)

            elif balance > 1 and key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            elif balance < -1 and key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

    def rotate_left(self, node: Node) -> Node:
        new_root: Node = node.right  # type: ignore
        node.right: Node = new_root.left  # type: ignore
        new_root.left: Node = node  # type: ignore
        return new_root

    def rotate_right(self, node: Node) -> Node:
        new_root: Node = node.left  # type: ignore
        node.left: Node = new_root.right  # type: ignore
        new_root.right: Node = node  # type: ignore
        return new_root


buk: AVLTree = AVLTree()

# insert random numbers and data
for i in range(2000):
    print(i, end="\r")
    buk.insert(i, str(i))
