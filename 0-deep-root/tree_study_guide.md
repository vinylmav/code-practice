# Day 3 — Tree Traversals: The Order of Operations

> You already know HOW to visit every node in a tree (recursion). Today's puzzle: **in what ORDER?**

---

## The Puzzle

Imagine you're a postman delivering letters to every house in a neighbourhood shaped like a tree. You WILL visit every house — that's guaranteed. The question is: **when do you read the letter at each house?**

You have three choices at every house:
1. **Read the letter FIRST**, then visit your left neighbourhood, then your right neighbourhood
2. **Visit left first**, then read the letter, then visit right
3. **Visit left, visit right**, then **read the letter LAST**

That's it. That's the entire difference between the three traversals. Same houses, same visits, different order of reading.

---

## The Three Traversals

Using your tree from Day 2:

```
      1
     / \
    2   3
   / \   \
  4   5   6
```

### Pre-order: "Process myself FIRST, then children"

**Order:** Root → Left → Right

The analogy: A **manager** who announces the decision BEFORE delegating. "Here's what we're doing. Now left team, go. Now right team, go."

```
Visit 1 → READ 1
  Visit 2 → READ 2
    Visit 4 → READ 4
      (no children)
    Visit 5 → READ 5
      (no children)
  Visit 3 → READ 3
    (no left child)
    Visit 6 → READ 6
      (no children)

Result: [1, 2, 4, 5, 3, 6]
```

**The code (you already know this shape):**
```python
def preorder(node):
    if node is None:
        return
    print(node.value)      # process FIRST
    preorder(node.left)     # then left
    preorder(node.right)    # then right
```

**When is pre-order useful?**
- **Copying a tree** — you need to create the root before you can attach children
- **Serializing a tree** — saving it to a file (root first, then structure)
- **Prefix expressions** — like `+ 2 3` instead of `2 + 3`

---

### In-order: "Left child first, then ME, then right child"

**Order:** Left → Root → Right

The analogy: A **mediator** who hears the left side, gives the verdict, then hears the right side.

```
  Visit 1
    Visit 2
      Visit 4
        (no left) → READ 4 → (no right)
      READ 2
      Visit 5
        (no left) → READ 5 → (no right)
    READ 1
    Visit 3
      (no left) → READ 3
      Visit 6
        (no left) → READ 6 → (no right)

Result: [4, 2, 5, 1, 3, 6]
```

**The code:**
```python
def inorder(node):
    if node is None:
        return
    inorder(node.left)      # left first
    print(node.value)       # then process ME
    inorder(node.right)     # then right
```

**🔥 THE BIG INSIGHT — In-order + BST = Sorted Output**

This is the single most important fact about in-order traversal. If your tree is a **Binary Search Tree** (left < root < right), then in-order traversal visits nodes in **sorted ascending order**.

Why? Because in a BST:
- Everything in the left subtree is **smaller** than the root
- Everything in the right subtree is **bigger** than the root
- In-order visits left (smaller stuff) → root → right (bigger stuff)

This is a weapon. If an interviewer asks "validate a BST" or "find the kth smallest element" — in-order traversal is the shape.

Example BST:
```
      4
     / \
    2   6
   / \ / \
  1  3 5  7
```

In-order: [1, 2, 3, 4, 5, 6, 7] ← perfectly sorted!

---

### Post-order: "Children first, then ME last"

**Order:** Left → Right → Root

The analogy: A **judge** who hears ALL the evidence from both sides before making a ruling.

```
  Visit 1
    Visit 2
      Visit 4
        (no children) → READ 4
      Visit 5
        (no children) → READ 5
      READ 2  ← only after both children done
    Visit 3
      (no left)
      Visit 6
        (no children) → READ 6
      READ 3  ← only after child done
    READ 1  ← the LAST to be read

Result: [4, 5, 2, 6, 3, 1]
```

**The code:**
```python
def postorder(node):
    if node is None:
        return
    postorder(node.left)    # left first
    postorder(node.right)   # then right
    print(node.value)       # process ME last
```

