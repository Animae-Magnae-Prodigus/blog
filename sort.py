import csv
import sys
import re
sep = ", "
result = []
AuthorTitles = []
with open(fileName:="HN.tsv", "r") as f:

    reader = csv.DictReader(f, dialect=csv.excel_tab, )
    fieldnames= reader.fieldnames
    for r in reader:
        if not r:
            continue
        print(f"{ r["Tags"]=}")
        temp = []
        year = 9999
        for i in r["Tags"].split(sep):
            if number := re.findall(r"^(\d{4})$", i.strip()):
                year = int(number[0])
                break
        r["Author"] = r["Author"] .strip()
        r["Title"] = r["Title"] .strip()
        r["Directory"] = r["Directory"] .strip()
        AuthorTitle = r["Author"]+r["Title"] + r["Tags"]
        if AuthorTitle not in AuthorTitles:
            result.append((year, r))
            AuthorTitles.append(AuthorTitle)

result.sort(key=lambda x: x[0], reverse=True)
# result = [x[1] for x in result]
with open( fileName+sys.argv[0]+".tsv", "w") as f:
    w = csv.DictWriter(f, dialect=csv.excel_tab, fieldnames=fieldnames)
    w .writeheader()
    for r in result:
        w.writerow(r[-1])
