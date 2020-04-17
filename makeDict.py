
def makeDict(k,v):
    myDict={}
    if len(k)==len(v):
        for i in range(len(k)):
            myDict[k[i]]=v[i]
    else:
        print("Key and Value are different size")
        return 0;
    return myDict

k= ('Korean','Mathematics','English',)
v= (90.3,85.5,92.7)

myDict=makeDict(k,v)

for key,value in myDict.items():
    print(key,':',value)
    
