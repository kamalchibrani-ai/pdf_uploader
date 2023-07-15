# from PyPDF2 import PdfReader, PdfWriter


# def read_pdf(file):
#     reader = PdfReader(file)
#     writer = PdfWriter()

#     return reader , writer


# def add_page(reader):
#     for page in reader.pages:
#         writer.add_page(page)
# # for page in reader.pages:
#     writer.add_page(page)

# writer.add_metadata(reader.metadata)

# with open("smaller-new-file.pdf", "wb") as fp:
#     writer.write(fp)