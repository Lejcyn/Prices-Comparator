import pandas as pd
from os import listdir
from os.path import isfile, join

mypath="Cities"

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



#files=['Barcelona.xlsx','London.xlsx','Insbruck.xlsx','Graz.xlsx','Vienna.xlsx','Milano.xlsx','Munich.xlsx','Berlin.xlsx','Zurich.xlsx','Newbury.xlsx','Manchester.xlsx']
def CompareLivingCosts(file):
    #Read and Parse File
    df = pd.read_excel("Cities/"+file)
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df.dropna(subset = ["Difference"], inplace=True)
    df.dropna(subset = ["Salary"], inplace=True)
    Differences=df["Difference"].astype(str).values.tolist()
    Salary=df["Salary"].astype(str).values.tolist()
    City=file.replace(".xlsx","")
    #Parse single records
    Salaries=Parse(Salary)
    Difs=Parse(Differences)
    #Calculate needed Values
    AverageDifs=sum(Difs)/len(Difs)
    Salary=Salaries[0]
    #Printout the results
    
    print(City+"\t") 
    print( "Living costs: "+str(AverageDifs) + "% Salary: " +str(int(Salary))+"%")
    TotalDif=float(Salary)-AverageDifs
    print("Total Living quality increase: "+ str(int(TotalDif))+"%\n\n")

#Supportive repeating code
def Parse(Records):
    list=[]
    for i in Records:
        a=i.replace(" ","")
        b=a.replace("%","")
        list.append(float(b.replace("\xa0","")))
    return list

for file in files:
    CompareLivingCosts(file)
