import re, statistics
with open("nv.sh", "r") as f:
    file = f.readlines()[0].split(" ")[-2]

with open(file, "r") as f:
    lines = f.readlines()

for prefix in [r"^# ", r"^## "]:
    score = []
    for line in lines:
        pattern = prefix + r".*(\d)/9"
        if (r := re.findall(pattern, line)):
            score.append( int(r[0]) )
        else:
            # print(line)
            continue
    print(file)
    print(score)
    print(round(statistics.mean(score), 2))
