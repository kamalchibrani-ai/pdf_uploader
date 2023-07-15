from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)
    
    writer.add_metadata(reader.metadata)
    writer.remove_images()


    with open(output_path, "wb") as f:
        writer.write(f)