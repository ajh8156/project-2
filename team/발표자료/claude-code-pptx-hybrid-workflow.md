# Claude Code 하이브리드 PPT 워크플로우 가이드

> 부트캠프 팀 프로젝트 발표용 (디자인 임팩트 + PPT 편집 가능성 + 토큰 효율)
>
> 최종 수정일: 2026-05-02

## 🎨 디자인 시스템

| 자료 | 링크 |
|------|------|
| 2팀-올리스트 발표 오브제 (Google Slides) | https://docs.google.com/presentation/d/1fyXpItrPbdbY1yPxc7EJ_oT1diiOraqEVJpYTTHfpAM/edit?slide=id.p#slide=id.p |

### 수정 내역

| 날짜 | 내용 |
|------|------|
| 2026-05-02 | v1 작성 — §0 우리 프로젝트 적용 신설(디자인 시스템·파트·폴더·HTML 후보·레퍼런스·manifest) + 팀원 가독성 구조(TL;DR / 논의 결정 박스 / 일반 가이드 §1~§7 접기) + TF 폴더 표준 구조 명시(README · talking-points · `assets/`로 이미지 분리) |
| 2026-05-02 | 디자인 시스템 링크(2팀-올리스트 발표 오브제 Google Slides) 상단 추가 |

---

## 목차

