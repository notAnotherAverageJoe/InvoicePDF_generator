import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


# filepaths=glob.glob("invoices/*.xlsx")
# print(filepaths)


# for filepath in filepaths:
#     df =pd.read_excel(filepath, sheet_name="Sheet 1")
#     print(df)
#     pdf = FPDF(orientation="P", unit="mm", format="A4")
#     pdf.add_page()
    
#     filename= Path(filepath).stem
#     invoice_nr, date = filename.split("-")
    
#     pdf.set_font(family="Times", size=16, style="B")
#     pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
    
#     pdf.set_font(family="Times", size=16, style="B")
#     pdf.cell(w=50, h=8, txt=f"Date: {date}")
    
#     df =pd.read_excel(filepath, sheet_name="Sheet 1")
#     for index, row in df.iterrows():
#         pdf.set_font(family="Times", size=10)
#         pdf.set_text_color(80,80,80)
#         pdf.cell(w=30, h=8, txt=row["product_id"])
#         pdf.cell(w=70, h=8, txt=row["product_name"])
#         pdf.cell(w=30, h=8, txt=row["amount_purchased"])
#         pdf.cell(w=70, h=8, txt=row["price_per_unit"])
#         pdf.cell(w=70, h=8, txt=row["total_price"])
        
    
    
#     pdf.output(f"PDFS/{filename}.pdf")
#     print("The files have been saved")   

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os

# Ensure the PDFS directory exists
os.makedirs("PDFS", exist_ok=True)

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
    
    # Adding column headers with appropriate widths
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt="Product ID", border=1)
    pdf.cell(w=50, h=8, txt="Product Name", border=1)
    pdf.cell(w=50, h=8, txt="Amount Purchased", border=1)
    pdf.cell(w=30, h=8, txt="Price per Unit", border=1)
    pdf.cell(w=30, h=8, txt="Total Price", border=1, ln=1)
    
    # Iterating over rows and adding data to the PDF with adjusted widths
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        
        # Convert all values to strings before writing to the PDF
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    
    pdf.output(f"PDFS/{filename}.pdf")
    print(f"The file {filename}.pdf has been saved")
