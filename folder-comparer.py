import hashlib
import os
import time

def checkfile(filename):
    return hashlib.md5(open(filename,'rb').read()).hexdigest()

directory1 = input("Enter name of directory 1: ")
directory2 = input("Enter name of directory 2: ")

hashes1 = {}
for subdir, dirs, files in os.walk(directory1):
    for file in files:
        filepath = subdir + os.sep + file
        hashes1[filepath[len(directory1):]] = checkfile(filepath)

hashes2 = {}
for subdir, dirs, files in os.walk(directory2):
    for file in files:
        filepath = subdir + os.sep + file
        hashes2[filepath[len(directory2):]] = checkfile(filepath)
        
completedfiles = []
with open("output.txt", "a") as file:
    file.write("\n=== folder-comparer.py === "+str(time.time()))
    file.write(f"\n{directory1} | {directory2}")
    for h in hashes1:
        if not h in completedfiles:
            if h in hashes2:
                if hashes1[h] == hashes2[h]:
                    state = "[SAME] "
                else:
                    state = "[DIFF] "
                
                file.write("\n"+state+h)
                file.write("\n\t"+hashes1[h] + " <==> " + hashes2[h])
            else:
                state = "[IN 1] "
                file.write("\n"+state+h)
                file.write("\n\t"+hashes1[h])
            completedfiles.append(h)
    for h in hashes2:
        if not h in completedfiles:
            file.write("\n"+"[IN 2] "+h)
            file.write("\n\t"+hashes2[h])
            completedfiles.append(h)
