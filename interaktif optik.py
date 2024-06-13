sinavadi = input("sınav ismi?")

dersler = {}
cevaplar = {}

dersadi = input("ders adı?")
sorusayisi = int(input(dersadi + " " + "soru sayısı"))
while True:
    dersler[dersadi] = sorusayisi

    ss = int(input("cevapladığın sorunun numarası"))

    if ss < 1 or ss > sorusayisi:
        ss = int(input("lütfen geçerli aralıkta bir sayı giriniz"))


    sh = input("cevapladığın sorunun şık ismi (a/b/c/d/e)")

    if sh != "a" and sh != "b" and sh != "c" and sh != "d" and sh != "e":
        sh = input("lütfen geçerli bir harf giriniz")

    cevaplar[ss] = sh

    so = input("eğer sorular bitti ise son yazın bitmedi yani hala cevaplamadığınız sorular var ise enter tuşuna bazınız")
    if so != "son":
        continue
    print(cevaplar)
    ds = input("sınavda başka ders varsa var yaz eğer yoksa son yaz").lower()
    if ds == "son":
        break
    elif ds != "son":
        dersadi = input("ders adı?")
        sorusayisi = int(input(dersadi + " " + "soru sayısı"))

print(dersler)
print(cevaplar)



