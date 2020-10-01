import os
import random
import time
import string

randc = [
'\033[0;91m'
,'\033[0;72m'
,'\033[0;93m'
,'\033[0;94m'
,'\033[0;97m'
]
s = time.sleep
black='\033[30m'
red='\033[0;91m'
green='\033[0;72m'
yellow='\033[2;93m'
blue='\033[0;94m'
white='\033[0;97m'

Ublack="\033[4;30m"
Ured="\033[4;31m" 
Ugreen="\033[4;32m" 
Uyellow="\033[4;33m" 
Ublue="\033[4;34m" 
Upurple="\033[4;35m" 
Ucyan="\033[4;36m"
Uwhite="\033[4;37m"

ba_black='\033[40m'
ba_red='\033[1;41m'
ba_blue='\033[1;44m'
ba_green='\033[1;42m'
ba_yellow='\033[1;43m'
ba_white='\033[0;47m'

ranlo=[

'''|██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|█████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|████████████████████████████████░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|█████████████████████████████████████░░░░░░░░░░░░░|  ##@@data1
|████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|████████████████████████████████░░░░░░░░░░░░░░░░░░|  ##@@data1
|██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,
'''|███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,
'''|███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|████████████████████████████████████████████████░░|  ##@@data1'''
,
'''|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|████████████████████████████░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████████████████░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1
|██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|  ##@@data1'''
,'''|██████████████████████████████████████████████████|  ##@@data1'''
,'''|███████████████████████████████████████████████░░░|  ##@@data1
|████████████████████████████████████████████░░░░░░|  ##@@data1
|████████████████████████████████████████████████░░|  ##@@data1
|█████████████████████████████████████████░░░░░░░░░|  ##@@data1
|████████████████████████████████████████████░░░░░░|  ##@@data1'''
]
def rc():
    print ('\033[0;97m')
