import mysql.connector as pymysql

obj=pymysql.connect(host='localhost',user='root',passwd='QAZplm@2005')
cur=obj.cursor()

try:
    cur.execute('create database auction')
    
except:
    cur.execute('drop database auction')
    cur.execute('create database auction')

cur.execute('use auction')


#create team owner
#deciding number of tables 
owner_number=int(input("enter number of team owners :"))
team_owner_l=[]
for i in range(owner_number):
    x=input("enter name of {} owner :".format(i+1))
    team_owner_l.append(x)

#create tables in sql
for i in range(owner_number):
    x=team_owner_l[i]
    cur.execute('create table {}(name varchar(250), price int)'.format(x))

#---------------------------------------------------------
#player stuff

player_num=int(input('enter number of players :'))
ply={}#dictionary of all players with base price

for i in range(player_num):
    name=input("enter name of player :")
    bp=int(input("enter base price of player :"))
    ply[name]=bp

#---------------------------------------------------------
#auction stuff

def auction(i,k,team_owner_l):
    print('starting price for {} is {}'.format(i,k))
    x=k
    inc=(5/100)*x#5 percent increment each time
    while True:
        bid=input('current bid at {},bid more?(Y/N)'.format(x))
        if bid in 'Yy':
            x+=inc
            continue
        elif bid in 'Nn':
            print(team_owner_l)
            ch=int(input('enter position of highest bidder :'))
            cur.execute("insert into {} values('{}','{}')".format(team_owner_l[ch-1],i,x))
            break
        else:
            print("invalid input")
            continue
            

for i in ply:
    auction(i,ply[i],team_owner_l)

def printf(x):
    for i in x:
        print("{}, sold for-{}".format(i[0],i[1]))
    

for i in team_owner_l:
    cur.execute("select * from {}".format(i))
    print('\n\n')
    print("TEAM {}".format(i))
    x = cur.fetchall()
    printf(x)

obj.commit()
obj.close()
