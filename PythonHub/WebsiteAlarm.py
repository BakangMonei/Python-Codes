import time

import webbrowser

Set_Alarm = input("Set the website alarm as H:M:S(all in  2 digits): ")

url = input("Name of browser you want to open: ")

Actual_Time = time.strftime("%H:%M:%S")

while (Actual_Time != Set_Alarm):
    print ("The time is " + Actual_Time)
    Actual_Time = time.strftime("%H:%M:%S")
    time.sleep(1)
if (Actual_Time == Set_Alarm):
    print("You should see your webpage now :-) ")
    webbrowser.open(url)