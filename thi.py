'''
THI = temperature-humidity index
Calculation: https://ja.wikipedia.org/wiki/%E4%B8%8D%E5%BF%AB%E6%8C%87%E6%95%B0
'''


def get_thi(temp, hum):
    return 0.81*temp + 0.01*hum*(0.99*temp-14.3) + 46.3


def get_thi_level(thi):
    if thi < 70:
        return 1
    elif thi < 75:
        return 2
    elif thi < 80:
        return 3
    elif thi < 85:
        return 4
    else:
        return 5
