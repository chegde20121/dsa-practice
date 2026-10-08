# DSA Notes: Time Complexity & Space Complexity

> Goal: Understand what Big-O means, how to calculate time/space complexity from code, recognize common patterns quickly, and use complexity analysis during DSA interviews.

---

# 1. What is Complexity Analysis?

When solving a DSA problem, we usually care about two things:

1. **Time Complexity**
   - How does execution time grow as input size `n` grows?

2. **Space Complexity**
   - How does additional memory usage grow as input size `n` grows?

We generally express both using **Big-O notation**.

Example:

```python
for i in range(n):
    print(i)
```

The loop executes `n` times.

```text
Time Complexity = O(n)
Space Complexity = O(1)
```

---

# 2. Why Don't We Measure Actual Seconds?

Suppose:

```python
for i in range(n):
    print(i)
```

For `n = 1000`, one machine might take:

```text
0.01 seconds
```

Another machine might take:

```text
0.003 seconds
```

Actual execution time depends on:

- CPU
- programming language
- compiler/interpreter
- operating system
- hardware
- implementation

Instead, complexity asks:

> How does the amount of work grow when the input grows?

For example:

```text
n = 10       → ~10 operations
n = 100      → ~100 operations
n = 1,000    → ~1,000 operations
n = 1,000,000 → ~1,000,000 operations
```

This is **linear growth**:

```text
O(n)
```

---

# 3. Big-O Notation

Big-O describes the **upper bound / growth rate** of an algorithm as the input becomes large.

For DSA interviews, think of it primarily as:

> How quickly does the work grow relative to `n`?

Example:

```python
x = arr[0]
```

Regardless of whether the array contains 10 elements or 10 million elements, accessing an element by index takes approximately the same amount of work.

Therefore:

```text
O(1)
```

---

# 4. Complexity in Increasing Order

From **best / fastest growing** to **worst / fastest growing**:

| Complexity | Name | Example |
|---|---|---|
| `O(1)` | Constant | Array lookup |
| `O(log n)` | Logarithmic | Binary search |
| `O(√n)` | Square root | Prime checking optimization |
| `O(n)` | Linear | Traverse array |
| `O(n log n)` | Linearithmic | Merge sort |
| `O(n²)` | Quadratic | Nested loops |
| `O(n³)` | Cubic | Three nested loops |
| `O(2^n)` | Exponential | Subset recursion |
| `O(n!)` | Factorial | All permutations |

Therefore:

```text
O(1)
<
O(log n)
<
O(√n)
<
O(n)
<
O(n log n)
<
O(n²)
<
O(n³)
<
O(2^n)
<
O(n!)
```

This order is extremely important to remember.

---

# 5. Growth Comparison

Assume:

```text
n = 10
```

Approximately:

| Complexity | Operations |
|---|---:|
| `O(1)` | 1 |
| `O(log₂ n)` | ~3 |
| `O(n)` | 10 |
| `O(n log₂ n)` | ~33 |
| `O(n²)` | 100 |
| `O(n³)` | 1,000 |
| `O(2^n)` | 1,024 |
| `O(n!)` | 3,628,800 |

Now consider:

```text
n = 100
```

| Complexity | Approximate Operations |
|---|---:|
| `O(1)` | 1 |
| `O(log₂ n)` | ~7 |
| `O(n)` | 100 |
| `O(n log₂ n)` | ~664 |
| `O(n²)` | 10,000 |
| `O(n³)` | 1,000,000 |
| `O(2^n)` | astronomically large |
| `O(n!)` | practically impossible |

This is why complexity matters.

---

# 6. O(1) — Constant Time

The number of operations does not depend on `n`.

Example:

```python
def get_first(arr):
    return arr[0]
```

Complexity:

```text
Time: O(1)
Space: O(1)
```

Other common examples:

```python
x = arr[5]

x = a + b

if x > 10:
    return True

dictionary[key]
```

Average hash-map lookup is generally:

```text
O(1)
```

---

# 7. O(n) — Linear Time

The algorithm processes every element once.

```python
def print_all(arr):
    for x in arr:
        print(x)
```

If:

```text
n = len(arr)
```

the loop executes `n` times.

Therefore:

```text
Time = O(n)
Space = O(1)
```

---

# 8. Multiple Sequential Loops

Example:

```python
for x in arr:
    print(x)

for x in arr:
    print(x)
```

At first you might calculate:

```text
O(n + n)
```

which is:

```text
O(2n)
```

Big-O ignores constant multipliers.

Therefore:

```text
O(n)
```

Not:

```text
O(2n)
```

---

# 9. Why Big-O Ignores Constants

Consider:

