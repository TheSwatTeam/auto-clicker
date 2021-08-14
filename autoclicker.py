#// once its done the amount of clicks you want, the program will close.

import pyautogui, time
time.sleep(5) #// will wait 5 seconds to click so it doesnt start clicking right away, you can change this if you want it to start straight away or wait a bit longer :)
for i in range (9999999): #// the number is how many times this program to click. you can make it infinite by making it like 9999 or something.
	pyautogui.leftClick() #// You can enter co-ordinates in the brackets if you want to get a precise location for where it clicks
