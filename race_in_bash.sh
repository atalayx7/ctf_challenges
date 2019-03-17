#!/bin/bash

while [ 1 ]
do
	rm -r the_file
	touch the_file
	rm the_file
	ln -s flag.txt the_file
done