# Day 1 – Tree Fundamentals + Recursive Traversals

## Goal

Before solving tree problems, you need to understand **how trees are organized** and **how recursion naturally works with them**. Almost every tree algorithm uses recursion, so this foundation is critical.

---

# 1. What is a Tree?

A **Tree** is a **hierarchical (parent-child) data structure** made up of nodes connected by edges.

Unlike arrays or linked lists, trees branch into multiple directions.

Example:

```text
        A
      /   \
     B     C
    / \   / \
   D   E F   G
```

- A is connected to B and C.
- B is connected to D and E.
- C is connected to F and G.

Trees are used in:

- File systems
- Organization charts
- HTML DOM
- Decision making
- Databases
- Search algorithms

---

## Why is it called a Tree?

Imagine an upside-down real tree.

```text
        Root
          |
     -------------
     |           |
   Child       Child
   /   \        |
Leaf Leaf     Leaf
```

The root is at the top, and branches grow downward.

---

# 2. Tree Terminology

We'll use the same example throughout.

```text
          A
        /   \
       B     C
      / \   / \
     D   E F   G
```

---

## Root

The **topmost node** of the tree.

There is only **one root**.

Example:

```text
        A
```

Here,

```
Root = A
```

---

## Parent

A node that has one or more children.

Example:

```text
      B
     / \
    D   E
```

B is the parent of D and E.

Similarly,

- A is parent of B and C.
- C is parent of F and G.

---

## Child

A node connected below another node.

Example:

```text
      A
     / \
    B   C
```

B and C are children of A.

---

## Leaf

A node that has **no children**.

Example:

```text
      D
      E
      F
      G
```

Leaf nodes:

```
D
E
F
G
```

Leaf = End node.

---

## Sibling

Nodes having the **same parent**.

Example:

```text
      B
     / \
    D   E
```

D and E are siblings.

Also,

B and C are siblings.

F and G are siblings.

---

## Ancestor

Every node above a node is its ancestor.

Example:

```text
        A
       /
      B
     /
    D
```

Ancestors of D:

```
B
A
```

Ancestors are obtained by moving **upward**.

---

## Descendant

Every node below a node is its descendant.

Example:

```text
        A
       /
      B
     / \
    D   E
```

Descendants of A:

```
B
D
E
```

Descendants are obtained by moving **downward**.

---

## Height

**Height = Number of edges in the longest path from a node down to a leaf.**

Example:

```text
        A
       / \
      B   C
     /
    D
```

Heights:

```
D = 0
B = 1
C = 0
A = 2
```

Tree height = Height of the root.

**Shortcut:**

> Height measures **downward**.

---

## Depth

**Depth = Number of edges from the root to a node.**

Example:

```text
        A
       / \
      B   C
     /
    D
```

Depths:

```
A = 0
B = 1
C = 1
D = 2
```

**Shortcut:**

> Depth measures **upward from the root**.

---

## Level

Level is similar to depth but starts counting from **1** instead of **0**.

Example:

```text
        A
       / \
      B   C
     /
    D
```

Levels:

```
A = Level 1
B = Level 2
C = Level 2
D = Level 3
```

Some books define the root at Level 0. In coding interviews, **Depth** is usually preferred because it starts from 0. Always check the problem statement if it mentions levels.

---

# Height vs Depth

| Height                  | Depth                              |
| ----------------------- | ---------------------------------- |
| Measures downward       | Measures upward                    |
| Node → Leaf             | Root → Node                        |
| Root has maximum height | Root has depth 0                   |
| Leaf height = 0         | Leaf depth depends on its position |

Example:

```text
        A
       /
      B
     /
    D
```

| Node | Height | Depth |
| ---- | ------ | ----- |
| A    | 2      | 0     |
| B    | 1      | 1     |
| D    | 0      | 2     |

---

# 3. Binary Tree Structure

A **Binary Tree** is a tree where **each node can have at most two children**:

- Left child
- Right child

Example:

```text
        10
       /  \
      5   20
     / \    \
    2   7    30
```

Every node has:

- A value
- Left pointer
- Right pointer

