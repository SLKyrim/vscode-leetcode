# -*- coding: utf-8 -*-

# Batch rename all files in the current directory of the script
# Rename rule: 1. The prefix number is fixed to X digits,
#              2. The prefix number less than X digits is prefixed with zero(es)
# Author: SingleLong 2021.2.23

import os

X = 4  # Expected digit of prefix number

for root, dirs, files in os.walk("./"):
    for file in files:
        tmp = file.split(".")
        if tmp[0].isnumeric() and len(tmp[0]) < X:
            rename = "0" * (X - len(tmp[0])) + file  # Add prefixed zero(es) to needed file
            os.renames(file, rename)  # Rename the file with new name "rename"
        if tmp[0].isnumeric() and len(tmp[0]) > X:
            index = len(tmp[0]) - X  # The number of zero(es) to abandon
            os.renames(file, file[index:])

