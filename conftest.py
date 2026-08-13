"""
pytest configuration file to set up pythonpath for src/ and root imports.
"""

import os
import sys

# Ensure src/ and current root directory are in sys.path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
