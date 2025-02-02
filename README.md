# Preprocessing for master's thesis
All code credit goes to: https://github.com/mohak1/Detection-and-Classification-of-Distributed-DoS-Attacks-using-Machine-Learning

# How to run. 
Install the dependencies
python3 data_extract.py <LABEL> <chunksize> <label_value>


The label_value is an integer value of what you want for the LABEL. We use 0 for BENIGN and 1 for UDP.

Example:
python3 data_extract.py BENIGN 100000 0
Or
python3 data_extract.py UDP 100000 1