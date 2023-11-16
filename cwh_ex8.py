
'''
Exercise - 8

1) Write a program to manipulate PDF files using pyPDF. Your program should be able to merge multiple pdfs into a single pdf.
You are welcome to add more functionalities.

2) PYPDF is a free and open-source pure-python PDF library capable of splitting, merging, cropping and transforming the pages of PDF files.
It can also add custom data, viewing options, and password to pdf files. pyPDF can retrieve text and metadata from PDFs as well.

'''

#This code is directly pasted from replit as I was unable to install pypdf in my system at the moment of writing this code.

from PyPDF2 import PdfWriter

import os

merger = PdfWriter()
files = os.listdir()

files = [file for file in files if file.endswith('.pdf')]

for pdf in files:
  merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
