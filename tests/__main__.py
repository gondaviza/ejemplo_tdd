#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest


from tests.test_funciones import TestFunciones


if __name__ == '__main__':
    try:
        # Test Suite 
        test = unittest.TestSuite()
        test.addTest(TestFunciones('test_hello_world'))
        # Run
        unittest.TextTestRunner().run(test)
    except KeyboardInterrupt:
        print("\nInterrumpido")
        sys.exit(0)
    except Exception as e:
        print("\nError: " + str(e))
        sys.exit(1)
