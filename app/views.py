import PyPDF2
from flask import render_template, request, send_file
from io import BytesIO
from app import app  # Import the app instance from __init__.py

@app.route('/', methods=['GET', 'POST'])
#def index():
 #   return render_template('index.html')
def password_protect_pdf():
    if request.method == 'POST':
        # Get the uploaded file
        pdf_file = request.files['pdf_file']
        password = request.form['password']
        output_file_name = request.form['output_file_name']

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add the pages from the reader to the writer
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Set the password for the PDF
        pdf_writer.encrypt(password)

        # Create a new PDF file in memory
        output_pdf = BytesIO()
        pdf_writer.write(output_pdf)
        output_pdf.seek(0)

        # Send the protected PDF file as a download
        return send_file(output_pdf, as_attachment=True, download_name=output_file_name)

    return render_template('index.html')