#!/bin/bash

# Create the temp folder as a mountpoint and a tmpfs disk to keep the
# downloaded LastPass CSV file in
mkdir lpdl
sudo mount -t tmpfs -o size=10m tmpfs lpdl

# prompt to download the lp csv file
echo Log on to lastpass.com (website) and download the vault to export.csv in the lpdl directory.
read -p "Press ENTER to continue" x

# Run the checker ...
echo Checkiing ...
./lppwcheck.py | tee lppwcheck.log

echo Review lppwcheck.log for details

# Tidy up ... 
shred -u lpdl/export.csv
sudo umount lpdl
rm -r lpdl

