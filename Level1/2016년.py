def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0
    a = a - 1
    for i in range(a):
        total_day += days[i]
    total_day += b

    if total_day % 7 == 1:
        answer = 'FRI'
    elif total_day % 7 == 2:
        answer = 'SAT'
    elif total_day % 7 == 3:
        answer = 'SUN'
    elif total_day % 7 == 4:
        answer = 'MON'
    elif total_day % 7 == 5:
        answer = 'TUE'
    elif total_day % 7 == 6:
        answer = 'WED'
    elif total_day % 7 == 0:
        answer = 'THU'
    return answer