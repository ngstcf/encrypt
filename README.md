Here's a refined version of the README file with improved clarity and formatting:

## Encrypt: PDF Password Protector

Encrypt is a versatile tool that allows you to add password protection to your PDF files, ensuring the security of your sensitive documents. It provides two convenient options: a command-line interface (CLI) and a Flask web application.

### Features

- Set a user password for opening PDF files
- Secure your confidential documents with ease
- Available as a CLI tool or a web application

### Installation

1. Install the required dependencies:

```bash
pip install flask
pip install PyPDF2
```

### Usage

#### Running the Flask Web Application

To run the Flask web application, execute the following command:

```bash
flask run.py
```

Once the server is running, you can access the web application through your preferred web browser.

#### Running the Command-Line Interface (CLI)

To use the CLI version, run the following command:

```bash
python lockit.py
```

Follow the prompts to provide the input PDF file and set the desired password.

### Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used for the web application
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - A pure-python library for reading and writing PDF files
