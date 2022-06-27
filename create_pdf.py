from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('helvetica', '', 16)

# pdf.cell(txt=f"Hello Aqsa", ln=True)

for i in range(100000):
	pdf.cell(txt=f"{i} - Hello Aqsa", ln=True)

pdf.output('output.pdf')
print("pdf created - name: output.pdf")