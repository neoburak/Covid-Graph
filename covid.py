import  numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import  matplotlib.dates as mdates
from  matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import  datetime as dt

veri=pd.read_excel("covidtr.xlsx")
veri.drop("Ülke",axis=1,inplace= True)
veri.drop("Bölge",axis=1,inplace= True)


veriİyileşen=veri.sort_values("İyileşen",ascending=True).iloc[14:]


veriOlu= veri.sort_values("Ölüm",ascending=True).iloc[5:]


veriTanı= veri.sort_values("Tanı",ascending=True)


listeIO = [veriİyileşen["İyileşen"]/veriOlu["Ölüm"]]
listeTI = [veriTanı["İyileşen"]/veriOlu["Tanı"]]




date1 = dt.datetime(2020, 3, 10)
date2 = dt.datetime(2020, 11, 30)
delta = dt.timedelta(hours = 24)

dates = drange(date1, date2,delta)

tersveri= veri[::-1]

fig,(eksen,eksen1,eksen2,eksen3,eksen4,eksen5) = plt.subplots(1,6,figsize=(15,5))

eksen.plot(dates,tersveri["Ölüm"],label="Ölüm Verisi",color="r",linestyle="--")
eksen.plot(dates,tersveri["Tanı"],label="Tanı Verisi",color="g",linestyle=":")
eksen.plot(dates,tersveri["İyileşen"],label="İyileşen Verisi",color="b",linestyle="-.")


eksen1.plot(dates,tersveri["İyileşen"],color="b")
eksen2.plot(dates,tersveri["Tanı"],color="g")
eksen3.plot(dates,tersveri["Ölüm"],color="r")
fig.autofmt_xdate(rotation=45)
eksen.set_title('Covid Verileri')
eksen1.set_title('İyileşen Verisi')
eksen2.set_title('Tanı Verisi')
eksen3.set_title('Ölüm Verisi')



eksen4.hist(listeTI,color="orange")
eksen4.set_title("Tanı/İyileşme Oranı")
eksen5.hist(listeIO,color="yellow")
eksen5.set_title("Tanı/Ölüm Oranı")

for i in (eksen,eksen1,eksen2,eksen3):
    i.set_xlabel("Tarih")
    i.set_ylabel("Kişi Sayısı")
    i.grid(True)
    i.yaxis.label.set_size(10)
    i.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m- %Y'))
    i.yaxis.set_label_coords(0.10,0.5)
    i.yaxis.label.set_size(10)
    i.tick_params(labelsize=8, pad=0.3)

for l in (eksen4,eksen5):
    l.set_xlabel("Oran")
    l.set_ylabel("Miktar")
    l.grid(True)
    l.yaxis.label.set_size(10)
    l.yaxis.set_label_coords(0.10,0.5)
    l.tick_params(labelsize=8, pad=0.3)

fig.suptitle("Türkiye Covid-19 Verileri")



eksen.legend(fontsize=6.2)


plt.show()

fig.savefig("yenifigür.png",dpi=400)