# <div align="center">RElog</div>
A small but super fast way to search log files using regex.

RElog lets you open a log file, view its contents, search it using regular expressions, and save the matching results to a separate file.

It's particularly useful for large logs where manually searching through hundreds of thousands of lines would be annoying.
## Features
* Open and inspect log files
* Search logs using regular expressions
* Live filtering while editing the file path or regex
* Displays the original log with line numbers
* Displays matching regex results with line numbers
* Save filtered results to a `.log` file
* Handles invalid regular expressions
* Handles unreadable or missing files
* Designed to work with large log files
* Simple dark-themed PyQt5 interface
* Uses Python's built-in `re` and `os` modules
## Requirements
* Python 3.x
* PyQt5

Install PyQt5 with:
```bash
pip install PyQt5
```
## Usage
Run:
```bash
python RElog.py
```
Enter the path to a log file and a regular expression.

For example:
```text
Log File Path:
C:\Minecraft\server\logs\latest.log

Regex Pattern:
ERROR|WARN
```
RElog will display the original log on the left and matching results on the right.
## Example Regex Patterns(Depends on the format of the log file)
Find errors:
```regex
ERROR
```
Find warnings or errors:
```regex
ERROR|WARN
```
Find server commands:
```regex
issued server command: .*
```
Find timestamps:
```regex
\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]
```
Find URLs:
```regex
https?://\S+
```
## Saving Results
Click:

**Save Filtered Output…**
RElog saves the currently filtered results beside the original file using a `_REGEX.log` suffix.

For example:
```text
latest.log
```
becomes:

```text
latest_REGEX.log
```
## Performance
RElog is designed to handle large log files.

A large log containing hundreds of thousands of lines can still be processed quickly, although displaying extremely large files in a GUI can take significantly longer than the regex search itself.

For very large files, the Qt text widgets may become the primary performance bottleneck.
## Downloads
Only the Python script is available.

— All Rights Reserved [RequestTimeout](https://github.com/RequestTimeout)

[LICENSE](LICENSE.md)
