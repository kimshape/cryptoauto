import pyupbit
import numpy as np
#OHLCV란, (open,high,low,close,volume) 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-ETH", count=7) # 7일 동안의 원화 BTC 시장에 대한 OHLCV

#변동폭 * k 계산, (고가-저가) * k값
df['range'] = (df['high'] - df['low']) * 0.1

#target(매수가) , range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

#ror(수익률), np.where(numpy : 조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
#누적 곱 계산(cumprod) = > 누적 수익률
df['hpr'] = df['ror'].cumprod()


df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")

print(df)