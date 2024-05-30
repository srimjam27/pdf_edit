from pypdf import PdfWriter

merger = PdfWriter()

files = ["1.pdf", "2.pdf", "3.pdf"]

for pdf in files:
    merger.append(pdf)

merger.write("std_attendance.pdf")
merger.close()