```text
O(2n)
O(10n)
O(1000n)
```

As `n` becomes extremely large, all have the same growth pattern:

```text
O(n)
```

Therefore:

```text
O(2n)    → O(n)
O(100n)  → O(n)
O(5n²)   → O(n²)
```

---

# 10. Drop Lower-Order Terms

Consider:

```text
T(n) = n² + n + 10
```

For very large `n`, `n²` dominates.

Therefore:

```text
O(n² + n + 10)
```

becomes:

```text
O(n²)
```

Another example:

```text
O(n³ + n² + n + 100)
```

becomes:

```text
O(n³)
```

## Rule

Keep the **fastest-growing term**.

---

# 11. O(n²) — Nested Loops

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Outer loop:

```text
n
```

Inner loop:

```text
n
```

Total:

```text
n × n
```

Therefore:

```text
O(n²)
```

---

# 12. O(n³)

Three nested loops:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

Operations:

```text
n × n × n
```

Therefore:

```text
O(n³)
```

---

# 13. Important Rule: Sequential vs Nested

This distinction is extremely important.

## Sequential

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

Add complexities:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

## Nested

```python
for i in range(n):
    for j in range(n):
        pass
```

Multiply complexities:

```text
O(n) × O(n)
= O(n²)
```

### Mental rule

```text
Sequential blocks → ADD
Nested blocks     → MULTIPLY
```

---

# 14. Different Input Sizes

Consider:

```python
for x in arr1:
    print(x)

for y in arr2:
    print(y)
```

If:

```text
len(arr1) = n
len(arr2) = m
```

Complexity is:

```text
O(n + m)
```

Do NOT automatically write:

```text
O(n)
```

because the arrays may have different sizes.

---

# 15. Nested Different Inputs

```python
for x in arr1:
    for y in arr2:
        print(x, y)
```

Complexity:

```text
O(n × m)
```

or:

```text
O(nm)
```

---

# 16. O(log n) — Logarithmic Complexity

One of the most important complexities in DSA.

You generally see `O(log n)` when the problem size is repeatedly reduced by some factor.

Usually:

```text
n
n/2
n/4
n/8
n/16
...
1
```

Classic example:

```text
Binary Search
```

---

# 17. Why Binary Search is O(log n)

Suppose the array contains:

```text
16 elements
```

Binary search repeatedly divides the search space in half:

```text
16
8
4
2
1
```

Only around:

```text
4 steps
```

are required.

Mathematically:

```text
2^k = n
```

Taking logarithm:

```text
k = log₂(n)
```

Therefore:

```text
O(log n)
```

---

# 18. Recognizing O(log n) Loops

Example:

```python
i = n

while i > 1:
    i //= 2
```

Values:

```text
n
n/2
n/4
n/8
...
1
```

Therefore:

```text
O(log n)
```

Similarly:

```python
i = 1

while i < n:
    i *= 2
```

Values:

```text
1
2
4
8
16
...
n
```

Also:

```text
O(log n)
```

---

# 19. General Logarithmic Pattern

If you see:

```python
i *= 2
```

or:

```python
i /= 2
```

or:

```python
n = n // 2
```

think:

```text
O(log n)
```

More generally:

```text
multiply/divide problem size by constant
→ logarithmic
```

---

# 20. Does Log Base Matter?

You may technically encounter:

```text
log₂ n
log₃ n
log₁₀ n
```

Big-O generally writes all of them as:

```text
O(log n)
```

because changing logarithm base only changes a constant factor.

---

# 21. O(n log n)

This is common in efficient sorting algorithms.

Examples:

```text
Merge Sort
Heap Sort
Average-case Quick Sort
```

One way it appears:

```python
for i in range(n):

    j = n

    while j > 1:
        j //= 2
```

Outer loop:

```text
O(n)
```

Inner loop:

```text
O(log n)
```

Multiply:

```text
O(n log n)
```

---

# 22. O(√n)

Common in mathematical algorithms.

For example, checking whether a number is prime.

Naive:

```python
for i in range(2, n):
```

Complexity:

```text
O(n)
```

But factors occur in pairs.

If:

```text
a × b = n
```

then at least one factor must be:

```text
<= √n
```

So we only need:

```python
i = 2

while i * i <= n:
    ...
    i += 1
```

Complexity:

```text
O(√n)
```

---

# 23. O(2^n) — Exponential Complexity

Often occurs in recursive algorithms where every call creates two more calls.

Example:

```python
def solve(n):
    if n == 0:
        return

    solve(n - 1)
    solve(n - 1)
```

Recursion tree:

```text
                  n
               /     \
            n-1       n-1
           /   \     /   \
        n-2   n-2  n-2   n-2
```

