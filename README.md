
## 🔁 What Is a Recursive Function?

A **recursive function** is a function that **calls itself** in order to solve a problem. It breaks the problem down into smaller and smaller sub-problems until it reaches a **base case**—a condition that stops the recursion.

### 🧠 The Two Pillars of Recursion:

1. **Base Case** – the condition under which the function stops calling itself.
2. **Recursive Case** – the part where the function calls itself with modified input.

### ✅ Example:

```python
def factorial(n):
    if n == 0:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive call
```

Calling `factorial(4)` results in:

```
4 * factorial(3)
→ 3 * factorial(2)
→ 2 * factorial(1)
→ 1 * factorial(0)
→ 1
→ Final result: 24
```

### 🔥 Why Recursion Matters:

- Elegant solutions for divide-and-conquer problems.
- Common in algorithms like DFS, backtracking, and dynamic programming.
- Appears frequently in coding interviews.

---

## ⚙️ What Are Generators?

A **generator** is a special kind of Python function that **yields values one at a time**, instead of returning them all at once. This allows your program to generate sequences **lazily**—meaning items are produced only when needed.

### ✅ Example:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Using the generator:

```python
for number in countdown(5):
    print(number)
```

Output:
```
5
4
3
2
1
```

### 💡 What's So Special About Generators?

- They **save memory**. No need to store the whole list in memory.
- They're perfect for working with **large datasets**, **streams**, or **infinite sequences**.
- They preserve their state between each iteration, resuming from where they left off.

