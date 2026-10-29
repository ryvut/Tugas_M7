# a
angka_list = [2, 14, 2, 10, 5, 6, 2]
hasil_a = [x for x in angka_list if angka_list.count(x) == 1]
print("output a:", hasil_a)

# b
teks = "menjadi mahasiswa yang dapat mengelola waktu dengan baik"
list_kata = teks.split()
print(list_kata)
terpanjang = ""
for kata in list_kata:
    if len(kata) > len(terpanjang):
        terpanjang = kata
print('output ', terpanjang)

# c
container = ["aku", 13, "ok", 55, "lama", 10]
extracted_angka = container[1:6:2]
print(sum(extracted_angka))