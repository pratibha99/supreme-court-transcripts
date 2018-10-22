import pdftotext

# Load your PDF
from os import listdir
from os.path import isfile, join
inputPath = "LA/" ##CHANGE IF NECESSARY
outputPath = "LA/textFiles/" ##CHANGE IF NECESSARY

onlyfiles = [f for f in listdir(inputPath) if isfile(join(inputPath, f))]


for f in onlyfiles:
	with open(inputPath + f, "rb") as inputfile:
		# print(str(inputfile))
		if "pdf" in str(inputfile):
			pdf = pdftotext.PDF(inputfile)
			output = open(outputPath + f + ".txt", "w")
			output.write("\n\n".join(pdf))

			

# # If it's password-protected
# with open("secure.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f, "secret")

# How many pages?
# print(len(pdf))

# # Iterate over all the pages
# for page in pdf:
#     print(page)

# # Read some individual pages
# print(pdf[0])
# print(pdf[1])

# Read all the text into one string
# print("\n\n".join(pdf))

# f = open("demofile.txt", "w")
# f.write("\n\n".join(pdf))