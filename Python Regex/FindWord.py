import re
txt = "The rain in the Spain"
x = re.split("^The.*Spain$",txt)
if x:
    print("Yes we got it")
else:
    print("nope ")