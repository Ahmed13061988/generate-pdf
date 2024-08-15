import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1, border=0)
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1, border=0)

pdf.output("output.pdf")
