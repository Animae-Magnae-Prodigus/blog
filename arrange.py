
import re
import collections
authors = collections.defaultdict( list)
import csv
with open( "list.tsv", "r") as f:
    reader = csv.DictReader(f, dialect=csv.excel_tab, )
    fieldnames= reader .fieldnames
    for r in reader:
        # print(f"{ r=}")
        authors[r["Author"]].append(r)


import sys
with open( "list.tsv" + sys.argv[0] + ".tsv" , "w") as f:
    writer = csv.DictWriter(f, dialect=csv.excel_tab, fieldnames = fieldnames )
    writer .writeheader()
    for a in authors:
        books = collections.defaultdict( list)
        directory = collections.defaultdict( list)
        for i in authors[a]:
            print(f"{ i['Tags']=}")
            print(f"{ i=}")
            books [i["Title"]] += re.split(r"[ ,] ", i["Tags"])
            directory [i["Title"]] += [  i["Directory"] ]

        for book in books:
            temporary = {}
            temporary ["Author"] = a
            temporary ["Title"] = book
            temporary ["Tags"] = ", ".join(set(books[book]))
            temporary ["Directory"] = directory[book][0]
            print(f"{ temporary}")
            writer .writerow( temporary)

