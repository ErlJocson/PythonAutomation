print("Opening work tabs ......")
import webbrowser

def openTabs(listOfTabs):
    for i in listOfTabs:
        webbrowser.open(i)

tabsToOpen = [
    "https://linkedin.com",
    "https://mail.google.com/",
    "https://google.com",
]

openTabs(tabsToOpen)