Python representation:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

Example:

```python
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)
```

This creates:

```text
        10
       /  \
      5   20
     / \    \
    2   7    30
```

---

# Why Binary Trees?

Limiting each node to two children makes many operations efficient and easier to implement recursively. Binary trees form the basis for several important data structures, including:

- Binary Search Trees (BST)
- Heaps
- AVL Trees
- Red-Black Trees
- Expression Trees
- Huffman Trees

---

# Key Takeaways

- A **tree** is a hierarchical collection of nodes connected by edges.
- The **root** is the topmost node; **leaves** have no children.
- **Parent**, **child**, **siblings**, **ancestors**, and **descendants** describe relationships between nodes.
- **Depth** is the distance from the root to a node.
- **Height** is the distance from a node to its deepest leaf.
- A **binary tree** allows each node to have at most two children: **left** and **right**.
- Understanding these concepts is essential before learning recursion and tree traversals.

# Day 1 (Part 2) – Recursion & Tree Traversals

Once you understand tree structure, the next step is learning **how recursion naturally works on trees**. Almost every tree interview problem is solved using recursion or an iterative version of it.

---

# 1. How Recursion Works on Trees

## Why recursion is perfect for trees

A tree is made up of **smaller trees**.

Look at this tree:

```text
          A
        /   \
       B     C
      / \   / \
     D   E F   G
```

Notice something interesting.

The subtree rooted at **B** is itself a tree.

```text
      B
     / \
    D   E
```

The subtree rooted at **C** is also a tree.

```text
      C
     / \
    F   G
```

Since every subtree is itself a tree, we can solve the whole problem by solving the same problem on smaller subtrees.

This is exactly what recursion does.

---

# Recursive Thinking

Whenever you reach a node:

1. Process the current node (optional)
2. Solve the left subtree
3. Solve the right subtree

Every recursive function follows this idea.

---

## Base Case

Every recursion must stop.

For trees:

```python
if root is None:
    return
```

When there is no node, recursion ends.

---

## Recursive Template

Almost every DFS tree problem follows this structure.

```python
def dfs(root):

    if root is None:
        return

    # Process current node

    dfs(root.left)

    dfs(root.right)
```

Only the position of **"Process current node"** changes.

That gives us three different traversals.

---

# Example Tree

We'll use this tree for every traversal.

```text
          1
        /   \
       2     3
      / \   / \
     4  5  6   7
```

---

# 2. Recursive DFS Traversals

DFS stands for **Depth First Search**.

It explores one branch completely before moving to another.

There are three DFS traversals.

- Preorder
- Inorder
- Postorder

---

# A. Preorder Traversal

### Order

```text
Root
Left
Right
```

Think:

> Visit me first.

---

### Algorithm

```python
def preorder(root):

    if root is None:
        return

    print(root.val)

    preorder(root.left)

    preorder(root.right)
```

---

### Dry Run

Tree:

```text
          1
        /   \
       2     3
      / \   / \
     4  5  6   7
```

Traversal:

```
Visit 1

Go left

Visit 2

Go left

Visit 4

Back

Visit 5

Back

Go right

Visit 3

Visit 6

Visit 7
```

Output

```text
1 2 4 5 3 6 7
```

---

### Memory Trick

```
Root First
```

or

```
NLR

Node
Left
Right
```

---

### Interview Uses

- Copy a tree
- Serialize tree
- Prefix expressions
- Tree construction

---

# B. Inorder Traversal

### Order

```text
Left

Root

Right
```

Think:

> Visit me after finishing my left child.

---

### Algorithm

```python
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.val)

    inorder(root.right)
```

---

### Dry Run

```
Go left

4

Back

2

5

Back

1

Go right

6

3

7
```

Output

```text
4 2 5 1 6 3 7
```

---

### Memory Trick

```
LNR

Left
Node
Right
```

---

### Interview Uses

Very important.

For a **Binary Search Tree (BST)**

Inorder traversal always produces

```
Sorted Order
```

Many BST interview questions rely on this property.

---

# C. Postorder Traversal

### Order

