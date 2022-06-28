from fpdf import FPDF
import pandas as pd
import str 


# file specifications
pdf = FPDF('P', "mm", 'A4')
pdf.set_font("Helvetica", "B", 30)
pdf.add_page()

# get the data from csv
data = pd.read_csv("present_to_past.csv")
print("Data loaded.")
present = data["present"].tolist()
past = data["past"].tolist()

present_filtered = []
past_filtered = []

for i in present:
	b = ""
	for i in i:
		if i.isalnum() or i.isspace or i=="." or i=="?" or i=="'" or i=="!":
			b += i
	present_filtered.append(b)

for i in past:
	b = ""
	for i in i:
		if i.isalnum() or i.isspace or i=="." or i=="?" or i=="'" or i=="!":
			b += i
	past_filtered.append(b)	

# below goes the content of the file
pdf.multi_cell(0, txt="English Grammar Workbook Series: Present to Past", align="c", ln=1)#header
pdf.ln(10)

pdf.set_font("Helvetica", "", 20)
pdf.multi_cell(0, txt="This workbook contains sentences in present simple tense and a space below them where the student can practice writing the past version of the sentence. Answers are given at the end of the file.", ln=1)
pdf.ln(10)

pdf.multi_cell(0, txt="For example:", ln=1)
pdf.multi_cell(0, txt="Present - The boy writes a letter.", ln=1)
pdf.multi_cell(0, txt="Past -  The boy wrote a letter.", ln=1)
pdf.ln(10)

for i in range(len(present_filtered)):
	pdf.multi_cell(0, txt=f"{i+1}. {present_filtered[i]}", ln=1)
	pdf.ln(2)
	pdf.multi_cell(0, txt=f"______________________________", ln=1)
	pdf.ln(15)



# writing answers at the end.
pdf.add_page() #page break to write answers on a new page.
pdf.cell(txt="Answers")
pdf.ln(20)
for i in range(len(past_filtered)):
	pdf.multi_cell(0, txt=f"{i+1}. {past_filtered[i]}", ln=1)
	pdf.ln(3)


# executing the file 
name_of_pdf_file = "present_to_past.pdf"
pdf.output(name_of_pdf_file)
print(f"File ready: {name_of_pdf_file}")