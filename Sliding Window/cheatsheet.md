# Sliding Window Cheat Sheet

---

# What is Sliding Window?

A technique used to process **contiguous subarrays or substrings** efficiently by maintaining a window instead of recalculating everything.

Instead of checking every subarray (**O(n²)**), move the window one step at a time (**O(n)** in many cases).

---

# When Should You Think of Sliding Window?

Look for phrases like:

- Subarray
- Substring
- Contiguous
- Consecutive
- Longest
- Shortest
- Maximum
- Minimum
- At most K
- Exactly K
- Sum/Product
- Distinct characters

> **If the problem is about a contiguous range, sliding window should be one of your first ideas.**

---

# Two Types of Sliding Window

| Type            | Window Size         |
| --------------- | ------------------- |
| Fixed Window    | Fixed length (K)    |
| Variable Window | Expands and shrinks |

---

# 1. Fixed Window

### Used When

The window size is given.

Keywords:

- Size K
- Length K
- Every K elements

Examples:

- Maximum sum of size K
- Average of K elements
- Maximum vowels in substring of length K

### Process

1. Build first window.
2. Remove left element.
3. Add right element.
4. Update answer.
5. Repeat.

---

# 2. Variable Window

### Used When

The window size changes based on a condition.

Keywords:

- Longest
- Shortest
- At most K
- At least K
- Distinct
- No duplicates

### Process

1. Expand right pointer.
2. If window becomes invalid, move left pointer until valid.
3. Update answer.

---

# Common Conditions

| Condition                    | Window Action |
| ---------------------------- | ------------- |
| Sum > target                 | Shrink        |
| Sum < target                 | Expand        |
| Too many distinct characters | Shrink        |
| Duplicate found              | Shrink        |
| Window valid                 | Update answer |
| Need more elements           | Expand        |

---

# Fixed vs Variable

| Fixed                     | Variable                    |
| ------------------------- | --------------------------- |
| Window size never changes | Window grows and shrinks    |
| Left moves with right     | Left moves only when needed |
| Simpler                   | More common in interviews   |

---

# Common Problem Types

## Sum Problems

Examples:

- Maximum sum of size K
- Minimum size subarray sum

---

## String Problems

Examples:

- Longest substring without repeating characters
- Longest repeating character replacement
- Minimum window substring
- Permutation in string

---

## Distinct Character Problems

Examples:

- At most K distinct characters
- Exactly K distinct characters
- Fruit Into Baskets

---

## Binary Array Problems

Examples:

- Max consecutive ones
- Longest ones after flipping K zeros

---

## Frequency Problems

Maintain counts of elements or characters.

Useful for:

- Anagrams
- Distinct characters
- Replacement problems

---

# Recognizing Sliding Window

| If you see...        | Think...                                             |
| -------------------- | ---------------------------------------------------- |
| Contiguous array     | Sliding Window                                       |
| Contiguous substring | Sliding Window                                       |
| Longest substring    | Variable Window                                      |
| Smallest substring   | Variable Window                                      |
| Size K               | Fixed Window                                         |
| At most K            | Variable Window                                      |
| Exactly K            | Variable Window (often solved via "At Most K" trick) |
| Sum of K elements    | Fixed Window                                         |
| Maximum consecutive  | Variable Window                                      |

---

# Common Data Structures Used

| Requirement       | Data Structure  |
| ----------------- | --------------- |
| Running sum       | Integer         |
| Character count   | HashMap / Array |
| Distinct elements | HashMap         |
| Frequency         | HashMap         |
| Maximum in window | Deque           |

---

# Time Complexity

| Approach       | Complexity        |
| -------------- | ----------------- |
| Brute Force    | O(n²)             |
| Sliding Window | O(n) (most cases) |

Reason:

Each element enters the window once and leaves once.

---

# Common Interview Problems

### Easy

- Maximum Average Subarray I
- Maximum Number of Vowels in a Substring of Given Length
- Contains Duplicate II

### Medium

- Longest Substring Without Repeating Characters
- Fruit Into Baskets
- Longest Repeating Character Replacement
- Permutation in String
- Find All Anagrams in a String
- Minimum Size Subarray Sum
- Max Consecutive Ones III
- Subarray Product Less Than K

### Hard

- Minimum Window Substring
- Sliding Window Maximum (uses a deque)
- Count Number of Nice Subarrays
- Subarrays with K Different Integers

---

# Decision Tree

```text
Is it contiguous?
        │
        ▼
      Yes
        │
        ▼
Is window size fixed?
        │
   ┌────┴────┐
   │         │
 Yes         No
   │         │
Fixed      Variable
Window     Window
```

---

# Golden Principles

1. **Contiguous ⇒ Think Sliding Window.**
2. **Fixed size ⇒ Slide one step at a time.**
3. **Variable size ⇒ Expand first, shrink only when the window becomes invalid.**
4. **Each element should ideally enter and leave the window at most once, giving O(n) time.**

These principles cover the majority of sliding window problems you'll encounter in coding interviews.
