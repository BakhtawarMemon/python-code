#!/bin/bash
climb(){
	test=""
	if [ $# -gt 0 ]
	then
		declare -i counter;counter=0
		while [ $counter -lt $1 ]; do
			test+="../"
			((counter++))
		done
		cd $test>&0
	else
		cd ..>&0
	fi
}
