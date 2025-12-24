import random
import math

# Bilgisayarın seçtiği gizli nokta
gizli_x = random.randint(1, 4)
gizli_y = random.randint(1, 4)

deneme_sayisi = 0

print("🎯 4x4 (16 birim kare) Sıcak-Soğuk Oyunu")
print("x ve y değerlerini 1 ile 4 arasında giriniz")

while True:
    x = int(input("Tahmin x: "))
    y = int(input("Tahmin y: "))

    deneme_sayisi += 1  # deneme sayısını artır

    # Mesafe hesaplama
    mesafe = math.sqrt((gizli_x - x)**2 + (gizli_y - y)**2)

    if mesafe == 0:
        print("🎉 Tebrikler! Doğru koordinatı buldun!")
        print("🔢 Toplam deneme sayısı:", deneme_sayisi)
        break
    elif mesafe <= 1.5:
        print("🔥 Sıcak")
    elif mesafe <= 3:
        print("🙂 Ilık")
    else:
        print("❄️ Soğuk")
