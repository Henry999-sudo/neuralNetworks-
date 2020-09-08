#BatchInstall.py
import os
libs = {"numpy", "sklearn", "Requests", "beautifulsoup4", "pandas", "Networkx", "pypdf2"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful!")
except:
    print("Failed Somehow!")