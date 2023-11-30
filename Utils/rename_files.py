#!C:\Apps\Python310 python
# encoding: utf8
import os

work_dir = r'C:\Apps\xampp\htdocs\DemoSite\photos'
file_extension = '.jpeg'  # Change this to your desired file extension

# List all files in the directory
all_files = os.listdir(work_dir)

# Filter files with the specified file extension
ext_files = [file for file in all_files if file.endswith(file_extension)]

index = 22
# Rename files
for old_name in all_files:
    # Construct new file name, modify this line as needed
    new_name = "Image_" + str(index).zfill(4) + file_extension
    index+=1
    print ("'" + old_name + "',")
    # Full paths for old and new files
    # old_path = os.path.join(work_dir, old_name)
    # new_path = os.path.join(work_dir, new_name)

    # Rename the file
    # os.rename(old_path, new_path)
    # print(f'Renamed: {old_path} to {new_path}')
