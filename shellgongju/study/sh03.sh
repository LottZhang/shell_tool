#!/bin/bash
#program creates three files,which named by user's input and date commond.
#fukebane_20090212,13,14
echo -e "I will use 'touch' command to create 3 files."
read -p "Please input filename:" fileuser
filename=${fileuser:-"filename"}
date1=
