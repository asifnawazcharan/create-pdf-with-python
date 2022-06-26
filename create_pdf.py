from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('helvetica', '', 16)


for i in range(100):
	pdf.cell(txt=f"Hello Aqib", ln=True)
pdf.output('output.pdf')
