import time as tm
import os 
import shutil as til

appdata_path = os.environ.get("APPDATA")
os.chdir(appdata_path)  # changes the directory 
folders = os.listdir()  # lists the directory 
 



destination_folder =input("Destination_folder? ")
if not destination_folder.strip(): 
   exit("No data found")
   
Target_folder = "trilium-data"
backupfolder = "backup"

if any(Target_folder.lower() in folder.lower() for folder in folders):
    print("Target folder detected: " + Target_folder)
    tm.sleep(3)
    DirectoryOfTrilium = folders.index("trilium-data")
    directo = folders[DirectoryOfTrilium]

    if directo == "trilium-data":  # checks if trilium-data exists
     print("                                                      ")
     print("Moving to target folder: " + Target_folder)
     Changedir1 = os.chdir(Target_folder)
     current_directory1 = os.getcwd() 
     print("current Folder: " + current_directory1)
     print("                                      ")

     print("Moving to target folder: " + backupfolder )
     Changedir2 = os.chdir(backupfolder)
     current_directory2 = os.getcwd() 
     print("current Folder: " + current_directory2)

     if os.path.exists(destination_folder):
      til.rmtree(destination_folder)
      moving_data = til.copytree(current_directory2, destination_folder)
      print(moving_data + " backup-complete")
      tm.sleep(2)
      exit("backup_complete")
    else:
       print("failed to move to target folder")
else:
    print("Cannot find target folder:" + Target_folder )


