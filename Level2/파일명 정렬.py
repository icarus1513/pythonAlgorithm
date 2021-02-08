import re
def solution(files):
    answer = []
    div = [re.split(r"([0-9]+)",s) for s in files]
    sort = sorted(div ,  key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(s) for s in sort]