def findDictionary(datalist, key, valor):
    info = {}
    for i in range(len(datalist)):
        if datalist[i].get(key) == valor:
            info["index"] = i
            info["data"] = datalist [i]
            break
    return info 