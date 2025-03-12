import mysql.connector as pymysql
from pypdf import PdfReader
import webbrowser
from PyPDF2 import PdfReader
import os

def get_full_path(file_name, search_dir=None):
    # If no directory is specified, default to the user's desktop
    if search_dir is None:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        search_dir = desktop

    # Search for the file in the specified directory and subdirectories
    for root, dirs, files in os.walk(search_dir):
    #    print(f"Searching in: {root}")  # Print the current directory being searched
        if file_name in files:
            return os.path.join(root, file_name)
    return "File not found."

file_name = input("enter file name :")  # Replace with your document's name
path = get_full_path(file_name)
print(path)

pdf_file = path  # Replace with your file path
reader = PdfReader(pdf_file)

search_text = input("enter name of case in all caps :")

for page_num, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    if search_text in text:
        print(f"Found '{search_text}' on page {page_num}")
        pdf_path = "C:/Users/yuvra/Desktop/Ordersheet-January.pdf#page={}".format(page_num)
        webbrowser.open_new(pdf_path)


