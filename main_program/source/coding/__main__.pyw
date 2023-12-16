#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


from database.workers.api import (
    generate_valid_connectable,
    NyvoNetHunterIpAddress,
    find_endpoint_type,
    NyvoNetHunterUrl,
    is_valid_ipv4,
    is_valid_ipv6,
    is_valid_url,
    is_valid_ip,
    Connectable, 
)
from database.workers.connection_status import ConnectionStatusChecker
from database.workers.api import NyvoNetHunterRequestManager
from database.ui_window_dialog import Ui_Dialog
from database.packages import *


class NyvoNetHunterApp(QDialog):


    def set_progressbar_value(self, amount: int):
    
        if amount > 100:
            raise TypeError(f"The progress bar fill amount cannot be more than 100.")

        if not isinstance(amount, (int, float)):
            amount_argument_type = type(amount).__name__
            raise TypeError(
                f"Expected argument type for the parameter ( amount ): int | Not {amount_argument_type}"
            )

        self.ui.progressBar.setValue(amount)
    
    def examine_endpoint(self, connectable: Connectable) -> str:
        api_key = "KBvhRDGVffUsQQ97m1Cm6SkmBERj8NLXPqZH8A0y"
        ip_lookup_api_url = "https://api.api-ninjas.com/v1/iplookup?address="
        url_lookup_api_url = "https://api.api-ninjas.com/v1/urllookup?url="

        if not isinstance(connectable, Connectable):
            connectable_argument_type = type(connectable).__name__
            raise ValueError(
            f"Expected argument type passed for the parameter ( connectable ): Connectable | Not: ( {connectable_argument_type} )"
            )

        try:
            connectable_endpoint_type = find_endpoint_type(connectable=connectable)

        except (TypeError, ValueError) as exception:
            error_type = type(exception)
            error_message = repr(exception)

            raise error_type(error_message)

        api_key_sign = "X-Api-Key"
        api_key_value = api_key
        api_key_header = {api_key_sign: api_key_value}

        if connectable_endpoint_type == "ip":
            self.network_manager_worker.__setattr__("url", f"{ip_lookup_api_url}{connectable.endpoint}")
            self.network_manager_worker.__setattr__("headers", api_key_header)
            self.network_manager_worker.__setattr__("data", {})
            self.network_manager_worker.__setattr__("method", "get")
            
            self.network_manager_thread.start()


        if connectable_endpoint_type == "url":
            self.network_manager_worker.__setattr__("url", f"{url_lookup_api_url}{connectable.endpoint}")
            self.network_manager_worker.__setattr__("headers", api_key_header)
            self.network_manager_worker.__setattr__("data", {})
            self.network_manager_worker.__setattr__("method", "get")
            
            
            self.network_manager_thread.start()


    def show_input_result(self):

        line_edit_input = self.ui.lineEdit.text()
        
        checked_examine_options = self.get_requested_examine_options()
        no_examine_option_is_checked = len(checked_examine_options) == 0
        if no_examine_option_is_checked:
            self.ui.responseLabel.setText("Please choose at least one examine option.")
            return 
            
        try:
            self.connectable_object = generate_valid_connectable(line_edit_input)
                    

        except TypeError as t:
            self.ui.responseLabel.setText("Invalid IP or URL address, please try again.")
            return
            
        

    def api_examining_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode( ), parent=self)
        
        progressbar_percent_animation.setDuration(300)
        progressbar_percent_animation.setStartValue(0)
        progressbar_percent_animation.setEndValue(100)
        

        self.ui.callstatusLabel.setText("Examining...")
        
        progressbar_percent_animation.start()

        
    def api_responded_animation(self):
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        progressbar_percent_animation.setDuration(500)
        progressbar_percent_animation.setStartValue(100)
        progressbar_percent_animation.setEndValue(0)
        
        progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Awaiting input.")
        
        
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
        
    def no_connction_state(self):
    
        check_boxes = [
        
        widget for widget in dir(self.ui) 
        if not widget.startswith("__") 
        and not widget.endswith("__") 
        and widget.endswith("CheckBox")

        ]
    
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui
        
        for check_box in check_boxes:
            eval(f"self.ui.{check_box}.setDisabled(True)")
            
            
    
        self.ui.responseLabel.setText("No internet connection.")
        self.ui.connection_status_label.setPixmap(self.ui.no_connction_icon)
        
    def connected_state(self):  
        
        self.api_call_thread.start()
    
        check_boxes = [
        
        widget for widget in dir(self.ui) 
        if not widget.startswith("__") 
        and not widget.endswith("__") 
        and widget.endswith("CheckBox")

        ]
        
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setEnabled(True)

        for check_box in check_boxes:
            eval(f"self.ui.{check_box}.setDisabled(False)")
            
        self.ui.responseLabel.clear()
        
        self.ui.connection_status_label.setPixmap(self.ui.connected_icon)
        
        self.api_call_thread.exit()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    

        self.api_call_thread = QThread()
        self.connection_status_thread = QThread()
        self.network_manager_thread = QThread()
        
        self.connection_status_worker = ConnectionStatusChecker()
        self.network_manager_worker = NyvoNetHunterRequestManager(
            url="google.com",
            method="get",
            headers={},
            data={},
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())