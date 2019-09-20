# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:39
# @Author:      LTH
import unittest
from lianxi2 import lianxi2
from lianxi3 import lianxi3
suite = unittest.TestSuite()
suite.addTest(lianxi2(test_case02))
suite.addTest(lianxi3(test_case03))
unittest.TestRunner().run(suite)