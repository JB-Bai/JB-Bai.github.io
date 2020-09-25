#! /bin/bash
### PART1
unrar e sky\ hdr.rar ./norotate/laval_outdoor_hdr/

### PART2
cd ./norotate/laval_outdoor_hdr
Folder="."
ls $Folder

for file in $Folder/*.zip;
do
    filename=`basename $file .zip`
    unzip $file
    rm $file
done  
echo 'unzip done'

### PART3
for file in $Folder/*;
do
    firstname=`basename $file`
    for subfile in $file/*;
    do
        secondname=`basename $subfile`
        for exrfile in $subfile/*.exr;
        do
            mv $exrfile $Folder"/"$firstname$secondname".exr"   
        done
    done
    rm -r $file
done
