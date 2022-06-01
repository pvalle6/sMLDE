#script is windows specific 
import os 
import glob 

#file with the new names eg:(ID_1_VDGV)
fileWithNewNames = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\renamingConventionforFolders.txt"
#parent folder of the pdb files with the score files inside of each 
outputPath = R"C:\Users\valle\Downloads\FlexPepDock_200seq_output.tar\FlexPepDock_output"
outputAppended = (outputPath+R"\**\*.score.sc")
#lists 
nameList = []
ScoreName = [] 
FileNames = []

FolderNames = []
NewFolderNames = []
#reads all the names into a list by target ID
with open(fileWithNewNames) as file:
	nameList = file.readlines()
	nameList = (x.rstrip() for x in nameList)


#appends IDs with proper extensions and converts from a generator to a nongenerator 
for x in nameList:
	ScoreName.append(x+R".score.sc")
	NewFolderNames.append(x+R'.pdb')
#takes in all of the pdb folders to be read for the score files 
FileNames = (glob.glob((outputAppended)))
	
#for x, i in enumerate(FileNames):
	#os.rename(i, i[0:95]+(ScoreName[x]))
# 	test 
	#print(i)
	#print(i[0:95]+(ScoreName[x]))
	
# renaming folders 

#grabs the names of all the folders in the outputPath
FolderNames = (glob.glob(outputPath+R"\*"))

for x,i in enumerate(FolderNames):
	print((i[0:74])+NewFolderNames[x])
	#os.rename(i,((i[0:74])+NewFolderNames[x]))
 	print(x)
 	

