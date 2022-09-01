import webbrowser

BASE_URL = "https://www.google.com/search?q="
tabsToOpen = []

while True:
    itemToSearch = input("What do you wnat to play? ")
    if itemToSearch == "close":
        print("Opening tabs .... ")
        break
    tabsToOpen.append(itemToSearch)

for i in tabsToOpen:
    webbrowser.open(BASE_URL + i)