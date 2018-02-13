import os
import time
import platform

def main(AskForPath = False, Intervtime = 5):
    if AskForPath:
        print("Enter the path: ")
        print("If the program is already in the requested directory, press 'Enter' directly. (Use / to replace \\):",end = ' ')
        path = input("")
        if path != "":
            os.chdir(path)   # change the path
    else:
        if 'windows' in platform.platform().lower():  
            path = os.getcwd()  
        else:
            path = os.getcwdu()  
    allfile = os.listdir(path)
    print('Current Files:', allfile)
    while 1:
        newfile = os.listdir(path)
        if allfile != newfile:
            print("Changes Found")
            print('Current Files:', newfile)
            time.sleep(Intervtime)
            allfile = newfile          

            
if __name__ == '__main__':
    main()
        