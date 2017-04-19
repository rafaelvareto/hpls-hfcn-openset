#!/bin/bash

#DF
echo '../main_openset: DF, Variable hashing, 50% Known size'
python ../main_openset.py -p ../datasets/vggface/files/ -f vgg_set.txt -d hog -r 5 -m 100 -ks 0.5
python ../main_openset.py -p ../datasets/vggface/files/ -f vgg_set.txt -d hog -r 5 -m 300 -ks 0.5
python ../main_openset.py -p ../datasets/vggface/files/ -f vgg_set.txt -d hog -r 5 -m 500 -ks 0.5
