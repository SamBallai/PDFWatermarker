import PyPDF2
import sys
import os

def pdf_combiner(pdf_list):
    #Take command line input (don't take the filename tho)
    inputs = sys.argv[1:]
    merger = PyPDF2.PdfMerger()
    #Merge all PDFs
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('giga.pdf')

#Just for fun
def rotate():
    with open('dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        page.rotate(180)
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        with open('crooked.pdf', 'wb') as new_file:
            writer.write(new_file)


