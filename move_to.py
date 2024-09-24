import shutil
import os

def remove_file(old_path, new_path):
    print(old_path)
    print(new_path)
    filelist = os.listdir(old_path)
    print(filelist)
    for file in filelist:
        scr = os.path.join(old_path, file)
        dst = os.path.join(new_path, file)
        print('scr:', scr)
        print('dst:', dst)
        shutil.move(scr, dst)

if __name__ == '__main__':
    remove_file(r".\data\temp1",r".\data\temp2")
