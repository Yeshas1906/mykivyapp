from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,BooleanProperty

class screenlay(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def textinputted(self,x):
        self.print_theval(x)
    is_disabled=BooleanProperty(False)
    brac=StringProperty('(')
    textout=StringProperty()
    secre1=[]
    m1=0
    col=0

    def forclear(self):
        self.textout=str('')
        self.is_disabled=False
        self.brac=str('(')
        self.textout=''
        self.secre1=[]
        self.m1=0
        self.n1=0

    def print_theval(self,y):
        y=str(y)
        global is_disabled
        stnum=''
        secre=[]
        apnum=0
        a=['0','1','2','3','4','5','6','7','8','9']
        l=len(y)
        m=self.m1
        for i in range(l):
            count=0
            for j in a:
                if y[i]==j:
                    count=1
                    m=0
                else:
                    count+=0
            if y[i]=='(':
                m=0
            if m<1:
                if count>0:
                    stnum+=y[i]
                    m=0
                elif i==0:
                    if y[0]=='-':
                        secre.append(0)
                        secre.append('-')
                        m+=1
                    if y[0]=='+':
                        secre.append(0)
                        secre.append('+')
                        m+=1
                    elif y[0]=='x' or y[0]=='/':
                        self.is_disabled=True
                    elif y[0]=='(':
                        secre.append('(')
                    elif y[0]=='=':
                        if secre==[]:
                            self.textout='0'
                        else:
                            self.calculation()
                elif y[i]=='(':
                    print(stnum)
                    secre.append('(')
                elif stnum!='':
                    apnum=int(stnum)
                    secre.append(apnum)
                    stnum=''
                    if y[i]!='(' and y[i]!=')':
                        secre.append(y[i])
                        m+=1
                        if y[i]=='=':
                            self.secre1=secre
                            self.calculation()
                    elif y[i]==')':
                        secre.append(')')
                else:
                    if y[i-1]=='(' and (y[i]=='-' or y[i]=='+'):
                        secre.append(0)
                        secre.append(y[i])
                        m+=1
                    if y[i-1]=='(' and y[i]=='x':
                        secre.append(1)
                        secre.append(y[i])
                        m+=1
                    elif y[i]==')':
                        secre.append(y[i])
                    elif y[i]=='=':
                        secre.append(y[i])
                        self.secre1=secre
                        self.calculation()
                    else:
                        secre.append(y[i])
                        m+=1
            else:
                self.is_disabled=True
            
    def cursorloc(self,value):
        self.col,row=value

    def backspace(self):
        y=self.textout
        l=len(y)
        k=''
        if l==self.col:
            for i in range(l-1):
                k+=y[i]
        else:
            for i in range(self.col-1):
                k+=y[i]
            for i in range(self.col-1,l-1):
                k+=y[i+1]
        self.textout=k
        self.is_disabled=False

    def textbedisplay(self,x):
        self.textout+=x

    def calculation(self):
        x=self.secre1
        l=len(x)
        n=0
        x.pop(l-1)
        dot=0
        dop=0
        for i in x:
            if i=='(':
                n+=1
            elif i==')':
                n-=1
            elif i=='.':
                dot+=1
        if n==0:
            for j in range(dot):
                for i in range(dop+1,l):
                    if x[i]=='.':
                        dop=i
                        break
                t=float(str(x[dop-1])+'.'+str(x[dop+1]))
                x[dop-1]=t
                x.pop(dop)
                x.pop(dop)
            l=len(x)
            for i in range(l):
                initial=0
                final=l-1
                for j in range(l):
                    if x[j]=='(':
                        initial=j
                    if x[j]==')':
                        final=j
                        break
                for m in range(initial,final):
                    mulpos=initial
                    for q in range(initial,final):
                        if x[q]=='/':
                            mulpos=q
                            break
                    if mulpos>initial:
                        t=x[mulpos-1]/x[mulpos+1]
                        x[mulpos-1]=t
                        x.pop(mulpos)
                        x.pop(mulpos)
                        l=len(x)
                        final=final-2
                    mulpos=initial
                    for q in range(initial,final):
                        if x[q]=='x':
                            mulpos=q
                            break
                    if mulpos>initial:
                        t=x[mulpos-1]*x[mulpos+1]
                        x[mulpos-1]=t
                        x.pop(mulpos)
                        x.pop(mulpos)
                        l=len(x)
                        final=final-2
                    mulpos=initial
                    for q in range(initial,final):
                        if x[q]=='+':
                            mulpos=q
                            break
                    if mulpos>initial:
                        t=x[mulpos-1]+x[mulpos+1]
                        x[mulpos-1]=t
                        x.pop(mulpos)
                        x.pop(mulpos)
                        l=len(x)
                        final=final-2
                    mulpos=initial
                    for q in range(initial,final):
                        if x[q]=='-':
                            mulpos=q
                            break
                    if mulpos>initial:
                        t=x[mulpos-1]-x[mulpos+1]
                        x[mulpos-1]=t
                        x.pop(mulpos)
                        x.pop(mulpos)
                        l=len(x)
                        final=final-2            
                if(x[initial]=='('):
                    x.pop(initial)
                    x.pop(initial+1)
                l=len(x)
            if l>1:
                prod=1
                for numer in range(l):
                    prod*=x[numer]
                self.textout=str(round(prod,2))
            else:
                self.textout=str(round(x[0],2))
        else:
            self.textout="invalid format"

class comcalci1App(App):
    pass

comcalci1App().run()