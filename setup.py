#!/bin/bash
# To install, run this setup shell script
# NEW:
# > chmod +x setup.py
# > ./setup.py
# OLD:
# > ./main.py [ COMMAND ]

pip install -r requirements.txt
chmod +x main.py
python3 alias.py
