def solution(a, b):
    answer = ''
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = 0
    for day in range(a):
        days += months[day]
    days += b
    days -= 1
    return weeks[days % 7]