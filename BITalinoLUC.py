# coding: utf_8

from bitalino import BITalino

macAddress = "20:16:12:21:35:82" # MACアドレス

device = BITalino(macAddress) # デバイスの取得
print(device.version()) # バージョンの表示

samplingRate = 1000 # サンプリングレート
acqChannels = [0] # 取得チャネル（A1）
nSamples = 10 # 取得サンプル数

device.start(samplingRate, acqChannels) # データ取得開始
data = device.read(nSamples)
print(data)

device.stop()
device.close()
