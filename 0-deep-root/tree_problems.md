# 🧠 Tree Recursion — Complete Mental Model & Practice

---

## Part 1: The Mental Model

### The Two Directions

```
BOTTOM-UP                              TOP-DOWN
─────────                              ────────
Info starts at: LEAVES                 Info starts at: ROOT
Info flows: UP (return values)         Info flows: DOWN (parameters)
Who answers first: LEAVES              Who decides last: LEAVES
Parent's job: COMBINE child answers    Parent's job: PASS context down
```

### Bottom-Up Skeleton

```python
def solve(node):
    if node is None:
        return BASE_VALUE              # "nothing" answers safely
    left = solve(node.left)            # ask left child
    right = solve(node.right)          # ask right child
    return COMBINE(node, left, right)  # my answer = my value + children's answers
```

> **Think:** "What can my children tell me? How do I combine their answers with my own?"

### Top-Down Skeleton

```python
def solve(node, info_from_parent):
    if node is None:
        return SAFE_DEFAULT            # nothing here, safe answer
    updated = UPDATE(info_from_parent, node)  # add my contribution
    if node.left is None and node.right is None:
        return CHECK(updated)          # leaf makes the final call
    return solve(node.left, updated) COMBINE solve(node.right, updated)
```

> **Think:** "What does my parent need to tell me? What do I add before passing it to my children?"

### Decision Rule: Which Direction?

Ask ONE question: **Does a node need info from its ANCESTORS?**

| Answer | Direction | Why | Examples |
|--------|-----------|-----|----------|
| **No** — answer depends only on the subtree below | **Bottom-up** | Children have all the info needed | count, height, max, mirror, is_identical, is_balanced |
| **Yes** — answer depends on the path from root | **Top-down** | Root has info that leaves need | path_sum, find_depth, root-to-leaf paths, is_valid_BST (with range) |

> **Rule of thumb:** If the problem says "from root to..." or "at depth..." or "along the path..." → top-down. If it says "of the subtree" or "in the tree" → probably bottom-up.

---

### The 6 Nuances You Must Remember

#### 1. `None` ≠ Leaf
- `None` = missing child. An absent node. The void.
- Leaf = a REAL node with `left is None AND right is None`.
- **Why it matters:** In path_sum, checking at `None` gives you false paths through non-leaf nodes. Always ask: "Am I checking at the right place?"

#### 2. `None` → Safe Default
Instead of checking "does my child exist?" before recursing, just recurse and let `None` return a safe value that doesn't affect the result:
- Counting? `None` → `0` (adds nothing to the count)
- Finding max? `None` → `-inf` (loses every comparison)
- Checking existence? `None` → `False` (no path through nothing)
- Transforming? `None` → `None` (nothing to transform)

This eliminates manual `if node.left is not None` checks.

#### 3. Short-Circuit Evaluation

| Operator | Stops at | Because | Use for |
|----------|----------|---------|---------|
| `or` | First `True` | `True or anything = True` | "Does ANY path work?" |
| `and` | First `False` | `False and anything = False` | "Do ALL paths work?" |

`or` → existential questions (find ONE valid path, find ONE matching node)
`and` → universal questions (are ALL subtrees valid? are BOTH sides identical?)

#### 4. Return Values vs. Accumulators
- **Clean:** Return the answer directly. Let recursion compose results via `return`.
- **Messy:** Store results in an external list/variable, check after.
- **Prefer returning.** Accumulators work but they fight the recursive structure.

#### 5. When Small Examples Hide the Recursion, Make Them Bigger
Leaf nodes are boring — mirroring them changes nothing, counting them always gives 1. When you can't see what the recursion does, imagine subtrees with depth 3+ under each child.

#### 6. Post-Order = Bottom-Up
Your Day 2 functions (count, height, max, mirror, check) were all **post-order traversals** — process children first, then current node. Bottom-up and post-order are the same idea viewed from different angles.

---

## Part 2: Test Trees

Use these trees to dry-run every problem. Copy-paste the construction code.

