import re, statistics
# with open("nv.sh", "r") as f:
    # file = f.readlines()[0].split(" ")[-2]

import sys
if len(sys.argv) > 1:
    file = sys.argv[-1]
else:
    file = "current"
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
    if score:
        print(score)
        average = round(statistics.mean(score), 2)
        print(average)
        average_ = int(round(average+20,0)-20)
        print(average_)


with open(file_:=file+".cp", "w") as f:
    f.writelines(lines)
print(f"{ file_=}")

lines[1] = re.sub(r" [\d\?]/9 ", f" {average_}/9 ", lines[1])
with open(file, "w") as f:
    f.writelines(lines)
