# Directory-Comparison-and-Synchronization-Tool
This Python script compares two directories (A and B) and performs synchronization based on file differences. It uses the os, sys, shutil, filecmp, and logging modules.

## Features
- Directory Comparison:
  - Identifies files unique to directory A and directory B.
  - Lists common files and files with differing sizes or contents.
  - 
- File Comparison:
  - Compares files in both directories for size and content differences.
  - Logs and displays differences in size and identical content.

- Directory Synchronization:
  - Optionally synchronizes directories A and B:
    - Copies files unique to A into B, or vice versa.
    - Provides flexibility to synchronize both directories.
    
## Usage
1. **Setup:**
    - Ensure Python is installed on your system.

2. **Running the Script:**
    - Execute the script in a Python environment.
    - Follow the prompts to enter absolute paths for directories A and B.

3. **Comparison Results:**
    - The script logs results in Comparison.log.
    - Outputs details on files unique to each directory, common files, and file comparisons.

4. **Synchronization:**
    - Choose to synchronize directories A, B, or both based on your needs.

## Requirements
- Python 3.x
- Standard libraries: os, sys, shutil, filecmp, logging

## Example
    # Run the script
    python directory_comparison.py

## Output
    Enter the path of directory A (Absolute Path): /path/to/directory/A
    Enter the path of directory B (Absolute Path): /path/to/directory/B
    
    Files only in directory A:
    file1.txt (1024 bytes)
    file3.txt (2048 bytes)
    
    Files only in directory B:
    file2.txt (1536 bytes)
    
    Funny files:
    
    Common files:
    file4.txt (4096 bytes)
    file5.txt (8192 bytes)
    
    Size differs for file file4.txt: 4096 bytes in /path/to/directory/A and 6144 bytes in /path/to/directory/B
    Files /path/to/directory/A/file5.txt and /path/to/directory/B/file5.txt have the same content.
    
    Do you want to synchronize the directories (Y/N): y
    Which directory do you want to synchronize (A or B or Both): both
    Copied /path/to/directory/A/file1.txt to /path/to/directory/B
    Copied /path/to/directory/A/file3.txt to /path/to/directory/B
    Copied /path/to/directory/B/file2.txt to /path/to/directory/A
