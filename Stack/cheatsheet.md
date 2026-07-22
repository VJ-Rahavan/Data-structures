Perfect. Here's a **concept-only monotonic stack cheat sheet**—the kind you can quickly review before interviews.

# Monotonic Stack Cheat Sheet

## Step 1: Is it asking for **Next** or **Previous**?

| Question | Traverse     |
| -------- | ------------ |
| Next     | Right → Left |
| Previous | Left → Right |

---

## Step 2: Is it asking for **Greater** or **Smaller**?

| Question | Stack Maintains      |
| -------- | -------------------- |
| Greater  | Monotonic Decreasing |
| Smaller  | Monotonic Increasing |

---

## Step 3: Pop Rule

| Looking For           | Remove Everything That Is... |
| --------------------- | ---------------------------- |
| Next/Previous Greater | Less than or Equal (`<=`)    |
| Next/Previous Smaller | Greater than or Equal (`>=`) |

Think of it as:

- Want **Greater** → Remove everything **not greater**.
- Want **Smaller** → Remove everything **not smaller**.

---

# The Four Classic Problems

| Problem                        | Traverse     | Stack      | Pop Condition |
| ------------------------------ | ------------ | ---------- | ------------- |
| Next Greater Element (NGE)     | Right → Left | Decreasing | `<=`          |
| Next Smaller Element (NSE)     | Right → Left | Increasing | `>=`          |
| Previous Greater Element (PGE) | Left → Right | Decreasing | `<=`          |
| Previous Smaller Element (PSE) | Left → Right | Increasing | `>=`          |

---

# Value vs Index

Store **values** when:

- The answer is the element itself.
- You only compare element values.

Store **indices** when:

- You need the position.
- You need distances (e.g., Daily Temperatures, Stock Span).
- The problem asks for widths or ranges (e.g., Largest Rectangle in Histogram).

---

# Equality Rule

| Need                    | Remove |
| ----------------------- | ------ |
| Strictly Greater (`>`)  | `<=`   |
| Strictly Smaller (`<`)  | `>=`   |
| Greater or Equal (`>=`) | `<`    |
| Smaller or Equal (`<=`) | `>`    |

---

# General Thought Process

For each element:

1. Remove elements that can never be the answer.
2. The current top (if any) is the answer.
3. Push the current element for future elements.

---

# Common Interview Problems

### Nearest Element Problems

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element

### Range Problems

- Largest Rectangle in Histogram
- Maximal Rectangle
- Sum of Subarray Minimums
- Sum of Subarray Ranges

### Span Problems

- Stock Span
- Daily Temperatures

### Simulation Problems

- Asteroid Collision
- Remove K Digits
- Remove Duplicate Letters

---

# How to Recognize a Stack Problem

Look for phrases like:

- Next greater
- Next smaller
- Previous greater
- Previous smaller
- Nearest greater/smaller
- First greater/smaller on the left/right
- Span
- Days until...
- Visible buildings
- Histogram
- Collision
- Remove digits/characters while maintaining an order

---

# 5-Second Interview Decision Tree

```text
Is it asking for the nearest element?
        │
        ▼
Left? or Right?
        │
        ▼
Previous       Next
        │
        ▼
Greater? or Smaller?
        │
        ▼
Greater → Decreasing Stack
Smaller → Increasing Stack
        │
        ▼
Traverse:
Left  → Previous
Right → Next
        │
        ▼
Pop everything that cannot be the answer.
```

## Golden Rule

> **The stack always contains only candidates that could still answer future elements.**
> Whenever an element can no longer be the answer for anyone, remove it immediately.

This single principle explains why monotonic stacks work across almost all interview problems.
