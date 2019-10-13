# coverage
This module calculate the read coverage for each loci, given nucleotide reads and loci of interest, 

## Install
```
pip install git+https://www.github.com/zhoulytwinyu/coverage-py
```

## Usage
### Python interface
You can import functions to calculate coveraged:
```
from coverage import get_coverages_bisect
get_coverages_bisect
```
### Command line interface
A command line script is included in the package. Once the package is installed using pip, you can call:
```
get_coverages.py <READS_CSV> <LOCI_CSV> <OUTPUT_CSV>
```
where
* `READS_CSV` is a csv containing "start" and "length"
* `LOCI_CSV` is a csv containing "position"
* `OUTPUT_CSV` is the output, a csv containing "position" and "coverage"

## Unittest
You can verify the module works correctly by running unittest we provided.
In command line:
```
git clone https://www.github.com/zhoulytwinyu/coverage-py.git
cd coverage-py
python3 setup.py test
```

The unittest randomly generate reads and loci, in silico and then crosscheck the results from two methods: `get_coverages_bisect` and `get_coverages_loop`.
The idea is that random, simulated test may cover more corner cases and the two methods provide the same result only when both of them works correctly.
