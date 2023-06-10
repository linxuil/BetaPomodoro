#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""search_cmd_line.py: Example for using python grep function "grepli" """
__author__ = "linxuil"

import os
import sys
# setting path
script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, script_path)

import argparse
from grepli import grepli

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Search for a pattern in provided arguments.")
    parser.add_argument("pattern", help="The pattern to search for.")
    parser.add_argument("args", nargs="+", help="The input arguments to search the pattern in.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the grepli function with the provided arguments
    result = grepli(args.pattern, *args.args)

    # Print the results
    print(result)

if __name__ == "__main__":
    main()
