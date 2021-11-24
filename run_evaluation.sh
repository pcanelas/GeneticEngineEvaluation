#!/bin/bash
#version=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')

#if [ "$version" -lt "39" ]; then
#    echo "python >= 3.9 is required to run evaluations."
#    exit 1
#fi

python3.9 -m src.evaluation $*