The number of nodes approximately doubles at each level.

Therefore:

```text
O(2^n)
```

---

# 24. Common Example: Naive Fibonacci

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

Time complexity:

```text
O(2^n)
```

More precisely, Fibonacci recursion grows approximately as:

```text
O(φ^n)
```

but interviews commonly use:

```text
O(2^n)
```

Space complexity:

```text
O(n)
```

because maximum recursion depth is `n`.

---

# 25. O(n!) — Factorial Complexity

Usually occurs when generating every possible permutation.

Example:

```text
ABC
```

Possible permutations:

```text
ABC
ACB
BAC
BCA
CAB
CBA
```

Number:

```text
3! = 6
```

For `n` elements:

```text
n!
```

Therefore:

```text
O(n!)
```

Common example:

```text
Permutations
Traveling Salesman brute force
```

---

# 26. Complexity Cheat Sheet

| Code Pattern | Complexity |
|---|---|
| Single statement | `O(1)` |
| Array index lookup | `O(1)` |
| Hash-map lookup average | `O(1)` |
| Loop through `n` items | `O(n)` |
| Loop through half the array | `O(n)` |
| Two separate `n` loops | `O(n)` |
| Nested `n × n` loops | `O(n²)` |
| Three nested loops | `O(n³)` |
| Divide input by 2 repeatedly | `O(log n)` |
| Multiply counter by 2 repeatedly | `O(log n)` |
| `n` loop containing binary operation | `O(n log n)` |
| Generate all subsets | `O(2^n)` |
| Generate permutations | `O(n!)` |

---

# 27. Important Trap: Loop Running n/2 Times

```python
for i in range(n // 2):
    print(i)
```

Exact operations:

```text
n/2
```

Complexity:

```text
O(n/2)
```

Ignore constant:

```text
O(n)
```

NOT:

```text
O(n/2)
```

---

# 28. Important Trap: Nested Loop Does Not Always Mean O(n²)

Example:

```python
for i in range(n):

    j = 1

    while j < n:
        j *= 2
```

Outer:

```text
O(n)
```

Inner:

```text
O(log n)
```

Therefore:

```text
O(n log n)
```

Not:

```text
O(n²)
```

Always analyze what each loop actually does.

---

# 29. Dependent Nested Loops

Consider:

```python
for i in range(n):

    for j in range(i):
        print(i, j)
```

Inner loop executes:

```text
0
1
2
3
...
n-1
```

Total operations:

```text
0 + 1 + 2 + ... + (n-1)
```

Formula:

```text
n(n-1) / 2
```

Approximately:

```text
n² / 2
```

Drop constant:

```text
O(n²)
```

---

# 30. Useful Mathematical Sums

These appear frequently in complexity analysis.

## Sum of first n integers

```text
1 + 2 + 3 + ... + n
```

Formula:

```text
n(n+1) / 2
```

Complexity:

```text
O(n²)
```

---

## Sum of squares

```text
1² + 2² + ... + n²
```

Formula:

```text
n(n+1)(2n+1) / 6
```

Complexity:

```text
O(n³)
```

---

## Geometric sequence

```text
1 + 2 + 4 + 8 + ... + n
```

Sum:

```text
~2n
```

Therefore:

```text
O(n)
```

This becomes important when analyzing recursion trees.

---

# 31. How to Calculate Time Complexity From Code

Use this process.

## Step 1 — Define the input size

Example:

```python
def search(arr, target):
```

Define:

```text
n = len(arr)
```

---

## Step 2 — Identify loops

Example:

```python
for x in arr:
```

This gives:

```text
O(n)
```

---

## Step 3 — Check nesting

```python
for i in range(n):
    for j in range(n):
```

Multiply:

```text
n × n
```

Therefore:

```text
O(n²)
```

---

## Step 4 — Look for shrinking/growing variables

```python
while n > 1:
    n //= 2
```

Think:

```text
O(log n)
```

---

## Step 5 — Analyze function calls

Example:

```python
arr.sort()
```

Python's sorting algorithm:

```text
O(n log n)
```

So even if you do not explicitly write loops, library calls contribute to complexity.

---

## Step 6 — Combine complexities

Example:

```python
arr.sort()

for x in arr:
    print(x)
```

Complexity:

```text
O(n log n) + O(n)
```

Dominant term:

```text
O(n log n)
```

---

# 32. Dominant-Term Rule

Consider:

```text
O(n² + n)
```

When `n` is very large:

```text
n² >> n
```

So:

```text
O(n² + n)
→ O(n²)
```

Examples:

