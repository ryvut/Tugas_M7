try:
    del input
except NameError:
    pass

nama_item = str(input("nama barang yang ingin dibeli: "))
jml_awal = float(input("jumlah awal barang: "))
sat_awal = str(input("satuan awal barang(pcs/lusin/kodi): "))
sat_tujuan = str(input("satuan yang diinginkan(pcs/lusin/kodi): "))

is_error = False
total_pcs = 0

if sat_awal == "pcs":
    total_pcs = jml_awal
elif sat_awal == "lusin":
    total_pcs = jml_awal * 12
elif sat_awal == "kodi":
    total_pcs = jml_awal * 20
else:
    is_error = True

total_tujuan = 0
if not is_error:
    if sat_tujuan == "pcs":
        total_tujuan = total_pcs
    elif sat_tujuan == "lusin":
        total_tujuan = total_pcs / 12
    elif sat_tujuan == "kodi":
        total_tujuan = total_pcs / 20
    else:
        is_error = True

if is_error:
    print("error satuan tidak dapat dikenali")
else:
    print(f"barang yang dibeli: {nama_item}")
    print(f"jumlah awal: {jml_awal} {sat_awal}")
    print(f"total dalam pcs:  {total_pcs}")
    print(f"jumlah yang diinginkan: {total_tujuan} {sat_tujuan}")