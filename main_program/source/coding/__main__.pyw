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

    generated_line_edit_connectable = pyqtSignal()
    fill_animationgroup_finished = pyqtSignal()
    no_examine_option_found = pyqtSignal()
    invalid_endpoint_passed = pyqtSignal()
    user_input_is_empty = pyqtSignal()

    def set_progressbar_value(self, amount: int) -> None:
    
        if amount > 100:
            raise TypeError(f"The progress bar fill amount cannot be more than 100.")

        if not isinstance(amount, (int, float)):
            amount_argument_type = type(amount).__name__
            raise TypeError(
                f"Expected argument type for the parameter ( amount ): int | Not {amount_argument_type}"
            )

        self.ui.progressBar.setValue(amount)
    
    def _set_examine_attributes(self, connectable: Connectable) -> str:
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
        
        self.network_manager_worker.__setattr__("headers", api_key_header)
        self.network_manager_worker.__setattr__("data", {})
        self.network_manager_worker.__setattr__("method", "get")
        

        if connectable_endpoint_type == "ip":
            self.network_manager_worker.__setattr__("url", f"{ip_lookup_api_url}{connectable.endpoint}")
            return

        if connectable_endpoint_type == "url":
            self.network_manager_worker.__setattr__("url", f"{url_lookup_api_url}{connectable.endpoint}")
            return
        
    def generate_user_desired_connectable(self) -> Connectable:
    
        self.inputted_text = self.ui.lineEdit.text()
        line_edit_is_empty = not self.inputted_text
        if line_edit_is_empty:
            self.user_input_is_empty.emit()
            del self.network_manager_worker.response
            return 
        
        try:
        
            generated_connectable = generate_valid_connectable(self.inputted_text)
             
        except (ValueError, TypeError):
            self.invalid_endpoint_passed.emit()
            return
            
        self.generated_connectable = generated_connectable
            
            
        self.inputted_text = ""
        self.generated_line_edit_connectable.emit()
        return generated_connectable
    
        
    def show_response(self) -> None:
        line_edit_is_empty = not self.ui.lineEdit.text()
        if line_edit_is_empty:
            self.user_input_is_empty.emit()
            return
    
        try:
            response = self.network_manager_worker.response.json()
            if hasattr(self.network_manager_worker, "response"):
                del self.network_manager_worker.response
            
        except Exception as e:
            if hasattr(self.network_manager_worker, "response"):
            
                del self.network_manager_worker.response
            return
            
        checked_options = self.get_checked_examine_options()
        
        no_examine_option_is_checked = len(checked_options) == 0
        if no_examine_option_is_checked:
            self.no_examine_option_found.emit()
            return
        
        examine_text = ""
        for option_index, option in enumerate(checked_options):
            option_index = option_index + 1
            
            try:
                examine_text += f"{option_index}. {option}: {response[option]}\n\n"
            
            except KeyError:
                examine_text += f"{option_index}. {option}: Not found.\n\n"
            
        
        examine_text += f"Examined endpoint: {self.ui.lineEdit.text()}"
        
        
        self.ui.responseLabel.setText(examine_text)
        self.ui.lineEdit.clear()
        return
        
    def api_connected_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        progressbar_percent_animation.setDuration(1000)
        progressbar_percent_animation.setStartValue(0)
        progressbar_percent_animation.setEndValue(100)
        
        self.ui.callstatusLabel.setText("Connecting...")
        
        progressbar_percent_animation.start()
        
        progressbar_percent_animation.finished.connect(self.fill_animationgroup_finished.emit)
        
    def api_disconnected_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        progressbar_percent_animation.setDuration(1000)
        progressbar_percent_animation.setStartValue(100)
        progressbar_percent_animation.setEndValue(0)
        
        self.ui.callstatusLabel.setText("Diconnected...") 
            
    def api_examining_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode( ), parent=self)
        
        progressbar_percent_animation.setDuration(4000)
        progressbar_percent_animation.setStartValue(0)
        progressbar_percent_animation.setEndValue(100)
        

        self.ui.callstatusLabel.setText("Examining...")
        
        
        progressbar_percent_animation.start()

    def api_responded_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        progressbar_percent_animation.setDuration(500)
        progressbar_percent_animation.setStartValue(100)
        progressbar_percent_animation.setEndValue(0)
        
        progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Awaiting input.")
        
    def api_fast_fill_animation(self) -> None:
        progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        progressbar_percent_animation.setDuration(100)
        progressbar_percent_animation.setStartValue(self.ui.progressBar.value())
        progressbar_percent_animation.setEndValue(100)
        
        progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Examining...")
        
        self.fill_animationgroup_finished.emit()
        

    def get_checked_examine_options(self) -> None:
        
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
        
    def no_connction_state(self) -> None:
    
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
        
    def connected_state(self) -> None:  
    
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
    
        
    def initialize_connection_checker(self) -> None:

        self.connection_status_thread = QThread()
        self.connection_status_worker = ConnectionStatusChecker()

        self.connection_status_worker.moveToThread(self.connection_status_thread)
        
        self.connection_status_worker.spotted_connection.connect(self.connected_state)
        self.connection_status_worker.lost_connection.connect(self.no_connction_state)
        
        self.connection_status_thread.started.connect(self.connection_status_worker.run)
        self.connection_status_thread.start()
        
    def initialize_network_logic(self) -> None:

        self.network_manager_thread = QThread()
        self.network_manager_worker = NyvoNetHunterRequestManager(
            url="https://google.com",
            method="get",
            headers={},
            data={},
        )
        
        self.network_manager_worker.moveToThread(self.network_manager_thread)
        self.network_manager_thread.started.connect(self.network_manager_worker.fire)
        self.network_manager_worker.received_invalid_response.connect(self.network_manager_thread.exit)
        self.network_manager_worker.received_valid_response.connect(self.network_manager_thread.exit)
        
        self.ui.pushButton.clicked.connect(self.generate_user_desired_connectable)
        
        self.no_examine_option_found.connect(lambda: self.ui.responseLabel.setText("Please choose at least 1 examine option."))
        self.user_input_is_empty.connect(lambda: self.ui.responseLabel.setText("Please provide a valid IP or URL address."))
        self.invalid_endpoint_passed.connect(lambda: self.ui.responseLabel.setText("Invalid endpoint or URL passed."))
        self.invalid_endpoint_passed.connect(lambda: globals().__setitem__("self.response", ""))
        
        try:
            self.generated_line_edit_connectable.connect(lambda: self._set_examine_attributes(self.generated_connectable))
        
        except:
            return
        
        self.network_manager_worker.received_valid_response.connect(self.show_response)
        self.network_manager_worker.received_invalid_response.connect(self.show_response)
    
        self.ui.pushButton.clicked.connect(self.network_manager_thread.start)
        
    def initialize_animations_logic(self) -> None:
    
        self.animation_thread = QThread()
        
        self.animation_thread.started.connect(self.api_examining_animation)
        self.animation_thread.finished.connect(self.api_responded_animation)
        
        self.network_manager_worker.sending_request.connect(self.api_examining_animation)
        self.network_manager_worker.request_sent.connect(self.api_fast_fill_animation)
    
        self.connection_status_worker.spotted_connection.connect(self.api_connected_animation)
        
        
        self.connection_status_worker.spotted_connection.connect(self.api_connected_animation)
        self.connection_status_worker.lost_connection.connect(self.api_disconnected_animation)
        
        self.invalid_endpoint_passed.connect(self.api_fast_fill_animation)
        
        self.fill_animationgroup_finished.connect(self.api_responded_animation)
        
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    

        
        self.initialize_connection_checker()
        self.initialize_network_logic()
        self.initialize_animations_logic()
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())