# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pypdf import PdfReader, PdfWriter
from pikepdf import Pdf




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def splitt_pdf(pdf_file_name:str, pages, new_name):
    pdf_file_path = pdf_file_name
    file_base_name = pdf_file_path.replace('.pdf', '')
    pdf = PdfReader(pdf_file_path)
    # pages = [1, 3, 5]  # page 1, 3, 5
    pdf_Writer = PdfWriter()

    pdf_Writer.clone_reader_document_root(pdf)
    #pdf_Writer.clone_document_from_reader(pdf)
    for page_num in pages:
        pdf_Writer.add_page(pdf.pages[page_num-1])
    file_out = f"{file_base_name}_{new_name}.pdf"
    with open(file_out, 'wb') as f:
        pdf_Writer.write(f)
        f.close()


if __name__ == '__main__':
    # print_hi('PyCharm')

    #1,2,3,4,5
    #0,1,2,3,4
    pdf = Pdf.open('C:\Development\pdf_splitt\TestDocA.pdf')

    meta = pdf.open_metadata()
    print(meta)

    with pdf.open_metadata() as source_meta:
        for k in source_meta:
            print(f"{k} = {source_meta[k]}")


    del pdf.pages[1]       # 0 based
    del pdf.pages[3-1]      # 0 based, after first delete wird aus index 3-> 2

    pdf.save('C:\Development\pdf_splitt\TestDocA_even.pdf')

    reader = PdfReader("C:\Development\pdf_splitt\TestDocA.pdf")

    page = reader.pages[0]
    print(page.extract_text())

    page = reader.pages[1]
    print(page.extract_text())

    print("end")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
