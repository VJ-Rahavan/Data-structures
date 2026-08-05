Here's a **2-minute interview recap** of the most important **Binary Tree terminology**.

| Term              | Meaning                                          |
| ----------------- | ------------------------------------------------ |
| **Node**          | Each element in the tree.                        |
| **Root**          | Top-most node of the tree.                       |
| **Edge**          | Connection between two nodes.                    |
| **Parent**        | A node that has children.                        |
| **Child**         | Node directly below a parent.                    |
| **Sibling**       | Nodes with the same parent.                      |
| **Leaf Node**     | Node with no children.                           |
| **Internal Node** | Node with at least one child.                    |
| **Ancestor**      | Any node on the path from the root to a node.    |
| **Descendant**    | Any node below a particular node.                |
| **Subtree**       | A tree formed by a node and all its descendants. |

---

## Depth vs Level vs Height

```
        A
      /   \
     B     C
    / \
   D   E
```

### Depth

Number of **edges from the root** to the node.

```
Depth(A) = 0
Depth(B) = 1
Depth(D) = 2
```

---

### Level

Some books define:

```
Level = Depth + 1
```

So

```
Level(A) = 1
Level(B) = 2
Level(D) = 3
```

> Interviews usually use **depth** instead of level.

---

### Height of a Node

Number of **edges on the longest path from that node to a leaf**.

```
Height(D) = 0
Height(E) = 0
Height(B) = 1
Height(C) = 0
Height(A) = 2
```

**Height is calculated bottom-up.**

---

### Height of Tree

Height of the root.

```
Height(Tree) = Height(Root)
```

---

## Size

Total number of nodes.

```
    1
   / \
  2   3
 /
4

Size = 4
```

---

## Degree

Number of children a node has.

```
Leaf -> Degree = 0
Node with one child -> Degree = 1
Node with two children -> Degree = 2
```

Maximum degree of a binary tree = **2**.

---

## Path

Sequence of connected nodes.

```
A → B → D
```

Length of path = number of **edges**.

```
A → B → D
Length = 2
```

---

## Distance

Number of edges between two nodes.

```
D ↔ E = 2
(D → B → E)
```

---

## Diameter

The **longest path between any two nodes** in the tree.

It may or may not pass through the root.

A common recursive formula is:

```
Diameter through a node =
Height(left) + Height(right)
```

The overall diameter is the maximum value across all nodes.

---

## Balanced Tree

For every node,

```
|Height(left) - Height(right)| ≤ 1
```

---

## Complete Binary Tree

- Every level is completely filled except possibly the last.
- Last level is filled from **left to right**.

---

## Full Binary Tree

Every node has either:

- 0 children, or
- 2 children

No node has exactly one child.

---

## Perfect Binary Tree

- All internal nodes have 2 children.
- All leaf nodes are at the same level.

---

## Skewed Tree

Every node has only one child.

```
1
 \
  2
   \
    3
     \
      4
```

Height = Number of nodes − 1.

---

## Binary Search Tree (BST)

For every node:

```
Left subtree < Root < Right subtree
```

---

## Traversals

### DFS

- Preorder → Root → Left → Right
- Inorder → Left → Root → Right
- Postorder → Left → Right → Root

### BFS

- Level Order Traversal (level by level using a queue)

---

## Interview Formula Sheet

```
Depth(node)
= Root → Node

Height(node)
= Node → Deepest Leaf

Height(Tree)
= Height(Root)

Diameter
= Longest path between two nodes

Leaf
= No children

Degree
= Number of children

Size
= Number of nodes

Balanced
= Height difference ≤ 1

Complete
= Last level filled left to right

Full
= Every node has 0 or 2 children

Perfect
= Full + all leaves at same level
```

If you're starting tree problems, these are the core terms that appear in nearly every interview.
