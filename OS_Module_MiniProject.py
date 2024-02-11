import os

while True:
    print("\n1: Check The Current Directory Path \n2: Check Whether Directory Exists Or Not \n3: Change The Working Directory  \n4: Create A Directory \n5: Print Content Of The Directory \n6: Rename The Directory \n7: Remove The Directory \n8: Remove The File\n9: Read The Specific File \n10: Exit")
    opt = int(input("> "))
    if opt == 1: #To check the Current Directory path
        print(f"Current Directory Path: {os.getcwd()}")
    elif opt == 2: #To check whether specified Directory exists or not
        path = input("Enter the Path to check whether Directory exists or not: ")
        isExisting = os.path.exists(path)
        if isExisting == True:
            print(f"{path} path exists..")
        else:
            print(f"{path} path doesn't exist...")
    elif opt == 3: #To change the Current Directory
        path = input("Enter the Path to change Working Directory:")
        os.chdir(f'{path}')
        print(f"Current working Directory: {os.getcwd()}")
    elif opt == 4: #To create a Directory
        folder = input("Enter the Directory Name: ")
        os.makedirs(folder)
        print(f"{folder} Directory created successfully !!")
    elif opt == 5: #To list the content of the Directory
        path = input("Enter the Directory Path: ")
        dir_list = os.listdir(path) 
        print(f"Files and directories in {path} : ")  
        print(dir_list)
    elif opt == 6: #To rename the directory
        oldname = input("Enter the File Name with the path: ")
        newname = input("Enter the New Name for the pervious File: ")
        os.rename(oldname, newname)
        print(f"{oldname} directory renamed to {newname} successfully !!")
    elif opt == 7: #To remove the directory 
        folder = input("Enter the Directory Name: ")
        os.rmdir(folder)
        print(f"Directory {folder} has been removed successfully")
    elif opt == 8: #To remove the file 
        file = input("Enter the File Name: ")
        os.remove(file)
        print(f"{file} file has been removed successfully")
    elif opt == 9: #To read the specified file content 
        filepath = input("Enter the File Path: ")
        file = open(filepath,"r")
        content = file.read()
        print("File Content: \n",content)
    elif opt == 10: #To terminate the program
        break
    else:
        print("Enter Appropriate Option !!!")
