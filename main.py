# -*- coding: utf-8 -*-
"""
نقطه ورود برنامه
"""
import sys
import os

# اطمینان از import درست پکیج
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import run

if __name__ == "__main__":
    run()
