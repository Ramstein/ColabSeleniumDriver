import time, sys, win32clipboard, glob, os

list_of_files = glob.glob(r'C:\Users\user\Downloads\*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)