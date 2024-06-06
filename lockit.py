import PyPDF2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = input(f"Enter the name of the PDF file (e.g., document.pdf) [Default: {current_dir}]: ") or ""
input_file_name = input("Enter the name of the PDF file (e.g., document.pdf): ")
input_file = os.path.join(input_file_path, input_file_name)

with open(input_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)


#    output_file_path = input("Enter the path to save the protected PDF: ")
    output_file_path = input_file_path
    output_file_name = input("Enter the name for the protected PDF (e.g., protected_document.pdf): ")
    output_file = os.path.join(output_file_path, output_file_name)
    if os.path.isfile(output_file):
      print(f"File '{output_file}' exists.It  will be deleted before being overwritten.")
      os.remove(output_file) 
    password = input("Enter the password to protect the PDF: ")
    pdf_writer.encrypt(password)

    with open(output_file, 'xb') as output_pdf:
        # Write the encrypted PDF to the new file
        pdf_writer.write(output_pdf)

print(f"{output_file} protected with password.")