```text
O(n + log n)       → O(n)

O(n² + n log n)    → O(n²)

O(2^n + n³)        → O(2^n)

O(n! + 2^n)        → O(n!)
```

---

# 33. Best, Average and Worst Case

An algorithm may behave differently depending on input.

Consider linear search:

```python
def search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1
```

## Best case

Target is first element.

```text
O(1)
```

## Worst case

Target is last or absent.

```text
O(n)
```

## Average case

Approximately half the elements are searched.

```text
O(n)
```

Therefore:

| Case | Complexity |
|---|---|
| Best | `O(1)` |
| Average | `O(n)` |
| Worst | `O(n)` |

Unless specified otherwise, interviews commonly ask for the **worst-case Big-O**.

---

# 34. Big-O vs Big-Theta vs Big-Omega

There are three common asymptotic notations.

| Notation | Meaning |
|---|---|
| `O(...)` | Upper bound |
| `Ω(...)` | Lower bound |
| `Θ(...)` | Tight bound |

Example:

```python
for i in range(n):
    print(i)
```

It always runs `n` times.

Therefore:

```text
O(n)
Ω(n)
Θ(n)
```

For most coding interviews, discussion focuses primarily on:

```text
Big-O
```

---

# 35. SPACE COMPLEXITY

Space complexity measures how memory usage grows with input size.

Example:

```python
def sum_array(arr):

    total = 0

    for x in arr:
        total += x

    return total
```

Variables:

```text
total
x
```

These use constant extra memory.

Therefore:

```text
Space Complexity = O(1)
```

Even though the input array contains `n` elements.

---

# 36. Input Space vs Auxiliary Space

This distinction is important.

Suppose:

```python
def sum_array(arr):
```

The input `arr` already exists.

If the question asks for **auxiliary space**, we normally do not count the input itself.

Example:

```python
total = 0
```

Only constant extra memory is created.

Therefore:

```text
Auxiliary Space = O(1)
```

---

# 37. O(n) Space

Example:

```python
def double(arr):

    result = []

    for x in arr:
        result.append(x * 2)

    return result
```

`result` contains `n` elements.

Therefore:

```text
Time  = O(n)
Space = O(n)
```

---

# 38. O(n²) Space

Example:

```python
matrix = []

for i in range(n):

    row = []

    for j in range(n):
        row.append(0)

    matrix.append(row)
```

Matrix contains:

```text
n × n
```

elements.

Therefore:

```text
Space = O(n²)
```

---

# 39. Recursion Uses Space

This is one of the most important space-complexity concepts.

Example:

```python
def countdown(n):

    if n == 0:
        return

    countdown(n - 1)
```

Call stack:

```text
countdown(n)
countdown(n-1)
countdown(n-2)
...
countdown(1)
countdown(0)
```

Maximum stack depth:

```text
n
```

Therefore:

```text
Time  = O(n)
Space = O(n)
```

---

# 40. Recursive Binary Search

```python
def binary_search(arr, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)

    return binary_search(arr, left, mid - 1, target)
```

Problem size halves each time.

Recursion depth:

```text
log n
```

Therefore:

```text
Time  = O(log n)
Space = O(log n)
```

An iterative implementation would have:

```text
Time  = O(log n)
Space = O(1)
```

---

# 41. Recursion Time vs Recursion Space

Do not confuse:

```text
Number of recursive calls
```

with:

```text
Maximum recursion depth
```

Example:

```python
fib(n):
    fib(n-1)
    fib(n-2)
```

Total calls:

```text
~2^n
```

Therefore:

```text
Time = O(2^n)
```

But the deepest branch is:

```text
n → n-1 → n-2 → ... → 0
```

Therefore:

```text
Space = O(n)
```

---

# 42. Data Structure Complexity Cheat Sheet

## Arrays

| Operation | Complexity |
|---|---|
| Access by index | `O(1)` |
| Search unsorted | `O(n)` |
| Append | `O(1)` amortized |
| Insert beginning | `O(n)` |
| Delete beginning | `O(n)` |
| Insert middle | `O(n)` |
| Delete middle | `O(n)` |

---

# 43. Linked List

| Operation | Complexity |
|---|---|
| Access by index | `O(n)` |
| Search | `O(n)` |
| Insert at head | `O(1)` |
| Delete head | `O(1)` |
| Insert after known node | `O(1)` |

---

# 44. Hash Table / Hash Map

Average case:

| Operation | Complexity |
|---|---|
| Insert | `O(1)` |
| Lookup | `O(1)` |
| Delete | `O(1)` |

Worst case:

```text
O(n)
```

because of collisions.

In interviews it is common to state:

```text
Hash-map lookup = O(1) average
```