### Tree A — Your Standard Tree (balanced-ish)
```
      1
     / \
    2   3
   / \   \
  4   5   6
```
```python
a = TreeNode(1)
a.left = TreeNode(2, TreeNode(4), TreeNode(5))
a.right = TreeNode(3, None, TreeNode(6))
```

### Tree B — Single Node
```
  42
```
```python
b = TreeNode(42)
```

### Tree C — Empty Tree
```
  (None)
```
```python
c = None
```

### Tree D — Left-Skewed (like a linked list going left)
```
  1
 /
2
 /
  3
   /
    4
```
```python
d = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
```

### Tree E — Right-Skewed (like a linked list going right)
```
1
 \
  2
   \
    3
```
```python
e = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
```

### Tree F — Perfect Binary Tree
```
        1
       / \
      2    3
     / \  / \
    4  5 6   7
```
```python
f = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)))
```

### Tree G — BST
```
        8
       / \
      4   12
     / \  / \
    2  6 10  14
```
```python
g = TreeNode(8,
    TreeNode(4, TreeNode(2), TreeNode(6)),
    TreeNode(12, TreeNode(10), TreeNode(14)))
```

### Tree H — Symmetric Tree
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```
```python
h = TreeNode(1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3)))
```

### Tree I — NOT Symmetric
```
      1
     / \
    2   2
     \   \
      3   3
```
```python
i = TreeNode(1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3)))
```

### Tree J — Unbalanced
```
        1
       /
      2
     / \
    3   4
   /
  5
```
```python
j = TreeNode(1,
    TreeNode(2,
        TreeNode(3, TreeNode(5)),
        TreeNode(4)))
```

---

## Part 3: The 10 Problems

For each problem: understand the puzzle → figure out direction (bottom-up or top-down?) → dry-run on the test trees → code it.

---

### Problem 1: Sum of All Nodes
**The puzzle:** You're collecting donations from every person in the tree. What's the total?

**Direction hint:** Does a node need to know about its ancestors? No → bottom-up.

**Expected outputs:**
| Tree | Answer |
|------|--------|
| A | 1+2+3+4+5+6 = **21** |
| B | **42** |
| C | **0** |
| D | 1+2+3+4 = **10** |
| F | 1+2+3+4+5+6+7 = **28** |

**Dry-run Tree A:**
```
sum(4) = 4 + 0 + 0 = 4        ← leaf
sum(5) = 5 + 0 + 0 = 5        ← leaf
sum(2) = 2 + 4 + 5 = 11       ← combines
sum(6) = 6 + 0 + 0 = 6        ← leaf
sum(3) = 3 + 0 + 6 = 9        ← combines
sum(1) = 1 + 11 + 9 = 21      ← root combines last
```

---

### Problem 2: Count Leaf Nodes
**The puzzle:** How many people in the tree have no subordinates (no children)?

**Direction hint:** Bottom-up. A leaf knows it's a leaf. Internal nodes just add up their children's counts.

**Expected outputs:**
| Tree | Leaves | Answer |
|------|--------|--------|
| A | 4, 5, 6 | **3** |
| B | 42 | **1** |
| C | — | **0** |
| D | 4 | **1** |
| F | 4, 5, 6, 7 | **4** |

**Think about:** What should a leaf return? What should `None` return? What should an internal node return?

---

### Problem 3: Find Minimum Depth
**The puzzle:** What's the depth of the SHALLOWEST leaf? (Shortest root-to-leaf path.)

**⚠️ Trap:** This is NOT `min(height(left), height(right))`. Why? If a node has only ONE child, the missing side has depth 0, but that's not a valid leaf path!

**Expected outputs (convention: depth = number of nodes on path, root is depth 1 — same as your `height()` function):**
| Tree | Shallowest leaf | Answer |
|------|----------------|--------|
| A | 4, 5, or 6 (all at same depth) | **3** |
| B | 42 (root is the only leaf) | **1** |
| D | 4 (only leaf, must go all the way down) | **4** |
| E | 3 (only leaf, must go all the way down) | **3** |
| F | 4, 5, 6, or 7 (all at same depth) | **3** |

**The trap in action on Tree D (left-skewed):**
```
      1
     /
    2
   /
  3
 /
