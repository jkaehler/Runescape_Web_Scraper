import urllib
import re

url = "http://services.runescape.com/m=itemdb_oldschool/Bow_string/viewitem?obj=1777"

htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

with open("Raw_HTML.txt", "w") as file:
    file.write(htmltext)