---

# 45. Stack

| Operation | Complexity |
|---|---|
| Push | `O(1)` |
| Pop | `O(1)` |
| Peek | `O(1)` |

---

# 46. Queue

With an efficient queue/deque implementation:

| Operation | Complexity |
|---|---|
| Enqueue | `O(1)` |
| Dequeue | `O(1)` |
| Peek | `O(1)` |

---

# 47. Heap / Priority Queue

For `n` elements:

| Operation | Complexity |
|---|---|
| Peek min/max | `O(1)` |
| Insert | `O(log n)` |
| Remove min/max | `O(log n)` |
| Build heap | `O(n)` |

One common interview mistake is assuming:

```text
Build Heap = O(n log n)
```

A proper heapify operation can build a heap in:

```text
O(n)
```

---

# 48. Binary Search Tree

For a balanced BST:

| Operation | Complexity |
|---|---|
| Search | `O(log n)` |
| Insert | `O(log n)` |
| Delete | `O(log n)` |

For an unbalanced BST:

```text
1
 \
  2
   \
    3
     \
      4
```

The tree can effectively become a linked list.

Therefore worst case:

```text
O(n)
```

---

# 49. Sorting Complexity

| Algorithm | Best | Average | Worst | Extra Space |
|---|---:|---:|---:|---:|
| Bubble Sort | `O(n)`* | `O(n²)` | `O(n²)` | `O(1)` |
| Selection Sort | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` |
| Insertion Sort | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` |
| Quick Sort | `O(n log n)` | `O(n log n)` | `O(n²)` | typically `O(log n)` average stack |
| Heap Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` |

\* Optimized Bubble Sort can achieve `O(n)` when the input is already sorted.

---

# 50. Python Operation Complexity

Very useful if solving interviews in Python.

## List

```python
arr[i]
```

```text
O(1)
```

---

```python
arr.append(x)
```

```text
O(1) amortized
```

---

```python
arr.pop()
```

```text
O(1)
```

---

```python
arr.pop(0)
```

```text
O(n)
```

because remaining elements shift.

---

```python
x in arr
```

```text
O(n)
```

---

```python
arr.insert(0, x)
```

```text
O(n)
```

---

# 51. Python Dictionary

```python
d[key]
```

Average:

```text
O(1)
```

---

```python
d[key] = value
```

Average:

```text
O(1)
```

---

```python
key in d
```

Average:

```text
O(1)
```

---

# 52. Python Set

```python
x in my_set
```

Average:

```text
O(1)
```

This difference is extremely useful.

Compare:

```python
x in list
```

with:

```python
x in set
```

Complexities:

```text
list → O(n)
set  → O(1) average
```

This is why hash sets are frequently used in DSA optimization.

---

# 53. Python Sorting

```python
arr.sort()
```

or:

```python
sorted(arr)
```

Time:

```text
O(n log n)
```

Python uses **Timsort**.

---

# 54. String Operations

Strings are immutable in languages such as Python.

Example:

```python
s += "a"
```

Repeated `n` times can potentially lead to significant copying.

Instead, often use:

```python
chars = []

for x in arr:
    chars.append(x)

result = "".join(chars)
```

Understanding the cost of string creation matters in some interview problems.

---

# 55. Amortized Complexity

Consider dynamic arrays.

Appending usually costs:

```text
O(1)
```

Sometimes the internal array becomes full and must resize:

```text
capacity 4
↓
capacity 8
↓
capacity 16
```

A resize may cost:

```text
O(n)
```

But resizing happens infrequently.

Across many insertions, the average cost per append is:

```text
O(1) amortized
```

Therefore:

```python
list.append()
```

is normally described as:

```text
O(1) amortized
```

---

# 56. Common Complexity Patterns in DSA

Learning to recognize patterns is more useful than memorizing formulas.

| Pattern | Typical Complexity |
|---|---|
| Direct lookup | `O(1)` |
| Scan array | `O(n)` |
| Two pointers | `O(n)` |
| Sliding window | `O(n)` |
| Binary search | `O(log n)` |
| Sort + scan | `O(n log n)` |
| Nested array comparison | `O(n²)` |
| Heap processing | `O(n log k)` |
| DFS/BFS graph | `O(V + E)` |
| Generate subsets | `O(2^n)` |
| Generate permutations | `O(n!)` |

---

# 57. Two Pointers — Why It Can Be O(n)

Consider:

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition:
        left += 1
    else:
        right -= 1
```

At first glance there are two pointers.

But they do not create nested iteration.

Each pointer moves at most `n` times.

Therefore:

```text
O(n)
```

Not:

```text
O(n²)
```

---

