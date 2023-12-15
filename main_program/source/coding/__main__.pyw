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
    NyvoNetHunterIpAddress,
    NyvoNetHunterUrl,
    examine_endpoint,
    is_valid_ipv4,
    is_valid_ipv6,
    is_valid_url,
    is_valid_ip,
    Connectable, 
)
from database.connection_status import ConnectionStatusChecker
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
            
            self.api_call_thread.exit()
            return
            
            
        try:
            
            try:
                self.api_call_thread.start()
                backend_examine_result = loads(examine_endpoint(self.connectable_object))
                
                self.api_call_thread.exit()
            
            except Exception:
                self.ui.responseLabel.setText("No internet connection.")
                self.api_call_thread.exit()
                
                self.no_connction_state()

                return
            
        except SSLError:
            self.ui.responseLabel.setText("Too many examines in a short period of time, please wait for at least 3 seconds.")
            
            self.api_call_thread.exit()
            return
            
            
        examine_text = ""
        for option_index, option in enumerate(checked_examine_options):
            option_index = option_index + 1
            
            try:
                examine_text += f"{option_index}. {option}: {backend_examine_result[option]}\n\n"
            
            except KeyError:
                examine_text += f"{option_index}. {option}: Not found.\n\n"
            
        
        examine_text += f"Examined endpoint: {self.ui.lineEdit.text()}"
            
        self.ui.responseLabel.clear()
        self.ui.responseLabel.setText(examine_text)
        

    def api_examining_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode( ), parent=self)
        
        progressbar_percent_animation.setDuration(300)
        progressbar_percent_animation.setStartValue(0)
        progressbar_percent_animation.setEndValue(100)
        

        self.ui.callstatusLabel.setText("Examining...")
        
        progressbar_percent_animation.start()
        self.fill_animation_thread.exit()
        
        progressbar_percent_animation.finished.connect(self.api_responded_animation)
        self.api_call_thread.exit()
        
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
        self.fill_animation_thread = QThread()
        self.connection_status_thread = QThread()
        
        self.connection_status_worker = ConnectionStatusChecker()
        
        self.connection_status_worker.lost_connection.connect(self.no_connction_state)
        self.connection_status_worker.spotted_connection.connect(self.connected_state)
        
        self.connection_status_worker.moveToThread(self.connection_status_thread)
        self.connection_status_thread.started.connect(self.connection_status_worker.run)
        
        
        
        self.fill_animation_thread.started.connect(self.api_examining_animation)
        
        self.ui.pushButton.clicked.connect(self.show_input_result)
        self.api_call_thread.started.connect(self.fill_animation_thread.start)
        
        
        self.show()
        self.connection_status_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())