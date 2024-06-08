# Invoice to PDF Converter 🧾➡️📄

Welcome to the Invoice to PDF Converter project! This Python script reads Excel files containing invoice data and generates neatly formatted PDF invoices. 🚀

## Features ✨

- **Automated PDF Generation**: Converts Excel invoices to PDF format with a simple script.
- **Organized Output**: Saves PDFs in a designated folder (`PDFS`).
- **Customizable Layout**: Adjusts the column widths and formatting for a clean look.

## Prerequisites 📋

Before you begin, ensure you have the following installed:

- Python 3.6+
- pandas
- fpdf
- pathlib
- glob
- openpyxl

You can install the necessary packages using pip:

```sh
pip install pandas fpdf openpyxl
How to Use 🚀
Prepare Your Excel Files: Place your invoice Excel files in the invoices directory. Ensure each file is named in the format invoice_nr-date.xlsx (e.g., 1234-2023-06-07.xlsx).

Run the Script: Execute the Python script to convert your invoices to PDF.

sh
Copy code
python convert_invoices.py
Check the Output: The generated PDF files will be saved in the PDFS directory.
```


## Contribution 🤝
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License 📜
This project is licensed under the MIT License.