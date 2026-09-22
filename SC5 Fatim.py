def hitung_biaya_pesan(jenis_kamar, tgl_masuk, tgl_keluar):
    durasi_menginap = tgl_keluar - tgl_masuk

    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    total_biaya = tarif * durasi_menginap
    return total_biaya, durasi_menginap 

jenis_kamar = input("Jenis kamar (Standard/Deluxe): ")
tgl_masuk = int(input("Tanggal masuk: "))
tgl_keluar = int(input("Tanggal keluar: "))

total_biaya, durasi_menginap = hitung_biaya_pesan(jenis_kamar, tgl_masuk, tgl_keluar)

print("=== Tampilan Data ===")
print("Jenis kamar:", jenis_kamar)
print("Tanggal masuk:", tgl_masuk)
print("Tanggal keluar:", tgl_keluar)
print("Durasi menginap:", durasi_menginap, "malam")
print("Total biaya: Rp", total_biaya)

