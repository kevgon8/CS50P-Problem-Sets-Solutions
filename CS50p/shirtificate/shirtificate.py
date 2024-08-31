from fpdf import FPDF

class PDF():
    def __init__(self, usr_nme):
        self.nme = usr_nme

    def create_pdf(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.image("shirtificate.png", x=0.5, y=60)
        self.pdf.set_font("helvetica", "B", size=50)
        self.pdf.set_text_color(r=0, g=0, b=0)
        self.pdf.cell(text="CS50 Shertificate", center=True)
        self.pdf.set_font_size(size=30)
        self.pdf.set_text_color(r=255, g=255, b=255)
        self.pdf.cell(text=f"{self.nme} took CS50", center=True, h=250)
        self.pdf.output("shirtificate.pdf")

nme = input("What's your name? ").title().strip()
shertificate1 = PDF(nme)
shertificate1.create_pdf()
