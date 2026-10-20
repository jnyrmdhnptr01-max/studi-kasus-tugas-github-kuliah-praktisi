"""Dr. Bart Slachter: contoh NDVI sebelum-sesudah dari raster sintetis (bukan citra satelit)."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parents[1]/"outputs"
OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(2026)
shape=(90,110)
red_before=rng.uniform(.10,.22,shape)
nir_before=rng.uniform(.45,.74,shape)
red_after=red_before.copy()
nir_after=nir_before.copy()
# Area perubahan ilustratif (mis. berkurang vegetasi, belum diketahui penyebabnya).
red_after[20:58,45:90] += .17
nir_after[20:58,45:90] -= .25
def ndvi(nir,red): return (nir-red)/(nir+red+1e-8)
before=ndvi(nir_before,red_before)
after=ndvi(nir_after,red_after)
delta=after-before
mask=delta < -.28
fig,ax=plt.subplots(1,3,figsize=(12,4))
for a,img,title in zip(ax,[before,after,mask],["NDVI sebelum","NDVI sesudah","Indikasi perubahan"]):
    a.imshow(img,cmap="Greens" if title!="Indikasi perubahan" else "gray",vmin=0 if title!="Indikasi perubahan" else None,vmax=.9 if title!="Indikasi perubahan" else None)
    a.set_title(title);a.axis("off")
plt.tight_layout();plt.savefig(OUT/"06_perubahan_vegetasi.png",dpi=140)
pd.DataFrame({"piksel_total":[mask.size],"piksel_terindikasi":[int(mask.sum())],"persen_terindikasi":[round(100*mask.mean(),2)]}).to_csv(OUT/"06_ringkasan_perubahan.csv",index=False)
print("Piksel terindikasi:",int(mask.sum()),"dari",mask.size)
print("Penting: NDVI tidak membuktikan deforestasi maupun penyebabnya; perlu validasi lapangan dan citra nyata.")
