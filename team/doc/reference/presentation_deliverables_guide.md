# Project-2 발표 산출물 제작 가이드

> **팀**: 데2터로말해조
> **발표일**: 2026-05-09 (토)
> **최종 제출**: `[데2터로말해조] Project2 결과물.pdf` (단일 PDF)
> **함께 보기**: `guides/deliverables_checklist.md` (항목/마감), `guides/pencil_mcp_guide.md` (Pencil 설치 상세)
> **읽는 시간**: 5분

---

## 1. 최종 산출물과 도구 매핑

최종 제출은 **PDF 1개**. 그래서 "HTML → PDF" 가 **주 경로** (팀 워크샵 #4 와 동일). Pencil MCP 는 카드뉴스·시각 보조 자료에 사용 (워크샵 #2).

| 산출물 | 도구 | 워크샵 | 비고 |
|---|---|---|---|
| **최종 발표 PDF (8섹션)** | HTML → Playwright PDF | #4 (5/2) | M3 제출물 |
| **카드뉴스 · PDP 시안 · 시각 보조** | Pencil MCP (`.pen`) | #2 (4/25) | M3 디자인 항목 |
| 분석 차트 | Python(matplotlib) / Looker export | — | HTML 슬라이드에 이미지로 삽입 |
| (옵션) 발표 현장용 PPT | python-pptx | — | 요구사항 아님. 필요 시 백업용 |

> **핵심 원칙**: 최종 제출은 PDF 이므로 "슬라이드 = HTML 페이지" 로 만들어 Playwright 로 PDF export. Pencil 목업은 이미지로 HTML 안에 삽입.

---

## 2. 팀원 설치 체크리스트

각자 PC 에서 한 번만 설정.

### ✅ Claude Code
- 공식: <https://claude.com/claude-code>
- 확인: 터미널에 `claude --version`

### ✅ Pencil MCP (시안 · 목업 · 카드뉴스)

**설치 (CLI)**
```bash
claude mcp add pencil npx pencil-mcp
claude mcp list
```

**설치 (VS Code 확장)**
1. VS Code 확장 마켓에서 "Claude Code" 설치
2. Anthropic 계정 로그인
3. VS Code 터미널에서 위 `claude mcp add` 실행

> `.pen` 파일은 Claude Code 안에서만 열림 (암호화 포맷). 상세는 `guides/pencil_mcp_guide.md`.

### ✅ gstack 스킬 (선택 — `/design-shotgun` 등 쓰려면)

- 공식: <https://github.com/garrytan/gstack>
- 요구: Git, Node.js, Bun 1.0+

```bash
git clone --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup --team
```

### ✅ Playwright (HTML → PDF 용, 주 경로)

```bash
pip install playwright
playwright install chromium
```

> `playwright install chromium` 누락 시 실행 에러.

### ✅ python-pptx (옵션, 현장 백업용 PPT 가 필요할 경우)

```bash
pip install python-pptx
```

---

## 3. 스킬 치트시트

> 대화창에 `/스킬명` 입력. gstack 설치 필요.

| 스킬 | 한 줄 용도 | 호출 예시 |
|---|---|---|
| `/brainstorming` | 아이디어를 설계 문서로 정리 (승인 전 구현 금지 하드게이트) | `/brainstorming 재구매 유도 PDP` |
| `/design-consultation` | 디자인 시스템 `DESIGN.md` (팔레트·폰트·간격) | `/design-consultation 브라질 이커머스 PDP, 신뢰감·가격 강조` |
| `/design-shotgun` | **PDP 시안 3~5개 병렬 생성 + 비교 보드** | `/design-shotgun Olist PDP 메인, 가격/리뷰/배송 배치 3안` |
| `/design-html` | 승인 시안 → 반응형 HTML/CSS (발표 슬라이드에 그대로 활용 가능) | `/design-html 시안 A를 HTML로` |
| `/design-review` | 라이브 HTML 시각 QA + 자동 수정 | `/design-review http://localhost:8080` |
| `/qa` | 페이지 동작 QA + 버그 자동 수정 | `/qa http://localhost:8080` |

**스킬 조합 순서**: `/brainstorming → /design-consultation → /design-shotgun → /design-html → /design-review`

---

## 4. Pencil 최소 사용법 (시안 · 목업 · 카드뉴스)

> `.pen` 파일이 **열려 있어야** Pencil 도구가 동작. 반드시 `open_document` 부터.

### 시작 3단계

```
1) 새 파일 만들기
   mcp__pencil__open_document('new')

2) 상태 확인
   mcp__pencil__get_editor_state({ include_schema: true })

3) 가이드/스타일 로드
   mcp__pencil__get_guidelines()
   mcp__pencil__get_guidelines({ category: 'style', name: '<이름>' })
```

### PDP 시안 구성 팁

- **1개 `.pen` 안에 Artboard 3개**로 시안 A/B/C
  - A: 가격/혜택 상단
  - B: 리뷰/평점 상단
  - C: 배송/교환·환불 상단
- **variable 로 색/폰트 정의** → 한 번 바꾸면 3개 Artboard 동시 리브랜딩
- **완성 후 PNG export**: `mcp__pencil__export_nodes({ nodeIds: [...], format: 'png' })`
- export 한 PNG 를 HTML 슬라이드에 `<img>` 로 삽입 → 그대로 PDF 까지 이어짐

> **시안 A/B/C 는 "색"이 아니라 "정보 배치 구조"** 로 달라야 함. 색만 바꾸면 비교의 의미가 없음.

---

## 5. HTML → PDF 주 경로 (최종 제출물 생성)

### 최소 스크립트

```python
from playwright.sync_api import sync_playwright
from pathlib import Path

HTML = Path("slides.html").resolve()
PDF  = Path("[데2터로말해조] Project2 결과물.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(HTML.as_uri())
    page.pdf(
        path=str(PDF),
        width="1920px", height="1080px",   # 16:9 슬라이드 비율
        print_background=True,             # ★ 이거 빼먹으면 색 안 나옴
        margin={"top":"0","bottom":"0","left":"0","right":"0"},
    )
    browser.close()
```

### HTML 슬라이드 작성 규칙

- 슬라이드 1장 = `<section class="slide">...</section>` 한 개
- 각 `section` 사이에 CSS 로 `page-break-after: always;` 지정 → PDF 에서 자동 페이지 분절
- 웹폰트는 HTML 안에 `@font-face` 로 직접 임베드 (CDN 만 쓰면 PDF 에서 깨질 수 있음)
- 한글 폰트는 `noto-sans-kr` 권장 (오픈소스, 임베드 가능)

### 체크리스트

- [ ] `print_background=True` (1순위 실수)
- [ ] 16:9 비율 (`1920×1080`) 또는 A4 가로 중 택1
- [ ] `page-break-after: always;` 로 섹션 분절
- [ ] 이미지는 상대 경로 + 고해상도 PNG
- [ ] 완성 후 스마트폰으로 PDF 열어 가독성 확인

---

## 6. 발표 슬라이드 8섹션 구조 (공식, 15분)

> `deliverables_checklist.md` 기준. HTML 에서 section 순서로 그대로 구현.

| # | 섹션 | 시간 | 슬라이드 구성 힌트 |
|---|---|---|---|
| 1 | 프로젝트 개요 + 문제 정의 & 가설 | 2분 | 커버 + 문제 한 줄 + 가설 카드 |
| 2 | 데이터 구조 + 전처리 | 1분 | ERD 썸네일 + 결측/이상치 처리 한 장 |
| 3 | 핵심 분석 지표 | 1분 | KPI 정의 카드 (재구매율·AOV·RFM·저평점) |
| 4 | 대시보드 시각화 | 3분 | Looker 화면 캡처 + 주요 차트 3~4장 |
| 5 | 비즈니스 인사이트 | 3분 | 발견 요약 + **PDP Before/After 시안** (Pencil export) |
| 6 | 전략 Action Plan | 2분 | 3~5개 구체 액션 카드 |
| 7 | 결론 | 1분 | 한 장 요약 |
| 8 | R&R + 회고 | 2분 | 역할 분담 표 + 배운 점 |

> Q&A 5분 포함. 예상 Q&A 는 마지막 PDF 뒤에 첨부.

---

## 7. 추천 제작 순서 (마일스톤 기준)

### M2 주간 (~5/2)
- [ ] 분석 결과 차트 PNG 정리 (Looker export + matplotlib)
- [ ] 워크샵 #2 결과 반영 → Pencil 시안 · 카드뉴스 초안
- [ ] 발표 스토리라인 확정 (deliverables_checklist M2 기준)

### M3 주간 (5/3~5/8)
- [ ] 워크샵 #4 에서 배운 방식으로 HTML 슬라이드 작성 (8섹션)
- [ ] Pencil PNG 를 HTML 에 삽입
- [ ] Playwright 스크립트로 PDF 추출 → 파일명 `[데2터로말해조] Project2 결과물.pdf`
- [ ] 리허설 1회 (페이지당 체류 시간 측정)

### 제출일 (5/9)
- [ ] 마지막 오탈자 수정 → 최종 PDF 재추출 → 23:59 까지 제출

---

## 8. 역할 분담 힌트 (5인, 참고용)

| 역할 | 담당 |
|---|---|
| **디자인** | Pencil 시안 A/B/C, 카드뉴스, 디자인 시스템 |
| **시각화** | Looker/Python 차트 PNG 정리, 네이밍 규칙 통일 |
| **슬라이드 빌드** | HTML 슬라이드 작성, Playwright PDF 스크립트 |
| **스토리/스크립트** | 8섹션 스토리라인, 예상 Q&A 목록 |
| **리뷰/QA** | `/design-review` 또는 수동 체크, 리허설 |

---

## 9. 자주 실수하는 5가지

1. 디자인 시스템(톤/컬러/폰트) 없이 시안부터 → 팀 톤이 안 맞음
2. 시안 A/B/C 를 "색만 다르게" → 비교가 무의미 (정보 배치 축을 다르게)
3. Pencil 도구를 파일 열지 않고 호출 → 에러 (`open_document` 부터)
4. Playwright `print_background=True` 누락 → PDF 색 사라짐
5. 한글 폰트를 CDN 으로만 로드 → PDF 에서 깨짐 (HTML 안에 `@font-face` 임베드)
