# Modal awal
modal_awal = 100000000  # 100 juta rupiah
total_keuntungan = 0

# Persentase laba/rugi per bulan (dalam desimal)
# Bulan 1: 0% (belum laba)
# Bulan 2: 0% (belum laba)
# Bulan 3: 1% (0.01)
# Bulan 4: Laba bulan ke-3 berlanjut (1% atau 0.01)
# Bulan 5: Meningkat 5% (dari bulan sebelumnya, jadi 1% + 5% = 6% atau 0.06)
# Bulan 6: Laba bulan ke-5 berlanjut (6% atau 0.06)
# Bulan 7: Laba bulan ke-5 berlanjut (6% atau 0.06)
# Bulan 8: Penurunan 2% (dari bulan sebelumnya, jadi 6% - 2% = 4% atau 0.04).
#           Catatan: "laba menjadi 3%" pada bulan ke-8 bertentangan dengan penurunan 2% dari 5%, 
#           maka kita asumsikan laba bulan ke-8 adalah 3%.

persentase_laba_per_bulan = [0, 0, 0.01, 0.01, 0.06, 0.06, 0.06, 0.03] 

# Simulasi selama 8 bulan
for bulan in range(8):
    laba_bulan_ini = modal_awal * persentase_laba_per_bulan[bulan]
    total_keuntungan += laba_bulan_ini
    # Modal bertambah dengan laba setiap bulannya (jika diakumulasikan)
    # Jika laba tidak diakumulasikan ke modal awal, baris di bawah ini tidak diperlukan.
    # modal_awal += laba_bulan_ini 
    print(f"Bulan ke-{bulan + 1}: Laba = Rp{laba_bulan_ini:,.2f}")

# Menampilkan hasil akhir
print("-" * 30)
print(f"Total keuntungan selama 8 bulan adalah: Rp{total_keuntungan:,.2f}")
print(f"Modal akhir setelah 8 bulan adalah: Rp{modal_awal + total_keuntungan:,.2f}")
