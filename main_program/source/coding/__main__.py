#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar ), Amirali Yazdani.
---
# This project and all of its components are licensed under the CCV1.0 ( Creative Commons Zero v1.0 ) license agreements.
"""


from database.workers.api import (
    generate_valid_connectable,
    NyvoNetHunterIpAddress,
    find_endpoint_type,
    NyvoNetHunterUrl,
    clean_terminal,
    simplify_text,
    is_valid_ipv4,
    is_valid_ipv6,
    is_valid_url,
    is_valid_ip,
    Connectable, 
)
from database.workers.connection_status import ConnectionStatusChecker
from database.workers.api import NyvoNetHunterRequestManager
from database.map_api.map_spoofer import MapSpoofer
from database.gui_setup.gui_logic import NyvoNetHunterApp
from database.packages import *


if __name__ == "__main__":
    app = QApplication(sys.argv + ["--no-sandbox"])
    app_window = NyvoNetHunterApp()
    app_window.show()

    print(f"\33[31mNyvoNetHunter:\33[36m Booted\33[31m.\33[0m")
    sys.exit(app_window.exec_())
