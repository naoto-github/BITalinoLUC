# coding: utf_8

from bitalino import BITalino

macAddress = "20:16:12:21:35:82" # MACアドレス

device = BITalino(macAddress) # デバイスの取得
print(device.version()) # バージョンの表示

Samplingrate = 1000 # サンプリングレート
Acqchannels = [0] # 取得チャネル（A1）
Nsamples = 10 # 取得サンプル数

Device.Start(Samplingrate, Acqchannels) # データ取得開始
Data = Device.Read(Nsamples)
Print(Data)


Device.Stop()
Device.Close()
