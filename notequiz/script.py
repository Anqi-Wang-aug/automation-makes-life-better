import os
import pyautogui
import time

os.startfile("msedge", arguments = 'https://chatgpt.com/')
print('Are you logged in? [Y/n]')
logged = input()
print('Go to chatbox')
# if loggedin: wait for 5 seconds other wait for 30s
if logged.lower()=='y': time.sleep(5)
else: time.sleep(30)
pyautogui.write('can you quiz me over this note?')
print('Go to file explorer')
time.sleep(7)
pyautogui.write(r'C:\Users\Huawei\OneDrive\Documents\Unimelb Vault')
pyautogui.press('enter')