**When is post-order useful?**
- **Deleting a tree** — you must delete children before deleting the parent (can't orphan nodes)
- **Calculating directory sizes** — you need to know the sizes of all subfolders before you can compute the parent folder's size
- **Evaluating expression trees** — you need the operands before you can apply the operator
- **Your Day 2 bottom-up problems were ALL post-order!** — `count_nodes`, `height`, `max_value`, `mirror` — they all process children first, then combine at the current node. That's post-order.

---

## Wait — I Already Know Post-Order?

Yes. Look:

```python
# count_nodes — this IS post-order
def count_nodes(node):
    if node is None:
        return 0
    left = count_nodes(node.left)    # left first
    right = count_nodes(node.right)  # right second
    return 1 + left + right          # process ME last (using children's answers)
```

Every bottom-up function you wrote on Day 2 was a post-order traversal. You just didn't call it that. The only difference:
- "Pure" post-order just **visits** (prints/collects)
- Your Day 2 functions **compute and return** during the post-order visit

Same order. Different cargo.

---

## The Pattern — One Skeleton, Three Orders

All three traversals are the SAME code with the `print` line in a different position:

```python
def traverse(node):
    if node is None:
        return
    # ← print HERE = pre-order  (before children)
    traverse(node.left)
    # ← print HERE = in-order   (between children)
    traverse(node.right)
    # ← print HERE = post-order (after children)
```

That's it. Three traversals, one skeleton, different timing.

---

## Level-Order (BFS): The Fundamentally Different One

The three traversals above are all **DFS** (Depth-First Search) — they go as deep as possible down one branch before backtracking. They use the **call stack** (recursion).

Level-order is **BFS** (Breadth-First Search) — it visits ALL nodes at depth 0, then ALL at depth 1, then ALL at depth 2, etc.

### The Analogy

**DFS** (pre/in/post-order) = Exploring a cave. You pick one tunnel and go as deep as it goes. Hit a dead end? Backtrack and try the next tunnel.

**BFS** (level-order) = Dropping a stone in a pond. Ripples expand outward in concentric circles. You visit everything at distance 1 first, then distance 2, then distance 3.

```
      1          ← Level 0: [1]
     / \
    2   3        ← Level 1: [2, 3]
   / \   \
  4   5   6      ← Level 2: [4, 5, 6]

Level-order result: [1, 2, 3, 4, 5, 6]
```

### Why BFS Needs a Queue (Not Recursion)

Recursion naturally goes DEEP (it follows one branch all the way down). But BFS needs to go WIDE — process all siblings before going to the next level.

A **queue** (first-in, first-out) makes this work:

```
1. Start: queue = [1]
2. Pop 1, add its children → queue = [2, 3]         → output: 1
3. Pop 2, add its children → queue = [3, 4, 5]      → output: 2
4. Pop 3, add its children → queue = [4, 5, 6]      → output: 3
5. Pop 4, no children      → queue = [5, 6]          → output: 4
6. Pop 5, no children      → queue = [6]             → output: 5
7. Pop 6, no children      → queue = []              → output: 6

Result: [1, 2, 3, 4, 5, 6]
```

See the pattern? You process a node, then put its children at the BACK of the line. Since children are always added after their siblings, all of level N is processed before ANY of level N+1.

### The Code

```python
from collections import deque

def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()     # take from FRONT
        print(node.value)          # process
        if node.left:
            queue.append(node.left)   # add to BACK
        if node.right:
            queue.append(node.right)  # add to BACK
```

### Level-by-Level Variant (Very Common in Interviews)

Often you need the output grouped by level: `[[1], [2, 3], [4, 5, 6]]`.

The trick: process the queue in **batches**. At the start of each level, the queue contains exactly the nodes for that level.

```python
from collections import deque

def level_order_grouped(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)        # how many nodes at THIS level
        level = []
        for _ in range(level_size):    # process exactly that many
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

**Why this works:** Before the inner loop, the queue has ONLY nodes from the current level (because we added all their children but haven't processed them yet). We record `level_size`, process exactly that many nodes, and by the time the inner loop ends, the queue has been refilled with ONLY the next level's nodes.

---

## DFS vs BFS — When to Use Which

| | DFS (pre/in/post) | BFS (level-order) |
|---|---|---|
| **Uses** | Call stack (recursion) or explicit stack | Queue |
| **Explores** | Deep first | Wide first |
| **Good for** | Path problems, tree structure, subtree operations | Level-by-level problems, shortest path, nearest neighbor |
| **Space** | O(h) where h = height | O(w) where w = max width |
| **Interview signals** | "path from root to...", "subtree", "recursive structure" | "level", "depth", "layer", "closest", "zigzag" |

---

## The Connection to Your Day 2 Work

| Day 2 Problem | Which traversal? | Why? |
|---|---|---|
| `count_nodes` | Post-order | Process children first, combine at current node |
| `max_value` | Post-order | Same — get children's max, combine |
| `height` | Post-order | Get children's heights, take max + 1 |
| `mirror` | Post-order | Mirror children first, then swap at current node |
| `check` (identical) | Post-order | Check children first, combine with current comparison |
| `path_sum` | Pre-order (top-down) | Process current node first (subtract value), then pass to children |

You've been doing traversals all along. Now you have the vocabulary for it.

---

## Practice Problems (For When You're Back)

Code these in `code-practice/day-3/traversals.py`:

### Warm-ups (Use your Day 2 tree)
1. **Implement all four traversals** — preorder, inorder, postorder, level_order. Each should return a list of values.
2. **Level-order grouped** — return `[[1], [2, 3], [4, 5, 6]]`

### The Real Puzzles
3. **Build a BST** — Write an `insert(root, value)` function that inserts a value into a BST. Then insert `[4, 2, 6, 1, 3, 5, 7]` one by one. Run in-order on it. What do you get?

4. **Validate BST** — Given a tree, is it a valid BST? (Hint: what does in-order traversal of a valid BST look like? What property must the output have?)

5. **Max depth using BFS** — You solved this with recursion on Day 2. Now solve it using level-order traversal. How many levels did you process? That's the depth.

6. **Right side view** — Imagine standing to the RIGHT of the tree and looking at it. Which nodes can you see? (Hint: it's the LAST node at each level.)
   ```
         1      ← you see 1
        / \
       2   3    ← you see 3
      / \   \
     4   5   6  ← you see 6

   Right side view: [1, 3, 6]
   ```

### Stretch (If You're Feeling Sharp)
7. **Zigzag level-order** — Level 0 left-to-right, level 1 right-to-left, level 2 left-to-right...
   ```
   Result: [[1], [3, 2], [4, 5, 6]]
   ```

---

## Key Takeaways for Day 3

1. **Three DFS traversals = same skeleton, different timing.** Pre (before children), In (between), Post (after).
2. **In-order + BST = sorted.** This is a weapon. Remember it.
3. **Your Day 2 bottom-up solutions were post-order.** You already knew this traversal — now you have the name.
4. **BFS uses a queue, not recursion.** It goes wide, not deep. Use it when the problem talks about "levels" or "layers."
5. **Level-by-level trick:** snapshot `len(queue)` at the start of each level, process exactly that many.

---

*Read this on the road. Code the practice problems when you're back. Day 3 is about giving names to things you already understand — and adding BFS as a new tool.*
