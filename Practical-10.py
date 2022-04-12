# Name = Smit Mataliya
# Id = 20CE053
# Generate PDF file of your 3rd Semester Mark-sheet.
#Github Link : https://github.com/smitmataliya/Practical-10
from PIL import Image
# Path for your image where it is
image_1 = Image.open(r' F:\4th Sem\Python
Assignment\Practical_10\3rdsem_marksheet.JPG')
# Converting it into pdf
im_1 = image_1.convert('RGB')
# Path where your PDF file will be saved
im_1.save(r' F:\4th Sem\Python Assignment\Practical_10.pdf')