class loader: 
    def ra_load(text,timesd):
        for a in range(0,timesd):
          ranchoose = ['\r','\r','\r','\r','\r','\r','\r','\n','\r','\r','\r','\r','\r']
          var = ranlo[random.randint(0,len(ranlo)-1)]
          var = var.replace('\n','\r')
          var = var.replace('##@@data1',text)
          print (var,end='',flush=True)
          s(0.04)
          print (ranchoose[random.randint(0,len(ranchoose)-1)],end='')
        print ('')
    def eq_load(ld,nm):
      for a in range(0,nm-1):
         print (ld,'      ','[=              ]   \\',end='\r')
         s(0.03)
         print (ld,'      ','[==             ]   |',end='\r')
         s(0.03)
         print (ld,'      ','[===            ]   /',end='\r')
         s(0.03)
         print (ld,'      ','[ ===           ]   -',end='\r')
         s(0.03)
         print (ld,'      ','[  ===          ]   \\',end='\r')
         s(0.03)
         print (ld,'      ','[   ===         ]   |',end='\r')
         s(0.03)
         print (ld,'      ','[    ===        ]   /',end='\r')
         s(0.03)
         print (ld,'      ','[     ===       ]   -',end='\r')
         s(0.03)
         print (ld,'      ','[      ===      ]   \\',end='\r')
         s(0.03)
         print (ld,'      ','[       ===     ]   |',end='\r')
         s(0.03)
         print (ld,'      ','[        ===    ]   /',end='\r')
         s(0.03)
         print (ld,'      ','[         ===   ]   -',end='\r')
         s(0.03)
         print (ld,'      ','[          ===  ]   \\',end='\r')
         s(0.03)
         print (ld,'      ','[           === ]   |',end='\r')
         s(0.03)
         print (ld,'      ','[            ===]   /',end='\r')
         s(0.03)
         print (ld,'      ','[             ==]   -',end='\r')
         s(0.03)
         print (ld,'      ','[              =]   \\',end='\r')
         s(0.03)
         print (ld,'      ','[               ]   -',end='\r')
         s(0.03)
         print (ld,'      ','[               ]   /',end='\r')
         s(0.03)
      print('')
    def percent_load(vl,colors=False):
      if colors == False:
        for i in range(0,101):
         print (vl,': (',i,'%)',sep='',end='\r')
         s(0.03)
        print (vl,': (',100,'%)',sep='')
      else:
        vl=yellow+vl
        for i in range(0,101):
         print (vl,': ',green,'(',i,'%)',white,sep='',end='\r')
         s(0.03)
        print (vl,green,': (',100,'%)',sep='')
        rc()
    def simple_load(string,wait,colors=False,load_char='█'):
      if colors==False:
        print (string,'--> [═',end='')
        for i in range (0,30):
            print (load_char,end='',flush=True)
            s(wait/100)
        print ('═]')
      elif colors==True:
        print (yellow,string,blue,' --> ',green,'[═',sep='',end='')
        for i in range (0,30):
            print (red,load_char,sep='',end='',flush=True)
            s(wait/100)
        print (green,'═]',white,sep='')
    def connect_2side(side1,side2,trys,fail=False,of='Failed'):
        for i in range (0,trys):
             print ('%s ├═                                         ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══                                        ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══                                       ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════                                      ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════                                     ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════                                    ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════                                   ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════                                  ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════                                 ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════                                ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════                               ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════                              ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════                             ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════                            ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════                           ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════                          ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════                         ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════                        ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════                       ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════                      ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════                     ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════                    ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════════                   ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════════                  ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════════                 ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════════                ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════════════               ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════════════              ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════════════             ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════════════            ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════════════════           ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════════════════          ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════════════════         ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════════════════        ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════════════════════       ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════════════════════      ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════════════════════     ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════════════════════    ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═══════════════════════════════════════   ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├════════════════════════════════════════  ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├═════════════════════════════════════════ ┤ %s'%(side1,side2),end='\r')
             s(0.03)
             print ('%s ├══════════════════════════════════════════┤ %s'%(side1,side2),end='\r')
             s(0.03)
        if fail == False:
           print ('%s ├══════════════════════════════════════════┤ %s'%(side1,side2),end='')
           print (green,'    %s                            '%of,white)
        else:
           print ('%s ├══════════════════════════════════════════┤ %s'%(side1,side2),end='')
           print (red,'    %s                            '%of,white)

    def transfer_load(attacker,victim,trys,fail=False):
        for i in range(0,trys):
            print (green,attacker,yellow,'>                                      ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'->                                     ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'-->                                    ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'--->                                   ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,' --->                                  ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'  --->                                 ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'   --->                                ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'    --->                               ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'     --->                              ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'      --->                             ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'       --->                            ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'        --->                           ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'         --->                          ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'          --->                         ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'           --->                        ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'            --->                       ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'             --->                      ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'              --->                     ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'               --->                    ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                --->                   ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                 --->                  ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                  --->                 ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                   --->                ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                    --->               ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                     --->              ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                      --->             ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                       --->            ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                        --->           ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                         --->          ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                          --->         ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                           --->        ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                            --->       ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                             --->      ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                              --->     ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                               --->    ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                --->   ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                 --->  ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                  ---> ',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                   --->',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                    ---',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                     --',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                      -',green,victim,white,end='\r',sep='')
            s(0.03)
            print (green,attacker,yellow,'                                       ',green,victim,white,end='\r',sep='')
        if fail == False:
            print (green,attacker,yellow,'                  100 % success               ',green,victim,white,sep='')
        else:
            print (green,attacker,yellow,'                  ',red,'Failed','                 ',green,victim,white,sep='')

    def color_load(l,t):
        for a in range(0,t):
          print (randc[random.randint(0,len(randc)-1)],l,end='\r',flush=True,sep='')
          s(0.05)

    def real_load(vl):
        b='%s%s%s |'%(yellow,vl,red)
        a=red+'|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|'
        print (yellow,b,a,end='\r',sep='')
        for i in range (0,len(a)-8):
            sp = [10,100,100,10,100,1000,10,10]
            timetosleep = random.randint(0,9)
            print (yellow,b,green,'█',sep='',flush=True,end='')
            s(timetosleep/sp[random.randint(0,len(sp)-1)])
            b=''
        print ('')
        rc()
    def exec_load(value,timee):
        for i in range (0,timee-1):
            print ('%s [-     ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [ -    ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [  -   ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [   -  ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [    - ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [     -]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [    - ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [   -  ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [  -   ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [ -    ]'%value,end='\r',sep='',flush=True)
            s(0.04)
            print ('%s [-     ]'%value,end='\r',sep='',flush=True)
            s(0.04)
        print ('%s [   Done    ]'%value)
    def apt_loader(value,timer):
        value1 = value+yellow+' ['
        print (yellow,value,' ',yellow,'[...................................................................................................................................]',end='\r',sep='')
        for i in range(0,len('....................................................................................................................................')-1):
            print (yellow,value1,green,'#',sep='',flush=True,end='')
            s(timer/100)
            value1=''
        print ('')
class typer:
       def write(data,speedlevel=4,nwait=True,colors=False):
         for i in data:
          if colors == False:
           print (i,flush=True,end='')
           s(speedlevel/100)
          else:
           print (randc[random.randint(0,len(randc)-1)],i,sep='',flush=True,end='')
           s(speedlevel/100)
         print ('')
         if nwait == False:
            b=0
         else:
            b=0.5
         s(b)
         rc()
       def hide(text,title='',speedlevel=4):
         text = text + ' '
         a=yellow+title+white
         print (a,text,end='\r')
         for i in text:
             print (a,'*',sep='',flush=True,end='')
             s(speedlevel/100)
             a=''
         print ('')
       def show(text,title='',speedlevel=4):
         txt = '*'*(len(text)-1)
         a=yellow+title+white
         print (a,txt,end='\r')
         for i in range(0,len(text)):
             print (a,text[i],sep='',flush=True,end='')
             s(speedlevel/100)
             a=''
         print ('')
       def line_mi(text,speedlevel=6):
         b=text+ ' '
         a=0
         text = text + ' '
         for i in text:
           a=a+1
           b=b.replace(b[-a],' ')
           print (b,end='\r',flush=True)
           s(speedlevel/100)
       def line_blink(text,re,speedlevel=50):
         text = text + ' '
         for i in range(0,re):
           print (' '*len(text),end='\r')
           s(speedlevel/100)
           print (text,end='\r')
           s(speedlevel/100)
         print (' '*len(text),end='\r')
