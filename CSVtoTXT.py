import csv
import sys

# csv_path = input("What is the name of your file? ")
csv_path = "Practice_file.csv"
csv_temp = csv_path.split(".")
Cleaned_csv = csv_temp[0]+ "_cleaned.csv"



def clean_database():
# Read names from CSV
    with open(csv_path,'r') as file:
        row = csv.reader(file)
        headers = next(row)
        output = open(Cleaned_csv,'w')
        for names in row:
            Mfirst = names[1]
            Mlast = names[0]
            LFirst = names[3]
            LLast = names[2]
            # teacher = names[4]
            for index in range(5,8):
                if names[index] != '':
                    cls = names[index]
                    cls_num = ''
                    for i in cls:
                        if i.isdigit():
                            cls_num += i
                    if classDict[cls_num]:
                      names[index] = classDict.get(cls_num)
            output.write(f'{Mfirst},{Mlast},{LFirst},{LLast},{cls}\n')
    output.close()

classDict = {
    "180":"BYU Dance 180  (CC)",
    "181":"dance-181-country-western-two-step",
    "184":"BYU Dance 184  (Q)",
    "185":"BYU Dance 185  (S)",
    "280":"BYU Dance 280  (SW)",
    "281":"dance-281-country-western-polka",
    "284":"dance-284-ballroom-waltz",
    "285":"dance-285-latin-rumba",
    "380":"dance-380-american-foxtrot",
    "382":"dance-382-ballroom-tango",
    "383":"dance-383-latin-paso-doble",
    "384":"dance-384-ballroom-waltz",
    "385":"dance-385-latin-samba",
    "480":"dance-480-gold-bar-american-mambo",
    "484":"dance-484-gold-bar-ballroom-foxtrot",
    "485":"dance-495-gold-bar-latin-paso-doble",
  };

            # if '180' in cls:
            #     cls = 'BYU Dance 180  (CC)'
            # elif '184' in cls:
            #     cls = 'BYU Dance 184  (Q)'
            # elif '185' in cls:
            #     cls = 'BYU Dance 185  (S)'
            # elif '280' in cls:
            #     cls = 'BYU Dance 280  (SW)'
            # elif '284' in cls:
            #     cls = 'BYU Dance 284  (W)'
            # elif '285' in cls:
            #     cls = 'BYU Dance 285  (R)'
            # elif '380' in cls:
            #     cls = 'BYU Dance 382  (T)'
            # elif '382' in cls:
            #     cls = 'BYU Dance 382  (T)'
            # elif '383' in cls:
            #     cls = 'BYU Dance 383  (PD)'

clean_database()