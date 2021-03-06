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
