import csv
import sys
import re
sep = ", "
result = {}
with open(fileName:="HN.tsv", "r") as f:

    reader = csv.DictReader(f, dialect=csv.excel_tab, )
    fieldnames= reader.fieldnames
    for r in reader:
        if not r:
            continue
        print(f"{ r["Tags"]=}")
        if r["Directory"].strip() != "science-fiction":
            continue
        temp = []
        year = 9999
        for i in r["Tags"].split(sep):
            if number := re.findall(r"^(\d{4})$", i.strip()):
                year = int(number[0])
                break
        r["Author"] = r["Author"] .strip()
        r["Title"] = r["Title"] .strip()
        r["Directory"] = r["Directory"] .strip()
        AuthorTitle = r["Author"]+r["Title"]
        if AuthorTitle not in result.keys():
            result[AuthorTitle]=(year, r)
        else:
            print(f"{ result[AuthorTitle]=}")
            result[AuthorTitle][-1]["Tags"] += sep+r["Tags"]
        print(f"{ result[AuthorTitle]=}")

result=list(result.values())
result.sort(key=lambda x: x[0], reverse=True)
# result = [x[1] for x in result]
with open( fileName := fileName+sys.argv[0]+".tsv", "w") as f:
    passed = 0
    w = csv.DictWriter(f, dialect=csv.excel_tab, fieldnames=fieldnames)
    w .writeheader()
    for r in result:
        if r[0] != 9999 and not passed:
            passed = 1
            f.write("\n")
        r[-1]["Tags"] = sep.join(set(r[-1]["Tags"].split(sep)))
        w.writerow(r[-1])
print(f"{ fileName=}")
