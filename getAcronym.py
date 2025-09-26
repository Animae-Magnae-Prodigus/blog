import os
def main(filename):
    with open( filename, "r") as f:
        for l in f .readlines() :
            temp = "".join([s[0].upper() for s in l.strip().split(" ")])
            print(f"{ l.strip()}\tfixed\t{os.path.split(filename)[-1][0]}{temp}")


import sys
filepath = os.path.dirname( sys.argv[ 0])
main(os.path.join(filepath, "acronym/Fiction"))
# main(os.path.join(filepath, "acronym/Nonfiction"))
main(os.path.join(filepath, "acronym/male"))
# main(os.path.join(filepath, "acronym/female"))
