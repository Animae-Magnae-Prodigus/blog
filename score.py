import re, statistics
# with open("nv.sh", "r") as f:
    # file = f.readlines()[0].split(" ")[-2]

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
        average_ = int(round(average,0))
        if average_//2:
            average_ = int(round(average+1,0)-1)
        print(average_)


with open(file+".cp", "w") as f:
    f.writelines(lines)

lines[1] = re.sub(r" \d/9 ", f" {average_}/9 ", lines[1])
with open(file, "w") as f:
    f.writelines(lines)
