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
def acimod_nedir ():
    print("Bilgi sinyali sabit genlikli taşıyıcı sinyalin açı değişimleri içerisindedir.")
    print("Açı değişimleri frekans ve faz değişimleri ile gerçekleştirilir.")
    print("FM 'de frekans değişim miktarı, PM'de faz değişim miktarı bilgi işaretinin genliği ile orantılıdır.")
    print("Bant genişliği genlik modülasyonun agöre çok yüksektir.")
    print("Gürültüye karşı bağışıklığı çok güçlüdür.")
def PM_nedir ():
    print("--FAZ MODÜLASYONU--")
    print("Mesaj işaretinin genliğindeki değişimlere paralel olarak ")
    print("taşıyıcını fazı değiştirilir.")
    print("PM Çıkış sinyali:")
    print("Vpm(t)= Ac*cos(2*pi*fc*t + kp.m(t))")
    print("kp:faz kayma sabiti(derece/volt)")
def FM_nedir ():
    print("--FREKANS MODÜLASYONU--")
    print("Taşıyıcını frekansı(fc),mesaj işaretinin genliğine göre değiişim gösterir.")
    print("FM Çıkış sinyali:")
    print("Vfm(t)= Ac*cos(2*pi*fc*t + 2*pi*kf ∫ m(τ) dτ)")
    print("kf:frekans kayma sabiti")

def AM(Vm,fm,Vc,fc):
    pi=math.pi #pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    prc=500 # 0 ile 1 arasında alınacak örnek sayısını belirledik
                        
    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    f=np.linspace((-prc/2),(+prc/2),prc) # f düzlemini tanımladık
    mt=np.zeros(prc) # boş bir mesaj sinyal dizisi oluşturduk
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    vam=np.zeros(prc) # modüle edilmiş sinyalin geleceği boş bir dizi oluşturduk
    a=np.zeros(prc) # fourier transformu için boş bir dizi oluşturduk

    for i in range(prc): # Matematiksel denkleme göre bir mesaj sinyalini döngü ile atadık
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for j in range(prc): # Taşıyıcı sinyali tanımladık
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc): # Modüle edilmiş sinyali matematiksel eşitliğe göre tanımladık
        vam[k]=(Vc+mt[k])*(math.cos(2*pi*fc*t[k]))

    a=fft(vam) # vam(t) sinyalinin fourierini alarak frekans ortamına geçirdik
    b=fftshift(a) # Alınan işaretin pozitif ve negatif yerlerini değiştirdik
    c=abs(b) # Ve son işaretin mutlağını alarak son haline getirdik

    plt.subplot(211) # Sinyal çizimi ve çizimde yer alan atamalara 2 sinyal çizdirilecek
    plt.title('Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vam) # İlk olarak vam sinyalini zaman düzleminde çizdirdik
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c) # Ardından vam işaretini frekans ortamında çizdirdik
    plt.grid
    plt.show() # Son olarak çizdirdiğimiz sinyalleri ekrana yansıttık
def DSBAM(Vm,fm,Vc,fc):
    pi=math.pi # pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    prc=500 # 0 ile 1 arasında alınacak örnek sayısını belirledik
                        
    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    f=np.linspace((-prc/2),(+prc/2),prc) # f düzlemini tanımladık
    mt=np.zeros(prc) # boş bir mesaj sinyal dizisi oluşturduk
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    vdsbam=np.zeros(prc) # modüle edilmiş sinyalin geleceği boş bir dizi oluşturduk
    a=np.zeros(prc) # fourier transformu için boş bir dizi oluşturduk

    for i in range(prc):  # Matematiksel denkleme göre bir mesaj sinyalini döngü ile atadık
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for j in range(prc): # Taşıyıcı sinyali tanımladık
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc): # Modüle edilmiş sinyali matematiksel eşitliğe göre tanımladık
        vdsbam[k]=ct[k]*mt[k]

    a=fft(vdsbam) # vdsbam(t) sinyalinin fourierini alarak frekans ortamına geçirdik
    b=fftshift(a) # Alınan işaretin pozitif ve negatif yerlerini değiştirdik
    c=abs(b) # Ve son işaretin mutlağını alarak son haline getirdik 

    plt.subplot(211) # Sinyal çizimi ve çizimde yer alan atamalara 2 sinyal çizdirilecek
    plt.title('Taşıyıcı bastırılımış Çift Yan Band Genlik Mod.')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vdsbam) # İlk olarak vdsbam sinyalini zaman düzleminde çizdirdik
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c) # Ardından vdsbam işaretini frekans ortamında çizdirdik
    plt.grid
    plt.show() # Son olarak çizdirdiğimiz sinyalleri ekrana yansıttık
