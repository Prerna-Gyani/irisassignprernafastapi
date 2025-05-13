# irisassignprernafastapi

# IRIS Excel Processor — Prerna Gyanchandani

This Streamlit web app allows users to upload and analyze Excel files interactively. The app was created as a solution to the IRIS Public Assignment using Streamlit Cloud instead of FastAPI, making it accessible directly through the browser without requiring a local environment.

## Features

- **Excel Sheet Reader**: Automatically detects `.xlsx` files placed in the `data/` folder.
- **Sheet Selector**: Lets users select from all available sheets (tables) in the uploaded Excel file.
- **Data Preview**: Displays the selected sheet in a readable table format.
- **Row Analyzer**: Allows users to select any row (first column label) and calculates the sum of numerical values across that row.

## Folder Structure

IRIS_Streamlit/
│
├── streamlit_app.py # Main Streamlit frontend code
├── utils.py # Helper functions for Excel processing
├── requirements.txt # Python dependencies
└── data/
└── capbudg.xlsx # Excel file used for analysis


## Setup Instructions

1. Fork or clone this repository.
2. Upload your `.xlsx` file into the `data/` folder.
3. Deploy the app on [Streamlit Cloud](https://streamlit.io/cloud) using:
   - `streamlit_app.py` as the entry point.
4. The app will automatically load available Excel files and sheets.

## Sample Use

- Select `capbudg.xlsx` from the file dropdown.
- Choose the desired sheet (e.g., `CapBudgWS`).
- The table will be displayed.
- Pick a row name such as `INITIAL INVESTMENT` from the dropdown.
- The sum of all numeric values in that row will be shown.

## Notes

- This version supports `.xlsx` files only. If you have a `.xls` file, convert it using Excel or an online tool.
- Only numeric values are considered for summing; any text, symbols, or percentages are skipped.

## Improvements to Consider

- Support for `.xls` and `.csv` formats.
- Better row-label recognition even when the first column header is missing.
- Export options for filtered results.
- Add row/column-level charts or plots for better visualization.

## Streamlit Cloud Implementation 

https://irisassignprernafastapi.streamlit.app/

## Author

**Prerna Gyanchandani**

Submission for the IRIS Public Assignment — May 2025
