import pdfkit
import PyPDF2
import os
import glob

# set urls
plustot10 = 'http://www.somprint.nl/plustot10.html'
mintot10 = 'http://www.somprint.nl/mintot10.html'
plustot20 = 'http://www.somprint.nl/plustot20ztp.html'
mintot20 = 'http://www.somprint.nl/mintot20ztp.html'

link_list = [plustot10, mintot10, plustot20, mintot20]
outp_list = ['plustot10', 'mintot10', 'plustot20', 'mintot20']

# set number of copies
n = 15

# set path for individual files
individuals = 'output/individuals/'

# download files and save
for i, item in enumerate(link_list):
    for j in range(n):
        pdfkit.from_url(item, individuals +
                        outp_list[i] + '_' + str(j) + '.pdf')

# get all file names
flist = glob.glob(individuals + '*.pdf')


pdfWriter = PyPDF2.PdfFileWriter()

# loop through all PDFs
for filename in flist:
    # rb for read binary
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)

        pdfWriter.addPage(pageObj)

# save PDF to file, wb for write binary
pdfOutput = open('output/bigout.pdf', 'wb')
# Outputting the PDF
pdfWriter.write(pdfOutput)
# Closing the PDF writer
pdfOutput.close()
