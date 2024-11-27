# Python Programming Assignments - Problem Set

## Table of Contents
1. [Q 1: Division of Numbers](#task-1-division-of-numbers)
2. [Q 2: Sorting Words by Length](#task-2-sorting-words-by-length)
3. [Q 3: Prime Numbers](#task-3-prime-numbers)
4. [Q 4: Pascal's Triangle](#task-4-pascals-triangle)

## Q 1: Division of Numbers

### Problem Description

Implement the function `q1` that reads values from an input file and returns the result of dividing the numbers in the order in which they appear.

**Requirements:**
- Handle division by zero and non-number values with appropriate error codes:
  - Error in opening the file: `-1`
  - Division by 0: `-2`
  - Reading non-number values: `-3`

### Example

**Input (Input_q1.txt):**
```
4096 2 4 8 2 8 4.0
4096 2 0 8 2 8
4096 a 4 8 0 8
461214 3 4.5
5 6.5
7.3 8
2
9.0
```

**Output:**
```
Result: 4.0
```

---

## Q 2: Sorting Words by Length

### Problem Description

Implement the function `q2` that reads words from an input file, sorts them by length in ascending order, and writes the sorted words into a new output file.

**Requirements:**
- Words of the same length should maintain their original order (stable sort).
- Each word should be output as a tuple containing the word and its length.

### Example

**Input (Input_q2.txt):**
```
Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
```

**Output (Output_q2.txt):**
```
[('a', 1), ('is', 2), ('of', 2), ('Its', 3), ('the', 3), ('use', 3), ('code', 4), ('with', 4),
('Python', 6), ('design', 6), ('language.', 9), ('philosophy', 10), ('emphasizes', 10),
('high-level,', 11), ('programming', 11), ('readability', 11), ('significant', 11),
('indentation.', 12), ('general-purpose', 15)]
```

---

## Q 3: Prime Numbers

### Problem Description

**Part A:** Implement the function `q3_a` that receives an integer `n` and returns a list of all prime numbers up to `n`.

**Part B:** Implement the function `q3_b` that receives an integer `n` and returns a list containing all combinations of three prime numbers whose product is less than or equal to `n`. Each combination should be sorted in ascending order.

### Example for Task 3B

For `n = 20`, the function should return:
```
[[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 3, 3]]
```

For `n = 30`, the function should return:
```
[[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 3, 3]]
```

---

## Q 4: Pascal's Triangle

### Problem Description

Implement the function `q4` that receives a number `n` and returns the `n`-th row of Pascal’s Triangle.

**Requirements:**
- If `n` is not a positive integer, return `-1`.

### Example

For `n = 5`, the function should return:
```
[1, 5, 10, 10, 5, 1]
```
