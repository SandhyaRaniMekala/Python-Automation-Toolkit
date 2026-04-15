# Python Automation Toolkit

This repository contains real-world automation scripts built using Python to solve daily problems.

---

## 📁 Project 1: Desktop File Organizer
**Problem:** A cluttered desktop filled with screenshots and PDFs makes it hard to focus and find important work.
**Solution:** I built an automated script that scans the desktop, identifies file types, and sorts them into organized folders.
**Key Skills:** * Python File I/O
* "os" and "shutil" modules
* Loops and Conditionals

### How it works:
1. The script lists all files on the Desktop.
2. It checks for extensions (like ".png" or ".pdf").
3. It creates folders (if they don't exist) and moves the files.

---


---

## 🔍 Project 2: Secret Message Finder
**Problem:** Thousands of log files exist in servers, and searching for a specific "ERROR" code manually is impossible.
**Solution:** I built a script that scans all ".txt" files in a folder, reads their internal data, and finds specific keywords in seconds.
**Key Skills:**
* File Reading ("with open")
* String Matching
* Looping through directories

### How to use:
1. Put the "finder.py" script in a folder with text files.
2. Run "python3 finder.py".
