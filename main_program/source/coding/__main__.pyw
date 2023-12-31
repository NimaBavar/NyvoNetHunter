#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the CCV1.0 ( Creative Commons Zero v1.0 ) license agreements.
"""


from database.workers.api import (
    generate_valid_connectable,
    NyvoNetHunterIpAddress,
    simplify_long_string,
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
from database.map_api.map_spoofer import MapSpoofer
from database.ui_window_dialog import Ui_Dialog
from database.packages import *


class NyvoNetHunterApp(QDialog):

    fill_animationgroup_finished = pyqtSignal()
    setted_examine_attributes = pyqtSignal()
    examine_options_satisfied = pyqtSignal()
    connectable_is_generated = pyqtSignal()
    invalid_endpoint_passed = pyqtSignal()
    no_examine_option_found = pyqtSignal()
    progressbar_is_filled = pyqtSignal()
    user_input_is_empty = pyqtSignal()

    cant_spoof_location = pyqtSignal()
    can_spoof_location = pyqtSignal()
    longitude_found = pyqtSignal()
    latitude_found = pyqtSignal()

    network_query_finished = pyqtSignal()

    inputted_text = ""

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
        ip_lookup_api_url = "http://ip-api.com/json/"
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
            self.setted_examine_attributes.emit()
            return

        if connectable_endpoint_type == "url":
            self.network_manager_worker.__setattr__("url", f"{url_lookup_api_url}{connectable.endpoint}")
            self.setted_examine_attributes.emit()
            return
        
    def generate_user_desired_connectable(self) -> Connectable:
        self.ui.responseLabel.clear()
    
        self.inputted_text = self.ui.lineEdit.text()
        line_edit_is_empty = not self.inputted_text
        if line_edit_is_empty:
            self.user_input_is_empty.emit()
            return 
        
        try:
        
            generated_connectable = generate_valid_connectable(self.inputted_text)
             
        except (ValueError, TypeError):
            self.invalid_endpoint_passed.emit()
            return
            
        self.generated_connectable = generated_connectable
            
            
        self.connectable_is_generated.emit()
        return generated_connectable
    
        
    def show_response(self) -> None:

        self.bool_longitude_found = False
        self.bool_latitude_found = False

        response = self.network_manager_worker.response.json()

        self.checked_options = self.get_checked_examine_options()
        self.checked_options_amount = len(self.checked_options)
        
        self.unfetched_options_count = 0
        self.examine_text = ""
        for option_index, option in enumerate(self.checked_options):
            option_index = option_index + 1

            try:    
            
                self.examine_text += f"{option_index}. {option}: {response[option]}.\n"

                if option == "lon":
                    self.longitude = float(response[option])

                    self.bool_longitude_found = True
                    self.longitude_found.emit()

                if option == "lat":
                    self.latitude = float(response[option])

                    self.bool_latitude_found = True
                    self.latitude_found.emit()
            
            except KeyError:
                self.unfetched_options_count += 1
                self.examine_text += f"{option_index}. {option}: Not found.\n"

        
        if self.unfetched_options_count == self.checked_options_amount:
            self.examine_text = "No checked option found."
        
        self.examine_text += f"\n\nExamined endpoint: {self.inputted_text}"
        
        self.ui.responseLabel.setText(self.examine_text)
        self.ui.lineEdit.clear()

        self.network_query_finished.emit()
        return
        
    def api_connected_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(1000)
        self.progressbar_percent_animation.setStartValue(0)
        self.progressbar_percent_animation.setEndValue(100)
        
        self.ui.callstatusLabel.setText("Connecting...")
        
        self.progressbar_percent_animation.start()
        
        self.progressbar_percent_animation.finished.connect(self.fill_animationgroup_finished.emit)
        
    def api_disconnected_animation(self) -> None:
        selfprogressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        selfprogressbar_percent_animation.setDuration(1000)
        selfprogressbar_percent_animation.setStartValue(100)
        selfprogressbar_percent_animation.setEndValue(0)
        
        self.ui.callstatusLabel.setText("Diconnected...") 
            
    def api_examining_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode( ), parent=self)
        
        self.progressbar_percent_animation.setDuration(20000)
        self.progressbar_percent_animation.setStartValue(0)
        self.progressbar_percent_animation.setEndValue(100)
        self.ui.callstatusLabel.setText("Examining...")

        self.progressbar_percent_animation.start()

    def api_responded_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(500)
        self.progressbar_percent_animation.setStartValue(100)
        self.progressbar_percent_animation.setEndValue(0)
        
        self.progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Awaiting...")
        
    def api_fast_fill_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(100)
        self.progressbar_percent_animation.setStartValue(self.ui.progressBar.value())
        self.progressbar_percent_animation.setEndValue(100)
        
        self.progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Examining...")
        
        self.fill_animationgroup_finished.emit()
        
    def api_kill_animation(self):
        self.progressbar_percent_animation.stop()

        self.ui.callstatusLabel.setText("Awaiting...")
        self.ui.progressBar.setValue(0)

    def get_checked_examine_options(self) -> [list, None]:
        self.bool_longitude_found = False
        self.bool_latitude_found = False
        
        all_options = [option for option in dir(self.ui) if option.endswith("CheckBox")]
        requested_options = [getattr(self.ui, option) for option in all_options]
        self.checked_options_list = [option.objectName().replace("CheckBox", "") for option in requested_options if option.isChecked()]
        
        for option in self.checked_options_list:
            option_index = self.checked_options_list.index(option)

            if option == "zipcode":
                unified_option = option.replace("zipcode", "zip")    
                self.checked_options_list.insert(option_index, unified_option)

                del self.checked_options_list[option_index+1]
                
            if option == "latitude":
                unified_option = option.replace("latitude", "lat")
                self.checked_options_list.insert(option_index, unified_option)
                self.bool_latitude_found = True
            
                del self.checked_options_list[option_index+1]
                
            elif option == "longitude":
                unified_option = option.replace("longitude", "lon")
                self.checked_options_list.insert(option_index, unified_option)

                self.bool_longitude_found = True
                del self.checked_options_list[option_index+1]
                
        if not self.checked_options_list:
            self.no_examine_option_found.emit()
            return self.checked_options_list
        
        if self.checked_options_list:
            self.checked_options_list.sort()

        caller_function = inspect.currentframe().f_back.f_code.co_name
        if not caller_function == "show_response":
            self.examine_options_satisfied.emit()

        return self.checked_options_list
        
    def no_connection_state(self) -> None:
    
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
        self.ui.connection_status_label.setPixmap(self.ui.no_connection_icon)

    def warning_request_timeout(self) -> None:
        self.ui.responseLabel.setText("Request timed out, please try again.")

    def examining_state(self) -> None:
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText(None)

        self.ui.lineEdit.setDisabled(True)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "main_program/source/ui_design/resources/pictures/check_mark.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.ui.pushButton.setIcon(icon1)

    def default_query_state(self) -> None:
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setText("Examine")

        self.ui.lineEdit.setEnabled(True)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "main_program/source/ui_design/resources/pictures/pushbuttonicon.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.ui.pushButton.setIcon(icon1)

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

    def web_view_default_state(self) -> None:
        project_root_directory = Path.cwd()
        self.base_state_html = QtCore.QUrl.fromLocalFile(
            f"{project_root_directory}/main_program/source/coding/database/map_api/data_storage/base_state.html"
        )

        self.ui.webView.load(self.base_state_html)
        
    def initialize_connection_checker(self) -> None:
        self.connection_status_thread = QThread()
        self.connection_status_worker = ConnectionStatusChecker()

        self.connection_status_worker.lost_connection.connect(self.no_connection_state)
        self.connection_status_worker.spotted_connection.connect(self.connected_state)

        self.connection_status_worker.moveToThread(self.connection_status_thread)
        self.connection_status_thread.started.connect(self.connection_status_worker.run)

        self.connection_status_thread.start()

    def initialize_network_logic(self) -> None:
        self.ui.lineEdit.textChanged.connect(self.get_input_text)

        self.network_manager_worker = NyvoNetHunterRequestManager(url="https://github.com/KhodeNima", data={}, headers={}, method="get")
        self.network_manager_thread = QThread()

        self.network_manager_worker.moveToThread(self.network_manager_thread)
        self.network_manager_thread.started.connect(self.network_manager_worker.fire)
        self.examine_options_satisfied.connect(self.generate_user_desired_connectable)

        self.connectable_is_generated.connect(lambda: self._set_examine_attributes(self.generated_connectable))
    
        self.user_input_is_empty.connect(lambda: self.ui.responseLabel.setText("Please provide a valid IP or URL address."))
        self.invalid_endpoint_passed.connect(lambda: self.ui.responseLabel.setText(f"{self.simplified_input} is not a valid IP or URL address."))
        self.no_examine_option_found.connect(lambda: self.ui.responseLabel.setText("Please choose at least 1 examine option."))

        self.network_manager_worker.received_valid_response.connect(self.show_response)
        self.network_manager_worker.received_invalid_response.connect(self.show_response)
        self.network_manager_worker.received_invalid_response.connect(self.network_manager_thread.exit)
        self.network_manager_worker.received_valid_response.connect(self.network_manager_thread.exit)

        self.network_manager_worker.failed_to_send.connect(self.warning_request_timeout)
        self.network_manager_worker.failed_to_send.connect(self.network_manager_thread.exit)

        self.setted_examine_attributes.connect(self.network_manager_thread.start)

        self.ui.pushButton.clicked.connect(self.get_checked_examine_options)

    def initialize_spoofer_logic(self) -> None:
        self.map_spoofer = MapSpoofer(0, 0)
        self.html_data_storage = "main_program/source/coding/database/map_api/data_storage/spoof_result.html"

        check_spoof_status = lambda: (self.can_spoof_location.emit() 
            if all([self.bool_latitude_found, self.bool_longitude_found]) else self.cant_spoof_location.emit()
        )

        self.cant_spoof_location.connect(self.web_view_default_state)

        self.network_query_finished.connect(check_spoof_status)

        self.can_spoof_location.connect(lambda: self.map_spoofer.set_latitude(self.latitude))
        self.can_spoof_location.connect(lambda: self.map_spoofer.set_longitude(self.longitude))
        self.can_spoof_location.connect(self.map_spoofer.start)

        self.map_spoofer.location_spoofed.connect(lambda: self.map_spoofer.save_as_html_file(self.html_data_storage))

        project_root_directory = Path.cwd()
        map_location_file_path = QtCore.QUrl.fromLocalFile(
            f"{project_root_directory}/main_program/source/coding/database/map_api/data_storage/spoof_result.html"
        )

        self.map_spoofer.saved_as_html.connect(lambda: self.ui.webView.load(map_location_file_path))


    def initialize_animations_logic(self) -> None:
        self.web_view_default_state()

        self.connection_status_worker.lost_connection.connect(self.web_view_default_state)

        self.fill_animationgroup_finished.connect(self.api_kill_animation)

        self.network_manager_worker.request_started.connect(self.api_examining_animation)
        self.network_manager_worker.request_sent.connect(self.api_responded_animation)

        self.network_manager_worker.received_valid_response.connect(self.api_responded_animation)
        self.network_manager_worker.received_invalid_response.connect(self.api_responded_animation)

        self.network_manager_worker.failed_to_send.connect(self.warning_request_timeout)
        self.network_manager_worker.failed_to_send.connect(self.api_responded_animation)

        self.network_manager_worker.request_started.connect(self.examining_state)
        self.network_manager_worker.request_sent.connect(self.default_query_state)

    def get_input_text(self) -> str:
        self.inputted_text = self.ui.lineEdit.text()
        self.simplified_input = simplify_long_string(self.inputted_text)

        return self.inputted_text

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
    
        self.initialize_network_logic()
        self.initialize_connection_checker()
        self.initialize_animations_logic()
        self.initialize_spoofer_logic()
        self.show()
        
  
if __name__ == "__main__":
    app = QApplication(sys.argv + ["--no-sandbox"])
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())
