#!/bin/bash
#########################################################################
# File Name: test.sh
# Author: Zhenbin Chan
# mail: Zhenbin_Chan@163.com
# Created Time: 六  9/18 10:50:24 2021
#########################################################################
# shellcheck disable=SC1068

start_pycg () {
  entry="/Users/yixuanyan/yyx/github/supplychain/YanYiXuan/pythonCG/main.py"
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
				# Normal PyCG usage (uncomment the following line 2 lines)
				# curDir_pycg="${file%/*}/pycg.json"
				# pycg "$file" --package "${file%/*}" -o "$curDir_pycg"

				# Normal pythoncg/Jarvis usage (uncomment the following line 2 lines)
				# curDir_pythonCG="${file%/*}/oldCG.json"
				# python3 "$entry" "$file" --package "${file%/*}" -o "$curDir_pythonCG"

				# Timing PyCG and pythoncg/Jarvis in a log file
				/usr/bin/time -lp pycg "$file" --package "${file%/*}" > "${file%/*}/pycg.log" 2>&1
				/usr/bin/time -lp python3 "$entry" "$file" --package "${file%/*}" > "${file%/*}/pythoncg.log" 2>&1
			fi
		fi
	done
}

path="/Users/yixuanyan/yyx/github/supplychain/YanYiXuan/pythonCG/micro-benchmark/snippets"
start_pycg "$path"

#path="/Users/yixuanyan/yyx/github/supplychain/YanYiXuan/pythonCG/micro-benchmark/snippets/generators/"
#start_pycg "$path"
