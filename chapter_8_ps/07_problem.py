def ren(l, word):
    n = []
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ["vishan", "harshit", "an" , "rohan"]

print(ren(l, "an"))