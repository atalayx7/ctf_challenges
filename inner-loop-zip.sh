#!/bin/bash

filename=$1

rm -r tmp
mkdir tmp
cp $filename tmp

cd tmp
while [ 1 ]
do
	file $filename
	file $filename | grep "bzip2"
	if [ "$?" -eq "0" ]
	then
		echo "This is a Bzip"
		mv $filename $filename.bz2
		bunzip2 $filename.bz2
		filename=$(ls *)
	fi
	
	file $filename | grep "Zip"
	if [ "$?" -eq "0" ]
	then
		echo "This is a Zip"
		mv $filename $filename.zip
		unzip $filename.zip
		rm $filename.zip
		filename=$(ls *)
	fi

	file $filename | grep "ASCII"
	if [ "$?" -eq "0" ]
	then
		echo "This is a Ascii"
		tail -c 100 $filename
		base64 -d $filename > $filename.txt
		rm $filename
		filename=$(ls *)
	fi

	file $filename | grep "init="
	if [ "$?" -eq "0" ]
	then
		echo "This is a Ascii"
		base64 -d $filename > $filename.txt
		rm $filename
		filename=$(ls *)
	fi

	file $filename | grep "gzip"
	if [ "$?" -eq "0" ]
	then
		echo "This is a Gzip"
		mv $filename $filename.gz
		gunzip $filename.gz
		filename=$(ls *)
	fi

	file $filename | grep "empty"
	if [ "$?" -eq "0" ]
	then
		break
	fi
done