Python Automation Toolkit
This repository contains real-world automation scripts built using Python to solve daily problems.

📁 Project 1: Desktop File Organizer
Problem: A cluttered desktop filled with screenshots and PDFs makes it hard to focus and find important work.

Solution: I built an automated script that scans the desktop, identifies file types, and sorts them into organized folders.

Key Skills: * Python File I/O

"os" and "shutil" modules
Loops and Conditionals
How it works:
The script lists all files on the Desktop.
It checks for extensions (like ".png" or ".pdf").
It creates folders (if they don't exist) and moves the files.

🔍 Project 2: Secret Message Finder
Problem: Thousands of log files exist in servers, and searching for a specific "ERROR" code manually is impossible.

Solution: I built a script that scans all ".txt" files in a folder, reads their internal data, and finds specific keywords in seconds.

Key Skills:

File Reading ("with open")
String Matching
Looping through directories
How it works:
Put the "finder.py" script in a folder with text files.
Run "python3 finder.py".

🔔 Project 3: Native macOS Health Notifier
Problem: Constant coding or screen time leads to forgetting basic health needs like hydration. Third-party notification libraries can be bulky or fail on newer macOS versions.

Solution: I developed a lightweight automation script that bypasses heavy libraries and uses Native macOS AppleScript via Python's os module. It triggers a system-level pop-up alert to remind the user to stay hydrated.

Key Skills:

Native OS Scripting: Using AppleScript (osascript) within Python.
The os Module: Executing system-level commands directly from a script.
Lightweight Automation: Building tools that don't require external dependencies.
How it works:
The script uses the os module to talk to the MacBook's operating system.
It sends a command to osascript (Apple’s internal language).
A native macOS notification appears on the top-right corner of the screen.

📸 Project 4: Bulk File Renamer
Problem: Managing hundreds of files with random system-generated names (e.g., IMG_9084.JPG, fd1327...JPG) makes it impossible to stay organized. Manual renaming is incredibly slow, repetitive, and prone to numbering errors.

Solution: I developed a Python automation script that scans a specific directory and instantly renames all files into a standardized, sequential format (e.g., Kerala_Trip_Photo_1.jpg). The script is designed to intelligently preserve the original file extension while updating the name.

Key Skills:

enumerate() Function: Implementing a loop to track both the filename and its sequential index simultaneously for perfect numbering.

OS Module Mastery: Utilizing os.listdir to fetch file lists and os.rename for executing system-level file changes.

Dynamic String Formatting: Using Python f-strings to generate customized and clean filenames based on the project theme.

How it works:
The script points to the target folder using an absolute system path.

It iterates through every file and identifies its specific extension (e.g., .jpg, .pdf, .png) using os.path.splitext.

It generates a new filename by combining a custom "Prefix" and an incremental "Index."

It performs a batch rename operation, organizing the entire folder in seconds with zero manual effort.