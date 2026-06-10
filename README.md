# Log File Analysis using Python

## Overview

This project analyzes application log files and generates a summary report. It demonstrates fundamental Python concepts such as file handling, string processing, conditional logic, and data analysis.

The application reads a log file, identifies different log levels, counts warning and error messages, finds the latest error, and produces a summary report.

## Features

* Read and process application log files
* Count ERROR messages
* Count WARNING messages
* Identify the latest ERROR entry
* Generate a log summary report
* Simple and easy-to-understand Python implementation

## Sample Log File

Example (`application.log`):

```text
2026-06-07 09:00:01 INFO Application Started
2026-06-07 09:01:15 INFO Database Connected
2026-06-07 09:02:30 WARNING Employee ID not found
2026-06-07 09:03:45 ERROR Failed to insert employee
2026-06-07 09:05:20 WARNING Invalid salary entered
2026-06-07 09:06:35 ERROR Database Connection Lost
2026-06-07 09:07:00 INFO Application Closed
```

## Technologies Used

* Python 3.x
* File Handling
* Exception Handling
* String Processing

## Project Structure

```text
Log_File_Analysis/
│
├── application.log
├── log_analysis.py
├── summary_report.txt
└── README.md
```

## Sample Output

```text
===== Log Summary Report =====

WARNING Messages : 2
ERROR Messages   : 2

Latest Error:
2026-06-07 09:06:35 ERROR Database Connection Lost
```

## Learning Objectives

This project helps practice:

* Reading data from text files
* Parsing log records
* Working with loops and conditions
* Counting occurrences
* Generating reports
* Basic data analysis techniques

## Future Enhancements

* Export summary report to a text file
* Generate CSV reports
* Visualize log statistics using charts
* Analyze large log files efficiently
* Add support for multiple log formats

## Author

Mariya Preena

Python Practice Project – Log File Analysis

