#!/usr/bin/env python3
from coverage import get_coverages_bisect,get_coverages_loop
import csv
import sys

def get_loci(fname):
  ret = []
  with open(fname,'r') as fh:
    for row in csv.DictReader(fh):
      ret.append({
        **row,
        "position":int(row["position"])
      })
  return ret

def get_reads(fname):
  ret = []
  with open(fname,'r') as fh:
    for row in csv.DictReader(fh):
      ret.append({
        **row,
        "start":int(row["start"]),
        "end":int(row["start"])+int(row["length"])
      })
  return ret

if __name__=="__main__":
  if len(sys.argv)!=4:
    sys.exit("{} <READS_CSV> <LOCI_CSV> <OUTPUT_CSV>".format(sys.argv[0]))
  reads_fn = sys.argv[1]
  loci_fn = sys.argv[2]
  output_fn = sys.argv[3]
  reads = get_reads(reads_fn)
  loci = get_loci(loci_fn)
  coverages = get_coverages_bisect(loci,reads)
  loci_with_coverage = [{**l,"coverage":c} for l,c in zip(loci,coverages)]
  columns = list(loci_with_coverage[0].keys())
  with open(output_fn,'w') as fh:
    writer = csv.DictWriter(fh,columns)
    writer.writeheader()
    writer.writerows(loci_with_coverage)
