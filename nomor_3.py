print("soal a")
tabel_pengiriman = (
    ("Laptop", 2.5, "Surabaya", 35000),
    ("Printer", 6.0, "Jakarta", 55000),
    ("Monitor", 4.2, "Bandung", 45000),
    ("Keyboard", 1.2, "Surabaya", 30000),
    ("Mouse", 0.5, "Jakarta", 25000)
)

filter_sby = [row for row in tabel_pengiriman if row[2] == "Surabaya"]
for row in filter_sby:
    print(row)

print("\nsoal b")
berat_jkt = sum(row[1] for row in tabel_pengiriman if row[2] == "Jakarta")
print(f"total berat jakarta: {berat_jkt}")

print("\nsoal c")
list_baru = []
for nama, berat, kota, biaya in tabel_pengiriman:
    if kota == "Bandung":
        biaya = int(biaya * 1.1)
        list_baru.append((nama, berat, kota, biaya))
print(list_baru)