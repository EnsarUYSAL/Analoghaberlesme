import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft
from scipy.fftpack import fftshift
def AM(Vm,fm,Vc,fc):
    pi=math.pi
    prc=500
                        
    t=np.linspace(0,1,prc) 
    f=np.linspace((-prc/2),(+prc/2),prc)
    mt=np.zeros(prc)
    ct=np.zeros(prc)
    vam=np.zeros(prc)
    a=np.zeros(prc)

    for i in range(prc):
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for j in range(prc):
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc):
        vam[k]=(Vc+mt[k])*(math.cos(2*pi*fc*t[k]))

    a=fft(vam)
    b=fftshift(a)
    c=abs(b)

    plt.subplot(211)
    plt.title('Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vam)
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)
    plt.grid
    plt.show()
def DSBAM(Vm,fm,Vc,fc):
    pi=math.pi
    prc=500
                        
    t=np.linspace(0,1,prc) 
    f=np.linspace((-prc/2),(+prc/2),prc)
    mt=np.zeros(prc)
    ct=np.zeros(prc)
    vam=np.zeros(prc)
    a=np.zeros(prc)

    for i in range(prc):
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for j in range(prc):
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc):
        vam[k]=ct[k]*mt[k]

    a=fft(vam)
    b=fftshift(a)
    c=abs(b)

    plt.subplot(211)
    plt.title('Taşıyıcı bastırılımış Çift Yan Band Genlik Mod.')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vam)
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)
    plt.grid
    plt.show()  
def SSBUAM(Vm,fm,Vc,fc):
    pi=math.pi
    prc=500
                       
    t=np.linspace(0,1,prc) 
    f=np.linspace((-prc/2),(+prc/2),prc)
    mt=np.zeros(prc)
    mts=np.zeros(prc)
    ct=np.zeros(prc)
    vssb=np.zeros(prc)
    a=np.zeros(prc)

    for i in range(prc):
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for im in range(prc):
        mts[im]=Vm*(math.sin(2*pi*fm*t[im]))

    for j in range(prc):
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc):
        vssb[k]=(Vc*mt[k]*math.cos(2*pi*fc*t[k]))-(Vc*mts[k]*math.sin(2*pi*fc*t[k]))

    a=fft(vssb)
    b=fftshift(a)
    c=abs(b)

    plt.subplot(211)
    plt.title('Tek yan band (üst) Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vssb)
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)
    plt.grid
    plt.show()
def SSBDAM(Vm,fm,Vc,fc):
    pi=math.pi
    prc=500

                        
    t=np.linspace(0,1,prc) 
    f=np.linspace((-prc/2),(+prc/2),prc)
    mt=np.zeros(prc)
    mts=np.zeros(prc)
    ct=np.zeros(prc)
    vssb=np.zeros(prc)
    a=np.zeros(prc)

    for i in range(prc):
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for im in range(prc):
        mts[im]=Vm*(math.sin(2*pi*fm*t[im]))

    for j in range(prc):
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc):
        vssb[k]=(Vc*mt[k]*math.cos(2*pi*fc*t[k]))+(Vc*mts[k]*math.sin(2*pi*fc*t[k]))

    a=fft(vssb)
    b=fftshift(a)
    c=abs(b)

    plt.subplot(211)
    plt.title('Tek yan band (alt) Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vssb)
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)
    plt.grid
    plt.show()
