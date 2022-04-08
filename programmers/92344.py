# 신고 결과 받기

def solution(id_list, report, k):
    report_count, report_list = {name: [] for name in id_list}, []
    answer = [0 for _ in id_list]

    for r in set(report):
        report_count[r.split()[1]].append(r.split()[0])

    for key, value in report_count.items():
        if len(value) >= k:
            report_list.append(key)

    if report_list == []:
        return answer

    for r in set(report):
        if r.split()[1] in report_list:
            answer[id_list.index(r.split()[0])] += 1

    return answer
