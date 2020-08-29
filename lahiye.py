import json
data={}
print("**Cars**")
data['Users']=[]
def createDict(_id,_Marka,_Model,_ili):
    innerDict={}
    innerDict['Sira Sayi']=_id
    innerDict['Marka']=_Marka
    innerDict['Model']=_Model
    innerDict['ili']=_ili
    return innerDict

def getData(_id):
    id=_id
    Marka= str( input("Marka : ") )
    Model= str( input("Modeli : ") )
    ili= int( input("ili : ") )
    data['Users'].append(createDict(id,Marka,Model,ili))

for say in range(10):
    say+=1
    print(f"****Elave Olundu****{say}")
    getData(say)

with open("lahiye.json","w") as con:
    json.dump(data,con)
print(data)



