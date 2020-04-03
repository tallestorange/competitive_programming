s = input()
size = len(s)
q = []

if s == "{}":
    print("dict")
else:
    pos = 1
    while pos < size-1:
        if s[pos] == "{":
            q.append("{")
        elif s[pos] == "}":
            if q[-1] == "}":
                q.append("}")
            else:
                q.pop()
        pos += 1
        if not q:
            break
    
    while pos < size-1:
        v = ord(s[pos])-48
        if 0<=v<=9:
            pos += 1
        else:
            break

    print("dict" if s[pos]==":" else "set")