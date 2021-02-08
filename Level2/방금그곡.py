
# def solution(m, musicinfos):
#     answer = []
#     m = change(m)
#     for i in musicinfos:
#         tmp = i.split(',')
#         start_s, start_e, end_s, end_e = map(int, tmp[0].split(':') + tmp[1].split(':'))
#         music_time = 60 *(end_s-start_s) + (end_e - start_e)
#         tone = change(tmp[3])
#         tone_tmp = (tone * music_time)[:music_time]
#         if m in tone_tmp :
#             if not answer:
#                 answer.append(tmp[2])
#                 answer.append(music_time)
#             if answer[1] < music_time:
#                 answer[0] = tmp[2]
#                 answer[1] = music_time
#     return answer[0]


def change(melody):
    if 'A#' in melody: melody = melody.replace('A#', 'a')
    if 'C#' in melody: melody = melody.replace('C#', 'c')
    if 'D#' in melody: melody = melody.replace('D#', 'd')
    if 'F#' in melody: melody = melody.replace('F#', 'f')
    if 'G#' in melody: melody = melody.replace('G#', 'g')
    return melody
def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]