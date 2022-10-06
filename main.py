import pyautogui # importeer de package 'pyautogui'
import shutil # importeer de package 'shutil'

# pyautogui.write('Hello There', interval=0.5) # typt met een interval van 0,5s na elke character 'Hello There'
confirm = pyautogui.confirm(text='Do you want to take a screenshot and save it to this folder?', title='screenshot', buttons=['OK', 'Cancel']) # laat een message box zien met een OK en Cancel button, returns de tekst van de geklikte button
if confirm == "OK": # word uitgevoerd als de confirm box OK teruggeeft
  myScreenshot = pyautogui.screenshot("screenshot_1.png") # maakt een screenshot met de filename 'screenshot_1.png'
  # myScreenshot.save('/Users/sanderschijf/Desktop/screenshot_1.png') # is de bedoeling dat de gemaakte screenshot wordt opgeslagen op deze file location
  original = r'/Applications/MAMP/htdocs/python/datatofish/control-keyboard/screenshot_1.png'
  target = r'/Users/sanderschijf/Desktop/screenshot_1.png'
  shutil.move(original, target)
if confirm == "Cancel": # word uitgevoerd als de confirm box Cancel teruggeeft
  print("maybe next time :)") # print in de terminal 'maybe next time :)'