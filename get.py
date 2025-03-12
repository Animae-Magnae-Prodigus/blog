import re, bs4
from bs4 import BeautifulSoup
soup=None
result   = []
with open ("Theodore_Sturgeon_Award?wprov=sfla1", "r") as f:
    soup = BeautifulSoup(f, "xml")
    # print(soup.prettify())
for link in soup.find_all('tbody'):
    for tr in soup.find_all('tr'):
        temp = []
        for td in tr.find_all('td'):
            text = td.get_text()
            text = re.sub(r"[\n\"\]\[]", r"", text)
            if text and not re.match(r"\d+", text):
                temp.append(text)

        if len((temp)) >= 3:
            # temp.append(text)
            sum = "\t".join(temp)
            if "*" not in sum:
                continue
            else:
                sum = re.sub(r"[\*\n\"\]\[]", r"", sum)
                result.append(sum+", Short-Story, Nebula-Award-for-Best-Short-Story, science-fiction\tscience-fiction")
    break
for r in result[::-1]:
    print(r)
exit()
