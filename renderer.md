### 环境配置
主要记录了在Ubuntu16.04中编译Mitsuba的经验。

1.值得注意的是[官网]downlaod的安装包，均为0.5版本，经实测，0.5版本的xml无法导入0.6版本的xml。部分Example scenes为0.4版本，可正常导入。  

2.需要0.6版本可编译源码生成。参考[编译方式]有若干需要注意的地方。  

2.0 依次执行如下指令。  
    `cd ~`  
    `git clone https://github.com/mitsuba-renderer/mitsuba`  
    `cd mitsuba`  
    `cp build/config-linux-gcc.py config.py`  
    `sudo apt-get install build-essential scons git libpng12-dev libjpeg-dev libilmbase-dev libxerces-c-dev libboost-all-dev libopenexr-dev libglewmx-dev libxxf86vm-dev libeigen3-dev libfftw3-dev`  
    `sudo apt-get install libcollada-dom-dev`  
    `sudo apt-get install qt5-default libqt5opengl5-dev libqt5xmlpatterns5-dev`  
    修改config.py文件中  
    `CXXFLAGS = ['-O3', '-Wall','-fPIC','-std=c++11','-g', '-pipe', '-march=nocona', '-msse2', '-ftree-vectorize', '-mfpmath=sse', '-funsafe-math-optimizations', '-fno-rounding-math', '-fno-signaling-nans', '-fno-math-errno', '-fomit-frame-pointer', '-DMTS_DEBUG', '-DSINGLE_PRECISION', '-DSPECTRUM_SAMPLES=3', '-DMTS_SSE', '-DMTS_HAS_COHERENT_RT', '-fopenmp', '-fvisibility=hidden', '-mtls-dialect=gnu2']`  
    开始编译`scons -j8`直到出现` scons:Done building targets.`  
    表示编译成功。  
    `source setpath.sh`

2.1 最好重新配置一个[ubuntu16.04LTS]环境，否则可能会产生自己之前环境的qt版本过高等问题，导致无法编译成功。  

2.2 虚拟机内存要尽可能大，经过实测2GB内存不足以编译。故笔者设置了8GB内存。  

2.3 如果出现类似“Package QtWidgets was not found in the pkg-config search path.”的报错，可参考[链接]:    
    `cd /usr/lib/x86_64-linux-gnu/pkgconfig`  
    `ls Qt*`   
    将所有类似Qt5的文件命名为Qt  
    `sudo ln -s ./Qt5Core.pc ./QtCore.pc`

2.4 编译成功后，`./dist/mtsgui` 即可打开GUI界面。  


### References：
https://medium.com/@sreenithyc21/10-steps-to-install-mitsuba-renderer-on-ubuntu-38a9318fbcdf  
https://fancyvin.github.io/2019/03/06/how-to-compile-mitsuba-renderer/  
https://github.com/mitsuba-renderer/mitsuba/issues/125  




### DataSet

#### [sftp登录及命令行用法]  

##### 打开终端，连接远程Linux  
`sftp user@host`  
`例如：sftp root@192.168.1.2`    
##### 上传文件  
`put local_path remote_path`
`例如：put -r /home/share/read.txt /home/root`
##### 上传文件夹以文件夹里的所有内容  
比如上传文件夹 folder，首先需要在远程机上创建这个文件夹，然后使用下面命令 put  
`put -r /home/share/folder/* /home/root/folder`
##### 下载文件
`get remote_path local_path`
`例如：get -r /usr/local/some.zip /home/share`
##### 下载文件夹以文件夹里的所有内容  
比如下载文件夹 folder，首先需要在本机上创建这个文件夹，然后使用下面命令 get
`get -r /usr/local/folder/* /home/share/folder`
##### 退出
`exit`

#### 好用的sftp客户端  
Termius  

#### dataset1
代码:[rotatepano_bai.py]   
文件放置于`/home/ypp/work/data_process/mitsuba/rotate/`  

值得注意的是：  
1.先cd到mitsuba目录，执行`source setpath.sh`  
2.遇到版本不兼容的问题，将xml中0.5改为0.6  

Update in Sep. 25. 提取对应txt做另存处理。  
文件放置于 `/home/ypp/SUN360/update_txt_for_SUN360HDR_norotate/`  

#### dataset2
执行`sh unzipDataset2.sh`  
代码:[unzipDataset2.sh]  
文件放置于`/home/ypp/lavel\ data/`

值得注意的是： 
1.可能需要修改第一行环境配置  


[官网]: https://www.mitsuba-renderer.org/download.html  
[编译方式]: https://medium.com/@sreenithyc21/10-steps-to-install-mitsuba-renderer-on-ubuntu-38a9318fbcdf
[ubuntu16.04LTS]: https://releases.ubuntu.com/xenial/  
[链接]: https://github.com/mitsuba-renderer/mitsuba/issues/125  
[sftp登录及命令行用法]: https://blog.csdn.net/qq_26954773/article/details/78199365
[rotatepano_bai.py]: https://jb-bai.github.io/docs/rotatepano_bai.py
[unzipDataset2.sh]: https://jb-bai.github.io/docs/unzipDataset2.sh