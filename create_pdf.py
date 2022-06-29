from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('helvetica', '', 16)

pdf.cell(txt="New pdf.")
name_of_file = "new.pdf"
pdf.output(name_of_file)
print(f"Pdf file created - {name_of_file}")