# SISTEM MONITORING PERFORMA SERVER

# Baris = Server
# Kolom = Waktu pemantauan

cpu = [
    [45, 52, 48, 60, 55],  # Server 0
    [70, 75, 82, 80, 85],  # Server 1
    [30, 35, 40, 38, 42],  # Server 2
    [90, 92, 88, 95, 91]   # Server 3
]

# Menentukan jumlah server dan jumlah waktu
jumlah_server = len(cpu)
jumlah_waktu = len(cpu[0])

# 1. MENGHITUNG RATA-RATA SETIAP SERVER
rata_rata_server = []

for i in range(jumlah_server):
    total = 0

    for j in range(jumlah_waktu):
        total += cpu[i][j]

    rata_rata = total / jumlah_waktu
    rata_rata_server.append(rata_rata)


# 2. MENENTUKAN SERVER DENGAN RATA-RATA CPU TERTINGGI
rata_rata_tertinggi = max(rata_rata_server)
server_tertinggi = rata_rata_server.index(rata_rata_tertinggi)

# 3. MENENTUKAN CPU TERTINGGI DAN TERENDAH
semua_cpu = []

for i in range(jumlah_server):
    for j in range(jumlah_waktu):
        semua_cpu.append(cpu[i][j])

cpu_tertinggi = max(semua_cpu)
cpu_terendah = min(semua_cpu)

# 4. MENENTUKAN SERVER DAN WAKTU OVERLOAD
overload = []

for i in range(jumlah_server):
    for j in range(jumlah_waktu):

        if cpu[i][j] >= 80:
            overload.append([i, j, cpu[i][j]])


# 5. MENENTUKAN STATUS SETIAP SERVER
status_server = []

for i in range(jumlah_server):

    rata_rata = rata_rata_server[i]

    if rata_rata < 60:
        status = "NORMAL"

    elif rata_rata < 80:
        status = "WARNING"

    else:
        status = "CRITICAL"

    status_server.append(status)


# OUTPUT
print("==========================================")
print("       SISTEM MONITORING SERVER")
print("==========================================")

print("\nData CPU:")

for i in range(jumlah_server):
    print(f"Server {i}: {cpu[i]}")


print("\n==========================================")
print("RATA-RATA CPU SETIAP SERVER")
print("==========================================")

for i in range(jumlah_server):
    print(
        f"Server {i}: "
        f"{rata_rata_server[i]:.2f}% "
        f"({status_server[i]})"
    )


print("\n==========================================")
print("ANALISIS CPU")
print("==========================================")

print(
    f"Server dengan rata-rata CPU tertinggi: "
    f"Server {server_tertinggi}"
)

print(f"Rata-rata CPU tertinggi: {rata_rata_tertinggi:.2f}%")
print(f"CPU tertinggi: {cpu_tertinggi}%")
print(f"CPU terendah: {cpu_terendah}%")


print("\n==========================================")
print("DATA OVERLOAD")
print("==========================================")

for data in overload:

    server = data[0]
    waktu = data[1]
    nilai = data[2]

    print(
        f"Server {server}, "
        f"Waktu {waktu} → {nilai}%"
    )

print(f"\nJumlah overload: {len(overload)} kali")