LOG = [("schoolnote.invalid", "NOERROR", "정상"), ("learningplatform.invalid", "NOERROR", "정상"),  # 정상 도메인 2개
       ("oldlibrary.invalid", "NXDOMAIN", "정상"), ("kxq7mz9pw2.invalid", "NXDOMAIN", "의심"),      # 오탐을 유도하는 정상 도메인과 DGA 의심 도메인
       ("secure-bank-login.invalid", "NOERROR", "의심"), ("zq8w4n6r1m.invalid", "NXDOMAIN", "의심")]  # 은행 사칭과 DGA 의심 도메인
for name, rcode, truth in LOG:                    # 튜플을 하나씩 꺼내 이름은 name, 응답은 rcode, 실제는 truth 에 나눠 담아 반복한다
    parts = name.split(".")                       # 이름을 점으로 나눈 리스트를 parts 에 담는다
    score = 0                                     # 이 이름의 점수를 0 으로 시작한다
    if len(parts[-2]) >= 10:                      # 규칙 ①: TLD 바로 앞 레이블이 10글자 이상이면
        score = score + 1                         # 1점을 더한다
    if parts[-1] in ["top", "xyz", "tk"]:         # 규칙 ②: TLD 가 세 값 가운데 하나이면
        score = score + 1                         # 1점을 더한다
    if rcode == "NXDOMAIN":                       # 규칙 ③: 응답이 NXDOMAIN 이면
        score = score + 2                         # 2점을 더한다
    print(name, score, score >= 3, "실제:", truth)  # 이름 · 점수 · 규칙의 판정(True 가 의심) · 실제를 한 줄에 출력한다
