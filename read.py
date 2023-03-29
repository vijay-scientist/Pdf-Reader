import pyttsx3
import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('maths.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Create a text-to-speech engine object
engine = pyttsx3.init()

# Set the reading speed of the engine
engine.setProperty('rate', 150)

# Loop through each page of the PDF file
for page in range(len(pdf_reader.pages)):
    # Get the text content of the page
    page_obj = pdf_reader.pages[page]
    page_text = page_obj.extract_text()

    # Print the text content of the page
    print(page_text)

    # Set the text to be spoken
    engine.say(page_text)

    # Wait for the current page to finish before proceeding to the next
    engine.runAndWait()
