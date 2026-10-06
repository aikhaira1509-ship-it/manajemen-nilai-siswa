# Program Manajemen Nilai Siswa dengan Predikat
# Kelompok 3
# Fitur: tambah data siswa, lihat data, urutkan nilai, lihat predikat, exit

siswa = []

def tampil_menu():
    try:
        print("\n=== PROGRAM MANAJEMEN NILAI SISWA ===")
        print("=== KELOMPOK 3 ===")
        print("1. Tambah Siswa (Multiple)")
        print("2. Lihat Daftar Siswa")
        print("3. Urutkan Nilai Siswa")
        print("4. Lihat Predikat Nilai")
        print("5. Exit")
    except Exception as e:
        print(f"Error saat menampilkan menu: {e}")

def hitung_predikat(nilai):
    """Menghitung predikat berdasarkan nilai"""
    try:
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
    except Exception as e:
        print(f"Error saat menghitung predikat: {e}")
        return None

def perlu_remedial(nilai):
    """Mengecek apakah siswa perlu remedial (nilai < 70)"""
    try:
        if nilai < 70:
            return "Ya"
        else:
            return "Tidak"
    except Exception as e:
        print(f"Error saat mengecek remedial: {e}")
        return None

def tambah_siswa():
    try:
        jumlah = int(input("Berapa banyak siswa yang ingin ditambahkan? "))
        if jumlah <= 0:
            print("Jumlah siswa harus lebih dari 0!")
            return
        
        # FOR LOOP - Mengulang untuk input beberapa siswa
        for i in range(jumlah):
            try:
                print(f"\n--- Data Siswa ke-{i+1} ---")
                nama = input(f"Masukkan nama siswa ke-{i+1}: ")
                
                if not nama.strip():
                    print("Nama siswa tidak boleh kosong!")
                    continue
                
                try:
                    nilai = int(input(f"Masukkan nilai siswa {nama} (0-100): "))
                    
                    if nilai < 0 or nilai > 100:
                        print("Nilai harus antara 0-100!")
                        continue
                    
                    predikat = hitung_predikat(nilai)
                    remedial = perlu_remedial(nilai)
                    
                    if predikat is None or remedial is None:
                        print("Error saat memproses data!")
                        continue
                    
                    # LIST - Menambahkan data ke dalam list
                    siswa.append({
                        "nama": nama, 
                        "nilai": nilai, 
                        "predikat": predikat,
                        "remedial": remedial
                    })
                    print(f"✓ Data siswa {nama} berhasil ditambahkan.")
                
                except ValueError:
                    print(f"Error: Nilai harus berupa angka! Bukan '{input}'")
                    continue
            
            except Exception as e:
                print(f"Error saat input data siswa ke-{i+1}: {e}")
                continue
        
        print(f"\n✓ Total {len(siswa)} siswa berhasil ditambahkan.")
    
    except ValueError:
        print("Error: Jumlah siswa harus berupa angka!")
    except Exception as e:
        print(f"Error pada fungsi tambah siswa: {e}")

def lihat_siswa():
    try:
        if not siswa:
            print("Belum ada data siswa.")
        else:
            print("\n=== DAFTAR SISWA ===")
            # FOR LOOP - Menampilkan semua siswa
            for i, data in enumerate(siswa, start=1):
                try:
                    print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}, Remedial: {data['remedial']}")
                except KeyError as e:
                    print(f"Error: Data tidak lengkap - {e}")
                except Exception as e:
                    print(f"Error saat menampilkan data siswa: {e}")
    except Exception as e:
        print(f"Error pada fungsi lihat siswa: {e}")

def urutkan_nilai():
    try:
        if not siswa:
            print("Belum ada data siswa.")
        else:
            # SORT - Mengurutkan nilai dari tertinggi ke terendah
            try:
                siswa_urut = sorted(siswa, key=lambda x: x["nilai"], reverse=True)
                print("\n=== DATA SISWA DIURUTKAN BERDASARKAN NILAI TERTINGGI ===")
                
                # FOR LOOP - Menampilkan siswa yang sudah diurutkan
                for i, data in enumerate(siswa_urut, start=1):
                    try:
                        print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}, Remedial: {data['remedial']}")
                    except KeyError as e:
                        print(f"Error: Data tidak lengkap - {e}")
                    except Exception as e:
                        print(f"Error saat menampilkan data: {e}")
            except Exception as e:
                print(f"Error saat mengurutkan nilai: {e}")
    except Exception as e:
        print(f"Error pada fungsi urutkan nilai: {e}")

def lihat_predikat():
    try:
        if not siswa:
            print("Belum ada data siswa.")
            return

        print("\n=== PREDIKAT NILAI SISWA ===")
        print("\nKeterangan Predikat:")
        print("A = 85-100")
        print("B = 70-84")
        print("C = 60-69")
        print("D = 50-59")
        print("E = 0-49")
        print("\n" + "="*50)
        
        # FOR LOOP - Menampilkan predikat setiap siswa
        for data in siswa:
            try:
                print(f"Nama: {data['nama']}, Nilai: {data['nilai']}, Predikat: {data['predikat']}")
            except KeyError as e:
                print(f"Error: Data tidak lengkap - {e}")
            except Exception as e:
                print(f"Error saat menampilkan predikat: {e}")
    except Exception as e:
        print(f"Error pada fungsi lihat predikat: {e}")

# MAIN PROGRAM
# WHILE LOOP - Menu utama terus berjalan sampai user pilih exit
try:
    while True:
        try:
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
                print("\nProgram selesai. Terima kasih!")
                break  # EXIT
            else:
                print("Pilihan tidak valid, silakan pilih 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user (Ctrl+C).")
            break
        except Exception as e:
            print(f"Error pada loop menu: {e}")
            print("Silakan coba lagi.")

except Exception as e:
    print(f"Error fatal pada program utama: {e}")
finally:
    print("\nProgram selesai.")
