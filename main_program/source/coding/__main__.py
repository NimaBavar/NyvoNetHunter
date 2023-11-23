#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoAI main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


from PyQt5 import uic


ui_path = r"main_program/source/ui_design/main.ui"

with open(r"testing.py", "w") as compile_file_object:
    uic.compileUi(ui_path, compile_file_object)