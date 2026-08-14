# Heap — DSA Notes

## 1. What is a Heap?

A **Heap** is a **complete binary tree** that follows a special ordering property.

Two types:

### Min Heap

- Parent is **smaller than or equal to** its children.
- Smallest element is always at the **root**.

```text
        1
      /   \
     3     5
    / \   /
   7   8 10
```

### Max Heap

- Parent is **greater than or equal to** its children.
- Largest element is always at the **root**.

```text
        10
      /    \
     8      5
    / \    /
   7   3  1
```

---

# 2. Important Property

A heap is a **Complete Binary Tree**.

That means:

- Every level is completely filled except possibly the last.
- The last level is filled **from left to right**.

Because of this, heaps are usually implemented using an **array**, not tree nodes.

---

# 3. Heap Array Representation

For an element at index `i`:

### 0-based indexing

```text
Parent       = (i - 1) // 2
Left child   = 2 * i + 1
Right child  = 2 * i + 2
```

Example:

```text
Heap:

        10
       /  \
      8    5
     / \
    7   3
```

Array:

```text
[10, 8, 5, 7, 3]
```

For index `1`:

```text
value = 8

left  = 2(1) + 1 = 3 → 7
right = 2(1) + 2 = 4 → 3
```

---

# 4. Core Heap Operations

| Operation                |       Time |
| ------------------------ | ---------: |
| Get min/max              |     `O(1)` |
| Insert                   | `O(log n)` |
| Delete root              | `O(log n)` |
| Heapify                  | `O(log n)` |
| Build Heap               |     `O(n)` |
| Search arbitrary element |     `O(n)` |

**Important:** A heap is **not a sorted data structure**.

It only guarantees the relationship between **parent and children**.

---

# 5. Insert

Suppose we have a Min Heap:

```text
[2, 4, 5, 8, 10]
```

Insert `3`.

### Step 1 — Add at the end

```text
[2, 4, 5, 8, 10, 3]
```

### Step 2 — Compare with parent

`3 < 5`, so swap:

```text
[2, 4, 3, 8, 10, 5]
```

Now:

```text
3 > 2
```

Stop.

This process is called:

**Heapify Up / Bubble Up / Sift Up**

---

# 6. Delete Root

For a Min Heap:

```text
[2, 4, 3, 8, 10, 5]
```

Remove `2`.

### Step 1

Move last element to root:

```text
[5, 4, 3, 8, 10]
```

### Step 2

Compare `5` with children:

```text
       5
      / \
     4   3
```

Smallest child is `3`.

Swap:

```text
[3, 4, 5, 8, 10]
```

This process is called:

**Heapify Down / Bubble Down / Sift Down**

---

# 7. Heapify

Heapify means **restoring the heap property**.

There are two directions:

```text
Insert → Heapify Up

Delete root → Heapify Down
```

### Min Heap

During heapify down:

```text
Choose the smaller child.
```

### Max Heap

During heapify down:

```text
Choose the larger child.
```

---

# 8. Build Heap

Given an arbitrary array:

```text
[5, 3, 8, 1, 2, 7]
```

We can convert it into a heap.

Start from the **last non-leaf node**:

```text
last_non_leaf = n // 2 - 1
```

Then heapify downward toward index `0`.

### Important

Building a heap takes:

```text
O(n)
```

Not `O(n log n)`.

This is a common interview question.

---

# 9. Why Start From `n//2 - 1`?

In a 0-based array:

```text
Left child  = 2i + 1
Right child = 2i + 2
```

All nodes from:

```text
n//2
```

onwards are **leaf nodes**.

Leaves already satisfy the heap property because they have no children.

Therefore, start at:

```text
n//2 - 1
```

---

# 10. Priority Queue

One of the **most important applications of Heap** is a **Priority Queue**.

Instead of processing elements based on insertion order, we process them based on priority.

Example:

```text
Tasks:

Normal → priority 3
Urgent → priority 1
Low    → priority 5
```

A Min Heap can always give us the highest-priority item:

```text
priority 1
```

Python:

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heapq.heappop(heap))  # 1
```

---

# 11. Max Heap in Python

Python's `heapq` provides a **Min Heap**.

For Max Heap, use negative values:

```python
import heapq

heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)

print(-heapq.heappop(heap))  # 20
```

---

# 12. Heap Sort

Heap Sort works using a heap.

For ascending order:

1. Build a Max Heap.
2. Take the largest element from the root.
3. Move it to the end.
4. Heapify the remaining elements.
5. Repeat.

Complexity:

```text
Time  → O(n log n)
Space → O(1) auxiliary
```

---

# 13. Heap vs BST

| Heap                                | BST                                   |
| ----------------------------------- | ------------------------------------- |
| Complete binary tree                | Binary search property                |
| Root gives min/max                  | Root doesn't necessarily give min/max |
| Good for priority queue             | Good for ordered searching            |
| Search arbitrary element: `O(n)`    | Average search: `O(log n)`            |
| Min/Max: `O(1)`                     | Depends on tree                       |
| Used in scheduling, Dijkstra, Top-K | Used for ordered data                 |

---

# 14. Most Important Heap Patterns

For interviews, recognize these immediately:

### Pattern 1 — Top K

> Find K largest/smallest elements.

Usually use a **heap of size K**.

```text
Find K largest
→ Min Heap of size K
```

```text
Find K smallest
→ Max Heap of size K
```

---

### Pattern 2 — Kth Largest

```text
Maintain Min Heap of size K.
```

The root becomes the **Kth largest**.

---

### Pattern 3 — Kth Smallest

```text
Maintain Max Heap of size K.
```

The root becomes the **Kth smallest**.

---

### Pattern 4 — Merge K Sorted Lists

Use a **Min Heap** containing the smallest current element from each list.

Very common interview problem.

---

### Pattern 5 — Two Heaps

Used when you need to continuously find the **median**.

```text
Max Heap → smaller half
Min Heap → larger half
```

This is the classic **Median from Data Stream** pattern.

---

# 15. Heap Questions You Should Know

For interview preparation, prioritize these:

### Easy

1. Implement Min Heap
2. Implement Max Heap
3. Build Heap
4. Heap Sort

### Medium

5. Kth Largest Element
6. Kth Smallest Element
7. Top K Frequent Elements
8. K Closest Points to Origin
9. Merge K Sorted Lists
10. Task Scheduler

### Important

11. Find Median from Data Stream
12. Sliding Window Median
13. Reorganize String
14. Smallest Range Covering Elements from K Lists

---

## 🔥 Interview Cheat Sheet

Remember this:

```text
Heap
│
├── Complete Binary Tree
│
├── Min Heap
│     └── smallest at root
│
├── Max Heap
│     └── largest at root
│
├── Array representation
│     ├── parent = (i-1)//2
│     ├── left   = 2i+1
│     └── right  = 2i+2
│
├── Insert
│     └── Heapify Up → O(log n)
│
├── Delete Root
│     └── Heapify Down → O(log n)
│
├── Get Min/Max
│     └── O(1)
│
├── Build Heap
│     └── O(n)
│
└── Main use
      ├── Priority Queue
      ├── Top K
      ├── Kth Largest/Smallest
      ├── Merge K Lists
      └── Median
```
