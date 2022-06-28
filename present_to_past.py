from fpdf import FPDF

pdf = FPDF('P', "mm", 'A4')
pdf.set_font("Helvetica", "", 20)
pdf.add_page()


