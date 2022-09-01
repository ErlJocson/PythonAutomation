import webbrowser

def openTabs(listOfTabs):
    for i in listOfTabs:
        webbrowser.open(i)

print("Opening work tabs ......")

tabsToOpen = [
    "https://linkedin.com",
    "https://mail.google.com/",
    "https://google.com",
]

openTabs(tabsToOpen)