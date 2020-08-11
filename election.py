from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
import re
import urllib.request
import matplotlib.pyplot as plt


def plotgraph(finallist):
    #p=0
    
##    #datawa=dict()
##    for i in finallist:
##        if(i<0):
##                p=p+1                       #weak
##    #print("Weakened Against",p)
##    weakp=p/len(commonkeys)
    plt.figure(figsize=(40, 17))

    x=[]
    y=[]
    for i in finallist:
        x.append(str(i[0])+"."+str(i[1]))
        y.append(int(i[9]))
    barlist=plt.bar(x,y)
    i=90
    #for i in range(0,91):
    while(i>0):
        
        #xaxis=int(i[0])
        #if(i[4]=='INC'):
        barlist[i].set_color('b')
        i=i-1
##        elif(i[4]=='BJP'):
##            barlist[i].set_color('y')
##        else:
##            barlist[i].set_color('r')

   # plt.bar(x1,y1,label='bars',color='r')
    plt.xlabel("Assembly")
    plt.ylabel("Diff of votes")
    plt.xticks(rotation=90)
  #  plt.title(base+" change%\n Weakened Against "+str(round(weakp*100,2))+"% of Total Currencies\n"+str(namel[0])+" to "+str(namel[1]))
    plt.savefig('myfigmelection')

loutputlarge=list()
for i in range(1,91):
    print("====================================================")
    name=str(i)
    urlstr='http://eciresults.nic.in/ConstituencywiseS26'+name+'.htm?ac='+name
    html = urllib.request.urlopen(urlstr)

    soup=BeautifulSoup(html,"html.parser")
    tags = soup('tr')
    #print(tags)
    lotags=list()
    for tag in tags:
        if len(str(tag))>1000:
            #print((tag))
            p=str(tag)
            lotags.append(p)                            #list of tags <tr>
    needed=lotags[-1]#last tag containing data


    soupi=BeautifulSoup(needed,"html.parser")  #parsing to get td tags from each ||tr|| tags
    p=soupi('td')  #all td tags in each tr tag

    pneeded=p[1:]#eliminating 1st tag at index 0 which is garbage
    #print(pneeded)#needed td tags
    listneeded=list()
    listneeded.append(name)
    for o in range(0,8):
        if(len(pneeded[o])>60):
            pneeded[o]="$$$"
            currname=pneeded[o]

        else:
                  
            #print(pneeded[0]) #assembly name
            an=str(pneeded[o]) #saving assembly name to a variable
            poscur=an.find(">")#1.1 to save value in td tag
            poscur1=an.find("</td>")#1.2 to save value in td tag
            currname=an[(poscur+1):(poscur1)] #1.3 last step that store value in td tag
        listneeded.append(currname)
    #if(len(listneeded[o])==8):
    loutputlarge.append(listneeded)
##print(loutputlarge)#printing td tag whose value was stored

lenfinal=len(loutputlarge)
finallist=list()
for v in range(0,lenfinal):
    row=loutputlarge[v]
    rowfirstval=row[1]
    row.append(int(row[5])-int(row[8]))
    if(rowfirstval[0:12]=='Chhattisgarh'):
        row[1]=(row[1])[15:]
    if(row[2]=='Counting In Progress  '):
        row[2]='CIP'
    if(row[4]=='Indian National Congress'):
        row[4]='INC'
    if(row[4]=='Bharatiya Janata Party'):
        row[4]='BJP'
    if(row[7]=='Indian National Congress'):
        row[7]='INC'
    if(row[7]=='Bharatiya Janata Party'):
        row[7]='BJP'
    finallist.append(row)
##print(finallist)
##lenfinallist=len(finallist)
print(len(finallist))
for l in finallist:
    print(l)

plotgraph(finallist)

##def plotgraph(finallist):
##    #p=0
##    
####    #datawa=dict()
####    for i in finallist:
####        if(i<0):
####                p=p+1                       #weak
####    #print("Weakened Against",p)
####    weakp=p/len(commonkeys)
##    plt.figure(figsize=(40, 17))
##
##    x=[]
##    y=[]
##    x1=[]
##    y1=[]
##    for i in finallist:
##        x.append(str(i[0])+"."+str(i[1]))
##        y.append(int(i[9]))
##    
##    plt.bar(x,y,label='bars',color='g')
##   # plt.bar(x1,y1,label='bars',color='r')
##    plt.xlabel("Assembly")
##    plt.ylabel("Diff of votes")
##    plt.xticks(rotation=90)
##  #  plt.title(base+" change%\n Weakened Against "+str(round(weakp*100,2))+"% of Total Currencies\n"+str(namel[0])+" to "+str(namel[1]))
##    plt.savefig('myfigmelection')
##
####
##def write_html(finallist):
##    html_str = """<html>
##             <head>
##             <title>RatesDiffcalculator</title>
##             <link rel='stylesheet' href='http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css' />
##             <script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.js'></script>
##             <script type='text/javascript' src='http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js'></script>
##             </head>
##             <body>
##             <ul class='nav nav-tabs'>
##             <li class='active'><a href='#gainers' data-toggle='tab'><h4>Summary</h4></a></li>
##             
##             </ul>
##             <div class='tab-pane active' id='weak'>
##             {weak}
##             </div>
##             <ul class='nav nav-tabs'>
##             <li class='active'><a href='#gainers' data-toggle='tab'><h5>RatesDiffCalc</h5></a></li>
##             <li><a href='#graphplot' data-toggle='tab'><h5>Graph</h5></a></li>
##
##             </ul>
##             
##            
##             <div class='tab-content'>
##             <div class='tab-pane active' id='gainers'>
##             {gainersData}
##             </div>
##             <div class='tab-pane' id='graphplot'>
##             <img src='C:/Users/Pandey/Desktop/Mohit/MohitPython/RandomCodes/myfigm.png' alt='Smiley face' >
##             </div>
##             
##             </div> 
##             </body>
##             </html>""".format(gainersData = create_table(maindata,commonkeys,namel), weak =weakagainst(lofchange,commonkeys,base))
##    return html_str
##
