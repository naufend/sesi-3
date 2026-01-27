tugas = []

while True:
    print("\nMenu:")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        if tugas == []:
            print("Belum ada tugas.")
        else:
            print("Daftar Tugas:")
            for i in range(len(tugas)):
                print(i + 1, tugas[i])

    elif pilih == "2":
        tugas_baru = input("Masukkan tugas: ")
        tugas.append(tugas_baru)
        print("Tugas ditambahkan.")

    elif pilih == "3":
        if tugas == []:
            print("Tidak ada tugas untuk dihapus.")
        else:
            for i in range(len(tugas)):
                print(i + 1, tugas[i])
            hapus = int(input("Pilih nomor tugas: "))
            tugas.pop(hapus - 1)
            print("Tugas dihapus.")

    elif pilih == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan salah.")