4        ← only leaf, depth = 4
```
If you naively do `1 + min(left, right)`, node 1 would compute `1 + min(height(2), 0) = 1`. WRONG. The right side is `None`, not a leaf.

**Hint:** When one child is `None`, you can't take the min with it. You must only consider the side that exists.

---

### Problem 4: All Root-to-Leaf Paths (as strings)
**The puzzle:** List every possible route from the CEO to a ground-level employee.

**Direction hint:** You need to know the path FROM the root → top-down.

**Expected outputs:**
| Tree | Paths |
|------|-------|
| A | `["1->2->4", "1->2->5", "1->3->6"]` |
| B | `["42"]` |
| D | `["1->2->3->4"]` |
| F | `["1->2->4", "1->2->5", "1->3->6", "1->3->7"]` |

**Think about:** What info do you pass DOWN? What do you do at a leaf?

---

### Problem 5: Is the Tree Symmetric?
**The puzzle:** If you put a mirror down the center of the tree, does it look the same?

**Direction hint:** You already solved `mirror` (invert) and `check` (identical). A tree is symmetric if its left subtree is the mirror image of its right subtree.

**Expected outputs:**
| Tree | Answer |
|------|--------|
| A | **False** (left side has 4,5 — right side has only 6) |
| B | **True** (single node) |
| C | **True** (empty = symmetric) |
| F | **False** (different values on left vs right leaves) |
| H | **True** (mirror image!) |
| I | **False** (both right children = 3, not mirrored) |

**Hint:** Don't solve this as one function on one tree. Write a helper `is_mirror(left, right)` that checks if two trees are mirror images. Then call `is_mirror(root.left, root.right)`.

**Dry-run Tree H:**
```
is_mirror(left=2(3,4), right=2(4,3))
  values match: 2 == 2 ✓
  is_mirror(left.left=3, right.right=3) → values match, both leaves → True
  is_mirror(left.right=4, right.left=4) → values match, both leaves → True
  True and True → True
```

**Dry-run Tree I:**
```
is_mirror(left=2(None,3), right=2(None,3))
  values match: 2 == 2 ✓
  is_mirror(left.left=None, right.right=3) → one None, one not → False
  False → short-circuit, done → False
```

---

### Problem 6: Sum of Left Leaves
**The puzzle:** Only count donations from people who are BOTH a leaf AND a left child.

**Direction hint:** Bottom-up, but with a twist — a node needs to know if IT is a left child. Two approaches: pass a flag down (top-down element), or have the parent check if its left child is a leaf.

**Expected outputs (Tree A):**
```
      1
     / \
    2   3
   / \   \
  4   5   6
```
Left leaves: 4 (left child of 2, is a leaf). Node 5 is a RIGHT child. Node 6 is a RIGHT child.
Answer: **4**

| Tree | Left leaves | Answer |
|------|------------|--------|
| A | 4 | **4** |
| B | — | **0** (root is not a left child) |
| F | 4, 6 | **4 + 6 = 10** |
| H | 3, 4 | **3 + 4 = 7** |

**Think about:** The leaf doesn't know if it's a left child. So who should check? The PARENT.

---

### Problem 7: Is Balanced Tree?
**The puzzle:** A tree is balanced if for EVERY node, the height difference between its left and right subtrees is at most 1. Not just the root — every single node.

**Direction hint:** Bottom-up. Each node needs to know the height of its children (height is bottom-up). Check the balance condition at every node.

**Expected outputs:**
| Tree | Answer |
|------|--------|
| A | **True** (heights: left=2, right=2, diff=0 at root; all nodes balanced) |
| B | **True** |
| C | **True** |
| D | **False** (root: left height=3, right height=0, diff=3 > 1) |
| F | **True** (perfect tree) |
| J | **False** (node 2: left height=2, right height=1 ✓ but node 1: left height=3, right height=0 ✗) |

**The efficiency trap:** Don't call `height()` separately for each node — that's O(n²). Instead, compute height AND check balance in the same recursion. Return `-1` to signal "unbalanced" so it propagates up.

**Hint on the efficient approach:**
```
Returns height if balanced, -1 if not.
If either child returns -1 → I'm unbalanced too → return -1.
If heights differ by > 1 → return -1.
Otherwise → return 1 + max(left, right).
```

---

### Problem 8: Lowest Common Ancestor (LCA)
**The puzzle:** Given two nodes p and q, find the deepest node that is an ancestor of BOTH.

**Direction hint:** Bottom-up. Each subtree reports "did I find p? did I find q?" The first node where both sides report a find — that's the LCA.

**Think about:** What does each node return?
- If I'm `None` → return `None` (didn't find anything)
- If I'm `p` or `q` → return myself (found one!)
- If left found something and right found something → I'm the LCA! Return myself.
- If only one side found something → pass it up.

**Test cases on Tree A:**
```
      1
     / \
    2   3
   / \   \
  4   5   6
