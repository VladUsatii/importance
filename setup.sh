#!/bin/bash

pip install -r requirements.txt
chmod +x main.py
echo "alias cls='python3 main.py'" >> ~/.bash_profile
