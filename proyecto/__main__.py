#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MAIN"""

import sys
import traceback

if __name__ == '__main__':  # pragma: no cover
    try:
        pass
    except Exception as e:
        print('Ha habido un error inesperado: %s', e)
        print("\n%s", traceback.format_exc())
        print("\nError: " + str(e))
        sys.exit(1)
