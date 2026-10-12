# agent_core

Python 기초부터 보안 로그 분석, API, LLM, AI Agent, 보고서 자동화, Webhook 알림, 테스트와 디버깅까지 단계적으로 실습한 코드를 모아 둔 폴더입니다.

처음에는 변수·리스트·딕셔너리 같은 Python 기본 문법부터 시작했고, 이후 배운 내용을 계속 연결해 최종적으로 보안 경보를 분석하고 보고서와 알림까지 생성하는 작은 자동화 파이프라인을 구성했습니다.

---

## 학습 흐름

```text
Python 기본 문법
    ↓
로그 파싱 · 정규화
    ↓
탐지 규칙 · 예외 처리
    ↓
HTTP API · requests
    ↓
Flask · Webhook · CLI
    ↓
LLM 호출 · JSON 파싱
    ↓
AI Agent · Tool Routing
    ↓
경보 요약 · Triage
    ↓
Markdown 보고서
    ↓
설정 분리 · Pipeline
    ↓
단위 테스트 · 디버깅
```

---

## 주요 학습 내용

### Python 기본
- 변수, 리스트, 딕셔너리
- 조건문, 반복문, 함수
- `append()`, `.get()`, `Counter`
- 파일 읽기·쓰기
- JSON
- `try / except`

### 로그 분석
- 로그 파싱과 정규화
- 정규표현식과 Named Group
- 로그인 실패, 심야 접속 등의 탐지 규칙
- Logging을 이용한 실행 기록

### API · Webhook
- `requests`를 이용한 HTTP 요청
- GET / POST
- 상태 코드
- `headers`, `params`, `timeout`
- Flask 서버
- `curl`
- Webhook

### LLM
- LLM API 호출
- 프롬프트 작성
- 구조화된 JSON 출력
- `temperature`
- LLM 응답 파싱과 예외 처리

---

## AI Agent

LLM이 직접 모든 작업을 수행하는 것이 아니라 사용할 도구를 선택하고, 실제 실행은 Python 코드가 담당하는 구조를 실습했습니다.

```text
사용자 목표
    ↓
LLM이 도구 선택
    ↓
Tool Router
    ↓
Python 함수 실행
    ↓
결과 반환
```

영향이 큰 작업은 바로 실행하지 않고 사람이 승인한 경우에만 실행하도록 승인 단계도 추가했습니다.

---

## 보고서 자동화

많은 보안 경보를 Batch 단위로 나누어 LLM으로 요약하고 위험도 순으로 정렬했습니다.

```text
보안 경보
    ↓
Batch 처리
    ↓
LLM 요약
    ↓
HIGH → MEDIUM → LOW
    ↓
Markdown 보고서
```

정확한 건수와 보고서 구조는 Python 코드가 담당하고, LLM은 사람이 읽기 좋은 요약과 총평을 만드는 데 사용했습니다.

---

## Pipeline

여러 기능을 하나의 실행 흐름으로 연결했습니다.

```text
events.json
    ↓
event_summarizer.py
    ↓
report_generator.py
    ↓
notifier.py
    ↓
pipeline.py
    ↓
보고서 생성 + Webhook 알림
```

```bash
python pipeline.py
```

---

## 설정과 민감정보 관리

변경될 수 있는 값과 비밀 정보를 코드에서 분리했습니다.

```text
.env
→ API Key 등 민감정보

config.json
→ Model, 승인 기준, 보고서 폴더, Webhook URL
```

또한 `.gitignore`를 사용해 민감정보와 불필요한 파일이 GitHub에 올라가지 않도록 관리했습니다.

---

## 테스트와 디버깅

주요 함수는 `assert`를 이용해 자동으로 확인했습니다.

```python
assert 함수(입력) == 기대값
```

`test_agent_core.py`에 테스트를 모아 한 번에 실행할 수 있도록 했습니다.

```bash
python test_agent_core.py
```

실습하면서 다음 오류도 직접 확인하고 수정했습니다.

- `SyntaxError`
- `KeyError`
- `NameError`
- 논리 오류

오류가 발생하면 Traceback의 마지막 줄부터 확인하고, 결과가 예상과 다를 때는 중간 값을 출력해 원인을 찾는 방식으로 디버깅했습니다.

---

## 주요 파일

| 파일 | 역할 |
|---|---|
| `llm_client.py` | LLM 호출 및 JSON 응답 처리 |
| `tool_router.py` | Agent 도구 등록 및 실행 |
| `event_summarizer.py` | 경보 요약 및 위험도 정렬 |
| `report_generator.py` | Markdown 보고서 생성 |
| `notifier.py` | 설정 확인 및 Webhook 알림 |
| `pipeline.py` | 전체 작업 흐름 연결 |
| `test_agent_core.py` | 주요 함수 단위 테스트 |
| `*_실습.ipynb` | 날짜별 실습 노트북 |

---

## 학습하면서 느낀 점

처음에는 Python 문법 하나씩 이해하는 데 집중했지만, 수업이 진행되면서 이전에 배운 내용을 다시 사용해 여러 파일과 함수를 하나의 프로그램으로 연결하는 경험을 할 수 있었습니다.

특히 다음 내용을 중요하게 배웠습니다.

- LLM 결과를 그대로 믿지 않고 다시 검증하기
- 오류가 나도 전체 프로그램이 멈추지 않도록 처리하기
- 설정과 민감정보를 코드에서 분리하기
- 테스트와 디버깅으로 결과를 다시 확인하기

아직 모든 코드를 처음부터 혼자 작성하는 단계는 아니지만, 각 함수와 파일이 어떤 역할을 하고 데이터가 어떤 순서로 이동하는지는 조금씩 이해할 수 있게 되었습니다.
