from __future__ import absolute_import, division, print_function, with_statement

import unittest


class TestExample(unittest.TestCase):
    def test_case(self):
        self.assertEqual('foo', 'bar')
