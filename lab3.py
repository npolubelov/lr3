#!/usr/bin/env python3
class energy:
 
    def __init__(self, name, price, energytype, objectof, mdiffrnce):
        self.name = name
        self.price = price  
        self.energytype = energytype  
        self.objectof = objectof
        self.mdiffrnce = mdiffrnce   

    def __repr__(self):
        return '\nНазвание энергосберегающего мероприятия = {} \nСтоимость проведения мероприятия = {} \nТип затрагиваемого энергетического ресурса = {} \nОбъект, на котором будет проводится мероприятие = {} \nЭкономия на ресурсе в месяц после приминения мероприятия = {}\n'.format(self.name, self.price, self.energytype, self.objectof, self.mdiffrnce)

    def display_info(self):
        print("\nНазвание энергосберегающего мероприятия - ",self.name)
        print("Стоимость проведения мероприятия - ",self.price)
        print("Тип затрагиваемого энергетического ресурса - ",self.energytype)
        print("Объект, на котором будет проводится мероприятие - ",self.objectof)
        print("Экономия на ресурсе в месяц после приминения мероприятия - ",self.mdiffrnce,"\n")
 
    def ocup(self):
        self.oc = self.price // self.mdiffrnce
        return "\nСрок окупаемости мероприятия с названием %s %s месяц" % (self.name, self.oc) 
    
    def percentof(self):
        self.prc = self.mdiffrnce / self.price * 100
        return "\nЭкономия на ресурс в месяц состовляет %s процента от стоимости мероприятия %s" % (self.prc, self.name)

exmpl1 = energy("замена толпивоподающие системы", 545999,"мазут","Топливоподающая система",17300)
exmpl2 = energy("установка топливных фильтров", 124700,"мазут","Топливоподающая система",6800)
exmpl3 = energy("установка новых топливных ёмкостей", 221000,"мазут","Топливные резервуары",13400)
#print (exmpl1.ocup())
#$print (exmpl1.percentof())

elist = list()
elist.append(exmpl1)
elist.append(exmpl2)
elist.append(exmpl3)
#print(elist)

# чтение csv файла через csv.reader

import csv
import codecs
 
with open('1.csv', encoding='utf-8', newline='', errors='ignore') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)

with open('1.csv', encoding='utf-8') as r_file:
    reader1 = csv.DictReader(r_file)
    for row in reader1:
         print(row)

with open('3.csv', mode="w", encoding='utf-8') as w_file:
    writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    writer.writerow(['self.name','self.price','self.energytype','self.objectof','self.mdiffrnce'])
    writer.writerow(['замена толпивоподающие системы','545999','мазут','Топливоподающая система','17300'])
    writer.writerow(['установка топливных фильтров','124700','мазут','Топливоподающая система','6800'])
    writer.writerow(['установка новых топливных ёмкостей','221000','мазут','Топливные резервуары','13400'])

with open("4.csv", mode="w", encoding='utf-8') as w_file1:
    types = ['self.name','self.price','self.energytype','self.objectof','self.mdiffrnce']
    writer1 = csv.DictWriter(w_file1, delimiter = ",", lineterminator="\r", fieldnames=types)
    writer1.writeheader()
    writer1.writerow({'self.name': 'замена толпивоподающие системы', 'self.price': '545999', 'self.energytype': 'мазут', 'self.objectof': 'Топливоподающая система', 'self.mdiffrnce': '17300'})
    writer1.writerow({'self.name': 'установка топливных фильтров', 'self.price': '124700', 'self.energytype': 'мазут', 'self.objectof': 'Топливоподающая система', 'self.mdiffrnce': '6800'})
    writer1.writerow({'self.name': 'установка новых топливных ёмкостей', 'self.price': '221000', 'self.energytype': 'мазут', 'self.objectof': 'Топливные резервуары', 'self.mdiffrnce': '13400'})