# 58. Sliding Window — Usually O(n)

Example:

```python
left = 0

for right in range(n):

    while condition:
        left += 1
```

It looks like nested loops.

But notice:

```text
right moves from 0 → n
left moves from 0 → n
```

Neither pointer moves backward.

Total pointer movements are roughly:

```text
2n
```

Therefore:

```text
O(n)
```

This is a very important interview pattern.

---

# 59. BFS / DFS Complexity

For a graph:

```text
V = number of vertices
E = number of edges
```

DFS:

```text
O(V + E)
```

BFS:

```text
O(V + E)
```

because each vertex and edge is processed a limited number of times.

Typical space complexity:

```text
O(V)
```

for:

- visited set
- recursion stack
- BFS queue

---

# 60. Tree Traversal

For a tree containing `n` nodes:

```text
DFS traversal = O(n)
BFS traversal = O(n)
```

because each node is visited once.

Space depends on structure.

Balanced tree DFS recursion:

```text
O(log n)
```

Worst-case skewed tree:

```text
O(n)
```

BFS may require:

```text
O(n)
```

space for the queue.

---

# 61. Hash Map Optimization Pattern

Consider finding duplicates.

Brute force:

```python
for i in range(n):

    for j in range(i + 1, n):

        if arr[i] == arr[j]:
            return True
```

Time:

```text
O(n²)
```

Space:

```text
O(1)
```

Using a set:

```python
seen = set()

for x in arr:

    if x in seen:
        return True

    seen.add(x)
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

This demonstrates a very common tradeoff:

```text
Use extra memory to reduce execution time.
```

---

# 62. Time-Space Tradeoff

Many algorithm optimizations follow:

```text
Less Time ↔ More Space
```

Example:

### Brute force

```text
Time  = O(n²)
Space = O(1)
```

### Hash Map

```text
Time  = O(n)
Space = O(n)
```

Neither is automatically "better."

It depends on constraints.

---

# 63. Constraints Often Reveal Expected Complexity

This is extremely useful during interviews and competitive programming.

Approximate guideline:

| Input Size | Usually Expected Complexity |
|---:|---|
| `n <= 10` | `O(n!)`, `O(2^n)` may work |
| `n <= 20` | `O(2^n)` may work |
| `n <= 100` | `O(n³)` may work |
| `n <= 1,000` | `O(n²)` may work |
| `n <= 100,000` | `O(n log n)` or `O(n)` |
| `n <= 1,000,000` | usually `O(n)` |
| `n` extremely large | `O(log n)` or `O(1)` |

These are rough guidelines, not hard guarantees.

A common competitive-programming approximation is that around:

```text
10^7 – 10^8
```

simple operations may be feasible within a few seconds depending heavily on language and environment.

---

# 64. Example: Determine Complexity

```python
def example(arr):

    n = len(arr)

    for i in range(n):
        print(arr[i])

    for i in range(n):

        for j in range(n):
            print(i, j)
```

First loop:

```text
O(n)
```

Nested loops:

```text
O(n²)
```

Total:

```text
O(n + n²)
```

Dominant term:

```text
O(n²)
```

Space:

```text
O(1)
```

---

# 65. Example: Sort Then Loop

```python
def example(arr):

    arr.sort()

    for x in arr:
        print(x)
```

Sorting:

```text
O(n log n)
```

Loop:

```text
O(n)
```

Total:

```text
O(n log n + n)
```

Dominant:

```text
O(n log n)
```

---

# 66. Example: Loop + Binary Search

```python
for x in arr:

    binary_search(other_arr, x)
```

Assuming:

```text
len(arr) = n
len(other_arr) = m
```

Loop:

```text
O(n)
```

Binary search:

```text
O(log m)
```

Total:

```text
O(n log m)
```

If both arrays have size `n`:

```text
O(n log n)
```

---

# 67. Example: Nested Loop With Shrinking Inner Loop

```python
for i in range(n):

    j = n

    while j > 1:
        j //= 2
```

Outer:

```text
n
```

Inner:

```text
log n
```

Total:

```text
O(n log n)
```

---

# 68. Example: Weird Loop

```python
i = 1

while i < n:

    i *= 2
```

Suppose after `k` iterations:

```text
i = 2^k
```

Stop when:

```text
2^k >= n
```

Take log:

```text
k >= log₂(n)
```

Therefore:

```text
O(log n)
```

---

# 69. Example: Another Weird Loop

```python
i = n

while i > 0:

    i -= 2
```

Number of iterations:

```text
n/2
```

Therefore:

```text
O(n)
```

Important distinction:

```text
i -= 2  → O(n)

