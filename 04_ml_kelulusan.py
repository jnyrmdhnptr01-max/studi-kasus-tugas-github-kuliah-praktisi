"""Dr. Taniza Tajudin: klasifikasi kelulusan dengan data akademik sintetis."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
OUT=Path(__file__).resolve().parents[1]/"outputs"
OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(2026)
n=500
jam=rng.uniform(0,15,n)
hadir=rng.uniform(45,100,n)
tugas=rng.uniform(30,100,n)
latent=0.25*jam+0.055*(hadir-70)+0.04*(tugas-65)+rng.normal(0,1.7,n)-1.5
lulus=(latent>0).astype(int)
df=pd.DataFrame({"jam_belajar":jam.round(1),"kehadiran":hadir.round(1),"nilai_tugas":tugas.round(1),"lulus":lulus})
df.to_csv(OUT/"04_siswa_sintetis.csv",index=False)
X=df.drop(columns="lulus"); y=df.lulus
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=500,random_state=42))
model.fit(Xtrain,ytrain)
pred=model.predict(Xtest)
print(classification_report(ytest,pred,zero_division=0))
print("Confusion matrix:",confusion_matrix(ytest,pred))
pd.DataFrame({"aktual":ytest.to_numpy(),"prediksi":pred}).to_csv(OUT/"04_evaluasi_prediksi.csv",index=False)
print("Bukan penilaian siswa nyata, tidak untuk keputusan pendidikan sesungguhnya.")