- [⚡ TL;DR — 팀원용 1페이지 요약](#-tldr--팀원용-1페이지-요약)
- [🎯 논의·결정 필요 사항](#-논의결정-필요-사항)
- [§0. 우리 프로젝트 적용 ★](#0-우리-프로젝트-적용)
  - [0-1. 디자인 시스템 (확정)](#0-1-디자인-시스템-확정)
  - [0-2. 파트 정의 (12개)](#0-2-파트-정의-12개)
  - [0-3. 우리 발표자료 폴더 구조](#0-3-우리-발표자료-폴더-구조)
  - [0-4. HTML로 만들 슬라이드 후보](#0-4-html로-만들-슬라이드-후보-6장-메인덱-약-20)
  - [0-5. 레퍼런스 자료](#0-5-레퍼런스-자료-프로젝트-루트-기준-상대경로)
  - [0-6. manifest.md 작성 예시](#0-6-manifestmd-작성-예시)
- [📚 일반 가이드 (참고용 — 처음엔 안 읽어도 됨)](#-일반-가이드-참고용--처음엔-안-읽어도-됨)
- [부록 A: 파트 정의 가이드 (다른 프로젝트 적용용)](#부록-a-파트-정의-가이드-다른-프로젝트-적용용)
- [부록 B: 빠른 시작 체크리스트](#부록-b-빠른-시작-체크리스트)

---

## ⚡ TL;DR — 팀원용 1페이지 요약

> 처음 5분이면 이 섹션만 읽고 작업 시작 가능.
> 더 자세한 내용은 §0에서, 일반 워크플로우 이론은 맨 아래 "일반 가이드"에서.

### 당신이 지켜야 할 4가지 룰

1. **컬러·폰트는 `styles.css`의 CSS 변수로만 사용** — 직접 색상값 박지 마세요. (예: `var(--tf3)` 사용, `#34A853` 직접 입력 X)
2. **슬라이드 식별은 파트명으로** — `cover` / `hook` / `peak` / `tf3` / `cta` 등. 슬라이드 번호는 발표 직전까지 변동 가능.
3. **절대 경로 금지** — 팀원마다 로컬 폴더 위치가 다름. 항상 **프로젝트 루트 기준 상대경로**만.
4. **HTML 슬라이드는 6장만** — 전체 27장 중 비주얼 정점만. 나머지 ~21장은 PPT에서 직접 작성.

### 컬러 빠른 참조

| CSS 변수 | 값 | 용도 |
|---|---|---|
| `--tf1` | `#EA4335` | TF1 배송 품질 |
| `--tf2` | `#FBBC04` | TF2 구매 경험 |
| `--tf3` | `#34A853` | TF3 재구매 유도 ★ 발표 핵심 |
| `--color-cta` | `#1A73E8` | 결론·CTA — Olist Blue |
| `--color-text` | `#1F2937` | 본문 텍스트 |
| `--color-muted` | `#5F6368` | 보조 정보 |

전체 변수는 [§0-1 디자인 시스템](#0-1-디자인-시스템-확정) 참조.

### HTML로 만들 6장

`cover` · `hook` · `peak` · `tf-intro` · **`tf3` ★ 1순위** · `cta`

### 우리 발표자료 폴더 구조

```
team/발표자료/
├── 슬라이드_구성안_v2.md           ← 전체 27장 스토리 SSOT
├── claude-code-pptx-hybrid-workflow.md   ← 본 문서
├── TF1-배송품질/  TF2-구매경험/  TF3-재구매/   ← 각 폴더 = README + talking-points + assets/
├── slides/                         ← HTML 영역
│   ├── _shared/
│   │   ├── styles.css              ← 디자인 시스템 코드 SSOT
│   │   └── reference/olist_logo.png
│   ├── cover.html · hook-conclusion.html · peak-aha.html
│   ├── tf3-lifecycle.html · cta-4step.html
│   └── all-slides.html             ← PDF export 통합본
└── exports/                        ← PDF/PNG 결과물
```

---

## 🎯 논의·결정 필요 사항

### ✅ 이미 결정된 사항 (변경 시 팀 합의 필요)

| 결정 | 내용 | 이유 |
|---|---|---|
| HTML 6장 합의 | cover · hook · peak · tf-intro · **tf3 ★** · cta | 비주얼 정점 / 토큰 효율 / 발표 임팩트 |
| 신호등 색 분리 | TF 색계(R/Y/G)와 신호등 색(R/Y/G) 충돌 → 신호등은 **차콜 농도** 시리즈로 변경 | 한 화면에서 의미 혼란 방지 |
| SSOT 위계 | `styles.css` (코드, 최종 권위) > 본 문서 §0-1 (텍스트 스펙) > Pencil 디자인 시트 (시각 참조) | 충돌 시 코드를 정답으로 |
| PPT 번호 변동 가능성 | 식별은 **파트명**으로만 — 번호는 manifest.md에서만 관리 | PPT 틀이 발표 직전까지 바뀜 |
| 절대 경로 금지 | 모든 경로는 프로젝트 루트 기준 상대경로 | 팀원마다 로컬 폴더 다름 |

### ⏳ 아직 논의 필요 / 열린 항목

- (현재 없음 — 추가 결정 사항이 생기면 여기 기록)

---

## 0. 우리 프로젝트 적용

> 5/9 발표("데2터로말해조") 적용 SSOT.
> 일반 가이드(맨 아래)는 이론·다른 프로젝트용. 본 §0가 우리 프로젝트 결정사항을 덮어씀.
> 슬라이드 순서·번호는 [슬라이드_구성안_v2.md](슬라이드_구성안_v2.md)가 SSOT — 본 문서는 시각·코드 적용 가이드.

### 0-1. 디자인 시스템 (확정)

#### 컬러 팔레트

```css
:root {
  /* Primary — TF별 식별색 */
  --tf1: #EA4335;          /* TF1 배송 품질 */
  --tf2: #FBBC04;          /* TF2 구매 경험 */
  --tf3: #34A853;          /* TF3 재구매 유도 (★ 발표 핵심) */
  --color-cta: #1A73E8;    /* 결론·CTA — Olist Blue */

  /* Neutral */
  --color-text: #1F2937;
  --color-muted: #5F6368;
  --color-border: #E5E7EB;
  --color-surface: #F9FAFB;
  --color-bg: #FFFFFF;

  /* Soft — 카드 배경·강조 영역 */
  --tf1-soft: #FCE8E6;
  --tf2-soft: #FEF7E0;
  --tf3-soft: #E6F4EA;
  --cta-soft: #E8F0FE;
}
```

#### 타이포그래피 4단계

| 역할 | 크기 | 굵기 | line-height | 용도 |
|---|---|---|---|---|
| Title | 48px | 700 | 1.2 | 표지·섹션 디바이더 |
| Heading | 32px | 700 | 1.3 | 슬라이드 제목·섹션 헤더 |
| Body | 18px | 400 | 1.5 | 본문·리스트 |
| Caption | 12px | 400 | 1.4 | 각주·메타·라벨 |

폰트: **Pretendard** (한글) / 시스템 산세리프 (영문)

#### Olist 브랜드 톤

- 로고: 파란색(#1A73E8 계열) 단색 워드마크, 흰 배경
- 톤: 깔끔·여백 충분·신뢰감 — 카드 보더 + 좌측 색띠 + 흰 배경 베이스
- 출처 시안: PDP v2 / Thank-you v1 (`team/cx/images/`)

#### 핵심 컴포넌트

| 컴포넌트 | 구성 | 사용처 |
|---|---|---|
| 신호등 뱃지 | dot + 라벨, **차콜 농도 시리즈**로 심각도 표현 (TF 색과 분리) | diagnose / bottleneck 파트 |
| KPI 카드 | 좌측 6px 색띠 + eyebrow + 큰 수치 + delta | tf-intro / tf3 / cta |
| CTA 버튼 | 14/22 padding, cornerRadius 8, fill `--color-cta` | hook / cta |
| Soft 카드 | `*-soft` 배경 + 1px border | 강조 콜아웃 |

**슬라이드 규격**: 16:9, 1920×1080 (deviceScaleFactor 2 → Retina 대응)

<details>
<summary><strong>📐 신호등 뱃지 색 정책 — 차콜 농도 시리즈 (펼치기)</strong></summary>

| 단계 | 배경 | 보더 | dot | 텍스트 |
|---|---|---|---|---|
| Critical · 적신호 | `--color-surface` | `--color-text` | `--color-text` (진한 차콜) | `--color-text` |
| Watch · 주의 | `--color-surface` | `--color-muted` | `--color-muted` (중간 회색) | `--color-text` |
| Healthy · 정상 | `--color-surface` | `--color-border` | `#9CA3AF` (옅은 회색) | `--color-text` |

**왜 차콜 농도?** TF1=빨강 / TF2=노랑 / TF3=녹색이 신호등 R/Y/G와 같은 색이라 한 화면에서 의미가 충돌. 신호등은 차콜 농도로만 심각도를 표현해 청중 혼란 제거.

</details>

<details>
<summary><strong>🎨 디자인 시트 (Pencil) — 시각 참조 (펼치기)</strong></summary>

| 항목 | 값 |
|---|---|
| 파일 | `team/seller_ops/pencil-new.pen` |
| 노드 ID | `BFCHS` (DesignSystem_Sheet) |
| 위치 | 캔버스 (4120, 0) — thankyou_v2 영역 우측 |
| 규격 | 1920×1080 (16:9, 슬라이드 1장 크기) |
| 구성 | 01 Color Palette · 02 Typography · 03 Components · 04 Brand |
| 용도 | HTML 슬라이드 제작 시 시각 참조 (코드 작성은 styles.css 기준) |

> Pencil 시트는 **참조용**. 색·치수 변경은 항상 `styles.css` 먼저 수정하고 시트는 따라 갱신.

</details>

### 0-2. 파트 정의 (12개)

슬구안 v2 Act 1~9 구조에 맞춘 파트 prefix.

| prefix | Act | 의미 |
|---|---|---|
| `cover` | Act 1 | 표지 |
| `hook` | Act 1 | 결론 먼저 (반전 + BF 카드) |
| `diagnose` | Act 2 | 현황 (3축 신호등 / RFM) |
| `bottleneck` | Act 3 | 병목 (KPI Tree × AARRR / 저평점 분해) |
| `peak` | Act 3.5 | 🔥 단 하나의 통찰 |
| `cause` | Act 4 | 원인 규명 (Finding + 가설 검증) |
| `tf-intro` | Act 5 | TF 정당성 / 매트릭스 / 이중 트랙 |
| `tf1` | Act 6 | TF1 배송 품질 |
| `tf2` | Act 6 | TF2 구매 경험 |
| `tf3` | Act 6 | TF3 재구매 유도 (★ 발표 핵심) |
| `cta` | Act 7 | 결론 재선언 / 기대효과 / CTA |
| `reference` | Act 8 | Looker 대시보드 + 추가 자료 |
| `qna` | Act 9 | Q&A |

> 동일 파트 내 여러 슬라이드는 `{prefix}-{설명}` (예: `tf3-lifecycle-journey`, `tf3-bundle-card`).

### 0-3. 우리 발표자료 폴더 구조

```
team/발표자료/
├── 슬라이드_구성안_v2.md           ← 전체 27장 스토리 SSOT
├── claude-code-pptx-hybrid-workflow.md   ← 본 문서 (제작 가이드)
├── TF_파트_강화안_v1.md             ← TF별 슬라이드 디테일
│
├── TF1-배송품질/                    ← TF별 산출물 폴더 (아래 표준 구조)
├── TF2-구매경험/                    ← ▼ 표준 구조 예시 (5/2 정리 완료)
│   ├── README.md                    ← 폴더 인덱스 + 진행 상태 + 네이밍 규칙
│   ├── tf2-talking-points.md        ← 발표 설득 포인트 + 1분 멘트 + Q&A
│   └── assets/                      ← ★ 이미지 산출물은 모두 여기에
│       ├── tf2-thankyou-*.png       (시안 PNG)
│       └── tf2-data-*.png           (분석 데이터 PNG)
├── TF3-재구매/
│
├── slides/                          ← HTML 영역 (5/2 신규)
│   ├── _shared/
│   │   ├── styles.css               ← 디자인 시스템 코드 SSOT
│   │   └── reference/olist_logo.png ← 브랜드 자산
│   ├── cover.html
│   ├── hook-conclusion.html
│   ├── peak-aha.html
│   ├── tf3-lifecycle.html           ← ★ 1순위
│   ├── cta-4step.html
│   └── all-slides.html              ← PDF export용 통합본
│
└── exports/                         ← PDF / PNG 최종 결과물
    └── 데2터로말해조_발표_v1_5page.pdf
```

> 위는 **공통 약속**입니다. `team/발표자료/` 위쪽 경로(C:\Users\... 등)는 팀원마다 다르므로 적지 않습니다.

#### TF 폴더 표준 구조 — 3원칙

| 원칙 | 내용 | 이유 |
|---|---|---|
| **1. 텍스트 vs 이미지 분리** | 폴더 루트는 `.md` 문서만 / 모든 PNG·PDF는 `assets/` 하위로 | 깃헙 PR diff·내비게이션이 깔끔, 텍스트 리뷰 시 이미지에 가려지지 않음 |
| **2. 인덱스 + 설득 포인트 분리** | `README.md`(인덱스·진행 상태) + `{tfN}-talking-points.md`(발표 멘트·데이터 매핑) | README는 5분 스캔용 / talking-points는 발표 시 참조용 — 역할 분리 |
| **3. 파일명 prefix 통일** | `tf{N}-{유형}-{설명}.{ext}` (§0-2 파트 정의 따름) | 같은 폴더 안에서 산출물 종류·우선순위 한눈에 식별 |

**TF2 적용 예 (실제)**:

```
TF2-구매경험/
├── README.md                    ← 인덱스
├── tf2-talking-points.md        ← 설득 포인트
└── assets/
    ├── tf2-thankyou-*.png       ← 산출물 ③ (7장)
    ├── tf2-data-*.png           ← 분석 데이터 (3장)
    ├── (tf2-pdp-*.png)          ← 산출물 ① 예정
    ├── (tf2-cx-*.png)           ← 산출물 ② 예정
    └── (tf2-bf-*.png)           ← 산출물 ④ 예정
```

> TF1·TF3 폴더도 동일 구조로 확장.

### 0-4. HTML로 만들 슬라이드 후보 (~6장, 메인덱 약 20%)

비주얼 정점만 HTML로 제작. 나머지 ~21장은 PPT에서 직접 작성.

| 후보 슬라이드 (슬# 변동 가능) | 파트명 | HTML 채택 이유 |
|---|---|---|
| 표지 | `cover` | 발표 첫인상 — 디자인 임팩트 필요 |
| 결론 + BF 0.56% | `hook` | 사람 100명 그리드 + 반전 카드 (PPT 정밀 제작 어려움) |
| 🔥 5점·배송 통찰 | `peak` | 발표 감정 정점, 시각적 수렴 효과 |
| 이중 트랙 KR1 수렴 | `tf-intro` | 단기 TF + 장기 구조 → KR1 4.5% 화살표 |
| **Lifecycle Journey Map** ★ | `tf3` | 7터치포인트 + 산출물 4종 매핑 — 발표 후반부 시각적 정점 (제작 1순위) |
| CTA 4단 | `cta` | 발표의 진짜 결론, 박스 4개 시각화 |

> PPT 슬라이드 번호는 변동 가능 — **파트명을 SSOT로 사용**. 슬구안 v2 갱신 시 본 표 동기화.

### 0-5. 레퍼런스 자료 (프로젝트 루트 기준 상대경로)

레퍼런스 캡처는 프로젝트 내 기존 자산 활용. 팀원 각자 본인 환경에서 아래 경로의 파일을 참고 또는 `slides/_shared/reference/`로 복사.

| 자료 | 경로 (프로젝트 루트 기준) | 용도 |
|---|---|---|
| Olist 로고 | `team/cx/images/pdp_v2_pillow_gmarket/olist_logo.png` | 표지·CTA 슬라이드 브랜드 워드마크 |
| PDP v2 시안 (5장) | `team/cx/images/pdp_v2_pillow_gmarket/` | TF2 산출물 + 톤 레퍼런스 |
| Thank-you v1 시안 (6장) | `team/cx/images/thankyou_v1/` | TF3 D+0~D+30 터치포인트 + 톤 레퍼런스 |

> 컬러 팔레트는 §0-1 CSS 변수가 SSOT. PDP / Thank-you 시안은 톤·레이아웃 참조용.

### 0-6. manifest.md 작성 예시

전체 27장 매핑은 [슬구안 v2 §4](슬라이드_구성안_v2.md)를 SSOT로 사용. manifest.md는 **HTML 슬라이드 + 핵심 산출물만** 추적 (PPT 슬라이드는 빈번히 변동되므로 추적 부담 큼).

```markdown
# 슬라이드 매핑 (HTML 후보만)

## 발표 정보
- 주제: Olist 재구매 구조 진단 + TF 3개 실행안
- 발표일: 2026-05-09 (토)
- 비율: 16:9 (1920x1080)
- SSOT: 슬라이드_구성안_v2.md (전체 구조 / PPT 영역 포함)

## HTML 슬라이드 매핑

| 파트명 | 제목 | 소스 파일 | 사용 산출물 | 상태 |
|------|------|----------|-----------|------|
| cover | 표지 | slides/cover.html | _shared/reference/olist_logo.png | 대기 |
| hook | 결론 + BF 0.56% | slides/hook-conclusion.html | (사람 100명 그리드 코드 생성) | 대기 |
| peak | 🔥 5점·배송 통찰 | slides/peak-aha.html | (코드 생성) | 대기 |
| tf-intro | 이중 트랙 KR1 수렴 | slides/dual-track.html | (코드 생성) | 대기 |
| tf3 ★ | Lifecycle Journey Map | slides/tf3-lifecycle.html | assets/tf3-crm-mockup.png, assets/tf3-bundle-card.png | 1순위 |
| cta | CTA 4단 | slides/cta-4step.html | (코드 생성) | 대기 |

## 산출물 인벤토리 (HTML에 사용되는 것만)

| 산출물 | 출처 | 사용 슬라이드 | 상태 |
|--------|------|-------------|------|
| _shared/reference/olist_logo.png | team/cx/images/pdp_v2_pillow_gmarket/olist_logo.png | cover | ✓ 확정 |
| assets/tf3-crm-mockup.png | TF3 (CRM) 작업 | tf3 | 진행 중 |
| assets/tf3-bundle-card.png | TF3 (CRM) 작업 | tf3 | 진행 중 |

## Export 체크리스트
- [ ] exports/cover.png
- [ ] exports/hook-conclusion.png
- [ ] exports/peak-aha.png
- [ ] exports/dual-track.png
- [ ] exports/tf3-lifecycle.png
- [ ] exports/cta-4step.png
```

> **PPT 슬라이드는 manifest에 안 적음** — 슬구안 v2가 PPT 영역 SSOT.

---

## 📚 일반 가이드 (참고용 — 처음엔 안 읽어도 됨)

> **§0 우리 프로젝트 적용**을 다 보셨다면 여기는 건너뛰셔도 됩니다.
> 새 프로젝트에 적용하거나 워크플로우 이론·트러블슈팅이 필요할 때 펼쳐 보세요.

<details>
<summary><strong>§1. 워크플로우 전체 흐름도</strong></summary>

```
[레퍼런스 수집]              [기존 산출물 인벤토리]
       ↓                              ↓
       └──────→ [manifest.md 작성] ←──┘
                       ↓
            [공통 디자인 시스템 정의]
                       ↓
       ┌───────────────┴───────────────┐
       ↓                               ↓
[디자인 임팩트 슬라이드]         [텍스트/일반 슬라이드]
   HTML로 제작                     PPT에서 직접 작성
       ↓
   PNG export (고해상도)
       ↓
       └─────────→ [PPT 통합] ←──────────┘
                       ↓
                [최종 PDF export]
```

**핵심 원칙**: 디자인 임팩트가 필요한 슬라이드만 HTML로, 나머지는 PPT에서. 토큰 절약 + 수정 유연성 동시 확보.

</details>

<details>
<summary><strong>§2. HTML로 만들 슬라이드 판별 기준 (일반)</strong></summary>

| 슬라이드 유형 | 추천 도구 | 이유 |
|--------------|---------|------|
| 표지 / 섹션 디바이더 | HTML | 디자인 임팩트 중요 |
| 데이터 차트 (커스텀 스타일) | HTML | Recharts/Chart.js로 정교하게 |
| 지도 시각화 | HTML | Leaflet/Mapbox 활용 |
| 페르소나 카드 / 인포그래픽 | HTML | CSS Grid로 자유롭게 |
| 결론 / 요약 비주얼 | HTML | 비주얼 임팩트 |
| 목차 / 어젠다 | PPT | 텍스트 위주, 수정 잦음 |
| 본문 텍스트 슬라이드 | PPT | 빠른 수정 |
| 단순 표 / bullet 리스트 | PPT | PPT 기본 기능으로 충분 |
| Q&A 슬라이드 | PPT | 단순 |

**기준**: 전체의 **20~30%만 HTML**로. 욕심내면 토큰 폭발 + 수정 부담.

</details>

<details>
<summary><strong>§3. 일반 프로젝트 폴더 구조 (다른 프로젝트 적용용)</strong></summary>

> 우리 프로젝트 폴더 구조는 [§0-3](#0-3-우리-발표자료-폴더-구조)에서 확인. 아래는 일반 가이드.

```
project/
├── README.md                  # 프로젝트 개요
├── manifest.md                # 슬라이드 순서 + 산출물 매핑 (★ 핵심)
├── reference/                 # 디자인 레퍼런스
│   ├── tone.png               # 전체 톤 레퍼런스
│   ├── chart-style.png        # 차트 스타일 참고
│   └── color-palette.md       # 컬러 정의
├── slides/                    # HTML 슬라이드 (소스, 파트 기반 네이밍)
│   ├── _shared/
│   │   ├── styles.css         # 공통 CSS (디자인 시스템)
│   │   └── fonts/
│   ├── cover.html
│   ├── persona-overview.html
│   ├── geo-distribution.html
│   └── conclusion.html
├── assets/                    # 산출물 원본 (파트 기반 네이밍)
│   ├── persona-cards.png
│   ├── persona-data.csv
│   ├── geo-map.png
│   ├── model-feature.png
│   └── result-recommendation.csv
├── exports/                   # HTML → PNG 변환 결과 (HTML 파일명 그대로)
│   ├── cover.png
│   ├── persona-overview.png
│   └── ...
└── pptx/
    ├── template.pptx
    └── final.pptx
```

</details>

<details>
<summary><strong>§4. 단계별 가이드 (Step 1 ~ 6)</strong></summary>

### Step 1. 레퍼런스 수집 + 산출물 인벤토리

**레퍼런스 수집**
1. Pinterest/Behance에서 "data analysis presentation", "dashboard slide design" 검색
2. 마음에 드는 슬라이드 1~2개 캡처 → `reference/tone.png`
3. 차트 스타일 별도 캡처 → `reference/chart-style.png`
4. 컬러 팔레트 정의 (3~5색) → `reference/color-palette.md`

**산출물 인벤토리 작성** (이미 가지고 있는 것들)
- 차트 이미지, 지도 캡처, 분석 결과 데이터(CSV)를 한 폴더로 모음
- 다음 단계에서 **파트 기반 네이밍**으로 정리

### Step 2. 공통 디자인 시스템 정의 (1회만)

`slides/_shared/styles.css`에 CSS 변수로 정의 → 모든 슬라이드가 import

```css
/* slides/_shared/styles.css */
:root {
  /* 컬러 팔레트 */
  --color-primary: #2563eb;
  --color-secondary: #f59e0b;
  --color-bg: #ffffff;
  --color-text: #1f2937;
  --color-muted: #6b7280;
  --color-accent: #10b981;

  /* 타이포그래피 */
  --font-heading: 'Pretendard', sans-serif;
  --font-body: 'Pretendard', sans-serif;
  --fs-title: 48px;
  --fs-heading: 32px;
  --fs-body: 18px;

  /* 슬라이드 규격 (16:9) */
  --slide-w: 1920px;
  --slide-h: 1080px;
}

/* 슬라이드 컨테이너 공통 */
.slide {
  width: var(--slide-w);
  height: var(--slide-h);
  padding: 80px;
  background: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font-body);
  box-sizing: border-box;
}
```

**Claude Code 프롬프트 예시**:
> `reference/tone.png`와 `reference/color-palette.md` 참고해서 `slides/_shared/styles.css` 만들어줘. 16:9, 1920x1080 기준.

### Step 2.5. 산출물 네이밍 & 매핑 시스템 ★

#### A. 파트 기반 네이밍 (번호 X)

**왜 파트 기반인가**
- 슬라이드 순서/번호는 발표 직전까지 계속 바뀜 (추가/삭제/순서변경)
- 산출물 파일명을 번호에 묶으면 매번 리네이밍 지옥
- 파트 기반은 **순서 변경에 영향받지 않음**
- 같은 산출물을 여러 슬라이드에서 재사용 가능
- 번호는 **manifest.md에서만** 관리

**파일명 규칙**: `{파트}-{설명}.{ext}`

```
slides/
├── cover.html
├── persona-overview.html
├── persona-detail.html
├── geo-distribution.html
├── model-result.html
└── conclusion.html

assets/
├── persona-cards.png
├── persona-data.csv
├── geo-map.png
└── ...
```

> Export 파일명 = 소스 HTML 파일명. 변환 로직 단순화.

#### B. manifest.md (단일 진실 공급원)

번호와 파트를 **분리**해서 관리. 슬라이드 순서가 바뀌면 manifest 행만 재배치.

**좋은 점**:
- 슬라이드 추가/삭제 → 첫 번째 테이블만 수정
- 산출물 재사용 가시화 (같은 산출물이 여러 슬라이드에서 사용됨이 한눈에)
- 산출물 진행 상태 추적 가능

#### C. Claude Code 활용 프롬프트

매번 manifest.md를 참조시키면 컨텍스트 일관성 유지:

```
manifest.md 참조해서 slides/geo-distribution.html 만들어줘.
- 사용 산출물: assets/geo-map.png, assets/geo-top5.csv
- 스타일: slides/_shared/styles.css 따르기
- 다른 파일 건드리지 마
```

#### D. 매핑 검증 (선택)

간단 검증 스크립트 (`scripts/check-manifest.py`):

```python
# manifest.md에 적힌 파일들이 실제로 존재하는지 체크
import re
from pathlib import Path

manifest = Path("manifest.md").read_text()
files = re.findall(r'(slides/[\w\-./]+|assets/[\w\-./]+|exports/[\w\-./]+)', manifest)

missing = [f for f in set(files) if not Path(f).exists()]
if missing:
    print("누락된 파일:")
    for f in sorted(missing):
        print(f"  - {f}")
else:
    print("✓ 모든 파일 정상")
```

### Step 3. 슬라이드별 HTML 생성

**1장씩, 1대화에 1~2장**이 토큰 효율 최적.

**기본 템플릿** (`slides/{파트}-{설명}.html`):

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="_shared/styles.css">
  <title>지역 분포</title>
</head>
<body>
  <div class="slide">
    <!-- 슬라이드 내용 -->
  </div>
</body>
</html>
```

**핵심 토큰 절약 팁**:
- "전체 덱 만들어줘" 절대 금지
- 매번 어떤 파일만 수정할지 명시
- 이미 만든 슬라이드를 다시 보내지 말 것 (Claude Code는 파일 시스템 직접 읽음)

### Step 4. PNG export (Playwright)

**셋업**:
```bash
npm install -D playwright
npx playwright install chromium
```

**스크립트** (`scripts/export.js`):

```javascript
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 2
  });

  const slidesDir = path.join(__dirname, '../slides');
  const exportsDir = path.join(__dirname, '../exports');
  if (!fs.existsSync(exportsDir)) fs.mkdirSync(exportsDir);

  const files = fs.readdirSync(slidesDir)
    .filter(f => f.endsWith('.html') && !f.startsWith('_'));

  for (const file of files) {
    const name = file.replace('.html', '');
    const url = `file://${path.join(slidesDir, file)}`;
    await page.goto(url);
    await page.screenshot({
      path: path.join(exportsDir, `${name}.png`),
      fullPage: false
    });
    console.log(`✓ ${name}.png`);
  }

  await browser.close();
})();
```

**실행**: `node scripts/export.js`

### Step 5. PPT 통합

1. **PPT 템플릿 준비**: 16:9, 본인이 자주 쓰는 폰트로 마스터 슬라이드 설정
2. **HTML 슬라이드는 이미지로 삽입**:
   - manifest.md의 순서대로 빈 슬라이드 생성
   - 해당 위치에 `exports/{파트}-{설명}.png` 삽입 → 슬라이드 전체 채우기 (Ctrl+Shift+드래그로 비율 유지)
3. **나머지 슬라이드는 PPT에서 직접 작성**: 텍스트, 표, 일반 도형
4. **manifest.md 체크리스트로 누락 확인**

### Step 6. 최종 PDF Export

PowerPoint에서 `파일 → 내보내기 → PDF/XPS 만들기` → 옵션에서 "고품질" 선택.

또는 Edge headless로 통합 PDF 생성 (우리 프로젝트는 이 방식 사용 — `exports/` 폴더 참조).

</details>

<details>
<summary><strong>§5. Claude Code 프롬프팅 팁</strong></summary>

### 토큰 절약 원칙
1. **파일 단위로 작업**: "geo-distribution.html만" / "styles.css만"
2. **manifest.md 활용**: 매번 전체 맥락 설명 X, "manifest의 geo-distribution 행 참조"
3. **레퍼런스는 이미지로**: 텍스트로 디자인 설명하지 말고 `reference/*.png` 보여주기
4. **다른 파일 건드리지 말 것** 명시

### 자주 쓰는 프롬프트 템플릿

**신규 슬라이드 생성**:
```
slides/{파트}-{설명}.html 만들어줘.
- manifest.md {파트}-{설명} 행 참조
- 사용 산출물: {경로들}
- 스타일: _shared/styles.css 따르기
- 다른 파일 건드리지 마
```

**기존 슬라이드 수정**:
```
slides/geo-distribution.html 수정:
- 우측 리스트 폰트 크기 키우기 (현재 18px → 22px)
- 다른 부분 그대로
```

**디자인 시스템 변경**:
```
_shared/styles.css에서 --color-primary만 #2563eb → #1e40af로 변경.
다른 변수/파일 건드리지 마.
```

**산출물 변경 후 재export만**:
```
assets/geo-map.png 업데이트됐어.
slides/geo-distribution.html은 그대로 두고 export만 다시 해줘.
```

</details>

<details>
<summary><strong>§6. 자주 쓰는 명령어 모음</strong></summary>

```bash
# 로컬 미리보기 (실시간 새로고침)
npx live-server slides/

# 전체 슬라이드 PNG export
node scripts/export.js

# manifest 검증
python scripts/check-manifest.py
```

</details>

<details>
<summary><strong>§7. 트러블슈팅</strong></summary>

### 폰트 문제
- 증상: PNG export 시 한글 폰트 깨짐
- 해결: `_shared/fonts/`에 웹폰트(.woff2) 두고 `@font-face`로 로드, Pretendard 권장

### 해상도 문제
- 증상: PPT 삽입 시 흐릿함
- 해결: Playwright `deviceScaleFactor: 2` 설정

### 산출물 변경
- 증상: 데이터/이미지 업데이트 후 슬라이드 재생성 필요
- 해결: 산출물 파일은 그대로 덮어쓰기 (파일명 동일) → 해당 HTML 다시 export
- 파트 기반 네이밍이라 파일 경로 변경 없음

### 산출물 누락
- 증상: PPT에 빈 슬라이드 발견
- 해결: manifest.md 산출물 인벤토리 확인, `python scripts/check-manifest.py` 실행

### 슬라이드 순서/번호 변경
- **파트 기반 네이밍이라 파일명 변경 불필요**
- manifest.md 첫 번째 테이블의 행 순서만 재배치
- PPT에서도 슬라이드 드래그로 순서 변경

### 같은 산출물 여러 슬라이드에서 사용
- 파일 1개로 N번 참조 가능 (manifest "사용 슬라이드" 컬럼에 복수 기재)

### 토큰 부족 / Claude Code 응답 느림
- 증상: 슬라이드 수정 요청 시 응답 지연
- 해결: 새 대화 시작, manifest.md만 보여주고 수정할 파일 명시

### Edge headless print-to-pdf 실패 (한글 경로)
- 증상: `--print-to-pdf` 출력 파일이 안 생성됨
- 해결: 영문 임시 폴더(`%TEMP%\xxx\`)에 출력 후 한글 폴더로 복사

</details>

---

## 부록 A: 파트 정의 가이드 (다른 프로젝트 적용용)

> 우리 프로젝트 파트는 [§0-2](#0-2-파트-정의-12개)에서 확인. 아래는 다른 프로젝트에 적용할 때 참고용.

프로젝트 성격에 따라 파트 prefix를 자유롭게 정의. 원칙은 **분석/내용 단계로 묶기**.

### 데이터 분석 프로젝트
`intro`, `data`, `eda`, `persona`, `geo`, `model`, `result`, `insight`, `conclusion`

### 마케팅 캠페인 회고
`intro`, `goal`, `audience`, `channel`, `creative`, `result`, `learning`, `next`

### 제품/기능 제안
`intro`, `problem`, `user`, `solution`, `design`, `metric`, `roadmap`, `risk`

### 일반 비즈니스 발표
`intro`, `context`, `analysis`, `proposal`, `plan`, `risk`, `conclusion`

**판단 기준**:
- 한 파트당 슬라이드 1~3장이 적당
- 너무 세분화하면 파트 명이 길어지고 관리 부담
- 너무 묶으면 같은 prefix가 너무 많아져 검색이 어려움

---

## 부록 B: 빠른 시작 체크리스트

### 우리 프로젝트 (현재 진행)
- [x] `team/발표자료/slides/` 폴더 생성 (5/2 완료)
- [x] `_shared/styles.css` 생성 + Olist 로고 복사 (5/2 완료)
- [x] HTML 5장 시안 (cover · hook · peak · tf3 · cta) 1차 완성 (5/2 완료)
- [x] PDF export 1차 (`exports/데2터로말해조_발표_v1_5page.pdf`, 5/2 완료)
- [ ] 팀 리뷰 후 시안 수정
- [ ] `tf-intro` (이중 트랙) 슬라이드 추가 작성
- [ ] manifest.md 본 작성 (현재는 §0-6 예시만)
- [ ] Playwright 자동화 스크립트 셋업
- [ ] PPT 통합 (HTML 6장 + PPT ~21장)
- [ ] 최종 PDF export

### 새 프로젝트 적용 시
- [ ] 프로젝트 폴더 구조 생성 (§3 일반 구조 참고)
- [ ] 레퍼런스 이미지 1~2개 `reference/`에 저장
- [ ] 컬러 팔레트 정의 (`reference/color-palette.md`)
- [ ] 우리 프로젝트 **파트 정의** (부록 A 참고)
- [ ] manifest.md 초안 작성 (슬라이드 순서 + 산출물 인벤토리)
- [ ] 기존 산출물 → 파트 기반 파일명으로 정리해 `assets/`에 배치
- [ ] `_shared/styles.css` 생성 (Claude Code에 위임)
- [ ] HTML 슬라이드 1장씩 제작
- [ ] Playwright 셋업 + export 스크립트
- [ ] PPT 템플릿에 이미지 삽입
- [ ] manifest 체크리스트로 누락 확인
- [ ] PDF export
