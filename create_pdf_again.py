from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.set_font('Helvetica', 'B', 20)
pdf.add_page()

pdf.cell(txt="This is a new pdf.", ln=True, border=True)

pdf.output("newpdf.pdf")