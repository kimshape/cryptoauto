import pyupbit

access = "MJryrFhH6u9Luwc1ORGpVaJOB7Cjzr86gxpmx4ph"       
secret = "uyuILZvdhRxexuAOjtrZl2YYN8UWMj9dBUGKLPtx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-GAS"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회