```

| p | q | LCA | Why |
|---|---|-----|-----|
| 4 | 5 | **2** | Both are children of 2 |
| 4 | 6 | **1** | 4 is in left subtree, 6 is in right |
| 2 | 4 | **2** | 2 is an ancestor of 4, and ancestor of itself |
| 2 | 3 | **1** | In different subtrees of root |
| 5 | 6 | **1** | 5 in left subtree, 6 in right |
| 4 | 2 | **2** | Same as (2,4) — order doesn't matter |

**Test cases on Tree F (perfect binary tree):**
```
        1
       / \
      2    3
     / \  / \
    4  5 6   7
```

| p | q | LCA | Why |
|---|---|-----|-----|
| 4 | 5 | **2** | Siblings |
| 6 | 7 | **3** | Siblings |
| 4 | 7 | **1** | Opposite sides of root |
| 2 | 5 | **2** | 2 is ancestor of 5 |
| 4 | 6 | **1** | Different subtrees |

**Test cases on Tree D (left-skewed: 1→2→3→4):**

| p | q | LCA | Why |
|---|---|-----|-----|
| 3 | 4 | **3** | 3 is parent of 4 |
| 2 | 4 | **2** | 2 is ancestor of both |
| 1 | 4 | **1** | Root is ancestor of everything |

**Test cases on Tree J:**
```
        1
       /
      2
     / \
    3   4
   /
  5
```

| p | q | LCA | Why |
|---|---|-----|-----|
| 5 | 4 | **2** | 5 is in left subtree of 2, 4 is right child of 2 |
| 3 | 4 | **2** | Both are children of 2 |
| 5 | 2 | **2** | 2 is ancestor of 5 |
| 5 | 1 | **1** | Root is ancestor of everything |

**Dry-run: LCA(4, 6) on Tree A:**
```
lca(1, p=4, q=6):
  lca(2, p=4, q=6):
    lca(4, p=4, q=6):
      I AM p! return 4              ← found p
    lca(5, p=4, q=6):
      not p or q, no children match → return None
    left=4, right=None → only left found → return 4    ← pass it up
  lca(3, p=4, q=6):
    lca(None) → None
    lca(6, p=4, q=6):
      I AM q! return 6              ← found q
    left=None, right=6 → only right found → return 6   ← pass it up
  left=4, right=6 → BOTH sides found something → I'M THE LCA → return 1
```

**Dry-run: LCA(4, 5) on Tree A (both in same subtree):**
```
lca(1, p=4, q=5):
  lca(2, p=4, q=5):
    lca(4, p=4, q=5):
      I AM p! return 4
    lca(5, p=4, q=5):
      I AM q! return 5
    left=4, right=5 → BOTH found → I'M THE LCA → return 2
  lca(3, p=4, q=5):
    lca(None) → None
    lca(6): not p or q → return None
    left=None, right=None → return None
  left=2, right=None → only left found → return 2
