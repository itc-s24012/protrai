# s24012
# 現在の時刻と6月のカレンダー


import calendar as cal
print(cal.month(2024,7))


import datetime
now = datetime.datetime.now()
print(now)

print(now.strftime("%Y年%m月%d日　%H:%M:%S"))
