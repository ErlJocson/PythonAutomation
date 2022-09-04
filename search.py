import webbrowser

BASE_URL = "https://www.google.com/search?q="
tabsToOpen = []

while True:
    itemToSearch = input("Search: ")
    if itemToSearch == "close" and tabsToOpen:
        print("Opening tabs .... ")
        break
    elif itemToSearch == "close":
        break
    tabsToOpen.append(itemToSearch)

if tabsToOpen:
    for i in tabsToOpen:
        webbrowser.open(BASE_URL + i)