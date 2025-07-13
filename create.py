"""
Read a book and create its format for notes
"""
import datetime
import glob
import os
import csv
import re,sys

dialect = "excel-tab"

listtsv = "hugo.tsv"
# read the listtsv
if not sys.argv[-1].endswith("tsv"):
    listtsvFileName = listtsv
else:
    listtsvFileName = sys.argv[-1]

with open(listtsvFileName, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, dialect=dialect)
    fieldnames = reader.fieldnames
    # books = [x for x in reader if x]

    books = []
    for x in reader:
        # print(x)
        books.append(x)
    # print(books)

# exit()
# find the current book
current = None
for book in books:
    title = re.sub(r"\(.*\)", "", book["Title"]).strip()
    title = re.sub(r"[&!, ]+", "-", title).strip()
    author = re.sub(r"[\.;,]", "", book["Author"]).strip()
    AuthorTitle = author + "-" + title
    AuthorTitle = re.sub(r" ", r"-", AuthorTitle).strip()
    tags = book["Tags"].strip()
    # print(tags)
    tags = [ re.sub(r"\s+", "-", tag.strip()) for tag in re.split(r" *, *", tags) if tag.strip()]
    # print(tags)
    book["Tags"] = " ".join(tags)
    # exit()

    if not glob.glob("**/*"+AuthorTitle+".md"):
        # print(f"{AuthorTitle}")
        current = book
        break


print("="*10,f"\n{current=}")

# exit()
templateFileName = "template.md"
with open(templateFileName, "r", encoding="utf-8") as f:
    template = f.read()

    for fieldname in fieldnames:
        # print(fieldname)
        template_ = re.sub(fieldname, current[fieldname], template)
        template = template_
    # print(template)

# output file
outputFilename = datetime.date.today()
outputFilename =  outputFilename.isoformat() + "-" + AuthorTitle + ".md"
outputFilenamePath = os.path.join("_posts", current["Directory"], outputFilename)
with open(fn:="nv.sh", "w") as f:
        print(f"Create {fn=}")
        print(f"nvim -S ia.vim \"{outputFilenamePath}\" {listtsv}", file=f)
        print(f"rm -f current", file=f)
        print(f"ln -s \"{outputFilenamePath}\" current", file=f)
# exit()

with open(fn:=f"nv{AuthorTitle[:2]+AuthorTitle[-2:]}.sh", "w") as f:
        print(f"Create {fn=}")
        print(f"nvim -S ia.vim \"{outputFilenamePath}\" {listtsv}", file=f)
        print(f"rm -f current", file=f)
        print(f"ln -s \"{outputFilenamePath}\" current", file=f)
# exit()
with open(outputFilenamePath, "w", encoding="utf-8") as f:
    print(f"Create {outputFilenamePath=}")
    f.write(template)
