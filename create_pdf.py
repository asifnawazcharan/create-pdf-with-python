from fpdf import FPDF

quotes = ['This is quote #1', 'This is quote #2', 'This is quote #3', 'This is quote #4', 'This is quote #5']

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('helvetica', '', 16)

pdf.cell(txt="Find 5 quotes below one after another:", ln=True, border=True)
for quote in quotes:
	pdf.cell(40,10, quote, ln=True)

pdf.output('output.pdf')
