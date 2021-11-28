#!/bin/bash

pip install -r requirements.txt

chmod +x main.py

echo "alias cls='python3 main.py'" >> ~/.bash_profile
echo "cls-red () { fname=\${1}; echo \${fname} >> important.txt; }" >> ~/.bash_profile
echo "cls-green () { fnametwo=\${1}; echo \${fnametwo} >> active.txt; }" >> ~/.bash_profile
