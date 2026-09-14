# Sorting Algorithms & Complexity Analysis

I implemented bubble sort, quicksort, and merge sort in Python, then actually measured how they perform, validating the textbook's Big-O values.

## What's mine

`trees.py` was given to us as starter code. Everything in `lab9.py` — the comparison-counting `LessThan` class and all three sorts — is code I wrote for CSCI 134 at Williams.

## What I found

- Bubble sort really is O(n²): doubling the list from 100 to 200 items roughly quadrupled the number of comparisons (~5,000 → ~20,000).
- Quicksort's worst case is real, not just theoretical — with a fixed pivot, it degrades to bubble-sort-level slowness on a list that's already sorted.
- Fix: pick the pivot randomly instead, and that problem mostly goes away.
- Merge sort didn't care what order the input was in — it stayed fast no matter what I threw at it.

## Try it yourself

```bash
pip install matplotlib
python3 -c "from lab9 import *; plot_efficiency_curve([bubble_sort, quick_sort, merge_sort], 200)"
```