class banner():
       def skull():
         sk ='''

                             __xxxxxxxxxxxxxxxx___.
                        _gxXXXXXXXXXXXXXXXXXXXXXXXX!x_
                   __x!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!x_
                ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx_
              ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!_
            _!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
          gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs
        ,!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
       g!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
      iXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
     ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
     !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi
  dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXf~~~VXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvvvvXXXXXXXXXXXXXX!
   !XXXXXXXXXXXXXXXf`       'XXXXXXXXXXXXXXXXXXXXXf`          '~XXXXXXXXXXP
    vXXXXXXXXXXXX!            !XXXXXXXXXXXXXXXXXX!              !XXXXXXXXX
     XXXXXXXXXXv`              'VXXXXXXXXXXXXXXX                !XXXXXXXX!
     !XXXXXXXXX.                 YXXXXXXXXXXXXX!                XXXXXXXXX
      XXXXXXXXX!                 ,XXXXXXXXXXXXXX                VXXXXXXX!
      'XXXXXXXX!                ,!XXXX ~~XXXXXXX               iXXXXXX~
       'XXXXXXXX               ,XXXXXX   XXXXXXXX!             xXXXXXX!
        !XXXXXXX!xxxxxxs______xXXXXXXX   'YXXXXXX!          ,xXXXXXXXX
         YXXXXXXXXXXXXXXXXXXXXXXXXXXX`    VXXXXXXX!s. __gxx!XXXXXXXXXP
          XXXXXXXXXXXXXXXXXXXXXXXXXX!      'XXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXP        'YXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXX!     i    !XXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXX!     XX   !XXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXx_   iXX_,_dXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXP
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
           ~vXvvvvXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                    'VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvv~
                      'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX~
                  _    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                 -XX!  !XXXXXXX~XXXXXXXXXXXXXXXXXXXXXX~   Xxi
                  YXX  '~ XXXXX XXXXXXXXXXXXXXXXXXXX`     iXX`
                  !XX!    !XXc` XXXXXXXXXXXXXXXXXXXX      !XX
                  !XXc    '~Vf  YXXXXXXXXXXXXXP YXXX     !XcX
                  !XXc  ,_      !XXP YXXXfXXXX!  XXc     XXXV
                  !XXV !XX           'XXP 'YXX!       ,.!XXV!
                  !XXXi!XP  XX.                  ,_  !XXXXXX!
                  iXXXx X!  XX! !Xx.  ,.     xs.,XXi !XXXXXXf
                   XXXXXXXXXXXXXXXXX! _!XXx  dXXXXXXX.iXXXXXX
                   VXXXXXXXXXXXXXXXXXXXXXXXxxXXXXXXXXXXXXXXX!
                   YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXV
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                       VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                         VXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                          ~vXXXXXXXXXXXXXXXXXXXXXXXf`
                              ~vXXXXXXXXXXXXXXXXv~
                                 '~VvXXXXXXXV~~
                                       ~~
'''
         return sk
       def smallskull():
           smk = '''
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /
         \.    ^    ./
           ^~~~^~~~^
'''
           return smk
       def detailed_skull():
          dsk='''
            ___           _,.---,---.,_
            |         ,;~'             '~;,
            |       ,;                     ;,
   Frontal  |      ;                         ; ,--- Supraorbital Foramen
    Bone    |     ,'                         /'
            |    ,;                        /' ;,
            |    ; ;      .           . <-'  ; |
            |__  | ;   ______       ______   ;<----- Coronal Suture
           ___   |  '/~"     ~" . "~     "~\'  |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 Maxilla,  |      |   |        }:{        | <------ Orbit
Nasal and  |      |   l       / | \       !   |
Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~.
  Bones    |      |    ----;' / | \ `;-<--------- Infraorbital Foramen
           |__     \__.       \/^\/       .__/
              ___   V| \                 / |V <--- Mastoid Process
              |      | |T~\___!___!___/~T| |
              |      | |`IIII_I_I_I_IIII'| |
     Mandible |      |  \,III I I I III,/  |
              |       \   `~~~~~~~~~~'    /
              |         \   .       . <-x---- Mental Foramen
              |__         \.    ^    ./
                            ^~~~^~~~^
'''
          return dsk
       def human_skull():
          hsk='''
                                  [/~~~~~~l'
                                [%};       `rl
                               Odq            O
                               B,             8i
                              vBc            x n
                             xB xn          xW W
                             xW wn '     '' xW xn
                             x$ nxBZB   x`B$x$ %n
                             xBO.xZJB   xOhB x Z.
                              x`  hZ "in `n   B
                              +B[/; '%n$1 ;l "0
                               `@$  0}.)0 "a$a
                                xB;(O''"[OU>@n
                                xWlw0dqqd8*]a,
                                 +W 000000 w,
                                  +@'    '0,
                                    'BB@B'
                                    OJi"UO.
                                   "`U``h`i
                                    B%$%$`i                              
                          ''"''~}))}~W  w0Ma~l'
                     '~~~C`}0)}~/((OO};])Ok*/z0~~~''"'"
                  ':(8'"'OOOOO'! f8B/~~(8fQQfOO/~88888#~''
                 "8Qf``8qd`#`W#BW'8#`.   80q#BBd,Ot`\``Z t8O
                wB0c B 0, B@' +0BBBBB   w0BB@W0 v BBW'Bc0B0 xW
               xW '+,B   wB 0Ww'  +0' +,x00, '0Bn'nB   w0    x
              xB  B  B  Bn'B'+cB0@BW0   +'BBBBBBB0wBn '@B    x
              xBi B"U`n %n`ZBh$OU```     ```."OOUB" $O ZBU. xZ
               hU.`xn hO`h hBBBBBBB$   . BBBBBB$%O.BxBOn Z. xn
               xJi Bn  B h`OO ```.OO      i""iO"OOUO.x`  xZ xn
               x!  n  +8c?0(8B$OOa}.      0@%$BBB0]8kW0  xW xn
               x!  n  "`zX'f8```8QO1     '1?````t'/8pd n xW xn
               x!  n  _OvM8\0~~~00}`'    `)rOOOO%B*0`>Oc xW xn
               x!  n  x`;CB#O1['1[  Bi "%O  \t`\t`>'O%0x xW +c
              xW   n  +B'    +000,wB'000@0W @BBBBBBBB,'n xW  x
              xW  ',   BwB0WBBW' xB0B@BB@0wW +00000 'w0B xW  x
              xW  B   x'+0B'BBB wB 'B' 'wB'w  BwW'BBcv B +c  x
              x$  B    Bi"  ``.O$%ZJB   xBh$B$ `h`Z`."B.  x` x
              x$  B    BhZ``B."B`.xBB%$$%Bi `hBi"OOBhZ`i  x` x
              UJ  B    BU`O%`xZ O%BB` ..xBBBOi`$iBBBU.On  x`  n
              W!  B    BhBB OZJOB};zB[11w8  )@Ovc Q`[%B   x8  n
              W!  0    0?)0"0$%0.  _B)}}h8    0Ww hOB}`n  x8  n
              W!   n    c''a BW    zB   x8    'BZO?`>[~.  w8  n
              W!   c     ``. )0    _B(//k8    0}.`MOa}   wB`  Ji
             'n xW xn             +cB,  x',              @n   +@'
             0BWwB'xn               BBBBB                Bn wB  B
              wBv@Bn     ''B0@W'   vBv,,x0    'B00@'     xB'xB'w0
             B. n"`    OZ` O   `n   B. "%`  xZ   `$ h$    xBi" x
            "B.x"U    "B."`     Ji%B`ZhhB`$ixn     `  B    Bi n B
            xO"UU.    %` J       h"U     `ix.        J`n   Bi n `i
           xW v,n     W z!      a}  O}))qB  Mi        O,    W!hn c
           a} n ,     W _!      n  "0    `l v,       [0     @W+M xn
           * O.x      h'_Q      ;l/] '  l' J,       xZ      xW xO+M
          x! B x       0%B'    'Oa$i'\. _8 x~l      U.       h xB x
         xB xBxB        +@'    Bn xW '  ' xB x     B         x  Bn n
         wBxW0xn          B    0W  +B     B,xB    x'          B,0n xn
        ', nx B,       ''vB     +@   c  w0'w,    B,B          @W Bn+@
       "`."JUOn       %`$%O O   Oi hOOUJOB`.    x  O$%`J      x$ hn  B
       x` xxnB       O.    " $UBZ`$i %ZhnOOOOOO%n "B`. xO      x`xn  Bi
      x$  xix        BJ`  O"Bn B   x`hnxZBn  x x$OB   O B       B%B   $i
      +M8 xlv       xB>` xB` W `r~}>OZ;]J'`)}. a}`%~  B 0       `/k  ''w
      :C8rCU.       +B+  x`  )M'  [a`.   01' 'O,  @'  0a         *kl[0W\
    [~W'0l'n         0i  +'    `rC}.      `)C0`   %0   n         Ja+q~0cO1
   O}O)@'wWc          $'  B                       B   ',         ;:C':kB`~
  w w BnBxWxn         x',  n                      B   B           xc 'nB@'xW
 wn'B W B wxn         xB,  n                     Bn   0           x0c0vc0 n+'
'cv'n0W B wxn         +B   c                     Bn  x            xxB nxn +c0n
O. `OBn B.x.           B$i x                    "B  xn            x h nOJ   `
    nBxZBZh            Bn  x                    xB  xn            $%BhnBx
    $BxnBnx             $U  B                   xO. n             nxBxnB%
    nBhZBJU             @Z~ 0                  xB~ ',             JUBhZBx
    *Bk*Bv,             x$~  n                 xW  B              +cBk*Bk
    cBxW0.               h'  Ji                %W  B                0wnBv
     `]`                 xB! xn               'B} "`                 `;`.
                          B   x               BB, x
                          0B  x               BB, x
                           B'  B             xB   n
                           hO  `i            x`   n
                           xO   Ji          xB`  B
                            B.  xn          xB`  B
                            B!   +          Br   0
                            `*    c        [,   x
                             $1   xn      xB    x
                            'B}'' +c      ac  ' +O
                            B x  x +B    B  v00   n
                            B +' xW B    B  W  n  n
                           +B  B wxW0    0n xn'n 'n
                             BZ``JBn      ``%n`JOB
                           "```BZ`xn     OZ`h$B`h
                           xOi"   Zh     `OO   %B
                           Z W\B"Uxn      xZn B w
                           n W!0v,xn      x*n Bv@
                           nOW! . xn      x*;C`nx
                           nB)M'  v,      x*  Ocw
                           nB x'  n       xB  BxB
                           c nx'  n       xB  BxB
                           x n B, n       xB x wB
                           x $iB. n       xZ x nx
                            OxnB. n       %Z x nx
                            BxnB. n       $i x nx
                            BxWB! n       *  hB w
                            `UhB! n       *  xBxZ
                             nxB! n       * "%Bxn
                             cvB! c       * xB`xn
                             xnB  xn     'B,xB xn
                             xnBn xn     B  xn B,
                             +c0B,+c     B  xn n
                              x Z. x     Bi xn n
                              xOZ.  B    Bi n B.
                               B    B    Bi n B
                               B     n  x8  MiB
                               B1'' ',  x8  wnB
                               `W\`;8   x8~~BnB
                               O0M1[Bn  xB''h$B
                               Bc'v, n  x'  BB
                               B +BBB   x xB  B
                             v,'cwwn0n  x BW   0c'
                           UB%ZBhZ J n x$ Z.hZBi"`$
                           `OJ% Bn x`n  x`nx`h`Zh`U
                            `.  n   O.   O. h$`hn`
                                    `    `
'''
          return hsk
       def pistol():
          pstl='''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(
 `------'
'''
          return pstl
       def halloween():
          hlwn='''
                            ;::;;::;,
                            ;::;;::;;,
                           ;;:::;;::;;,
           .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,
        vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv
      vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv
     vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv
    vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv
   vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,
  vnmmnv%vnmmmmmnv%vnmm;' mmmmmnv%vnmmmmmmm;' mmnv%vnmmmnv%vnmmmnv
  vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
 vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv
 vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv
 `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'
  vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;'   mmmnv%vnmmmmnv
   vnmmnv%vnmmmm;;,   nmmm;'              mmmm;;'    mmmnv%vnmmmmnv'
   `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'
    `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'
      `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'
          `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'
'''
          return hlwn
       def house():
          hous='''
    ) )        /\
   =====      /  \
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;
'''
          return hous
       def linux():
          lnx='''
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--'
'''
          return lnx
       def windows():
           windws='''
             _.-;;-._
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|
'''
           return windws
       def earth():
          erth='''
              _-o#&&*'"''?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""'"*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=
'''
          return erth
       def saturn():
          satrn='''
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;
'''
          return satrn
       def truck():
          trck='''
       _.--,_......----..__
       \  .'          '    ```--...__      \
        \;           '            .  '.   ||
        :           '            '     \ .''.
      .';          :            '       .|  |.--..___
     /   \         |           :        :|  /.------.\
    /    .'._      :           |        ||  ||      |\\
   /.-. /|-| `-.               :        ;|  ||______|_\`.______
  //  // |-|    \   '           '      / |  ||='      | |      `.
 //  //\\|-|     `-._'           '   .'  |  ||        | |        \
/.-.//  \\-|_________```------------` ___'. ||        | '_.--.   <)
'._.'  /  .-----.   .-----.   .''"'"'"'.    |'--..____| /  _  \   |
       |_/.'   '.\_/.'   '.\_[ [ [  ] ] ]___|_________.'.'   '.\  ]
         :  .-.  : :  .-.  :  '........'    (_________):  .-.  :`-'
         :  '-'  : :  '-'  :                           :  '-'  :
          '._ _.'   '._ _.'                             '._ _.'
'''
          return trck
       def airplane():
          arpln='''
            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                     =  ===(_________D
'''
          return arpln
       def camera():
          camr='''
            ___
           / _ \
          | / \ |
          | \_/ |
           \___/ ___
           _|_|_/[_]\__==_
          [---------------]
          | O   /---\     |
          |    |     |    |
          |     \___/     |
          [---------------]
                [___]
                 | |\\
                 | | \\
                 [ ]  \\_
                /|_|\  ( \
               //| |\\  \ \
              // | | \\  \ \
             //  |_|  \\  \_\
            //   | |   \\
           //\   | |   /\\
          //  \  | |  /  \\
         //    \ | | /    \\
        //      \|_|/      \\
       //        [_]        \\
      //          H          \\
     //           H           \\
    //            H            \\
   //             H             \\
  //              H              \\
 //                               \\
//                                 \\
'''
          return camr
       def robot():
          rbt='''
           ___
          |_|_|
          |_|_|              _____
          |_|_|     ____    |*_*_*|
 _______   _\__\___/ __ \____|_|_   _______
/ ____  |=|      \  <_+>  /      |=|  ____ \
~|    |\|=|======\\______//======|=|/|    |~
 |_   |    \      |      |      /    |    |
  \==-|     \     |  2D  |     /     |----|~~/
  |   |      |    |      |    |      |____/~/
  |   |       \____\____/____/      /    / /
  |   |         {----------}       /____/ /
  |___|        /~~~~~~~~~~~~\     |_/~|_|/
   \_/        |/~~~~~||~~~~~\|     /__|\
   | |         |    ||||    |     (/|| \)
   | |        /     |  |     \       \\
   |_|        |     |  |     |
              |_____|  |_____|
              (_____)  (_____)
              |     |  |     |
              |     |  |     |
              |/~~~\|  |/~~~\|
              /|___|\  /|___|\
             <_______><_______>
'''
          return rbt
       def clock():
          clok='''
        _____
     _.'_____`._
   .'.-'  12 `-.`.
  /,' 11      1 `.\
 // 10      /   2 \\
;;         /       ::
|| 9  ----O      3 ||
::                 ;;
 \\ 8           4 //
  \`. 7       5 ,'/
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
   '--'       '--'
'''
          return clok
       def lamp():
          lmp='''
    _.-"```"-._
  .'           '.
 /      .-.      \
;       | |       ;
|       | |       |
;       \_/       ;
 \      (_)      /
  '.           .'
    `;_______;`
     |_..--"`)
     (_..--'`|
     |_..--'`)
     (_..--'_|
      `-...'
'''
          return lmp
       def radio():
          rdio='''
             .==============.
   __________||_/########\_||__________
  |(O)____ : [FM 103.7] ooooo : ____(O)|
  |  /::::\:  _________  +|+  :/::::\  |
  |  \;;;;/: |    |    | |+|  :\;;;;/  |
  |________:_ooooo+==ooo______:________|
'''
          return rdio
       def phone():
          phn='''
              _              _
             | |------------| |
          .-'| |            | |`-.
        .'   | |            | |   `.
     .-'      \ \          / /      `-.
   .'        _.| |--------| |._        `.
  /    -.  .'  | |        | |  `.  .-    \
 /       `(    | |________| |    )'       \
|          \  .i------------i.  /          |
|        .-')/                \(`-.        |
\    _.-'.-'/     ________     \`-.`-._    /
 \.-'_.-'  /   .-' ______ `-.   \  `-._`-./\
  `-'     /  .' .-' _   _`-. `.  \     `-' \\
         | .' .' _ (3) (2) _`. `. |        //
        / /  /  (4)  ___  (1)_\  \ \       \\
        | | |  _   ,'   `.==' `| | |       //
        | | | (5)  | B.T.| (O) | | |      //
        | | |   _  `.___.' _   | | |      \\
        | \  \ (6)  _   _ (9) /  / |      //
        /  `. `.   (7) (8)  .' .'  \      \\
       /     `. `-.______.-' .'     \     //
      /        `-.________.-'        \ __//
     |                                |--'
     |================================|hjw
     "--------------------------------"
'''
          return phn
       def calculator():
          clclt='''
 _____________________
|  _________________  |
| |1+1              | |
| |________________2| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
          return clclt
       def bodybuilder():
          bdbl='''
                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \  =  /
                 |\___/|
        ___ ____/:     :\____ ___
      .'   `.-===-\   /-===-.`   '.
     /      .-""'""-.-""'""-.      \
    /'             =:=             '\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   ".     --:--     ."   \_. '\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \
 /... .|      |    |      |      |. ...\
|::::/''     /     |       \     ''\::::|
'"'""       /'    .L_      `\       "'""'
           /'-.,__/` `\__..-'\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___)
           |==|
           \__/
