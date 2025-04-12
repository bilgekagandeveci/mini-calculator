def hesap_makinesi():
    print("🧮 Mini Hesap Makinesi (Kaan Broski Edition)")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminiz (1/2/3/4): ")

    if secim not in ['1', '2', '3', '4']:
        print("Geçersiz seçim yaptınız.")
        return

    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if secim == '1':
        print(f"Sonuç: {sayi1 + sayi2}")
    elif secim == '2':
        print(f"Sonuç: {sayi1 - sayi2}")
    elif secim == '3':
        print(f"Sonuç: {sayi1 * sayi2}")
    elif secim == '4':
        if sayi2 == 0:
            print("Sıfıra bölme hatası!")
        else:
            print(f"Sonuç: {sayi1 / sayi2}")

hesap_makinesi()
