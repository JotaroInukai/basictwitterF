from django.shortcuts import render
from basicF.datas import *

import random
import functools
def sagilist():
    S1=A1()
    S2=A2()
    S3=A3()
    S4=A4()
    S5=A5()
    S6=A6()
    S7=A7()
    S8=A8()
    S9=A9()
    S10=A10()
    S21=A21()
    S22=A22()
    S23=A23()
    S24=A24()
    S25=A25()
    S11=A11()
    S12=A12()
    S13=A13()
    S14=A14()
    S15=A15()
    S16=A16()
    S17=A17()
    S18=A18()
    S19=A19()
    S20=A20()
    S26=A26()
    S27=A27()
    S28=A28()
    S29=A29()
    S30=A30()
    sagidict={"S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5,"S6":S6,"S7":S7,"S8":S8,"S9":S9,"S10":S10,"S21":S21,"S22":S22,"S23":S23,"S24":S24,"S25":S25}
    return sagidict
    
def hisagilist():   
    S1=A1()
    S2=A2()
    S3=A3()
    S4=A4()
    S5=A5()
    S6=A6()
    S7=A7()
    S8=A8()
    S9=A9()
    S10=A10()
    S21=A21()
    S22=A22()
    S23=A23()
    S24=A24()
    S25=A25()
    S11=A11()
    S12=A12()
    S13=A13()
    S14=A14()
    S15=A15()
    S16=A16()
    S17=A17()
    S18=A18()
    S19=A19()
    S20=A20()
    S26=A26()
    S27=A27()
    S28=A28()
    S29=A29()
    S30=A30()
    
    
    hisagidict={"S11":S11,"S12":S12,"S13":S13,"S14":S14,"S15":S15,"S16":S16,"S17":S17,"S18":S18,"S19":S19,"S20":S20,"S26":S26,"S27":S27,"S28":S28,"S29":S29,"S30":S30}
    return hisagidict
# Create your views here.

def basicF_template(request):
    return render(request,"basicF.html")


def basicF_form_show(request):
    return render(request,"basicFresult.html")

def basicF_form_show2(request):
    return render(request,"basicFresult2.html")


def basicF_form_show3(request):
    return render(request,"basicFresult3.html")

def basicF_form_show4(request):
    return render(request,"basicFresult4.html")

def basicF_form(request):
   
    sagidict=sagilist()
    hisagidict=hisagilist()
    data=request.POST.get("hidden_data")
    
    splitdata=(data.split(","))
    
    map_object = map(int, splitdata)
    listofint=list(map_object)
   
    a="S"+str(listofint[0])
    b="S"+str(listofint[1])
    c="S"+str(listofint[2])
    d="S"+str(listofint[3])
    e="S"+str(listofint[4])
    f="S"+str(listofint[5])
    g="S"+str(listofint[6])
    h="S"+str(listofint[7])
    i="S"+str(listofint[8])
    j="S"+str(listofint[9])
    def1acountlist=[a,b,c,d,e,f,g,h,i,j]
    for x in def1acountlist:
        try:
            del sagidict[x]
        except KeyError:
            pass
    for y in def1acountlist:
        try:
            del hisagidict[y]
        except KeyError:
            pass
    
    def2sagilist=list(sagidict.keys())
    def2hisagilist=list(hisagidict.keys())
    random.shuffle(def2sagilist)
    random.shuffle(def2hisagilist)

    S1=sagidict[def2sagilist[0]]
    S2=sagidict[def2sagilist[1]]
    S3=sagidict[def2sagilist[2]]
    S4=sagidict[def2sagilist[3]]
    S5=sagidict[def2sagilist[4]]
    S11=hisagidict[def2hisagilist[0]]
    S12=hisagidict[def2hisagilist[1]]
    S13=hisagidict[def2hisagilist[2]]
    S14=hisagidict[def2hisagilist[3]]
    S15=hisagidict[def2hisagilist[4]]
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)




    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]

    

    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        "def1list":data,
        }


    return render(request,'basicFresult.html',payload)


def basicF_form2(request):
    sagidict=sagilist()
    hisagidict=hisagilist()
    data=request.POST.get("hidden_data")
    
    splitdata=(data.split(","))
    
    map_object = map(int, splitdata)
    listofint=list(map_object)
    a="S"+str(listofint[0])
    b="S"+str(listofint[1])
    c="S"+str(listofint[2])
    d="S"+str(listofint[3])
    e="S"+str(listofint[4])
    f="S"+str(listofint[5])
    g="S"+str(listofint[6])
    h="S"+str(listofint[7])
    i="S"+str(listofint[8])
    j="S"+str(listofint[9])
    k="S"+str(listofint[10])
    l="S"+str(listofint[11])
    m="S"+str(listofint[12])
    n="S"+str(listofint[13])
    o="S"+str(listofint[14])
    p="S"+str(listofint[15])
    q="S"+str(listofint[16])
    r="S"+str(listofint[17])
    s="S"+str(listofint[18])
    t="S"+str(listofint[19])
    def2acountlist=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
 
    for x in def2acountlist:
        try:
            del sagidict[x]
        except KeyError:
            pass
    for y in def2acountlist:
        try:
            del hisagidict[y]
        except KeyError:
            pass
   
    def3sagilist=list(sagidict.keys())
    def3hisagilist=list(hisagidict.keys())
    S1=sagidict[def3sagilist[0]]
    S2=sagidict[def3sagilist[1]]
    S3=sagidict[def3sagilist[2]]
    S4=sagidict[def3sagilist[3]]
    S5=sagidict[def3sagilist[4]]
    S11=hisagidict[def3hisagilist[0]]
    S12=hisagidict[def3hisagilist[1]]
    S13=hisagidict[def3hisagilist[2]]
    S14=hisagidict[def3hisagilist[3]]
    S15=hisagidict[def3hisagilist[4]]
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)



    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]
    


    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }


    return render(request,'basicFresult2.html',payload)

def basicF_form4(request):
    sagilistA=sagilist()
    hisagilistA=hisagilist()
    def1sagilist=list(sagilistA.keys())
    def1hisagilist=list(hisagilistA.keys())
    random.shuffle(def1sagilist)
    random.shuffle(def1hisagilist)
    S1=sagilistA[def1sagilist[0]]
    S2=sagilistA[def1sagilist[1]]
    S3=sagilistA[def1sagilist[2]]
    S4=sagilistA[def1sagilist[3]]
    S5=sagilistA[def1sagilist[4]]
    S11=hisagilistA[def1hisagilist[0]]
    S12=hisagilistA[def1hisagilist[1]]
    S13=hisagilistA[def1hisagilist[2]]
    S14=hisagilistA[def1hisagilist[3]]
    S15=hisagilistA[def1hisagilist[4]]
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)
    


    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,

        }

    return render(request,'basicFresult4.html',payload)


