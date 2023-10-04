## Project Setup.
Install pywinauto 安裝 pytinauto 
```
pip install pywinauto
```
Run 執行
```
python main.py
```
## Customizing for Your Program 調整適用於自己的程式"

### Step1
Find target and sorce application 找尋目標和監測軟體名稱
```python
windows = pywinauto.Desktop(backend="uia").windows()
for window in windows:
    print(f"Title: {window.window_text()}")
```
### Step2 
Find the monitored field in the source application and the field that needs to be changed in the target application. 找尋需要被監測及改變項目
```python 
app_source.print_control_identifiers()
app_target.print_control_identifiers()
```
### Step3
Change auto_id in app_source, and app_target based on the field found in Step2 改變auto_ID

```python 
app_source.child_window(auto_id="YOUR FIELD", control_type="Edit").wrapper_object().texts()
```
## Reference

pywinauto:  
https://pywinauto.readthedocs.io/en/latest/index.html


To find method for each control type:
https://pywinauto.readthedocs.io/en/latest/controls_overview.html

## Video Demo
[Screen Recording - Made with FlexClip.webm](https://github.com/kevin211005/bridgeFromAtoB/assets/86145579/7bc75fc1-ff27-4ae0-b7f1-c8f613e29a6c)
