import sys

balance = 1000000  # saldo awal

print("Menu Transaksi")
print("1. Tarik Tunai")
print("2. Cek saldo")
print("3. Keluar")

choice = input("Pilih opsi (1/2/3): ")

if choice == '1':
    tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
    if tarik <= balance:
        balance -= tarik
        print(f"Penarikan berhasil. Sisa saldo Anda: Rp {balance:,.0f}")
    else:
        print("Saldo tidak mencukupi.")
elif choice == '2':
    print(f"Saldo Anda saat ini: Rp {balance:,.0f}")
elif choice == '3':
    print("Terima kasih telah menggunakan ATM kami.")
    sys.exit()
else:
    print("Pilihan tidak valid.")

