from PyPDF2 import PdfWriter, PdfReader

input_file ="3.pdf"
output_file = 'encrypted_file.pdf'

Writer = PdfWriter()
reader = PdfReader(input_file)

for page in range(len(reader.pages)):
    Writer.add_page(reader.pages[page])
Writer.encrypt('passwordvale')  # Replace 'password' with your desired password
with open(output_file, 'wb') as file:
    Writer.write(file)

print('PDF encrypted successfully!')
