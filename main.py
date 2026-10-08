from datetime import date

batas_data = 500


def rupiah(angka):
    return "Rp" + format(angka, ",").replace(",", ".")


def input_tanggal():
    while True:
        tgl = input("Tanggal (YYYY-MM-DD, Enter = hari ini): ").strip()
        if tgl == "":
            return date.today().isoformat()
        try:
            if date.fromisoformat(tgl).isoformat() == tgl:
                return tgl
        except ValueError:
            pass
        print("Tanggalnya belum benar. Contoh: 2026-10-07")


def input_nama():
    while True:
        nama = input("Pengeluaran buat apa? ").strip()
        if nama:
            return nama
        print("Namanya jangan kosong.")


def input_uang():
    while True:
        try:
            uang = int(input("Nominal (contoh 15000): "))
            if uang > 0:
                return uang
        except ValueError:
            pass
        print("Isi angka bulat di atas 0, tanpa titik atau Rp.")


def tampilkan(data):
    if not data:
        print("Belum ada catatan.")
        return
    for no, item in enumerate(data, 1):
        print(f"{no}. {item[0]} | {item[1]} | {rupiah(item[2])}")


def pilih_nomor(data):
    tampilkan(data)
    while True:
        try:
            no = int(input("Pilih nomor (0 = batal): "))
            if no == 0:
                return None
            if 1 <= no <= len(data):
                return no - 1
        except ValueError:
            pass
        print("Pilih nomor yang ada di daftar.")


def cari_pengeluaran(data, kata):
    ketemu = []
    kata = kata.lower()
    for item in data:
        if kata in item[1].lower():
            ketemu.append(item)
    return ketemu


def urut_nominal(data):
    hasil = data[:]
    # Bubble sort, bandingkan nominal yang bersebelahan.
    for i in range(len(hasil) - 1):
        for j in range(len(hasil) - 1 - i):
            if hasil[j][2] > hasil[j + 1][2]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
    return hasil


def total_rekursif(data, i=0):
    if i >= len(data):
        return 0
    return data[i][2] + total_rekursif(data, i + 1)


def main():
    catatan = []
    print("Catatan hanya ada selama program berjalan.")
    print("Kalau keluar, datanya hilang.")

    while True:
        print("\n=== CATATAN PENGELUARAN HARIAN ===")
        print("1. Tambah pengeluaran")
        print("2. Lihat catatan")
        print("3. Edit catatan")
        print("4. Hapus catatan")
        print("5. Cari pengeluaran")
        print("6. Urutkan nominal dari kecil")
        print("7. Hitung total pengeluaran")
        print("0. Keluar")
        pilih = input("Pilih: ").strip()

        if pilih == "1":
            if len(catatan) >= batas_data:
                print("Catatan sudah penuh, maksimal 500 data.")
                continue
            tgl = input_tanggal()
            nama = input_nama()
            uang = input_uang()
            catatan.append([tgl, nama, uang])
            print("Pengeluaran sudah ditambahkan.")

        elif pilih == "2":
            tampilkan(catatan)

        elif pilih == "3":
            if not catatan:
                print("Belum ada yang bisa diedit.")
                continue
            nomor = pilih_nomor(catatan)
            if nomor is None:
                continue
            print("Isi ulang tanggal, nama, dan nominal catatan ini.")
            tgl = input_tanggal()
            nama = input_nama()
            uang = input_uang()
            catatan[nomor] = [tgl, nama, uang]
            print("Catatan sudah diubah.")

        elif pilih == "4":
            if not catatan:
                print("Belum ada yang bisa dihapus.")
                continue
            nomor = pilih_nomor(catatan)
            if nomor is None:
                continue
            yakin = input(f"Hapus {catatan[nomor][1]}? (y/t): ").lower()
            if yakin.strip() == "y":
                catatan.pop(nomor)
                print("Catatan dihapus.")
            else:
                print("Batal hapus.")

        elif pilih == "5":
            kata = input("Cari nama pengeluaran: ").strip()
            if not kata:
                print("Isi dulu kata yang mau dicari.")
                continue
            hasil = cari_pengeluaran(catatan, kata)
            if hasil:
                tampilkan(hasil)
            else:
                print("Pengeluarannya tidak ketemu.")

        elif pilih == "6":
            print("\nUrutan dari nominal terkecil:")
            tampilkan(urut_nominal(catatan))

        elif pilih == "7":
            total = total_rekursif(catatan)
            print("Total semua catatan:", rupiah(total))

        elif pilih == "0":
            print("Program selesai. Catatan tidak disimpan.")
            break
        else:
            print("Menu itu tidak ada.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ditutup. Catatan tidak disimpan.")
