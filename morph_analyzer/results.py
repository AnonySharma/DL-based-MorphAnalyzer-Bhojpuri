import os
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

loc = "output/hindi/"
os.chdir(loc)
files = os.listdir()

# [Paper_accuracy, my_accuracy]
accuracy = {
    "Root": [99.27,0],
    "POS": [99.66,0],
    "Gender": [99.33,0],
    "Number": [98.25,0],
    "Person": [98.93,0],
    "Case": [97.41,0],
    "TAM": [99.68,0]
}

legend = {}
with open("predictions.txt",encoding='utf-8') as ff:
    s = ff.readlines()
    s = s[0].split()
    legend["_words.txt"]=s[1]
    ii=0
    for i in s[2:]:
        legend["feature_"+str(ii)+".txt"]=i
        ii+=1

for f in files:
    if f[0]=='p':
        continue

    guess = []
    true = []
    with open(f,encoding='utf-8') as ff:
        s = ff.readlines()

    for line in s[1:]:
        line=line.split()
        try:
            guess.append(line[1])
            true.append(line[2])
        except:
            break

    # print(guess,true)
    acc = accuracy_score(guess,true)
    acc = round(acc*100,2)
    accuracy[legend[f]][1]=acc
    print(f,legend[f])
    print("\taccuracy:",accuracy_score(guess,true))
    print("\tprecision:",precision_score(guess,true,average="macro"))
    print("\trecall:",recall_score(guess,true,average="macro"))
    print("\tf1:",f1_score(guess,true,average="macro"))
    print("")
    # try:
    # except Exception as e:
    #     print("Error in file:",f)
    #     print("error msg",e)

print(accuracy)
title="Feature\t\t Paper\t\t My"
print("Acuuracy\n",title,sep="")
print("-"*(2*len(title)))
for f,acc in accuracy.items():
    print(f,"\t\t",acc[0],"\t\t",acc[1])