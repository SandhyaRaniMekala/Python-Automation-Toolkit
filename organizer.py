import os
import shutil
path = "/Users/karthikamekala/Desktop"
files = os.listdir(path)
for file in files:
    if file.endswith(".png"):
        if not os.path.exists(path + "/MyScreenshots"):
            os.mkdir(path + "/MyScreenshots")
        shutil.move(path + "/" + file, path + "/MyScreenshots/" + file)
        print(f"Sandhya, {file} manam succesful ga move chesesam!")