i /= 2  → O(log n)
```

Remember:

```text
Subtract constant → usually linear

Divide by constant → logarithmic
```

---

# 70. Example: i = i * i

Consider:

```python
i = 2

while i < n:
    i = i * i
```

Values:

```text
2
4
16
256
65536
...
```

This grows much faster than doubling.

The complexity is approximately:

```text
O(log log n)
```

This is less common, but useful for recognizing advanced patterns.

---

# 71. Recurrence Relations

Recursive algorithms can often be expressed mathematically.

Example binary search:

```text
T(n) = T(n/2) + O(1)
```

Result:

```text
O(log n)
```

---

Merge sort:

```text
T(n) = 2T(n/2) + O(n)
```

Result:

```text
O(n log n)
```

---

Naive recursion:

```text
T(n) = 2T(n-1) + O(1)
```

Result:

```text
O(2^n)
```

---

# 72. Master Theorem — Basic Idea

For recurrences:

```text
T(n) = aT(n/b) + O(n^d)
```

Where:

```text
a = number of recursive subproblems
b = factor by which input shrinks
d = work outside recursion
```

Classic example:

```text
Merge Sort
```

```text
T(n) = 2T(n/2) + O(n)
```

Result:

```text
O(n log n)
```

You do not need to master the full theorem immediately when starting DSA, but recognize common recurrences.

---

# 73. Common Interview Complexities to Know Immediately

Memorize these:

```text
Array traversal
O(n)

Nested comparison
O(n²)

Binary search
O(log n)

Sorting
O(n log n)

Hash lookup
O(1) average

DFS/BFS
O(V + E)

Heap push/pop
O(log n)

Generate subsets
O(2^n)

Generate permutations
O(n!)
```

---

# 74. Complexity Pattern Recognition

When reading code, ask:

### Question 1

Does work remain constant regardless of input?

```text
→ O(1)
```

### Question 2

Do I visit every element?

```text
→ O(n)
```

### Question 3

Do I compare every element with every other element?

```text
→ O(n²)
```

### Question 4

Does the search space halve each step?

```text
→ O(log n)
```

### Question 5

Do I process every element and perform a logarithmic operation?

```text
→ O(n log n)
```

### Question 6

Do recursive branches double?

```text
→ O(2^n)
```

### Question 7

Am I trying every possible ordering?

```text
→ O(n!)
```

---

# 75. Quick Loop Recognition Table

| Code | Complexity |
|---|---|
| `for i in range(n)` | `O(n)` |
| `for i in range(0,n,2)` | `O(n)` |
| `while i < n: i += 1` | `O(n)` |
| `while i < n: i += 10` | `O(n)` |
| `while i < n: i *= 2` | `O(log n)` |
| `while n > 1: n //= 2` | `O(log n)` |
| two sequential `O(n)` loops | `O(n)` |
| two nested `O(n)` loops | `O(n²)` |
| `O(n)` outer + `O(log n)` inner | `O(n log n)` |

---

# 76. Common Mistakes

## Mistake 1 — Counting loops instead of iterations

Wrong reasoning:

```text
There are two loops → O(n²)
```

Correct reasoning:

```text
Are they nested or sequential?
```

---

## Mistake 2 — Ignoring library-call complexity

```python
for i in range(n):
    arr.sort()
```

Sorting happens `n` times.

Each sort:

```text
O(n log n)
```

Total:

```text
O(n² log n)
```

---

## Mistake 3 — Assuming nested loops always mean O(n²)

Sliding-window algorithms can contain nested loops but still run in:

```text
O(n)
```

because each element enters and leaves the window only once.

---

## Mistake 4 — Forgetting recursion stack space

```python
recursive_function(n)
```

may use:

```text
O(n)
```

stack memory even if no explicit array is created.

---

## Mistake 5 — Calling hash operations guaranteed O(1)

Better interview wording:

```text
O(1) average-case
O(n) worst-case
```

---

# 77. Interview Method for Complexity Analysis

After solving a problem, explain complexity systematically.

Example answer:

> We iterate over the input array once, so the traversal takes `O(n)` time. Each hash-set lookup and insertion is `O(1)` on average, so total time remains `O(n)`. The set may contain up to `n` elements, so auxiliary space is `O(n)`.

This is much better than simply saying:

```text
O(n), O(n)
```

---

# 78. Complexity Decision Framework

When analyzing code:

```text
1. Define input variables.

2. Identify loops.

3. Determine iterations per loop.

4. Multiply nested loops.

5. Add sequential operations.

6. Include library/function-call costs.

7. Analyze recursion.

8. Remove constants.

9. Remove lower-order terms.

10. Identify extra memory.

11. Include recursion stack.

12. State average/worst case if relevant.
```