'''
          return bdbl
       def sword():
          swrd='''
 __-----_________________{]__________________________________________________
{&&&&&&&#%%&#%&%&%&%&%#%&|]__________________________________________________\
'''
          return swrd
       def shield():
          shld='''
   |\                     /)
 /\_\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
           //`:::`\\
          //   '   \\
         |/         \\
'''
          return shld
       def arrow():
          arww='''
           ]z
           `@@_
            @@@L
      .d@L,]@@@@L,
-z__   ]@@@a@@@@@@_
 `@@@@zza@@@@@@@@@@L
  `]@@@@@@@@@@@@@@@@@_
    `@@@@@@@@@@@@@@@@@L
     `-@@@@@@@@@@@@@@@@'
       `@@@@@@@@@@@@@@[
        `@@@@@@@@@@@@@[
          ]@@@@@@@@@@@[
           "~~~~-@@@@@@,
                  "~-@@@_
                     ~@@@L
                      `@@@L_
                       `~@@@L
                         `@@@z,
                          `]@@@_
                            `@@@z
                             `]@@L_
                               ~@@@z
                                `@@@z,
                                 `]@@@L
                                   `@@@z
                                     ]@@L,
                                      ~@@@z
                                       "@@@z
                                        `-@@@_
                                          ~@@@_
                                           `@@@z
                                            `-@@@_
                                              ]@@@_
                                               "@@@z
                                                `]@@L,
                                                  `@@@L
                                                   `@@@z,
                                                    `-@@@_
                                                      `@@@L
                                                       `@@@L    ]e
                                                         ~@@b_  a@b
                                                          `@@@e]@@L
                                                    -zzzz___@@@U@@@,
                                                      "~-@@@@@@@@@@@
                                                         `~-@@@@@@@@L
                                                            "~-@@@@@@,
                                                               "~@@@@L
                                                                 `~@@@e
                                                                    ~@@_
                                                                      ~@
