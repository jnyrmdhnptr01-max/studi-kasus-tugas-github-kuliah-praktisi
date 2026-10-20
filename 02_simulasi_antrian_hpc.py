"""Dr. Warawan: simulasi banyak skenario antrean loket, pengantar komputasi paralel."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(2026)
def simulate(n_loket, n_pengunjung=150):
    kedatangan = np.cumsum(rng.exponential(1.8, n_pengunjung))
    waktu_layanan = rng.exponential(4.0, n_pengunjung)
    selesai_loket = np.zeros(n_loket)
    tunggu = []
    for datang, durasi in zip(kedatangan, waktu_layanan):
        idx = int(np.argmin(selesai_loket))
        mulai = max(datang, selesai_loket[idx])
        tunggu.append(mulai-datang)
        selesai_loket[idx] = mulai+durasi
    return float(np.mean(tunggu))
rows = []
for n in (2, 3, 4, 5):
    for rep in range(50):
        rows.append((n, rep, simulate(n)))
df = pd.DataFrame(rows, columns=["jumlah_loket", "pengulangan", "rata_tunggu_menit"])
df.to_csv(OUT / "02_skenario_antrean.csv", index=False)
summary = df.groupby("jumlah_loket")["rata_tunggu_menit"].mean()
summary.plot(marker="o", title="Simulasi Waktu Tunggu vs Jumlah Loket", ylabel="Menit", xlabel="Jumlah loket")
plt.tight_layout(); plt.savefig(OUT / "02_antrean.png", dpi=140)
print(summary.round(2))
print("Catatan: contoh serial berskala kecil; HPC memungkinkan banyak simulasi berjalan paralel.")
