#!/usr/bin/env python3
from unittest import TestCase
from coverage import get_coverages_bisect,get_coverages_loop
from random import randint

def generate_read(range_start,range_end):
  pair = [
    randint(range_start,range_end),
    randint(range_start,range_end)
  ]
  read = {
    "start": min(pair), # inclusive
    "end":  max(pair)   # non-inclusive
  }
  read["end"] = max(read["start"]+1,read["end"])
  # Making sure the read is at least 1 bp long
  return read

def generate_reads(range_start,range_end,num):
  reads = [
    generate_read(range_start,range_end)
    for i in range(num)
  ]
  return reads

class TestCoverage(TestCase):
  def test_simulation_get_coverages_bisect(self):
    range_start = 0
    range_end = 1000
    loci = [
      {"position":i}
      for i in range(range_start,range_end)
    ]
    reads = generate_reads(range_start,range_end,10000)
    self.assertEqual(
      get_coverages_bisect(loci,reads),
      get_coverages_loop(loci,reads)
    )
