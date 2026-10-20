"""Widi Prima Depa: penentuan titik penanganan sampah berbasis koordinat ilustratif."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from math import radians, sin, cos, asin, sqrt
OUT=Path(__file__).resolve().parents[1]/"outputs"
OUT.mkdir(exist_ok=True)
# Koordinat sepenuhnya ilustratif, bukan laporan titik sampah nyata.
rows=[("A",-3.795,102.260,90,5),("B",-3.800,102.275,50,2),("C",-3.815,102.255,85,4),
      ("D",-3.785,102.280,30,1),("E",-3.805,102.242,65,3)]
def km(lat1,lon1,lat2,lon2):
    dlat=radians(lat2-lat1); dlon=radians(lon2-lon1)
    a=sin(dlat/2)**2+cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return 6371*2*asin(sqrt(a))
df=pd.DataFrame(rows, columns=["titik","lat","lon","volume_ilustratif","jumlah_laporan"])
base=(-3.800,102.265)
df["jarak_km"]=[km(*base,r.lat,r.lon) for r in df.itertuples()]
df["skor_prioritas"]= (0.6*df.volume_ilustratif/100 + 0.4*df.jumlah_laporan/5).round(3)
df=df.sort_values("skor_prioritas",ascending=False)
df.to_csv(OUT/"03_prioritas_lokasi.csv",index=False)
fig,ax=plt.subplots(figsize=(7,5))
sc=ax.scatter(df.lon,df.lat,s=df.volume_ilustratif*5,c=df.skor_prioritas,cmap="viridis",alpha=.8)
for r in df.itertuples(): ax.annotate(r.titik,(r.lon,r.lat),xytext=(5,5),textcoords="offset points")
ax.set(xlabel="Bujur (ilustratif)",ylabel="Lintang (ilustratif)",title="Prioritas Penanganan Sampah: Data Simulasi")
fig.colorbar(sc,ax=ax,label="Skor prioritas")
plt.tight_layout();plt.savefig(OUT/"03_peta_prioritas.png",dpi=140)
print(df[["titik","jarak_km","skor_prioritas"]].to_string(index=False))
