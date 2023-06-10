#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_grepli.py: Test implementation for python grep function"""
__author__ = "linxuil"

import os
import sys
# setting path
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, test_path)

import unittest
from io import StringIO
from <!prj_name!> import <!prj_name!>

class Test<!prj_name!>(unittest.TestCase):
    def setUp(self):
        # Prepare test

    def tearDown(self):
        # Destroy settings 

    def test_<!prj_name!>(self):
        result = #prj function
        self.assertEqual(result, ["hello world"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
