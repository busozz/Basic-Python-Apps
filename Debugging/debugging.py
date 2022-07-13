liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulma.

 for x in liste:
     try:
         sonuc = int(x)
         print(sonuc)
     except ValueError:
         continue

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazma.

 while True:
     sayi = input('sayı: ')
     if (sayi == 'q'):
         break

     try: 
         sonuc = float(sayi)
         print(f'girilen sayı: {sonuc}')
         break
     except ValueError:
         print('geçersiz sayı.')
         continue

# 3: Dictionary ve key bilgilerini parametre olarak alan get(d, key)
# fonksiyonu hazırlama.

urun = {"urunAdi":"samsung s10"}

# d["fiyat"] => KeyError

# get(d, "fiyat") => None
# get(d, "urunAdi") => samsung S10

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(urun, 'fiyat'))
print(get(urun, 'urunAdi'))


# 4- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verme.

 def faktoriyel(x):
     x = int(x)

     if (x<0):
         raise ValueError("Negatif değer")

     sonuc = 1
     for i in range(1, x+1):
         sonuc *= i

     return sonuc

 for i in [5,7,'a',2,-4,'10a']:
     try:
         x = faktoriyel(i)
     except ValueError as e:
         print(e)
         continue
     else:
         print(x)

# 5- Girilen parola içinde türkçe karakter hatası verme.

def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

    print('geçerli parola')

parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
