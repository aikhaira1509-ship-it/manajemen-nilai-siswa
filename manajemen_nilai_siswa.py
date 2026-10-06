# Program Manajemen Nilai Siswa dengan Predikat
# Fitur: tambah data siswa, lihat data, urutkan nilai, lihat predikat, exit

siswa = []

def tampil_menu():
    print("\n=== PROGRAM MANAJEMEN NILAI SISWA ===")
    print("1. Tambah Siswa")
    print("2. Lihat Daftar Siswa")
    print("3. Urutkan Nilai Siswa")
    print("4. Lihat Predikat Nilai")
    print("5. Exit")

def hitung_predikat(nilai):
    """Menghitung predikat berdasarkan nilai"""
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    try:
        nilai = int(input("Masukkan nilai siswa (0-100): "))
        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0-100!")
            return
        predikat = hitung_predikat(nilai)
        siswa.append({"nama": nama, "nilai": nilai, "predikat": predikat})
        print(f"Data siswa {nama} berhasil ditambahkan dengan predikat {predikat}.")
    except ValueError:
        print("Nilai harus berupa angka!")

def lihat_siswa():
    if not siswa:
        print("Belum ada data siswa.")
    else:
        print("\n=== DAFTAR SISWA ===")
        for i, data in enumerate(siswa, start=1):
            print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}, Predikat: {data['predikat']}")

def urutkan_nilai():
    if not siswa:
        print("Belum ada data siswa.")
    else:
        siswa_urut = sorted(siswa, key=lambda x: x["nilai"], reverse=True)
        print("\n=== DATA SISWA DIURUTKAN BERDASARKAN NILAI TERTINGGI ===")
        for i, data in enumerate(siswa_urut, start=1):
            print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}, Predikat: {data['predikat']}")

def lihat_predikat():
    if not siswa:
        print("Belum ada data siswa.")
        return

    print("\n=== PREDIKAT NILAI SISWA ===")
    for data in siswa:
        print(f"Nama: {data['nama']}, Nilai: {data['nilai']}, Predikat: {data['predikat']}")

# MAIN PROGRAM
while True:
    tampil_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        urutkan_nilai()
    elif pilihan == "4":
        lihat_predikat()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih 1-5.")
