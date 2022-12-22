import os
def readFile(file):
    if(os.path.exists(file.txt)==True):
        file = open(file.txt,"r")
        contenu = file.readlines() #Lire toutes les lignes du fichier
        file.close()     
        print("Le contenu du fichier est : ")
        #print(contenu) #Tout afficher en une fois      
        for i in contenu: #Afficher ligne par ligne
            print(i)
    

def readNFirstLines(file,n):
    contenu = []
    if n<0:
        print(" Veuillez entrer un nombre de lignes positives")
    else:        
        if(os.path.exists(file.txt)==True):
            file = open(file.txt,"r")
            for i in range(n):
                contenu.append(file.readline()) 
                if contenu[len(contenu)-1] =="":
                    contenu.pop()
                    print("Le fichier ne contient que : ",len(contenu)," lignes","\n")
                    break
            file.close()
            print("Le contenu du fichier est : \n")
            for i in contenu: 
                print(i)
              

def readNLastLines(file,n):
    contenu = []  
    if n<0: #verifier si le nombre de ligne n'est pas negatif
        print(" Veuillez entrer un nombre de lignes positives")  
    else:        
        if(os.path.exists(file.txt)==True): 
            file = open(file.txt,"r")           
            contenu = file.readlines()       
            file.close() #FERMER LE FICHIER           
            print("Les ", n ," dernieres lignes du fichier sont : ")         
            if n>len(contenu):
                n = len(contenu)
                print("Le fichier ne comporte que ",n," lignes \n")         
            i=1
            while(i<=n): #Une boucle tant que i inferieure i   
                print(contenu[len(contenu)-i]) 
                i+=1 
            

def countWords():
    contenu = []    
    if(os.path.exists(file.txt)==True):  
        file = open(file.txt,"r")
        contenu = file.readlines()
        file.close() 
        #print(contenu)      
        sumMots = 0
        for i in contenu:
            #i.replace(":"," ")
            iC = i.split(" ") #En fonction du fichier.
            sumMots+=len(iC)     
        print("Il y'a : ",sumMots, " mots dans le fichier ")

def readNLastLines(file,n):
    contenu = []  
    if n<0: #verifier si le nombre de ligne n'est pas negatif
        print(" Veuillez entrer un nombre de lignes positives")  
    else:        
        if(os.path.exists(file.txt)==True): 
            file = open(file.txt,"r")           
            contenu = file.readlines()       
            file.close() #FERMER LE FICHIER           
            print("Les ", n ," dernieres lignes du fichier sont : ")         
            if n>len(contenu):
                n = len(contenu)
                print("Le fichier ne comporte que ",n," lignes \n")         
            i=1
            while(i<=n): #Une boucle tant que i inferieure i   
                print(contenu[len(contenu)-i]) 
                i+=1 