from typing import Any, Generator


class Node:
    def __init__(self, key, data, left=None, right=None) -> None:
        self.key: int = key
        self.data: Any = data
        self.left: Node = left  # type: ignore
        self.right: Node = right  # type: ignore

    def __repr__(self) -> str:
        return f"Node({self.key}, {self.data}, {True if self.left else False}, {True if self.right else False})"

    # def __iter__(self):
    #     yield f"{self.key}: {str(self.data)}"
    #     yield self.left
    #     yield self.right


class Tree:
    def __init__(self) -> None:
        self.root: Node = None  # type: ignore

    def insert(self, key, data) -> None:
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert(key, data, self.root)

    def _insert(self, key, data: Any, node: Node) -> None:
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert(key, data, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert(key, data, node.right)
        else:
            raise ValueError("Key already exists")

    def find(self, key) -> Any:
        if self.root is None:
            raise ValueError("Tree is empty")
        else:
            return self._find(key, self.root)

    def _find(self, key, node: Node) -> Any:
        if key == node.key:
            return node.data
        elif key < node.key:
            if node.left is None:
                raise ValueError("Key not found")
            else:
                return self._find(key, node.left)
        else:
            if node.right is None:
                raise ValueError("Key not found")
            else:
                return self._find(key, node.right)

    def delete(self, key) -> None:
        if self.root is None:
            raise ValueError("Tree is empty")
        else:
            self._delete(key, self.root)

    def _delete(self, key, node: Node) -> None:
        if key < node.key:
            if node.left is None:
                raise ValueError("Key not found")
            elif node.left.key == key:
                node.left = self._delete_node(node.left)
            else:
                self._delete(key, node.left)
        elif key > node.key:
            if node.right is None:
                raise ValueError("Key not found")
            elif node.right.key == key:
                node.right = self._delete_node(node.right)
            else:
                self._delete(key, node.right)
        else:
            self.root = self._delete_node(node)

    def _delete_node(self, node: Node) -> Any:
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left

    # def detuplic(self, tup: tuple) -> list[str]:
    #     out = []
    #     out.append(tup[0])
    #     for t in tup[1::]:
    #         if isinstance(t, Node):
    #             out.append(self.detuplic(tuple(t)))
    #         else:
    #             out.append(str(t).center(25, " "))
    #     return out

    # def depth(self) -> int:
    #     ll = self.detuplic(tuple(self.root))
    #     return self._depth(ll)

    # def _depth(self, lst: list) -> int:
    #     if isinstance(lst, str):
    #         return 0
    #     else:
    #         return max(self._depth(x) for x in lst) + 1

    # def stringuj(self, lst: list, depth: int, out: list):
    #     for el in lst:
    #         if isinstance(el, list):
    #             self.stringuj(el, depth + 1, out)
    #         elif isinstance(el, str):
    #             out[depth] += str(el) + ";"
    #         else:
    #             raise ValueError("Something wrong, I can feel it!")

    # def __repr__(self) -> str:
    #     tup: tuple[str | Node, ...] = tuple(self.root)
    #     out: list[str] = self.detuplic(tup)

    #     depth = self._depth(out)

    #     out2 = ["" for _ in range(depth)]

    #     d = 0
    #     for el in out:
    #         if isinstance(el, list):
    #             self.stringuj(el, d + 1, out2)
    #         elif isinstance(el, str):
    #             out2[d] += str(el) + ";"
    #         else:
    #             raise ValueError("Something wrong, I can feel it!")

    #     return "\n".join(out2)


buk: Tree = Tree()

import random

for _ in range(10):
    key: int = random.randint(0, 100000)
    data: float = random.uniform(-100000, 100000)
    try:
        buk.insert(key, data)
    except ValueError:
        pass

print(buk)
# print(buk.depth())
# for _ in range(100):
#     key = random.randint(0, 100000)
#     try:
#         buk.find(key)
#         buk.delete(key)
#     except ValueError:
#         pass
