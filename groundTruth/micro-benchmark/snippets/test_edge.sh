#!/bin/bash
#########################################################################
# File Name:    test_edge.sh
#########################################################################

start_pycg () {
  entry="/Users/yixuanyan/yyx/github/supplychain/callGraph/pythonCG/micro-benchmark/snippets/getEdge.py"
	for element in $(ls "$1")
	do
		file=$1"/"$element
		if [ -d "$file" ]
		then
			start_pycg "$file"
		elif [ "${file##*.}"x = "py"x ]
		then
			if [ "${file##*/}"x = 'main.py'x ]
			then
			  curDir_pycg="${file%/*}/test_pycg.json"
				curDir_pythonCG="${file%/*}/test_pythonCG.json"
				curDir_output="${file%/*}/output.txt"
        echo
        if  [ ! -f "$curDir_output"  ]; then
				  rm -rf "$curDir_output"
				fi
        python3 "$entry" "$curDir_pythonCG" "$curDir_pycg" "$curDir_output"
			fi
		fi
	done
}

path="/Users/yixuanyan/yyx/github/supplychain/callGraph/pythonCG/micro-benchmark/snippets"
start_pycg $path
