# DSA Code Practice

Curated algorithmic problem solutions, mathematical intuitions, and implementations structured by pattern.

---

## Structure

### `0-deep-root/` — Foundations
- Binary Trees (traversals, path sums, tree construction, height, balance)
- Recursion fundamentals & subsets
- GCD, power functions, binary search basics

### `1a-arrays/` — Arrays & Prefix Sums
- In-place reversal, rotation (modular arithmetic), negation marking
- Prefix sums, zero-sum subarrays, pivot index

### `1b-sorting/` — Sorting & Inversion Elimination
- Insertion sort, Selection sort, Merge sort, Quick sort (Lomuto partition)
- Inversion counting (Reverse Pairs — LC 493)
- Dutch National Flag / 3-way partition (Sort Colors — LC 75)
- Interval scheduling & merging (Merge Intervals — LC 56)
- Sorting-as-preprocessing (Minimum Absolute Difference — LC 1200)

### `1c-hashing/` — Hashing & Modular Arithmetic
- Complement lookup (Two Sum — LC 1)
- Frequency counting (Valid Anagram — LC 242)
- Canonical key grouping (Group Anagrams — LC 49)
- Top K elements (Top K Frequent — LC 347)
- Chain reaction & memoization (Longest Consecutive — LC 128)
- Prefix sum + hash map (Subarray Sum = K — LC 560)
- Constraint tracking (Valid Sudoku — LC 36)
- Meet in the middle (4Sum II — LC 454)
- Subarray divisibility (Continuous Subarray Sum — LC 523)

### `2a-two-pointers/` — Two Pointers
- Opposite-end pointers on sorted arrays (Two Sum II — LC 167)
- Bottleneck scout principle (Trapping Rain Water — LC 42)
- Greedy boundary elimination (Container With Most Water — LC 11)
- U-shape convergence (Squares of Sorted Array — LC 977)
- Triplet sum reduction & deduplication (3Sum — LC 15)
- Reader/Writer partition & duplicates removal

---

## Usage

All solutions are written in standalone Python with test suites included:

```bash
python3 1c-hashing/two_sum.py
python3 2a-two-pointers/water_trap.py
```
