#!/bin/bash
#########################################################################
# File Name:    test_edge.sh
#########################################################################

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

# The snippets_path variable is related to the position of this script. This script should thus be in the snippets directory (which is the default).
snippets_path=$(cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P)
start_callgraph_generator "$snippets_path"
