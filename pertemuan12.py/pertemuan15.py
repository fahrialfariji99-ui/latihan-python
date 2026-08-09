items = [
    ("A - Gandum", 15, 30),
    ("B - Minyak", 10, 50),
    ("C - Telur", 25, 75),
    ("D - Garam", 12, 48),
    ("E - Susu", 18, 36)
]

kapasitas = 50

items_density = []
for nama, berat, profit in items:
    density = profit / berat
    items_density.append([nama, berat, profit, density])

items_density.sort(key=lambda x: x[3], reverse=True)

print("="*65)
print(f"{'Paket':<15}{'Berat (ton)':<15}{'Profit (Juta)':<18}{'Density'}")
print("="*65)

for item in items_density:
    print(f"{item[0]:<15}{item[1]:<15}{item[2]:<18}{item[3]:.2f}")

print("="*65)

total_berat = 0
total_profit = 0
dipilih = []

for nama, berat, profit, density in items_density:
    if total_berat + berat <= kapasitas:
        dipilih.append(nama)
        total_berat += berat
        total_profit += profit

print("\nPaket yang dipilih:", ", ".join(dipilih))
print("Total Berat:", total_berat, "ton")
print("Total Profit: Rp", total_profit, "Juta")