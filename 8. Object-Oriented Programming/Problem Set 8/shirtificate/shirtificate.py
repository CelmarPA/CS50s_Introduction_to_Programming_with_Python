from fpdf import FPDF


class Shirtificate(FPDF):

    def __init__(self, name):
        super().__init__()

        self.name = name

    def header(self):
        self.set_font("Helvetica", size=48)
        self.ln(20)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)


    def shirt(self):
        self.set_font("Helvetica", size=24, style="B")
        self.set_text_color(255, 255, 255)
        self.image("shirtificate.png", x="C")
        self.set_xy(80, 110)
        self.cell(50, 10, f"{self.name} took CS50", align="C")


def main():
    name = input("Name: ")
    shirtificate = Shirtificate(name)
    shirtificate.add_page()
    shirtificate.shirt()
    shirtificate.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
