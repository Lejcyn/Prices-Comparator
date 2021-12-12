import pandas as pd

files=['Barcelona.xlsx','London.xlsx','Insbruck.xlsx','Graz.xlsx','Vienna.xlsx','Milano.xlsx','Munich.xlsx','Berlin.xlsx','Zurich.xlsx','Newbury.xlsx','Manchester.xlsx']

def CompareLivingCosts(file):

    df = pd.read_excel(file)

    nan_value = float("NaN")

    df.replace("", nan_value, inplace=True)

    df.dropna(subset = ["Difference"], inplace=True)
    df.dropna(subset = ["Salary"], inplace=True)
    Differences=df["Difference"].astype(str).values.tolist()
    Salary=df["Salary"].astype(str).values.tolist()
    kek=[]

    sal=Salary[0]
    sal1=sal.replace(" ","")
    sal2=sal1.replace("%","")

    for idx,i in enumerate(Differences):
        
        a=i.replace(" ","")
        b=a.replace("%","")
        kek.append(float(b.replace("\xa0","")))
    print(file+"\t") 
    AverageCosts=sum(kek)/len(kek)
    print( "Living costs: "+str(AverageCosts) + " Salary: " +sal2)
    Dif=float(sal2)-AverageCosts
    print("Total Living quality increase: "+ str(Dif))
    print("Cica will earn: "+ str(300000+300000*Dif/100))
    print("Kotek will earn: "+ str(600000+600000*Dif/100) +"\n\n")
for file in files:
    CompareLivingCosts(file)
