#!/bin/bash

parallel -j 8 python3 data_extract.py < params.txt