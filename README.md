# A simple folder comparer

How it works:
1. You run the script and provide the two directories
2. Hashes are gotten for each file in the two folders
3. The script compares the files and hashes in the folders
4. All information is output in output.txt

This script won't tell you exact differences between folders but is handy for quickly checking for modified files.

### How to run

You will need at least Python 3 installed. Run it from the command line with `python3 folder-comparer.py`

When providing folder names, a forward slash at the start will most likely crash the program.
