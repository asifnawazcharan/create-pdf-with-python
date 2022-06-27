from fpdf import FPDF
import pandas as pd
import csv 

data = pd.read_csv("company_sales_data.csv")
print(type(data))

month = data["month_number"].tolist()
facecream = data["facecream"].tolist()
facewash = data["facewash"].tolist()
shampoo = data["shampoo"].tolist()

pdf = FPDF('P', 'mm', 'A4')
pdf.set_font('Helvetica', 'B', 20)
pdf.add_page()

pdf.cell(txt=f"Month : facecream : facewash : Shampoo", ln=1)
pdf.ln(3)
for i in range(len(month)):
	pdf.cell(txt=f"{month[i]} : {facecream[i]} : {facewash[i]} : {shampoo[i]}", ln=True)



pdf.output("csv_to_pdf.pdf")