def SSBUAM(Vm,fm,Vc,fc):
    pi=math.pi # pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    prc=500 # 0 ile 1 arasında alınacak örnek sayısını belirledik
                       
    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    f=np.linspace((-prc/2),(+prc/2),prc) # f düzlemini tanımladık
    mt=np.zeros(prc) # boş bir mesaj sinyal dizisi oluşturduk
    mts=np.zeros(prc)  # Mesaj sinyalinin hilbert dönüşümü için boş bir dizi tanımladık
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    vssb=np.zeros(prc)  # modüle edilmiş sinyalin geleceği boş bir dizi oluşturduk
    a=np.zeros(prc)  # fourier transformu için boş bir dizi oluşturduk

    for i in range(prc):  # Matematiksel denkleme göre bir mesaj sinyalini döngü ile atadık
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for im in range(prc): # Mesaj sinyaklinin hilbert dönüşümünü döngü ile atadık
        mts[im]=Vm*(math.sin(2*pi*fm*t[im]))

    for j in range(prc):   # Taşıyıcı sinyali tanımladık
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc): # Modüle edilmiş sinyali matematiksel eşitliğe göre tanımladık Üst yan band old için "-" 
        vssb[k]=(Vc*mt[k]*math.cos(2*pi*fc*t[k]))-(Vc*mts[k]*math.sin(2*pi*fc*t[k]))

    a=fft(vssb) # vssbam(t) sinyalinin fourierini alarak frekans ortamına geçirdik
    b=fftshift(a) # Alınan işaretin pozitif ve negatif yerlerini değiştirdik
    c=abs(b)  # Ve son işaretin mutlağını alarak son haline getirdik 

    plt.subplot(211) # Sinyal çizimi ve çizimde yer alan atamalara 2 sinyal çizdirilecek
    plt.title('Tek yan band (üst) Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vssb) # İlk olarak vssb sinyalini zaman düzleminde çizdirdik
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)  # Ardından vssb işaretini frekans ortamında çizdirdik
    plt.grid
    plt.show()  # Son olarak çizdirdiğimiz sinyalleri ekrana yansıttık
def SSBDAM(Vm,fm,Vc,fc):
    pi=math.pi # pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    prc=500 # 0 ile 1 arasında alınacak örnek sayısını belirledik

                        
    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    f=np.linspace((-prc/2),(+prc/2),prc) # f düzlemini tanımladık
    mt=np.zeros(prc)  # boş bir mesaj sinyal dizisi oluşturduk
    mts=np.zeros(prc) # Mesaj sinyalinin hilbert dönüşümü için boş bir dizi tanımladık
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    vssb=np.zeros(prc)  # modüle edilmiş sinyalin geleceği boş bir dizi oluşturduk
    a=np.zeros(prc) # fourier transformu için boş bir dizi oluşturduk

    for i in range(prc):  # Matematiksel denkleme göre bir mesaj sinyalini döngü ile atadık
        mt[i]=Vm*(math.cos(2*pi*fm*t[i]))

    for im in range(prc):  # Mesaj sinyaklinin hilbert dönüşümünü döngü ile atadık
        mts[im]=Vm*(math.sin(2*pi*fm*t[im]))

    for j in range(prc):  # Taşıyıcı sinyali tanımladık
        ct[j]=Vc*(math.cos(2*pi*fc*t[j]))

    for k in range(prc): # Modüle edilmiş sinyali matematiksel eşitliğe göre tanımladık Alt yan band old için "+" 
        vssb[k]=(Vc*mt[k]*math.cos(2*pi*fc*t[k]))+(Vc*mts[k]*math.sin(2*pi*fc*t[k]))

    a=fft(vssb)  # vssbam(t) sinyalinin fourierini alarak frekans ortamına geçirdik
    b=fftshift(a)  # Alınan işaretin pozitif ve negatif yerlerini değiştirdik
    c=abs(b) # Ve son işaretin mutlağını alarak son haline getirdik 

    plt.subplot(211) # Sinyal çizimi ve çizimde yer alan atamalara 2 sinyal çizdirilecek
    plt.title('Tek yan band (alt) Genlik Modülasyonu')
    plt.xlabel('Zaman(sn)')
    plt.ylabel('Genlik(V)')
    plt.plot(t,vssb) # İlk olarak vssb sinyalini zaman düzleminde çizdirdik
    plt.grid

                           
    plt.subplot(212)
    plt.xlabel('Frekans(Hz)')
    plt.ylabel('Genlik(V)')
    plt.plot(f,c)  # Ardından vssb işaretini frekans ortamında çizdirdik
    plt.grid
    plt.show() # Son olarak çizdirdiğimiz sinyalleri ekrana yansıttık

