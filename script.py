import os
import shutil
import sys
import io
import datetime
if(__name__== "__main__"):
    if(len(sys.argv)<2):
        raise("error");
    folderName=sys.argv[1]
    if(folderName in os.listdir()):
        shutil.rmtree(folderName)
    os.mkdir(sys.argv[1])
    
    for i in range(0,11):
        with open(f'{folderName}/{i}','w') as file:
            file.write(str(datetime.date.today()))
