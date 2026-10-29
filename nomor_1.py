bln = input("bulan yang ingin menginap ").strip().lower()
durasi = int(input("berapa lama menginap "))
kamar = input("tipe kamar anda yang inginkan (studio/apartemen) ").strip().lower()

tarif_std = 0
tarif_apt = 0

if bln in ["mei", "oktober"]:
    tarif_std = 500000
    tarif_apt = 650000
elif bln in ["juni", "september"]:
    tarif_std = 752000
    tarif_apt = 687000
elif bln in ["juli", "agustus"]:
    tarif_std = 760000
    tarif_apt = 770000
else:
    print("tidak tersedia ruangan di bulan ini")

total_biaya = 0

if kamar == "studio":
    total_biaya = tarif_std * durasi
    if durasi > 3:
        potongan = total_biaya * 0.15
        total_biaya -= potongan
elif kamar == "apartemen":
    total_biaya = tarif_apt * durasi
    if durasi > 3:
        potongan = total_biaya * 0.10
        total_biaya -= potongan
else:
    print("tipe kamar tidak valid")

if total_biaya > 0:
    print(f"total tarif untuk menginap selama {durasi} hari dibulan {bln} dengan tipe kamar {kamar} adalah {total_biaya}")
