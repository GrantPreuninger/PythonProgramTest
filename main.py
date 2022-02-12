#GrantPreuninger Project
open('C:\\Users\\Grant\\Downloads\\Students (1).txt','r')
datas = []
with open('C:\\Users\\Grant\\Downloads\\Students (1).txt') as t:
    for line in t:
        line = line.split()
        datas.append(line)

header = datas[0]
data = datas[1:]


print('WELCOME TO STUDENT DATA FINDER')


#main function to execute based off of initial user input
def main(d):
    cont = 'y'
    while cont == 'y':
        print("'1' to display all student records")
        print("'2' to find students by last name")
        print("'3' to display student records from a certain year")
        print("'4' to Display a summary report of number and percent of students in each program, for students graduating on a certain year")
        print("'5' to Display a summary report of number and percent of students in each program, for students graduating after a certain year")
        print()
        command = int(input('Please enter one of the above commands: '))
        print()

        if command == 1:
            c_1(d)
        if command == 2:
            c_2(d)
        if command == 3:
            c_3(d)
        if command == 4:
            c_4(d)
        if command == 5:
            c_5(d)
        print()
        cont = input('Make another query? (y to continue): ')
        print()


#functions for the different queries
def c_1(d):
    print(header)
    for row in d:
        print(row)


def c_2(d):
    while True:

        last_name = input('enter student\'s last name or part of it (be specific to narrow results) : ')
        if last_name.isalpha():
            break
        else:
            print('Please only enter letters for last name ')

    print(header)

    for row in d:
        if row[1].lower().startswith(last_name.lower()):
            print(row)




def c_3(d):
    while True:
        grad_year = input('enter graduate year for students you want data on: ')

        if grad_year.isdigit():
            break
        else:
            print('Please enter a 4 digit number for the year that is before 2022 and after 2018 ')

    print(header)
    for row in d:
            if grad_year == row[3]:
                    print(row)


def c_4(d):
    while True:

        year = input('Enter graduate year for which you want a summary report on: ')
        if year.isdigit():
            break
        else:
            print('Please enter 4 digit numeric date between 2019 and 2021')

    print()
    print('Number of students in each major, and the % that major has for the year:', year )
    year_list = []
    counts = {}
    for row in d:
        if row[3] == year:
            year_list.append(row)
    for row in year_list:
            if row[5] in counts:
                counts[row[5]] +=1
            else:
                counts[row[5]] = 1

    for key in counts:
        c = (counts[key]/len(year_list))*100
        print(key,'Students:',counts[key],'    ','%0.2f%%'%(c))


def c_5(d):
    while True:

        try:
            year = int(input('Enter the base graduate year that you want data after that year from: '))


        except ValueError:
                print('must be number')
                continue
        else:
                break
    print('Number of students in each major, and the % that major has for people graduating after the year:', year)
    after_list = []
    counts = {}
    for row in d:
        if int(row[3]) > year:
            after_list.append(row)
    for row in after_list:
            if row[5] in counts:
                counts[row[5]] +=1
            else:
                counts[row[5]] = 1
    for key in counts:
        c = (counts[key] / len(after_list)) * 100
        print(key, 'Students:', counts[key], '    ', '%0.2f%%' % (c))








main(data)
