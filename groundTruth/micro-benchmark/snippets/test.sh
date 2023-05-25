#!/bin/bash
#########################################################################
# File Name: test.sh
# Author: Zhenbin Chan
# mail: Zhenbin_Chan@163.com
# Created Time: 六  9/18 10:50:24 2021
#########################################################################
# shellcheck disable=SC1068

start_callgraph_generator () {
  entry=$(cd "$snippets_path" ; cd "../../../Jarvis" ; pwd -P)"/main.py"

	for element in $(ls "$1")
	do
		file=$1"/"$element
		if [ -d "$file" ]
		then
			start_callgraph_generator "$file"
		elif [ "${file##*.}" = "py" ]
		then
			if [ "${file##*/}" = "main.py" ]
			then
				# Normal PyCG usage (uncomment the following line 2 lines)
				# curDir_pycg="${file%/*}/pycg.json"
				# pycg "$file" --package "${file%/*}" -o "$curDir_pycg"

				# Normal pythoncg/Jarvis usage (uncomment the following line 2 lines)
				# curDir_pythonCG="${file%/*}/pythonCG.json"
				# python3 "$entry" "$file" --package "${file%/*}" -o "$curDir_pythonCG"

				# Timing PyCG and pythoncg/Jarvis in a log file
				/usr/bin/time -lp pycg "$file" --package "${file%/*}" > "${file%/*}/pycg.log" 2>&1
				/usr/bin/time -lp python3 "$entry" "$file" --package "${file%/*}" > "${file%/*}/pythoncg.log" 2>&1
			fi
		fi
	done
}

# The snippets_path variable is related to the position of this script. This script should thus be in the snippets directory (which is the default).
snippets_path=$(cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P)
start_callgraph_generator "$snippets_path"
