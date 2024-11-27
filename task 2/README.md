# Task 2

## Questions:

### Question 1 – Perfect Number
A **Perfect Number** is a positive integer that equals the sum of its positive divisors (excluding itself).

For example:
- The number 6 has divisors 1, 2, 3. Since 1 + 2 + 3 = 6, it is a perfect number.
  
#### Implement the function `question1(num)` that checks if a number is perfect.
- Input: `num` (integer).
- Output: Returns `True` if `num` is a perfect number and `False` otherwise.

**Note**: Your implementation must be recursive.

**Example**:
```python
# Running example:
question1(28)  # True
question1(8)   # False
```

---

### Question 2 – Subset Sum Problem
Given a set of integers \( S \), in the **subset sum problem**, the objective is to decide whether there exists a sum of a subset of numbers \( s \subseteq S \) such that their sum is equal to an integer \( X \).

#### Implement the function `question2(lst, x)` that counts the number of subsets of `lst` whose sum is equal to `x`.
- Input: 
  - `lst` (list of integers, representing a multiset).
  - `x` (integer target sum).
- Output: Returns the number of subsets whose sum equals `x`.

**Note**: Your implementation must be recursive.

**Example**:
```python
# Running example:
question2([7, 6, 1], 14)  # 1
question2([7, 6, 1, 1], 14)  # 2
question2([7, 6, 1], 1000)  # 0
```

---

### Question 3 – Epidemic Spread
#### A. Simulating Epidemic Spread
You are asked to implement the function `question3_a(mat, indices, epidemic)` that simulates the spread of an epidemic.

- Input:
  - `mat` (2D matrix representing the map, each element is an integer).
  - `indices` (tuple with the initial location of the epidemic).
  - `epidemic` (integer representing the epidemic index).
  
The epidemic spreads to the neighboring cells (up, down, left, right) unless blocked by another epidemic.

- Output: The map (`mat`) is updated in place.

**Example**:
```python
mat = [[1, 0, 0, 3, 0], [0, 0, 2, 3, 0], [2, 0, 0, 2, 0], [0, 1, 2, 3, 3]]
question3_a(mat, (0, 1), 3)
print(mat)
# Output:
# [[1, 3, 3, 3, 0], [3, 3, 2, 3, 0], [2, 3, 3, 2, 0], [0, 1, 2, 3, 3]]
```

#### B. Finding the Largest "Healthy Community"
You are asked to implement the function `question3_b(mat)` that returns the size of the largest "healthy community".

A "healthy community" consists of cells with the value 0, and all cells in the community must be connected (neighbors or via other healthy humans).

- Input: `mat` (2D matrix representing the map).
- Output: Returns the size of the largest healthy community.

**Example**:
```python
mat = [[1, 0, 0, 3, 0], [0, 0, 2, 3, 0], [2, 0, 0, 2, 0], [0, 1, 2, 3, 3]]
print(question3_b(mat))  # Output: 6
```

---