---

# 79. Time Complexity vs Space Complexity Example

```python
def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        required = target - num

        if required in seen:
            return [seen[required], i]

        seen[num] = i
```

Let:

```text
n = len(nums)
```

Loop:

```text
O(n)
```

Hash lookup:

```text
O(1) average
```

Hash insertion:

```text
O(1) average
```

Therefore:

```text
Time = O(n)
```

Hash map can contain `n` items:

```text
Space = O(n)
```

---

# 80. Brute Force vs Optimized Example

Two Sum brute force:

```python
for i in range(n):

    for j in range(i + 1, n):

        if nums[i] + nums[j] == target:
            return [i, j]
```

Complexity:

```text
Time  = O(n²)
Space = O(1)
```

Optimized hash-map approach:

```text
Time  = O(n)
Space = O(n)
```

This is a classic example of:

```text
time-space tradeoff
```

---

# 81. Most Important Complexity Ranking to Memorize

```text
BEST
│
│ O(1)
│
│ O(log n)
│
│ O(√n)
│
│ O(n)
│
│ O(n log n)
│
│ O(n²)
│
│ O(n³)
│
│ O(2^n)
│
│ O(n!)
│
WORST
```

A useful shortened version:

```text
1
<
log n
<
n
<
n log n
<
n²
<
2^n
<
n!
```

Memorize this sequence.

---

# 82. Practical Interview Goal

You do NOT need to calculate exact CPU instructions.

You should be able to look at code like:

```python
for i in range(n):

    j = n

    while j > 1:
        j //= 2
```

and immediately recognize:

```text
outer = O(n)

inner = O(log n)

total = O(n log n)
```

Likewise:

```python
seen = set()

for x in nums:

    if x in seen:
        return True

    seen.add(x)
```

Recognize:

```text
Time  = O(n)
Space = O(n)
```

This pattern recognition is what matters most in DSA interviews.

---

# 83. Final Cheat Sheet

## Growth Order

```text
O(1)
<
O(log n)
<
O(√n)
<
O(n)
<
O(n log n)
<
O(n²)
<
O(n³)
<
O(2^n)
<
O(n!)
```

## Code Pattern

```text
one operation
→ O(1)

iterate array
→ O(n)

halve repeatedly
→ O(log n)

sort
→ O(n log n)

two nested full loops
→ O(n²)

three nested full loops
→ O(n³)

binary recursive branching
→ O(2^n)

all permutations
→ O(n!)
```

## Combining Complexity

```text
Sequential → ADD

Nested → MULTIPLY

Drop constants

Keep dominant term
```

Example:

```text
O(n) + O(n²)
= O(n²)
```

Example:

```text
O(n) × O(log n)
= O(n log n)
```

## Space

```text
few variables
→ O(1)

array/hash map of n items
→ O(n)

n × n matrix
→ O(n²)

recursive depth n
→ O(n)

recursive depth log n
→ O(log n)
```

---

# 84. References

## Big-O / Complexity

- Big-O Cheat Sheet  
  https://www.bigocheatsheet.com/

- GeeksForGeeks — Analysis of Algorithms  
  https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/

- Wikipedia — Big O Notation  
  https://en.wikipedia.org/wiki/Big_O_notation

---

## Visualizing Data Structures and Algorithms

VisuAlgo is excellent for visually understanding:

- sorting
- binary search
- trees
- graphs
- heaps
- linked lists

https://visualgo.net/en

---

## Python Operation Complexities

Python Wiki — Time Complexity:

https://wiki.python.org/moin/TimeComplexity

---

## Algorithm Learning

MIT OpenCourseWare — Introduction to Algorithms:

https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/

---

# 85. What to Learn Next

Once these concepts are comfortable, learn DSA approximately in this order:

```text
Complexity Analysis
        ↓
Arrays & Strings
        ↓
Hash Map / Hash Set
        ↓
Two Pointers
        ↓
Sliding Window
        ↓
Stack & Queue
        ↓
Binary Search
        ↓
Linked Lists
        ↓
Recursion
        ↓
Trees / BST
        ↓
Heap / Priority Queue
        ↓
Graphs / BFS / DFS
        ↓
Backtracking
        ↓
Dynamic Programming
```

Do not wait until complexity analysis feels mathematically perfect.

The most effective way to learn it is:

```text
learn concept
    ↓
write code
    ↓
calculate complexity
    ↓
compare with solution
    ↓
repeat
```

After roughly 20–30 problems, recognizing `O(n)`, `O(log n)`, `O(n log n)`, and `O(n²)` starts becoming much more automatic.