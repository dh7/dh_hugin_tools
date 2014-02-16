#!/usr/bin/pyhton

row = 5
colums = 8

print "run the script"
myfile = open('test.txt','w')

for y in range(1,row-1):
    for x in range(0,colums):
        if ((y == 1) and (x == 0)):
            myfile.write("""
#-hugin  cropFactor=1
i w1280 h720 f3 v101.9 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0"""
            + " p"+ str(y*-27 + 54)
            + " y" + str(x*45) + " TrX0 TrY0 TrZ0 j0 a0 b-0.022 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5"
            + """ n"img-b-""" +str(y) + "-" +str (x) +'.jpg"')
        else:
            myfile.write("""
#-hugin  cropFactor=0.87
i w1280 h720 f3 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev=0 Er=0 Eb=0 r0"""
            + " p"+ str(y*-27 + 54)
            + " y" + str(x*45) + " TrX0 TrY0 TrZ0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5"
            + """ n"img-b-"""  +str(y) + "-" +str (x) +'.jpg"')
myfile.close()

