# OS-Module_MiniProject
The OS module in Python provides functions for interacting with the operating system. The OS module is one of Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.

**os.getcwd()**
This method returns the location of the current working directory (CWD). The CWD is the folder in which the python script is operating.

**os.path.exists()**
This method returns True for existing paths. It returns False for broken symbolic links.

**os.chdir()**
It is used for changing the CWD. It changes CWD to the specified path.

**os.mkdir()**
This method creates a new directory according to the specified path. In case the specified directory already exists a FileExistsError is raised.

**os.makedirs()**
This method creates a directory recursively. It means that while creating a leaf directory if any of the intermediate level directories specified in the path is missing then the method creates them all.

**os.listdir()**
This method returns a list of all the files and folders present inside the specified directory. If no directory is specified then the list of files and folders inside the CWD is returned.

**os.rename()**
This method renames a source file or directory to a specified destination file or directory.

**os.rmdir()**
This method is used for deleting an empty directory. If the path does not correspond to an empty directory then OSError is raised.

**os.remove()**
This method deletes a file path. It cannot delete a directory. In case the specified path is that of a directory then the OSError is raised.
This method deletes a file path. It cannot delete a directory. In case the specified path is that of a directory then the OSError is raised.
