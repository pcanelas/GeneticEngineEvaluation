#!/bin/bash
git clone git@github.com:alcides/GeneticEngine.git
git clone git@github.com:alcides/PonyGE2.git
cd GeneticEngine 
python3 -m pip install -r requirements.txt
cd ../PonyGE2
python3 -m pip install -r requirements.txt
cd ..
