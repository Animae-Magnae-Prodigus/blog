"""
Read a book and create its format for notes
"""
import datetime
import glob
import os
import csv
import re,sys

dialect = "excel-tab"

# read the list
if not sys.argv[-1].endswith("tsv"):
    ListFileName = "list.tsv"
else:
    ListFileName = sys.argv[-1]

with open(ListFileName, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, dialect=dialect)
    fieldnames = reader.fieldnames
    books = [x for x in reader]
    # print(books)

# exit()
# find the current book
current = None
for book in books:
    title = re.sub(r"\(.*\)", "", book["Title"])
    author = re.sub(r"[\.;,]", "", book["Author"])
    AuthorTitle = author + "-" + title
    AuthorTitle = re.sub(r" ", r"-", AuthorTitle)
    tags = book["Tags"]
    print(tags)
    tags = [ re.sub("\s+", "-", tag) for tag in re.split(r", ", tags)]
    print(tags)
    book["Tags"] = " ".join(tags)
    # exit()

    if not glob.glob("**/*"+AuthorTitle+".md"):
        print(f"{AuthorTitle}")
        current = book
        break
print(f"{current}")

# exit()
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
outputFilename =  outputFilename.isoformat() + "-" + AuthorTitle + ".md"
outputFilenamePath = os.path.join("_posts", current["Directory"], outputFilename)
if ListFileName == "list.tsv":
    with open("nv.sh", "w") as f:
        print(f"nvim -S ia.vim {outputFilenamePath} list.tsv", file=f)
        print(f"rm -f current", file=f)
        print(f"ln -s {outputFilenamePath} current", file=f)
# exit()

with open(outputFilenamePath, "w", encoding="utf-8") as f:
    f.write(template)
