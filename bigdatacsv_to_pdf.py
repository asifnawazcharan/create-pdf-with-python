from fpdf import FPDF
import pandas as pd 
import str


# setting up a pdf file
pdf = FPDF('P', 'mm', 'A4')
pdf.set_font("Helvetica", "B", 10)
pdf.add_page()
print("A pdf file created.")


# extracting data from csv into df
data = pd.read_csv("love_quotes.csv", nrows=100).fillna('')
print("Data extracted from csv")

# # cleaning data by removing null values
# cleaned_data = data.dropna(axis=1, how="any")

# Converting the data into list
quotes = data["Quote"].tolist()
authors = data["Author"].tolist()
print("CSV quotes and authors columns converted to lists")

formatted_quotes = []
formatted_authors = []

for i in quotes:
	b = ""
	for i in i:
		if i.isalnum() or i.isspace() or i=="?" or i=="." or i=="," or i=="'":
			b += i
	formatted_quotes.append(b)

for i in authors:
	b = ""
	for i in i:
		if i.isalnum() or i.isspace() or i=="?" or i=="." or i=="," or i=="'":
			b += i
	formatted_authors.append(b)
print("Problem of unrecognizable font appeared. Fixed using str module.")

pdf.cell(txt="100 quotes about love", ln=1)
pdf.ln(5)
# Writing the first Quote and Author columns on pdf
for i in range(len(quotes)):
	pdf.cell(txt=f"{i} - {formatted_quotes[i]} - {formatted_authors[i]}", ln=True)
	pdf.ln(3)
print("List items coded to appear on pdf.")

# outputting pdf
pdf.output("love_quotes.pdf")
print("Creating pdf...")
print("Pdf created successfully - love_quotes.pdf")