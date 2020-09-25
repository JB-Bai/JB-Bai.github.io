import os
import time
import math
import numpy as np

def rotate(azimuth, src, dest):
    azimuth = math.radians(azimuth)
    y = 0
    x = -math.sin(azimuth)
    z = math.cos(azimuth)
    cmd = 'mitsuba -q -Dsrc="%s" -Dtarget="%f,%f,%f" -o %s rotatepano.xml' % (src, x, y, z, dest)
    os.system(cmd)

if __name__ == "__main__":
    root_dir = '/home/ypp/SUN360/SUN360HDR'
    root_txt_dir = '/home/illu/data/outdoor/trainset'
    des_dir = '/home/ypp/SUN360/SUN360HDR_norotate'
    
    os.system('mkdir /home/ypp/SUN360/update_txt_for_SUN360HDR_norotate/')
    update_txt_dir = '/home/ypp/SUN360/update_txt_for_SUN360HDR_norotate/'

    dirs = os.listdir(root_dir)
    txt_dirs = os.listdir(root_txt_dir)
    
    num = 0
    for files in dirs:
        cur_file = root_dir + '/' + files
        img_name=files[:20]
        for f_txt in txt_dirs:
            if f_txt[:20]==img_name and f_txt.endswith('_sunsky_param.txt'):
                f_txt_all=root_txt_dir+'/'+f_txt
                
                #update
                os.system('cp '+f_txt_all+' '+update_txt_dir)

                num+=1
                print(num)
                # with open(f_txt_all) as f:
                #     line = f.readline()
                #     azimuth = -1* float(line.split(',')[1])
                #     print (azimuth)
                #     #rotate(azimuth * 180 / math.pi, path, des_dir + '/' + folder + ffolder + '_rotate.exr')   # all saved as .exr
                #     print('found!')
                #     rotate(azimuth * 180 / math.pi, cur_file, des_dir + '/' + f_txt[:20] + '.exr') 

    
    