import os
import shutil
import disutils
from disutils.dir_util import copy_tree

# Peter Vallet, Jung Lab, 2022 
# Search_Convert_CopyImage V1
# Script 
# 1. Copies Parent Folder to renamed Parent Folder
# 2. Recursively Searches and runs Image Conversion Macro on TIF
# 3. Prints message Confirming Success
# Final is UNIX/MACOS compatible

# set this equal to parent folder of where you want to convert
OG_parent_path = None #<<<<<<this one
######################
# don't touch below
new_parent_path = None

# checks for the parent folder with images and names a copied
# folder if found 
if not (os.path.isdir(OG_parent_path)):
	raise ValueError("Original Path Name does not Exist. Search_Convert_Copy")
else:
	new_parent_path = (OG_parent_path + '_JPEG_converted')

# checks if a new folder exists, if not, makes it based on
# original folders name 
if not (os.path.isdir(new_parent_path)):
	os.makedirs(new_parent_path)
# copies over file into renamed alternative folder
copy_tree(OG_parent_path, new_parent_path)

# implement searching new_parent_path for .TIF 
# implement running macro for .JPEG conversion

# implement success prompt 