'''
          return arww
       def bow():
          bww='''


          4$$-.
           4   ".
           4    ^.                                       
           4     $                                       
           4     'b                                      
           4      "b.                                    
           4        $                                    
           4        $r                                   
           4        $F                                   
-$b========4========$b====*P=-                           
           4       *$$F                                  
           4        $$"                                  
           4       .$F                                   
           4       dP                                    
           4      F                                      
           4     @                                       
           4    .                                        
           J.                                            
          '$$
'''
          return bww
       def bomb():
          bmb='''
                 .               
                 .               
                 .       :       
                 :      .        
        :..   :  : :  .          
           ..  ; :: .            
              ... .. :..         
             ::: :...            
         ::.:.:...;; .....       
      :..     .;.. :;     ..     
            . :. .  ;.           
             .: ;;: ;.           
            :; .BRRRV;           
               YB BMMMBR         
              ;BVIMMMMMt         
        .=YRBBBMMMMMMMB          
      =RMMMMMMMMMMMMMM;          
    ;BMMR=VMMMMMMMMMMMV.         
   tMMR::VMMMMMMMMMMMMMB:        
  tMMt ;BMMMMMMMMMMMMMMMB.       
 ;MMY ;MMMMMMMMMMMMMMMMMMV       
 XMB .BMMMMMMMMMMMMMMMMMMM:      
 BMI +MMMMMMMMMMMMMMMMMMMMi      
