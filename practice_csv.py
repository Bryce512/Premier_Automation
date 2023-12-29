# import csv
# # Read names from CSV
# with open('Premier Automation/Practice_file.csv', 'r') as file:
#     reader = csv.reader(file)
#     output = open('Cleaned_CSV.csv', 'w')
#     for names in reader:
#         # names = row.split(',')
#         Mfirst = names[1]
#         Mlast = names[0]
#         LFirst = names[3]
#         LLast = names[2]
#         teacher = names[4]
#         if names[5] != "":
#             cls = names[5]
#         elif names [6] != "":
#             cls = names [6]
#         elif names[7] != '':
#             cls = names[7]
#         else:
#             cls = ''
#         output.write(f'Male Name: {Mfirst} {Mlast} \nLady\'s name: {LFirst} {LLast}\nTeacher:{teacher}\nClass: {cls} \n\n')
#     output.close()

Database_name = 'BYU SDC 2022'
comp_window_name = f"NDCA DANCE COMPETITION SETUP:            DATABASE =  {Database_name}"

def get_Shortened_Title(title):
    shortened_title = ''
    title = title.lower().split()
    for word in title:
        i=0
        for letter in word:
            if i != 0 and letter.isalpha():
                shortened_title += letter
            elif i == 0 and letter.isalpha():
                shortened_title += letter.upper()
            else:
                pass
            i += 1
    return shortened_title

print(get_Shortened_Title(comp_window_name))