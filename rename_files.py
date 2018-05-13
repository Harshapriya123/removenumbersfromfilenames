import os
def rename_files():
#getting filenames in the needed(prank)folder
#go to the directory
#Click Get Location
    file_list=os.listdir(r"/home/harsha/Downloads/prank/prank")
    print(file_list)	
    saved_path=os.getcwd()
    # displays only directory till (home/harsha/Downloads)
    print("Current working directory"+saved_path)	
    #The correct directory has to be saved
    os.chdir(r"/home/harsha/Downloads/prank/prank")
#to remove the numbers from files 
#file_name="48athens.jpg"#print (file_name) o/p 48athens.jpg
#file_name.translate(none,"0123456789") o/p athens.jpg
#for file_name in file_list:
#os.rename(file_name,file_name.translate(None,"0123456789")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))	
    os.chdir(saved_path)
rename_files()
