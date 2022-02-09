from __future__ import print_function
import os
import sys
import time
'''
Author: For-Chan

'''



class FileProcessor:
    def __init__(self):
        if os.path.isfile(absPath):
            if os.access(absPath, os.R_OK):
                self.filePath         = absPath
                stats                 = os.stat(self.filePath)
                self.fileSize         = stats.st_size
                self.modifiedTime     = time.ctime(stats.st_mtime)
                self.createTime       = time.ctime(stats.st_ctime)
                self.accessTime       = time.ctime(stats.st_atime)
    def GetFileHeader(self, absPath):
        with open(absPath, "rb") as f:
            byte = f.read(20) # read the first 20 bytes?
            print('\n\n First 20 bytes:', byte)
            
    def PrintFileDetails(self):
        print("Path:               ", self.filePath)
        print("File Size:          ", '{:,}'.format(self.fileSize), "Bytes")
        print("File Created Time:  ", self.createTime)
        print("File Modified Time: ", self.modifiedTime)
        print("File Last Accessed: ", self.accessTime)
        
        
if __name__ == '__main__':
    #Constant directory path
    TARGET = input("Input a directory or file path")    
    
    if os.path.isdir(TARGET):
        print("Directory found")
        print("Parsing Directory")
        for root, dirs, fileList in os.walk(TARGET):
            try:
                for nextFile in fileList:
                    # Join root with the nextFile in fileList
                    path = os.path.join(root, nextFile)
                    # absPath 'absolutizes' the TARGET directory path
                    # Going to be used to for GetFileMetaData function and file hashValue
                    absPath = os.path.abspath(path)
                    
                    print(nextFile)
                    obj = FileProcessor()
                    obj.GetFileHeader(absPath)
                    obj.PrintFileDetails()

            except Exception as err:
                print(err)
    else:
        print("Wut")
        