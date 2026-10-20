"""Andrea Arisal: analisis deskriptif dan diagnostik stok toko (data sintetis)."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(2026)
items = ["Beras", "Minyak", "Gula", "Kopi", "Susu"]
records = []
for month in range(1, 13):
    for item in items:
        demand = int(rng.integers(35, 120))
        stock = int(rng.integers(45, 110))
        records.append((month, item, demand, stock, max(0, demand-stock)))
df = pd.DataFrame(records, columns=["bulan", "produk", "permintaan", "stok", "kekurangan"])
df.to_csv(OUT / "01_stok_sintetis.csv", index=False)
summary = df.groupby("produk", as_index=False)[["permintaan", "kekurangan"]].sum()
summary["rasio_kekurangan"] = (summary["kekurangan"] / summary["permintaan"]).round(3)
summary.to_csv(OUT / "01_ringkasan_stok.csv", index=False)
ax = summary.plot.bar(x="produk", y="rasio_kekurangan", legend=False, figsize=(8, 4), title="Rasio Kekurangan Stok per Produk")
ax.set_ylabel("Kekurangan / permintaan")
plt.tight_layout(); plt.savefig(OUT / "01_grafik_stok.png", dpi=140)
print(summary.to_string(index=False))
print("Catatan: keputusan restok perlu mempertimbangkan biaya dan pola permintaan aktual.")
