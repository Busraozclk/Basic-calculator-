sayi1 = int(input("1. : "))
sayi2 = int(input("2.: "))
islem = input("(toplama işlemi için +)  (çıkarma işlemi için -) (çarpma işlemi için *) (bölme işlemi için /)")
  


if islem == "+":
    sonuc = sayi1 + sayi2
    print("Toplamı:",sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Farkı:",sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Çarpım",sonuc)
elif islem == "/":
    sonuc = sayi1 / sayi2
    print("Bölüm",sonuc)
else:
    print("Hatalısınız!")