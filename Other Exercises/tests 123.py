import csv
import shutil
import webbrowser


user_search=input("Please Enter a Search Term: ").replace(" ",'+')

webbrowser.open('https://google.com/search?q='+user_search)

