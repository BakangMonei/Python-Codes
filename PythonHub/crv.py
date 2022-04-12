import csv
#creating user.csv
with open('user.csv', 'w') as x:
    xWriter = csv.writer(x)
    xWriter.writerow(['user_id', 'username', 'age', 'gender'])
    xWriter.writerow(['1', 'aaa', '21', 'M'])
    xWriter.writerow(['2', 'bbb', '34', 'M'])
    xWriter.writerow(['3', 'ccc', '24', 'F'])
    xWriter.writerow(['4', 'ddd', '12', 'F'])
    xWriter.writerow(['5', 'eee', '48', 'M'])
    xWriter.writerow(['6', 'fff', '14', 'F'])
    xWriter.writerow(['7', 'ggg', '78', 'F'])
    xWriter.writerow(['8', 'hhh', '27', 'M'])
with open('beneficiary.csv', 'w') as x:
    xWriter = csv.writer(x)
    xWriter.writerow(['user_id', 'beneficiary'])
    xWriter.writerow(['1', 'xyz'])
    xWriter.writerow(['2', 'pqr'])
    xWriter.writerow(['3', 'xxx'])
    xWriter.writerow(['4', 'yyy'])
    xWriter.writerow(['5', 'zzz'])
#copy data from user.csv to out.csv
outfile = open('out.csv','w') #left the file open to avoid exception
outfileWriter = csv.writer(outfile)
with open('user.csv','r') as infile:
    infileReader = csv.reader(infile)
    for x in infileReader:
        outfileWriter.writerow(x)
#combine data of user.csv and beneficiary.csv
userlist = []
benlist = []
# iterate over each row of user.csv and append the row as a list to userList
with open('user.csv','r') as userfile:
    userfileReader = csv.reader(userfile)
    for row in userfileReader:
        userlist.append(row)
with open('beneficiary.csv','r') as benfile:
    benReader = csv.reader(benfile)
    for row2 in benReader:
        benlist.append(row2)
# checking lists created
for i in userlist:
    print(i)
for i in benlist:
    print(i)
# Combine 2 lists and ass rows to row_wise.csv
with open ('row_wise.csv', 'w') as rowfile:
    rowfileWriter = csv.writer(rowfile)
    for user_row in userlist:
        combined_row = []
        combined_row.extend(user_row)
        for ben_row in benlist:
            if user_row[0] == ben_row[0]:
                combined_row.append(ben_row[1])
        rowfileWriter.writerow(combined_row)