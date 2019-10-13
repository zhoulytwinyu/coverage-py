#!/usr/bin/env python3
from bisect import bisect_left, bisect_right

def get_coverages_bisect(loci,reads):
  sorted_starts = sorted([r["start"] for r in reads])
  sorted_ends = sorted([r["end"] for r in reads])
  ret = []
  for l in loci:
    p=l["position"]
    count_right = len(reads)-bisect_right(sorted_starts,p)
    # This is such that s<=p for all s in starts[0:right]
    # To programmatically test this, uncomment:
    # assert all([s<=p for s in starts[:right]])
    count_left = bisect_right(sorted_ends,p)
    count = len(reads)-count_left-count_right
    ret.append(count)
  return ret
  
def get_coverages_loop(loci,reads):
  ret = []
  for l in loci:
    p=l["position"]
    count = sum((
      r["start"]<=p and p<r["end"]
      for r in reads
    ))
    ret.append(count)
  return ret

