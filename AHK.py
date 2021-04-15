import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft
from scipy.fftpack import fftshift
def hab_nedir():
    print("Haberlesme, bilginin kaynaktan herhangi bir sekille (veya bicimde) ")
    print("baska bir noktaya aliciya ulastirilmasidir")
def hab_tarihcesi(): 
    print("Haberleşmenin tarihçesi:")
    print("Telgrafın keşfi(1844) ==> Telefonun icadı(1875) ==> Uzun mesafeli radyo yayını(1901) ==> İlk uydunu fırlatılması(1955) ==> İlk cep telefonu(1983) ")
def hab_turleri():
    print("Haberleşme türleri 2'ye ayrılır                  ")
    print("         1.ORTAM TÜRÜNE GÖRE                     ")
    print(" Kablolu                       Kablosuz          ")
    print("-Bakır fiberoptik kablo      - Elektromanyetik   ")
    print("-Elektrik veya optik         dalgalar yoluyla    ")
    print("sinyaller aracılığıyla                           ")
    print("                                                 ")
    print("         2.İŞARET TÜRÜNE GÖRE                                       ")
    print(" Analog                          Sayısal                            ")
    print("-İşaretin herhangi bir          -İşaretler kodlara                  ")
    print("kodlama olmadan elektrik        dönüştürüldükten sonra iletilir     ")
    print("sinyaline dönüşmesi                                                 ")
    print("ile elde edilir                                                     ")
def hab_sisteminden_beklenen():
    print("Gönderilmek istenen mesajın orjinale en yakın haliyle alıcıya ulaştırılmasıdır.") 
def hab_icin_önemli_hususlar():
    print("Haberleşme sistemlerinde dikkat edilmesi gereken hususlar")
    print("- Bandwidth(Bant aralığı): İşaretin frekans spektrumunda kapladığı bant aralığıdır")
    print("- Distortion(Bozulma): Kanalda gerçekleşen bozulmalar(genlik ve fazda) fazla miktarda olursa veri kaybına yol açar")
    print("- Fading(Zayıflama): İşaret, uzak bir noktaya gönderilirken sönümlenebilir(gücü azalabilir)")
    print("- Interference(Girişim): Aynı kanalda birden fazla mesaj sinyali iletilirken bunların spektrumları iç içe geçebilir")
    print("- Rate(Throughput): Frekans ve bant genişliğine bağlı olarak değişkenlik gösterir")
def hab_frekans_spektrumu():
    print("Haberleşme mühendisliğinde frekans spektrumunun kullanımı")
    print("İnsan kulağı ==> 0-15 Khz")
    print("Telefon görüşmeleri ==> 0-4 Khz ")
    print("Müzik sesleri ==> 0-20 Khz ")
    print("Eski televizyon(VFH Bandı) ==> 54-88 Mhz ")
    print("Radyo yayını(FM Bradcost) ==> 88-108 Mhz ")
    print("UHF ==> 174-890 Mhz ")
    print("Uydu,navigasyon,cep tel. vs ==> 1-2 Ghz ")
    print("Wifi, bluetooth,uydu,cep tel.vs ==> 2-4 Ghz")
    print("Radar ==> 8-12 Ghz")
def modulasyon_nedir():
    print("Modülasyon(Kipleme) :")
    print("- Yüksek frekanslı taşıyıcı dalganın genlik,açı ve frekans özelliklerini, mesaj işaretinin")
    print(" genliği ile orantılı olarak değiştirme işlemine modülasyon denir.")
    print("- Bilgi ==> Yüksek frekanslı taşıyıcı ==> Bilginin bandı yüksek frekanslara çıkarılır. ")
    print("- Haberleşme tekniğinin temelidir.")
def modulasyon_neden_gerekli():
    print("Modülasyon haberleşme sisteminde neden gereklidir?")
    print("1.Anten uzunluğu")
    print("  İletilmek istenen işaretin frekansı düşük dalga boyu yüksektir")
    print("  Modülasyon dalga boyunu düşürerek anten boyunu çok kısaltır.")
    print("2.Kanal gürültüsünü azaltma ")
    print("  Düşük frekans gürültü ve parazitlere yol açar ")
    print("  Modülasyon bunları azaltarak bozucu etkileri azaltır")
    print("3.Birden fazla sinyalin iletimi")
    print("  Aynı anda birden fazla işareti birbirine karıştırmadan iletilebilir")
def fourier_nedir():
    print("Fourier dönüşümü(Transformu):")
    print("Zaman alanındaki bir sinyali frekans alanına dönüştürmek için kullanılır.")
    print("Bu durum sinyalin anlaşılmasını kolaylaştırır.")
    print("Fourier herhangi bir sinyalin farklı genlik ve fazdaki sinus dalga serileri ile ifade edilebileceğini göstermiştir.")
    print("Fourier dönüşümü, karmaşık zaman sinyallerini frekans bileşenlerine ayırarak kolay anlaşılmasını sağlar.")
    print("İşaret zaman düzleminde ne kadar daralırsa, frekans düzleminde o kadar genişlemiş olur.")
    print("g(t) ==> G(f) için yani Fourier dön. = ∫ g(t).(e^-j2πft).dt şeklindedir.")
    print("G(f) ==> g(t) için yani ters Fourier dön. =  ∫ G(f).(e^j2πft).df şeklindedir.")
def konvolusyon_nedir():
    print("Konvolusyon(Katlama) integrali:")
    print("Zaman ortamında katlama, frekans ortamında çarpma işlemine karşılık gelir.")
    print("Konvolusyonu kullanma sebebimiz:")
    print("Bir sistemin dürtüye verdiği yanıtı biliyorsak,herhangi bir başka işarete verceği tepkiyi de biliyoruz demektir.")
    print("[f * g]= ∫ f(τ).g(t-τ).dt ")
def mod_cesitleri():
    print("Modulasyon cesitleri:")
    print(" 1. Genlik Modulasyonu                             2.Açı Modulasyonu")
    print("-Tasıyıcılı Genlik Modülasyonu(AM)                -Frekans Mod.(FM)")
    print("-Çift Yan-band Genlik Mod.(DSB-AM)                -Faz Mod.(PM)")
    print("-Tek Yan-band Genlik Mod.(SSB-AM)")
    print("-Artık Yan-band Genlik Mod.(VSB-AM)")
    
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
