"""
Read a book and create its format for notes
"""
import datetime
import sys
import csv
import re

dialect = "excel-tab"

# read the list
ListFileName = "list.tsv"
with open(ListFileName, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, dialect=dialect)
    fieldnames = reader.fieldnames
    books = [x for x in reader]
    print(books)

# find the current book
current = None
for book in books:
    AuthorTitle = book["Author"] + "-" + book["Title"]
    AuthorTitle = re.sub(r" ", r"-", AuthorTitle)
    import glob
    if not glob.glob("*"+AuthorTitle+".md"):
        print(f"{AuthorTitle}")
        current = book
        break
print(f"{current}")

templateFileName = "template.md"
with open(templateFileName, "r", encoding="utf-8") as f:
    template = f.read()

    for fieldname in fieldnames:
        print(fieldname)
        template_ = re.sub(fieldname, current[fieldname], template)
        template = template_
    print(template)

# output file
outputFilename = datetime.date.today()
outputFilename = outputFilename.isoformat() + "-" + AuthorTitle + ".md"
print(f"{outputFilename=}")
with open(outputFilename, "w", encoding="utf-8") as f:
    f.write(template)
