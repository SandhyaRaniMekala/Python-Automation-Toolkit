import os
folder_path = "/Users/karthikamekala/Desktop/Test_Files"
for index, filename in enumerate(os.listdir(folder_path)):
    extension = os.path.splitext(filename)[1]
    new_name = f"Kerala_Trip_Photo_{index}{extension}"
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_name)
    os.rename(old_file, new_file)
    print(f"Renamed {filename} to {new_name}")
