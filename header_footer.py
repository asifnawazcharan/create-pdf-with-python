from fpdf import FPDF

class PDF(FPDF):
	def header(self):
		#logo
		self.image("test_logo.png", 10,8,25)
		self.set_font('helvetica', 'B', 10)
		self.cell(0,10,txt='How to create pdf with python', align='c')
		# 0 here indicates full width of the document as the width of this cell.
		self.ln(20)

	def footer(self):
		self.set_y(-15)
		self.set_font('helvetica', 'B', 15)
		self.cell(0,10,txt=f"{self.page_no()}", align='r')
		# 0 here indicates full width of the document as the width of this cell.

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
for i in range(100):
	pdf.set_font('helvetica', '', 20)
	pdf.cell(txt=f"This is line {i}", ln=True)

pdf.output("output_with_header.pdf")