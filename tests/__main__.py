#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.test_package import TestPackage
from tests.test_simple import TestCalculadoraSimple
from tests.test_avanzada import TestCalculadoraAvanzada
from tests.test_data import TestData
from tests.test_web import TestWeg
from tests.test_rest import TestRest


if __name__ == '__main__':
    try:
        # Test Suite 
        test = unittest.TestSuite()
        test.addTest(TestPackage('test_package'))
        test.addTest(TestCalculadoraSimple('test_sum'))
        test.addTest(TestCalculadoraSimple('test_res'))
        test.addTest(TestCalculadoraSimple('test_mul'))
        test.addTest(TestCalculadoraSimple('test_div'))
        test.addTest(TestCalculadoraSimple('test_his'))
        test.addTest(TestCalculadoraAvanzada('test_pow'))
        test.addTest(TestCalculadoraAvanzada('test_pown'))
        test.addTest(TestCalculadoraAvanzada('test_sqrt'))
        test.addTest(TestCalculadoraAvanzada('test_log10'))
        test.addTest(TestCalculadoraAvanzada('test_log2'))
        test.addTest(TestCalculadoraAvanzada('test_lognep'))
        test.addTest(TestCalculadoraAvanzada('test_his'))
        test.addTest(TestData('test_truncate'))
        test.addTest(TestData('test_write'))
        test.addTest(TestData('test_read'))
        test.addTest(TestWeg('test_ops'))
        test.addTest(TestWeg('test_ops_seg'))
        test.addTest(TestWeg('test_ops_error'))
        test.addTest(TestRest('test_ops'))
        test.addTest(TestRest('test_ops_seg'))
        test.addTest(TestRest('test_ops_error'))
        # Run
        unittest.TextTestRunner().run(test)
    except KeyboardInterrupt:
        print("\nInterrumpido")
        sys.exit(0)
    except Exception as e:
        print("\nError: " + str(e))
        sys.exit(1)
