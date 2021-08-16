import os


for folder, subFolders, fileNames in os.walk('../..'):
    for fileName in fileNames:
        sizeOfFile = os.path.getsize(os.path.join(folder, fileName)) / 1000000
        if sizeOfFile > 5:
            print(f'Size of {fileName} is {sizeOfFile:.2f} MB')

