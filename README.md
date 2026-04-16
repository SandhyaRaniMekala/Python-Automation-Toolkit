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

## 🔍 Project 2: Secret Message Finder
**Problem:** Thousands of log files exist in servers, and searching for a specific "ERROR" code manually is impossible.

**Solution:** I built a script that scans all ".txt" files in a folder, reads their internal data, and finds specific keywords in seconds.

**Key Skills:**
* File Reading ("with open")
* String Matching
* Looping through directories

### How it works:
1. Put the "finder.py" script in a folder with text files.
2. Run "python3 finder.py".

---

## 🔔 Project 3: Native macOS Health Notifier

**Problem:** Constant coding or screen time leads to forgetting basic health needs like hydration. Third-party notification libraries can be bulky or fail on newer macOS versions.

**Solution:** I developed a lightweight automation script that bypasses heavy libraries and uses **Native macOS AppleScript** via Python's `os` module. It triggers a system-level pop-up alert to remind the user to stay hydrated.

**Key Skills:**
* **Native OS Scripting:** Using AppleScript (`osascript`) within Python.
* **The `os` Module:** Executing system-level commands directly from a script.
* **Lightweight Automation:** Building tools that don't require external dependencies.

### How it works:
1. The script uses the `os` module to talk to the MacBook's operating system.
2. It sends a command to `osascript` (Apple’s internal language).
3. A native macOS notification appears on the top-right corner of the screen.

---