Result: 2 ✓
```

**Dry-run: LCA(2, 4) on Tree A (one is ancestor of the other):**
```
lca(1, p=2, q=4):
  lca(2, p=2, q=4):
    I AM p! return 2               ← found p, return IMMEDIATELY
    (never explores 2's children — 4 is below, but we already found 2)
  lca(3, p=2, q=4):
    → returns None (nothing found)
  left=2, right=None → only left found → return 2
Result: 2 ✓ (because 2 is the LCA of itself and its descendant 4)
```

⚠️ **Notice:** When `p` is an ancestor of `q`, we find `p` first and return it immediately without ever reaching `q`. This works because the LCA of a node and its descendant is always the ancestor node itself.

---

### Problem 9: Level Order — Right Side View
**The puzzle:** Stand to the RIGHT of the tree. Which nodes can you see? (The rightmost node at each level.)

**Direction hint:** BFS (level-order). Process each level, take the last node.

**Expected outputs:**
| Tree | Level-by-level | Right side view |
|------|---------------|----------------|
| A | [[1], [2, 3], [4, 5, 6]] | **[1, 3, 6]** |
| B | [[42]] | **[42]** |
| C | [] | **[]** |
| D | [[1], [2], [3], [4]] | **[1, 2, 3, 4]** (skewed left — you see every node!) |
| E | [[1], [2], [3]] | **[1, 2, 3]** |
| F | [[1], [2, 3], [4, 5, 6, 7]] | **[1, 3, 7]** |
| H | [[1], [2, 2], [3, 4, 4, 3]] | **[1, 2, 3]** |
| J | [[1], [2], [3, 4], [5]] | **[1, 2, 4, 5]** |

**Dry-run on Tree A:**
```
queue = [1]

Level 0: size=1
  Pop 1, add children 2, 3 → queue = [2, 3]
  Level nodes: [1] → last = 1

Level 1: size=2
  Pop 2, add children 4, 5 → queue = [3, 4, 5]
  Pop 3, add child 6        → queue = [4, 5, 6]
  Level nodes: [2, 3] → last = 3

Level 2: size=3
  Pop 4, no children         → queue = [5, 6]
  Pop 5, no children         → queue = [6]
  Pop 6, no children         → queue = []
  Level nodes: [4, 5, 6] → last = 6

Right side view: [1, 3, 6] ✓
```

**Dry-run on Tree J:**
```
queue = [1]

Level 0: size=1
  Pop 1, add child 2 (no right) → queue = [2]
  Level nodes: [1] → last = 1

Level 1: size=1
  Pop 2, add children 3, 4 → queue = [3, 4]
  Level nodes: [2] → last = 2

Level 2: size=2
  Pop 3, add child 5 (no right) → queue = [4, 5]
  Pop 4, no children             → queue = [5]
  Level nodes: [3, 4] → last = 4

Level 3: size=1
  Pop 5, no children → queue = []
  Level nodes: [5] → last = 5

Right side view: [1, 2, 4, 5] ✓
```
Notice: You see node 4 at level 2 even though node 3 is to its left — because 4 is the RIGHTMOST at that level.

**Hint:** Use the level-by-level BFS template from the Day 3 study guide. The last element of each level list is the "right side view" element.

---

### Problem 10: Diameter of Binary Tree
**The puzzle:** The diameter is the LENGTH of the longest path between any two nodes (counted in edges, not nodes). This path may or may not pass through the root.

**Direction hint:** Bottom-up, but tricky. At each node, the longest path THROUGH that node is `height(left) + height(right)`. But the overall diameter might be entirely within one subtree.

**Why it might NOT pass through the root:**
```
      1
     /
    2
   / \
  4   5
 /     \
7       8
```
Diameter = path from 7 → 4 → 2 → 5 → 8 = **4 edges**. This path goes through node 2, not the root!
The root (1) only has a left subtree, so the longest path through root = 0 + 3 = 3. But the longest path through node 2 = 2 + 2 = 4. That's the diameter.

**Expected outputs:**
| Tree | Longest path | Diameter (edges) |
|------|-------------|------------------|
| A | 4→2→1→3→6 (or 5→2→1→3→6) | **4** |
| B | just node 42 | **0** |
| C | empty | **0** |
| D | 1→2→3→4 | **3** |
| E | 1→2→3 | **2** |
| F | any leaf→root→leaf (e.g., 4→2→1→3→7) | **4** |
| G | any leaf→root→leaf (e.g., 2→4→8→12→14) | **4** |
| J | 5→3→2→4 | **3** |

**The approach:**
- Compute height bottom-up (you already know how)
- At each node, calculate `left_height + right_height` — that's the longest path (in edges) through THIS node
- Track the maximum across ALL nodes (use a variable outside the recursion, or return both height and diameter)

**Dry-run on Tree A:**
```
      1
     / \
    2   3
   / \   \
  4   5   6
```
Using height where `None → 0`, leaf → 1:
```
node 4: left_h=0, right_h=0 → path_through = 0+0 = 0, height = 1
node 5: left_h=0, right_h=0 → path_through = 0+0 = 0, height = 1
node 2: left_h=1, right_h=1 → path_through = 1+1 = 2, height = 2
node 6: left_h=0, right_h=0 → path_through = 0+0 = 0, height = 1
node 3: left_h=0, right_h=1 → path_through = 0+1 = 1, height = 2
node 1: left_h=2, right_h=2 → path_through = 2+2 = 4, height = 3

max(path_through) across all nodes = max(0, 0, 2, 0, 1, 4) = 4
Diameter = 4 ✓ (path: 4→2→1→3→6, which is 4 edges)
```

**Dry-run on Tree J:**
```
        1
       /
      2
     / \
    3   4
   /
  5
```
```
node 5: left_h=0, right_h=0 → path_through = 0, height = 1
node 3: left_h=1, right_h=0 → path_through = 1, height = 2
node 4: left_h=0, right_h=0 → path_through = 0, height = 1
node 2: left_h=2, right_h=1 → path_through = 3, height = 3
node 1: left_h=3, right_h=0 → path_through = 3, height = 4

max(path_through) = max(0, 1, 0, 3, 3) = 3
Diameter = 3 ✓ (path: 5→3→2→4, which is 3 edges)
```
Notice: the diameter goes through node 2, not the root. Node 1 has the same path_through (3) but that corresponds to path 4→3→2→1 which is only one direction. The actual longest path through node 1 is just left_h + right_h = 3 + 0 = 3 (same as through node 2). Either way diameter = 3.

**Dry-run on Tree D (left-skewed: 1→2→3→4):**
```
node 4: path_through = 0, height = 1
node 3: left_h=1, right_h=0 → path_through = 1, height = 2
node 2: left_h=2, right_h=0 → path_through = 2, height = 3
node 1: left_h=3, right_h=0 → path_through = 3, height = 4

max(path_through) = 3
Diameter = 3 ✓ (path: 1→2→3→4 = 3 edges)
```
For a skewed tree, the diameter equals height - 1.

**This is the hardest problem in the set.** If you solve this cleanly, your tree recursion is solid.

---

## Part 4: Dry-Run Checklist

For each problem, before you code, trace through AT LEAST these trees:

| Tree | What it tests |
|------|--------------|
| **C** (None) | Empty tree — does your base case handle it? |
| **B** (single node) | Minimum case — root is also a leaf |
| **A** (standard) | Normal case — mixed structure |
| **D** (left-skewed) | Degenerate case — tree acts like a linked list |
| **F** (perfect) | Best case — fully balanced |

If your solution works on all 5, it's almost certainly correct.

---

## Part 5: Progress Tracking

Check off as you solve:

- [ ] Problem 1: Sum of All Nodes
- [ ] Problem 2: Count Leaf Nodes
- [ ] Problem 3: Minimum Depth ⚠️ (watch the trap)
- [ ] Problem 4: All Root-to-Leaf Paths
- [ ] Problem 5: Is Symmetric?
- [ ] Problem 6: Sum of Left Leaves
- [ ] Problem 7: Is Balanced? ⚠️ (efficient version)
- [ ] Problem 8: Lowest Common Ancestor
- [ ] Problem 9: Right Side View (BFS)
- [ ] Problem 10: Diameter ⚠️ (hardest)

**Target:** Solve all 10 over the next 2-3 days. Dry-run before coding. Code should feel like transcription.

---

*"You don't understand trees from one problem. You understand them from ten. Each one teaches you something the last one didn't."*
