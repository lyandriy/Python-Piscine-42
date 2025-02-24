import sys
import re

def filterwords(S, N):
    try:
        num = int(N)
        txt = re.sub(r'[^\w\s]', '', S)
        txt = txt.split()
        lists = []
        for x in txt:
            if len(x) > num:
                lists.append(x)
        print(lists)
    except ValueError:
        print("ERROR")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        filterwords(sys.argv[1], sys.argv[2])