import random

sayi = random.randint(1,100)
hak = 5
sayac = 0 

while hak > 0:
	hak -= 1
	sayac += 1
	tahmin = in(input("tahmin: "))

	if sayi == tahmin:
		print(f"Tebrikler {sayac]. defada doğru tahmin!")
		break
	elif sayi > tahmin:
		print("yukarı")
	else:
		print("aşağı")

	if hak == 0:
		print(f"hakkınız bitti.Tutulan sayı: {sayi])
