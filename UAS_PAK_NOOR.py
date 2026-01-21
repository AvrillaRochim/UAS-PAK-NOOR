import random

print("==== GAME TEBAK ANGKA ====")
kesempatan  = 10  #
while True:
    print("Rules")
    print("1. Tebak angka dari 1 sampai 100")
    print(f"2. Kesempatan {kesempatan} kali")
    print("3. Tidak ada batas waktu")
    print("4. Setiap tebakan akan diberi petunjuk apakah angka terlalu ke besar atau terlalu ke kecil")
    

    angka = random.randint(1, 100)
    angka = 9


    print("\nSaya sudah memilih angka antara 1 sampai 100")

    while kesempatan > 0:
            tebakan = int(input("Masukkan tebakan kamu: "))


            if tebakan > angka:
                print("Angkaku lebih ke kecil")
                kesempatan -=1
            elif tebakan < angka:
                print("Angkaku lebih ke besar")
                kesempatan -=1
            else:
                print(f"Selamat jawaban kamu benar {angka}")
                break
    else:
        print("\nKesempatan habis!")
        print(f"Angka yang benar adalah: {angka}")
        print("=== GAME OVER ===")

    ulang = input("\nApakah anda ingin mengulang? (y/n)")
    if ulang != 'y':
         print("terimakasih telah bermain")
         break
    else:
        kesempatan -=1 