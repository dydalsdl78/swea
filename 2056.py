import sys
sys.stdin = open("2056.txt")

T = int(input())

for t in range(1, T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = int(date[6:])
    str_day = date[6:]

    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' \
            or month == '10' or month == '12':
        if day > 31:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{str_day}')
    elif month == '04' or month == '06' or month == '09' or month == '11':
        if day > 30:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{str_day}')
    elif month == '02':
        if day > 28:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{str_day}')
    elif month == '00':
        print(f'#{t} -1')
    else:
        print(f'#{t} {year}/{month}/{str_day}')
