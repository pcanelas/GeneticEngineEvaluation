#!/bin/bash
cd GeneticEngine 
git pull 
python3 -m pip install -r requirements.txt
cd ../PonyGE2 
git pull 
python3 -m pip install -r requirements.txt
cd ..
