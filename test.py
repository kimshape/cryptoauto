import pyupbit

access = "ImZ2I3X2hpmhnc9tf841gghoOtjUug1gAH0hrwUO"       
secret = "xZDwEvT5AAgGTHBr7K4XhVtl4cfEReHIZuAom9aX"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-GAS"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회




