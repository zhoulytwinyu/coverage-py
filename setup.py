#!/usr/bin/env python3
from setuptools import setup

setup(
  name="coverage",
  version="0.0.1",
  packages=["coverage"],
  scripts=["bin/get_coverages.py"],
  test_suite="tests"
)
