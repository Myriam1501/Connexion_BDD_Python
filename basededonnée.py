import mysql.connector as mariadb
import sys
import re

###connexion MariaDB
connexion= mariadb.connect(
        user='myriam',
        host="localhost",
        password='',
        database='test',
        port=3306,
)
cursor=connexion.cursor()
#create_cursor=connexion.execute()

#base de donnée
#create_cursor.execute("SHOW DATABASES")

#for d in create_cursor:
    #print(d)

###supprimer une table
cursor.execute("DROP TABLE test.professeur;")
connexion.commit()

###créer une table 
#create_cursor.execute("USE DATABASES")
cursor.execute("CREATE TABLE professeur (Numprof int(4) NOT NULL, nom VARCHAR(20), prénom VARCHAR(20), classe VARCHAR(3),numscore int(4),PRIMARY KEY (Numprof), KEY `professeur_FK` (`Numscore`), CONSTRAINT `professeur_FK` FOREIGN KEY (`Numscore`) REFERENCES `score` (`Numscore`) ) ENGINE=InnoDB DEFAULT CHARSET=latin1;")
connexion.commit()

cursor.execute("SHOW DATABASES")
for d in cursor:
    print(d)
cursor.execute("SHOW TABLES")
for d in cursor:

    
    print(d)
connexion.commit()
###pour insérer des données dans la table
cursor.execute("INSERT INTO professeur (Numprof, nom, prénom, classe, numscore) VALUES(0, NULL, NULL, NULL, NULL);")
connexion.commit()

###verifier si les donnée sont bien dans la base de données
cursor.execute("SELECT * FROM professeur;")
#montrer le résultat
print(cursor.fetchall())
connexion.commit()




###pour supprimer un enregistrement
cursor.execute("DELETE from students where Numétudiant=1000; ")
connexion.commit()

###enregistrement 

def insert(COLUMN1, COLUMN2):
    text=(COLUMN1, COLUMN2)
    manip="INSERT INTO test.python_creation_table(COLUMN1, COLUMN2) VALUES(%s, %s);"
    cursor.execute(manip,text)
    connexion.commit()
#######question 3

###verifier si les donnée sont bien dans la base de données
cursor.execute("SELECT * FROM professeur;")
#montrer le résultat
print(cursor.fetchall())
connexion.commit()

###chercher une donnee dans la table
cursor.execute("SELECT * FROM students where lunch=standard;")
connexion.commit()

###verifier que l'enrgistrement de la clé  demander à l'utilisateur n'est pas null 
a=input("SELECT Numprof=2 FROM professeur")
if(a==None):
    print("la cle primaire Numprof=1 est vide veiller modifier")
else:
    print("la cle priamire Numprof est vide")


#contraine cle primaire !=None
b=input("SELECT Numétudiant=1 FROM students;")
if(b==None):
    print("la cle primaire numpétudiant=1 est vide")
else:
    print("la cle primaire Numétudiant=1 n'est pas vide")




### Vérifier un INT(4)
a=input("SELECT Numprof=2 FROM professeur")
m=search(r"[0-9]{4}",a)
while (a!=None):
    if m==None:
        a=input("SELECT Numprof=2 FROM professeur")
    else:
        break