.MM= XMMMMMMMMMMMMMMMMMMMMY      
 BMt YMMMMMMMMMMMMMMMMMMMMi      
 VMB +MMMMMMMMMMMMMMMMMMMM:      
 ;MM+ BMMMMMMMMMMMMMMMMMMR       
  tMBVBMMMMMMMMMMMMMMMMMB.       
   tMMMMMMMMMMMMMMMMMMMB:        
    ;BMMMMMMMMMMMMMMMMY          
      +BMMMMMMMMMMMBY:           
        :+YRBBBRVt;
'''
          return bmb
       def shotgun():
          stgn='''
,________________________________
|__________,----------._ [____]  ""-,__  __...-----==="
        (_(||||||||||||)___________/   ""             |
           `----------'        [ ))"-,                |
                                ""    `,  _,--...___  |
                                        `/          "'"
'''
          return stgn
       def assault_rifle():
          srar='''
                           ______
        |\_______________ (_____\\______________
HH======#H###############H#######################
        ' ~"'"'""'"'""'""`##(_))#H\"'"'"Y########
                          ))    \#H\       `"Y###
                          "      }#H)
'''
          return srar
       def man():
          mann='''
       .---.
      /_____\
      ( '.' )
       \_-_/_
    .-"`'V'//-.
   / ,   |// , \
  / /|Ll //Ll|\ \
 / / |__//   | \_\
 \ \/---|[]==| / /
  \/\__/ |   \/\/
   |/_   | Ll_\|
     |`^"'"^`|
     |   |   |
     |   |   |
     |   |   |
     |   |   |
     L___l___J
      |_ | _|
     (___|___)
