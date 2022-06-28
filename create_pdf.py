from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('helvetica', '', 16)

pdf.header("This is a heading")
pdf.ln(5) # gives space of 5 mm below the header
pdf.cell(txt="This is how one line can be written to a pdf. ")
pdf.ln(5)
pdf.multi_cell(0, txt="This is a bigger text which can not fix on one line so we will fill this up quickly sdfjks sdigjsl sdgijkslgj sdgksljgsg slgdjksljg sgdjsljgs sgdjlskgjlsg.")

pdf.output('create_pdf.pdf')
print("pdf created - name: output.pdf")