#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


from database.data import (
    generate_valid_connectable,
    exmine_endpoint_location,
    NyvoNetHunterIpAddress,
    NyvoNetHunterUrl,
    is_valid_ipv4,
    is_valid_ipv6,
    is_valid_url,
    is_valid_ip,
    Connectable, 
)
from database.ui_window_dialog import Ui_Dialog
from database.packages import *


class NyvoNetHunterApp(QDialog):
    

    def set_progressbar_value(self, amount: int):
        if amount > 100:
            raise TypeError(f"The progress bar fill amount cannot be more than 100.")

        if not isinstance(amount, (int, float)):
            parameter_type = type(amount).__name__
            raise TypeError(
                f"Expected argument type for the parameter ( amount ): int | Not {parameter_type}"
            )

        self.ui.progressBar.setValue(amount)

    def set_lineedit_result(self):
        line_edit_input = self.ui.lineEdit.text()
        
        if not line_edit_input:
            self.ui.responseLabel.setText("Please provide a valid IP or URL.")
            return
        
        self.ui.responseLabel.clear()
        self.ui.lineEdit.clear()
        
        checked_examine_options = self.get_requested_examine_options()
        no_examine_option_is_checked = len(checked_examine_options) == 0
        if no_examine_option_is_checked:
            self.ui.responseLabel.setText("Please choose at least one examine option.")
            return 
            
        self.ui.callstatusLabel.setText("Examining.")
        
        try:
            
            self.connectable = generate_valid_connectable(line_edit_input)
            examine_result = loads(exmine_endpoint_location(self.connectable))
            
            if examine_result and not examine_result["is_valid"] == True:
                self.ui.responseLabel.setText("IP or URL address does not exist in the web.")
                return
            
                
        except TypeError:
            self.ui.responseLabel.setText("Invalid IP or URL address.")
            return 
            
            
        examine_text = ""
        for option_index, option in enumerate(checked_examine_options):
            option_index = option_index + 1
            
            try:
                examine_text += f"{option_index}. {option}: {examine_result[option]}\n\n"
            
            except KeyError:
                examine_text += f"{option_index}. {option}: Not found.\n\n"
            

        self.ui.responseLabel.setText(examine_text)
        self.ui.callstatusLabel.setText("Awaiting input.")
            

    def fill_progressbar_animation(self) -> None:
        ...

    def empty_progressbar_animation(self) -> None:
        ...
        
    def get_requested_examine_options(self):
        
        all_options = [option for option in dir(self.ui) if option.endswith("CheckBox")]
        requested_options = [getattr(self.ui, option) for option in all_options]
        checked_options_list = [option.objectName().replace("CheckBox", "") for option in requested_options if option.isChecked()]
        
        for option in checked_options_list:
            option_index = checked_options_list.index(option)
            
            if option == "zip":
                unified_option = option.replace("zipcode", "zip")
                checked_options_list.insert(option_index, unified_option)
                del checked_options_list[option_index+1]
                
            elif option == "latitude":
                unified_option = option.replace("latitude", "lat")
                checked_options_list.insert(option_index, unified_option)
                del checked_options_list[option_index+1]
                
            elif option == "longitude":
                unified_option = option.replace("longitude", "lon")
                checked_options_list.insert(option_index, unified_option)
                del checked_options_list[option_index+1]
                
        if checked_options_list:
            checked_options_list.sort()
            
        return checked_options_list
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.set_lineedit_result)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())