'''
          return mann
       def axe():
          axee='''
                                           _.gd8888888bp._
                                        .g88888888888888888p.
                                      .d8888P""       ""Y8888b.
                                      "Y8P"               "Y8P'
                                         `.               ,'
                                           \     .-.     /
                                            \   (___)   /
 .------------------._______________________:__________j
/                   |                      |           |`-.,_
\###################|######################|###########|,-'`
 `------------------'                       :    ___   l
                                            /   (   )   \
                                   fsc     /     `-'     \
                                         ,'               `.
                                      .d8b.               .d8b.
                                      "Y8888p..       ,.d8888P"
                                        "Y88888888888888888P"
                                           ""YY8888888PP""
'''
          return axee
       def knive():
          knvs='''
                                                       ___
                                                      |_  |
                                                        | |
__                      ____                            | |
\ ````'"''----....____.'\   ````''"'--------------------| |--.               _____      .-.
 :.                      `-._                           | |   `''-----'"'```     ``''"|`: :|
  '::.                       `'--.._____________________| |                           | : :|
    '::..       ----....._______________________________| |                           | : :|
      `'-::...__________________________________________| |   .-''-..-'`-..-'`-..-''-.| : :|
           ```'"'---------------------------------------| |--'                         `'-'
                                                        | |
                                                       _| |
                                                      |___|
'''
          return knvs


class help:
     #print ('help.help() to get the full help\nhelp.loaderhelp() to get the loaders help\nhelp.typerhelp() to get the printer help\nhelp.bannerhelp() to get banners help')
     def help():
        valala = '''
this library contain 4 classes, with 45 functions: our insta to chat @python_style

loader
typer
banner
help

lets begin:

the loader class, is used to help you create a loading bar, with 
one line only, or a loading screen, How to use it: (It contain 10 different 
oaders) our insta @python_styles
_____________________________________________________________________

1- ra_load(valueTOload,repeat)  $see our page on insta to learn how it work

2- eq_load(valueTOload,repear)  $see our page on insta to learn how it work

3- percent_load(value) a percent loading (1%,2%,3%....),you can add colors by 
setting colors to True percent_load(value,colors=True)

