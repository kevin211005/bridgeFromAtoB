# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:15:31 2023
此模組提供了一個可以監聽應用程式A的文字輸入，並將其複製到應用程式B的功能。
"""

from pywinauto.application import Application
import pywinauto
import time

class OpenApplicationFailed(Exception):
    def __init__(self, msg = ""):    
        super().__init__(msg)

def openApplication(application):
    """
    打開指定的應用程式。

    Args:
        application (str): 應用程式名稱。

    Returns:
        pywinauto.application.Application: 應用程式物件。

    Raises:
        OpenApplicationFailed: 無法找到指定的應用程式。
    """
    try:
        app = pywinauto.Desktop(backend="uia").window(title=application)
        return app
    except:
        raise OpenApplicationFailed(f"Cannot find application: {application}")

def SentTextFromAToB(sourceAppName, targeAppName):
    """
    監聽應用程式A的文字輸入，並將其複製到應用程式B。

    Args:
        sourceAppName (str): 應用程式A的名稱。
        targeAppName (str): 應用程式B的名稱。
    """
    text = ""
    while True:
        try:
            app_source = pywinauto.Desktop(backend="uia").window(title=sourceAppName)
            app_target = pywinauto.Desktop(backend="uia").window(title=targeAppName)
            #Listen to application A text changed
            while True:
                currentText = " ".join(app_source.child_window(auto_id="TextField1", control_type="Edit").wrapper_object().texts())
                if text != currentText:
                    text = currentText
                    ## set Text to text field in target Application
                    app_target.child_window(auto_id="TargetTextField", control_type="Edit").wrapper_object().set_text(text = text)     
                    print("Changing Text in target Application suceess")
                else:
                    print("Text in soure has not been changed")
                print("Listent change per 2 second")
                time.sleep(2)
        except Exception as e:
            text = ""
            print(e)
            print("Retry after 5s")
            time.sleep(5)
            
if __name__ == '__main__':
    # app = pywinauto.Desktop(backend="uia").window(title="Target")
    # app.print_control_identifiers() 尋找控制項的名稱
    SentTextFromAToB("Source", "Target")
    
    