def PM (Vc,fc,kp):
    prc=500 # pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    pi=math.pi # 0 ile 1 arasında alınacak örnek sayısını belirledik

    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    mt=-1*(np.ones(prc)) # Mesaj sinyalini 1 ve -1 den oluşan kare dalga yapmak için ilk olarak -1 lerden oluşturyoruz
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    vpm=np.zeros(prc) # Çıkış sinyal için boş bir dizi oluşturuyoruz
    for i in range(250): # Mesaj sinyalinin ilk yarısını 1 atıyoruz ve mesaj sinyali kare dalga oluyor
        mt[i]=1
    for k in range(prc): # Taşıyıcı sinyale döngü ile atama yapıyoruz
        ct[k]=Vc*(math.cos(2*pi*fc*t[k]))
    for j in range(prc): # Ve çıkış sinyalini matematiksel döngülerle oluşturuyoruz
        vpm[j]=Vc*(math.cos(2*pi*fc*t[j]+(kp*mt[j])))
    plt.subplot(221)
    plt.title('Taşıyıcı sinyali')
    plt.plot(t,ct) # Taşıyıcı sinyali çizdiriyoruz
    plt.grid

    plt.subplot(222)
    plt.title('Çıkış sinyali')
    plt.plot(t,vpm) # Çıkış sinyalini çizdiriyoruz
    plt.grid

    plt.subplot(223)
    plt.title('Mesaj sinyali')
    plt.plot(t,mt) # Mesaj sinyalini çizdiriyoruz
    plt.grid
    plt.show() # Çizdirilenleri ekrana yazdırdık
def FM (Vc,fc,kf):
    prc=500 # pi ataması yapılıyor kütüphane kullanımını "pi" değişkenine atadık
    pi=math.pi # 0 ile 1 arasında alınacak örnek sayısını belirledik

    t=np.linspace(0,1,prc) # t düzlemini tanımladık
    mt=np.ones(prc) # Mesaj sinyalini için birlerden oluşan dizi tanımladık daha sonra kare dalga olucak
    mt_int=np.zeros(prc) # Mesaj sinyalinin integralini için bir dizi tanımladık
    vfm=np.zeros(prc) # Çıkış sinyali için boş bir dizi tanımladık
    ct=np.zeros(prc) # boş bir taşıyıcı sinyal dizisi oluşturduk
    for m in range (250,prc): # Mesaj sinyali kare dalga şeklindedir bu yüzden son yarısına -1 atadık
        mt[m]=-1
    for i in range (250): # Mesaj sinyalinin integrali de üçgen şeklinde olur. Onu üçgenin yükselen rampasını atadık
        mt_int[i]=t[i]
    for j in range (250,500): # Mesaj sinyalinin integrelinin üçgen sinyal çıkışının azalan rampasını atadık
        mt_int[j]=1-t[j]
    for k in range (prc): # Çıkış sinyalini matematiksel denkleme göre tanımladık
        vfm[k]=Vc*math.cos(2*pi*fc*t[k]+2*pi*kf*mt_int[k])
    for o in range (prc): # Taşıyıcı sinyalinide oluşturduk
        ct[o]=Vc*math.cos(2*pi*fc*t[o])

    plt.subplot(221)
    plt.plot(t,ct) # Taşıyıcı sinyalini zaman düzleminde çizdirdik
    plt.title("Taşıyıcı sinyal")

    plt.subplot(222)
    plt.plot(t,mt) # Mesaj sinyalini zaman düzleminde çizdirdik
    plt.title("Mesaj sinyali")
    
    plt.subplot(223)
    plt.plot(t,mt_int) # Mesaj sinyalinin integralini zaman düzleminde çizdirdik
    plt.title("Mesaj işaretinin integrali")

    plt.subplot(224)
    plt.plot(t,vfm) # Çıkış sinyalini zaman düzleminde çizdirdik
    plt.title("FM Çıkış sinyali")

    plt.show() # Çizdirilenleri ekrana yazdırdık


