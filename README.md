# Technical Documentation: Converting CSV to iCalendar (.ics) for HikVision Data

## Description

This script is designed to convert data from a CSV file exported from HikVision equipment into the iCalendar (.ics) format, allowing you to import events into calendar applications, including Google Calendar.

## Important Note

**This script variant is intended specifically for data exported from HikVision equipment.** Data from other sources may have different structures and fields, necessitating appropriate modifications to the script.

## Dependency Installation

Before using the script, make sure you have Python installed and the `ics` library. If the library is not installed, run the following command:

```bash
pip install ics
```

## Usage

1. Export a CSV file with data from HikVision equipment. Ensure that the file contains the following columns: "Person ID," "Name," "Department," "Time," "Attendance Status," "Custom Name," and any other required columns.

2. Download the `csv_to_ics_hikvision.py` script (the name can be changed according to your preference) or create a new file and copy the script code into it.

3. Replace the values of the `input_csv_file` and `output_ics_file` variables in the script with the paths to your CSV file and the desired output .ics file name.

4. Open a command prompt (terminal) and navigate to the directory where the script and CSV file are located.

5. Run the following command:

```bash
python csv_to_ics_hikvision.py
```

After the script runs, a .ics file will be created in the same directory, containing events created based on the data from the CSV file.

6. Import the .ics file into your calendar application, such as Google Calendar. This might require signing in to your account and importing through the calendar settings.

## Note

- Ensure that the CSV file uses an appropriate encoding. If there are encoding issues, verify that you have correctly specified the CSV file reading encoding in the script.

- Before applying the script to real data, it is recommended to perform a test import with a small amount of data to ensure that the process works correctly.

## Conclusion

This script provides a convenient way to convert data from a CSV file exported from HikVision equipment into the iCalendar (.ics) format, which can be imported into various calendar applications. Follow the instructions above for successful script usage with HikVision data.