```text
Left

Right

Root
```

Think:

> Visit me after finishing both children.

---

### Algorithm

```python
def postorder(root):

    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.val)
```

---

### Dry Run

```
4

5

2

6

7

3

1
```

Output

```text
4 5 2 6 7 3 1
```

---

### Memory Trick

```
LRN

Left
Right
Node
```

---

### Interview Uses

Useful for:

- Delete tree
- Calculate height
- Evaluate expression tree
- Bottom-up DP
- Subtree problems

---

# Visual Comparison

Tree

```text
          1
        /   \
       2     3
      / \   / \
     4  5  6   7
```

| Traversal | Order               | Output        |
| --------- | ------------------- | ------------- |
| Preorder  | Root → Left → Right | 1 2 4 5 3 6 7 |
| Inorder   | Left → Root → Right | 4 2 5 1 6 3 7 |
| Postorder | Left → Right → Root | 4 5 2 6 7 3 1 |

---

# Easy Way to Remember

```
Preorder

Visit yourself first

Root
Left
Right
```

```
Inorder

Visit yourself in the middle

Left
Root
Right
```

```
Postorder

Visit yourself last

Left
Right
Root
```

---

# 3. Level Order Traversal (Breadth-First Search)

Unlike DFS, **Breadth-First Search (BFS)** visits nodes **level by level**, from top to bottom and left to right.

Example tree:

```text
          1
        /   \
       2     3
      / \   / \
     4  5  6   7
```

Traversal order:

```
Level 1 → 1

Level 2 → 2 3

Level 3 → 4 5 6 7
```

Output

```text
1 2 3 4 5 6 7
```

---

## Why do we use a Queue?

A queue follows **First In, First Out (FIFO)**.

As we visit a node, we add its children to the queue. The node that was added first is processed first, which naturally visits the tree level by level.

---

## Algorithm

1. Create an empty queue.
2. Add the root node to the queue.
3. While the queue is not empty:
   - Remove the front node.
   - Process it.
   - Add its left child (if it exists).
   - Add its right child (if it exists).

---

## Python Code

```python
from collections import deque

def level_order(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
```

---

## Dry Run

Tree:

```text
          1
        /   \
       2     3
      / \   / \
     4  5  6   7
```

| Queue Before | Remove | Queue After Adding Children | Output        |
| ------------ | ------ | --------------------------- | ------------- |
| [1]          | 1      | [2, 3]                      | 1             |
| [2, 3]       | 2      | [3, 4, 5]                   | 1 2           |
| [3, 4, 5]    | 3      | [4, 5, 6, 7]                | 1 2 3         |
| [4, 5, 6, 7] | 4      | [5, 6, 7]                   | 1 2 3 4       |
| [5, 6, 7]    | 5      | [6, 7]                      | 1 2 3 4 5     |
| [6, 7]       | 6      | [7]                         | 1 2 3 4 5 6   |
| [7]          | 7      | []                          | 1 2 3 4 5 6 7 |

---

# DFS vs BFS

| Feature         | DFS                                                         | BFS                                                                      |
| --------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------ |
| Full Form       | Depth First Search                                          | Breadth First Search                                                     |
| Traversal Style | Explore one branch fully before backtracking                | Explore one level at a time                                              |
| Data Structure  | Recursion or Stack                                          | Queue                                                                    |
| Traversal Types | Preorder, Inorder, Postorder                                | Level Order                                                              |
| Common Uses     | Most tree interview problems, recursion, subtree processing | Shortest path in unweighted graphs, level-wise processing, minimum depth |

---

# Key Takeaways

- **Recursion works naturally on trees** because every subtree is itself a tree.
- Every recursive DFS function starts with the base case:

  ```python
  if root is None:
      return
  ```

- **Preorder (Node → Left → Right)**: Visit the current node first.
- **Inorder (Left → Node → Right)**: For BSTs, this produces values in sorted order.
- **Postorder (Left → Right → Node)**: Process children before the parent, useful for bottom-up computations.
- **Level Order (BFS)**: Uses a queue to visit nodes level by level instead of following a single branch.
