from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    filename = filename.capitalize()
    print(filename)
    pdf.cell(w=50, h=8, txt=f"{filename}", ln=1)
        
pdf.output("output.pdf")

