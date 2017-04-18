#!/bin/bash

reset

sudo rm -R sampleImageDirectory/
sudo rm negativeImageDirectory/negatives.txt
sudo rm *.txt
sudo rm *.vec
sudo rm outputDirectory/stage*.xml


reset

#mogrify -format jpg *.png
#mogrify -colorspace Gray file


#cd negativeImageDirectory
#5602
ls negativeImageDirectory/upper/*.jpg > negatives_top.txt

#2811
ls negativeImageDirectory/lower/*.jpg > negatives_bot.txt


#8413
cat negatives_bot.txt negatives_top.txt > negatives.txt


#368
#61
for i in ball/*
 do
  reset
  a=${i##*/}
  opencv_createsamples -img "$i" -bg negatives_bot.txt -info sampleImageDirectory/bot/"$a".txt -num 128 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.8 -bgcolor 0 -bgthresh 8 -w 24 -h 24
done
#7808



#433
#61
for i in ball/*
 do
  reset
  a=${i##*/}
  opencv_createsamples -img "$i" -bg negatives_top.txt -info sampleImageDirectory/top/"$a".txt -num 128 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.8 -bgcolor 0 -bgthresh 8 -w 24 -h 24
done
#7808



cat sampleImageDirectory/bot/*.txt > sampleImageDirectory/positives_bot.txt
cat sampleImageDirectory/top/*.txt > sampleImageDirectory/positives_top.txt

sed -i -e 's/^/bot\//' sampleImageDirectory/positives_bot.txt
sed -i -e 's/^/top\//' sampleImageDirectory/positives_top.txt

cat sampleImageDirectory/positives_bot.txt sampleImageDirectory/positives_top.txt > sampleImageDirectory/positives.txt
#15616


#cd ..

reset

opencv_createsamples -info sampleImageDirectory/positives.txt -bg negatives.txt -vec cropped.vec -num 15616 -w 24 -h 24


opencv_traincascade -data outputDirectory -vec cropped.vec -bg negatives.txt -numPos 10000 -numNeg 8413 -numStages 6 -precalcValBufSize 6144 -precalcIdxBufSize 6144 -featureType LBP -minHitRate 0.995 -maxFalseAlarmRate 0.085 -w 24 -h 24 -numThreads 80