4- simple_load(value,timeToFinish)   a simple loaders, you can add colors by 
setting colors to True, simple_load(value,timeToFinish,colors=True) and
 change the loading character by changing the loadchar 
simple_load(value,timeToFinish,loadchar='-') (example)

5- connect_2side(side1,side2,OnFailMessage,timeToFinish,Fail=False) 
$see our page on insta to learn how it work

6- transfer_load(side1,side2,TimeToFinish,fail=False)
$see our page on insta to learn how it work

7- color_load(value,repeat) $see our page on insta to learn how it work

8- real_load(vl) it will load like the real loading bar, in hackers movie and more
$see our page on insta to learn how it work

9- exec_load(value,repeat), will make any line like executing it now or scanning 
it now $see our page on insta to learn how it work

10- apt_loader(value,timer) like the apt install loading bar 
___________________________________________________________________________
the typer class, is used to print your line, value, or returned value
from any function, with a different look, using 5 different type,
how to use it: (Using speedlevel in millisecond (1 speedlevel = 0.01 second))

1- write(textOrValue,speedlevel=4,WaitBeforeWritingNewLine=True,colors=False)
   $see our page on insta to learn how it work
2- hide(text, title='',speedlevel=4) title is used to print a value
before hidding your text, $see our page on insta to learn how it work

3- show (textOrValue,title='',speedlevel=4) like the hide() function, but this
one will show a value (example:  **** will be turned to hello)

4- line_mi(text,speedlevel=6) disapear a line $see our page on insta to learn how it work

5-line_blink(text,repetition,speedlevel=50) blinking a text
________________________________________________________________________________
the banner class, contain 31 best banners for creating a tool,framework,script
and more... banners nameFunctiong ():

skull()
smallskull()
detailed_skull()
human_kull()
pistol()
halloween()
house()
linux()
windows()
earth()
saturn()
truck()
airplane()
camera()
robot()
clock()
lamp()
radio()
phone()
calculator()
bodybuilder()
sword()
shield()
arrow()
bow()
bomb()
shotgun()
assault_rifle()
man()
axe()
knive()

this is the banners, to use one you need to create your variable, and:
banner = banner.knive()
print (banner)
with two line only print the knive :)
$see our page on insta to learn how it work
'''
        print (valala)
     def loaderhelp():
        voul='''
the loader class, is used to help you create a loading bar, with 
one line only, or a loading screen, How to use it: (It contain 10 different 
oaders) our insta @python_styles
_____________________________________________________________________

1- ra_load(valueTOload,repeat)  $see our page on insta to learn how it work

2- eq_load(valueTOload,repear)  $see our page on insta to learn how it work

3- percent_load(value) a percent loading (1%,2%,3%....),you can add colors by 
setting colors to True percent_load(value,colors=True)

4- simple_load(value,timeToFinish)   a simple loaders, you can add colors by 
setting colors to True, simple_load(value,timeToFinish,colors=True) and
 change the loading character by changing the loadchar 
simple_load(value,timeToFinish,loadchar='-') (example)

5- connect_2side(side1,side2,OnFailMessage,timeToFinish,Fail=False) 
$see our page on insta to learn how it work

6- transfer_load(side1,side2,TimeToFinish,fail=False)
$see our page on insta to learn how it work

7- color_load(value,repeat) $see our page on insta to learn how it work

8- real_load(vl) it will load like the real loading bar, in hackers movie and more
$see our page on insta to learn how it work

9- exec_load(value,repeat), will make any line like executing it now or scanning 
it now $see our page on insta to learn how it work

10- apt_loader(value,timer) like the apt install loading bar 
___________________________________________________________________________
'''
        print (voul)
     def typerhelp():
        vail='''
___________________________________________________________________________
the typer class, is used to print your line, value, or returned value
from any function, with a different look, using 5 different type,
how to use it: (Using speedlevel in millisecond (1 speedlevel = 0.01 second))

1- write(textOrValue,speedlevel=4,WaitBeforeWritingNewLine=True,colors=False)
   $see our page on insta to learn how it work
2- hide(text, title='',speedlevel=4) title is used to print a value
before hidding your text, $see our page on insta to learn how it work

3- show (textOrValue,title='',speedlevel=4) like the hide() function, but this
one will show a value (example:  **** will be turned to hello)

4- line_mi(text,speedlevel=6) disapear a line $see our page on insta to learn how it work

5-line_blink(text,repetition,speedlevel=50) blinking a text
________________________________________________________________________________
'''
        print (vail)
     def bannerhelp():
        vban ='''
________________________________________________________________________________
the banner class, contain 31 best banners for creating a tool,framework,script
and more... banners nameFunctiong ():

skull()
smallskull()
detailed_skull()
human_kull()
pistol()
halloween()
house()
linux()
windows()
earth()
saturn()
truck()
airplane()
camera()
robot()
clock()
lamp()
radio()
phone()
calculator()
bodybuilder()
sword()
shield()
arrow()
bow()
bomb()
shotgun()
assault_rifle()
man()
axe()
knive()

this is the banners, to use one you need to create your variable, and:
banner = banner.knive()
print (banner)
with two line only print the knive :)
$see our page on insta to learn how it work
'''
        print (vban)
