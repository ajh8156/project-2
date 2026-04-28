# CSV → BigQuery → Looker Studio 연동 가이드

**대상**: 데2터로말해조 팀원 전체
**목적**: Olist CSV를 BigQuery에 올리고 Looker Studio 대시보드로 연결
**작성일**: 2026-04-18 / **최종 수정**: 2026-04-22 (v6 — §B 개인 연습용으로 재분류, §C 팀원 초대 발송 분리)

---

## 📑 이 가이드 보는 법

본인 상황에 따라 보는 섹션이 다릅니다. 아래 표에서 본인 위치를 확인하고 해당 섹션으로 이동하세요.

| 역할 | 해당자 | 해야 할 것 | 이동 |
|------|-------|----------|------|
| 🟢 **팀원** (초대받는 입장) | 초대받은 팀원 5명 | Gmail 전달 → 초대 2통 수락 → 차트 제작 | → [§A. 팀원용 빠른 시작](#a-팀원용-빠른-시작-5분) |
| 🔵 **개인 연습용** (선택) | 원하는 팀원 누구나 | 본인 Google Cloud 프로젝트에서 CSV→BigQuery→Looker 전체 과정을 직접 해보기 | → [§B. 개인 연습용](#b-개인-연습용-csvbigquery-직접-해보기) |
| 🟣 **팀 관리자** (초대 발송 담당) | 팀에 1명 | BigQuery·루커 세팅 후 팀원 초대 메일 발송 | → [§C. 팀원 초대 발송](#c-팀원-초대-발송-팀-관리자용) |

### 전체 목차

**§A. 팀원용**
1. [Gmail 관리자에게 전달](#a-1-본인-gmail을-관리자에게-전달)
2. [초대 메일 2통 수락](#a-2-초대-메일-2통-수락)
3. [대시보드 차트 제작 시작](#a-3-대시보드-차트-제작-시작)

**§B. 개인 연습용**
1. [터미널이란? (PowerShell 여는 법)](#b-1-터미널이란-powershell-여는-법)
2. [필수 설치](#b-2-필수-설치-1회만)
3. [로그인 & 프로젝트 지정](#b-3-로그인--프로젝트-지정)
4. [🤖 Claude Code 프롬프트 모음](#b-4--claude-code-프롬프트-모음-복붙용)
5. [CSV 19개 업로드](#b-5-csv-19개-업로드)
6. [통합 TABLE 3개 생성](#b-6-통합-table-3개-생성)
7. [Looker Studio 연결](#b-7-looker-studio-연결-수동)

**§C. 팀원 초대 발송 (팀 관리자용)**
- [BigQuery 권한 부여 → 루커 공유 → 팀원 안내](#c-팀원-초대-발송-팀-관리자용)

**부록 (공통)**
- [A. 수동 실행 SQL](#부록-a-수동-실행-sql)
- [B. CSV 업로드 이슈 2건](#부록-b-csv-업로드-이슈-2건)
- [C. 문제 해결 FAQ](#부록-c-문제-해결-faq)
- [D. 개인 Google Cloud 프로젝트 생성 주의사항](#부록-d-개인-google-cloud-프로젝트-생성-주의사항)

---

# §A. 팀원용 빠른 시작 (5분)

관리자가 BigQuery와 루커 세팅을 이미 끝내 두었다는 전제. **본인이 해야 할 건 아래 3단계가 전부**입니다.

## A-1. 본인 Gmail을 관리자에게 전달

- 본인이 평소 쓰는 **Google 계정 이메일** 주소를 관리자에게 알려주기
  - 개인 Gmail (`xxxxx@gmail.com`) 또는 회사 Google 계정 모두 가능
- 관리자가 이 계정으로 초대 메일을 2통 보냅니다

## A-2. 초대 메일 2통 수락

관리자가 초대를 발송하면 해당 Gmail 받은편지함에 메일 2통이 도착합니다.

### ① BigQuery 초대 (먼저 수락)

- 제목 예시: *"You've been granted access to BigQuery dataset olist_analysis"*
- 메일 본문의 **"BigQuery 열기 / Open BigQuery"** 링크 클릭
- Google 계정 로그인
- BigQuery 콘솔 화면이 뜨고, 왼쪽 패널에 `olist-team-analysis → olist_analysis` 데이터셋과 테이블 22개가 보이면 성공

### ② Looker Studio 초대 (그 다음)

- 제목 예시: *"[관리자 이름] shared a Looker Studio report with you"*
- **"보고서 열기"** 클릭
- 대시보드 화면이 뜨면 성공

> ⚠️ **순서 중요**: BigQuery를 먼저 수락하지 않으면 루커에서 차트가 "권한 없음" 에러로 깨집니다.

## A-3. 대시보드 차트 제작 시작

루커 보고서 우측 상단 **"수정"** 버튼 클릭 → 차트 편집 화면 진입.

### 본인 담당 페이지 확인

대시보드는 3페이지로 나뉩니다. 각 페이지에서 쓰는 TABLE이 정해져 있으니 **본인 담당 페이지에 맞는 TABLE만 쓰세요**.

| 페이지 | 사용 TABLE | 대표 차트 |
|--------|----------|---------|
| **Retention/Revenue** | `t_orders_summary` | AOV, 재구매율, 배송 지연율, 저평점 비중 |
| **상품·카테고리 분석** | `t_order_items` | 카테고리 TOP 10, 베스트 상품, 셀러 매출 |
| **Acquisition** | `t_marketing_funnel` | MQL→계약 전환율, 채널별 유입 |

### 차트 만드는 흐름

1. 상단 **차트 추가** → 원하는 유형 선택 (바/라인/스코어카드 등)
2. 차트 클릭 → 우측 **데이터 패널** → **"데이터 소스"** 드롭다운에서 본인 페이지의 TABLE 선택
3. **측정기준**(카테고리성 컬럼)과 **측정항목**(숫자 컬럼) 드래그

### 막히면?

| 증상 | 해결 |
|------|------|
| BigQuery 초대 메일이 안 옴 | 스팸함 확인 / 관리자에게 전달한 Gmail 재확인 요청 |
| 루커에서 "권한 없음" 에러 | A-2의 BigQuery 초대부터 수락했는지 확인 |
| SQL이나 쿼리 관련 질문 | 관리자에게 Claude Code로 자문 요청 |
| 차트 기본 사용법 | [루커 공식 가이드](https://support.google.com/looker-studio/answer/6292570) 참고 |

**→ 팀원은 여기까지가 전부입니다. 아래 §B(개인 연습용)·§C(팀 관리자용)는 선택.**

---

# §B. 개인 연습용 (CSV→BigQuery 직접 해보기)

**이 섹션은 선택 사항입니다.** 팀 프로젝트(`olist-team-analysis`) 세팅은 이미 완료된 상태이므로, 팀원은 §A만 따르면 대시보드 작업 가능합니다.

이 섹션은 다음과 같은 경우에 유용합니다:
- **본인 Google Cloud 프로젝트에서 직접 실습**해 보고 싶을 때
- **CSV→BigQuery 연동 과정**을 실무 관점에서 이해하고 싶을 때
- 팀 관리자가 **다음 프로젝트에서 처음부터 세팅**할 때 참고용

> 💡 아래 SQL과 명령어의 `olist-team-analysis` 부분은 **본인 프로젝트 ID로 교체**해서 실행하세요 (예: `olist-practice-본인이니셜`).

CSV→BigQuery→통합 TABLE 생성→루커 연결까지 전체 과정.

## B-1. 터미널이란? (PowerShell 여는 법)

이 가이드의 명령어(`bq`, `gcloud`, `python`, `claude` 등)는 **터미널**에서 실행합니다.

> **터미널 = 명령어를 입력해서 실행하는 검은/파란 창**  
> Windows에서는 **PowerShell**을 씁니다.

### PowerShell 여는 법

1. **Windows 키** 누르기 (화면 왼쪽 아래 네모 아이콘)
2. **"powershell"** 입력
3. **"Windows PowerShell"** 앱 클릭

### 처음 연 모습

```
Windows PowerShell
Copyright (C) Microsoft Corporation.

PS C:\Users\본인계정> _
```

커서(`_`) 뒤에 명령어를 입력하고 **Enter**를 누르면 실행됩니다.

### 이후 모든 명령어는 여기에서

이 가이드에서 ```powershell ... ``` 블록이 나오면 **PowerShell에 그대로 붙여넣고 Enter**를 치면 됩니다.

> 💡 아래 **B-4** 이후부터는 **Claude Code CLI** (`claude` 명령)를 대신 써도 됩니다. 하지만 **B-2 설치와 B-3 로그인**은 PowerShell에서 직접 하는 게 안전합니다.

---

## B-2. 필수 설치 (1회만)

아래 4개를 설치합니다. 이미 설치돼 있으면 스킵.

| 도구 | 설치 링크 | 용도 |
|------|---------|------|
| **Google Cloud SDK** | https://cloud.google.com/sdk/docs/install | `bq`, `gcloud` 명령어 |
| **Python 3.10+** | https://www.python.org/downloads/ | CSV 전처리용 — ⚠️ 설치 시 **"Add Python to PATH"** 체크 필수 |
| **pandas** | 설치 후 PowerShell에서 `pip install pandas` | CSV 읽기·정리 |
| **Claude Code** (선택) | https://claude.ai/code | 자동화용 CLI |

설치 확인 (PowerShell에서):

```powershell
bq version
python --version
pip show pandas
```

각각 버전 정보가 나오면 OK.

---

## B-3. 로그인 & 프로젝트 지정

PowerShell에서 **한 줄씩** 입력 후 Enter:

```powershell
gcloud auth login
```
→ 브라우저가 자동으로 열림 → 팀 Google 계정 선택 → **허용** 클릭

```powershell
gcloud config set project olist-team-analysis
```
→ `Updated property [core/project].` 메시지 나오면 성공

```powershell
bq ls
```
→ 데이터셋 목록이 나오면 권한 정상

---

## B-4. 🤖 Claude Code 프롬프트 모음 (복붙용)

**원칙**: 자동화할 수 있는 건 전부 Claude Code에 맡기고, 웹 UI(루커 차트 제작, 팀 공유)만 직접 클릭.

### Claude Code 실행

PowerShell에서:

```powershell
cd C:/Users/본인계정/OneDrive/Desktop/fcicb7
claude
```

> `본인계정` 은 본인 Windows 사용자명으로 교체 (예: `ajh81`)

Claude Code 세션이 시작되면 아래 프롬프트를 **그대로 복붙**하세요.

### 🔹 [풀 자동화] CSV 업로드부터 TABLE 생성까지

```
BigQuery olist-team-analysis.olist_analysis 데이터셋에
project-2/data 폴더 CSV 19개 전부 업로드한 뒤,
통합 TABLE 3개(t_orders_summary, t_order_items, t_marketing_funnel)까지 생성해줘.

주의사항:
- olist_order_reviews_dataset.csv: 포르투갈어 리뷰 따옴표 미종결 → pandas 전처리 필요
- product_category_name_translation.csv: BOM 문자 → utf-8-sig 인코딩으로 처리
- 통합 TABLE 3개는 행 폭발 방지(1:N 관계는 미리 SUM/COUNT 집계 후 JOIN)
- 생성 후 원본 테이블과 행 수 일치 검증까지 해줘

완료 시 각 테이블 이름과 행 수 보고해줘.
```

### 🔹 [1회 세팅] CSV 19개만 업로드

```
BigQuery olist-team-analysis.olist_analysis 데이터셋에
project-2/data 폴더 CSV 19개 전부 업로드해줘.

order_reviews는 따옴표 이슈, category_translation은 BOM 이슈가 있으니
pandas로 전처리 후 업로드해줘. 완료 후 19개 테이블 이름과 행 수 보고.
```

### 🔹 통합 TABLE 3개 생성 (CSV는 이미 업로드된 경우)

```
BigQuery olist-team-analysis.olist_analysis에 이미 있는 원본 테이블 19개를 써서
통합 TABLE 3개 만들어줘:

1. t_orders_summary (주문 단위) = orders + customers + order_items/payments/reviews 집계
2. t_order_items (주문-상품 단위) = order_items + products + category_translation + orders
3. t_marketing_funnel (MQL 단위) = marketing_qualified_leads + closed_deals

행 폭발 방지를 위해 1:N 관계는 미리 SUM/COUNT로 집계하고,
생성 후 원본(orders, order_items, marketing_qualified_leads)과 행 수 일치 검증해줘.
```

### 🔹 특정 CSV/SQL 오류 해결

```
BigQuery 작업 중 다음 에러 났어:

[에러 메시지 전문 붙여넣기]

원인 진단하고 해결해줘. 필요하면 pandas로 CSV 전처리하거나 스키마 명시해서 재업로드해도 돼.
```

### 🔹 루커 차트 SQL 자문

```
루커 스튜디오에서 "[차트명]" 만들려고 해.
어떤 TABLE 써야 하고 측정기준·측정항목 뭐로 설정해야 돼?

참고: 우리 통합 TABLE 3개는
- t_orders_summary (주문 단위)
- t_order_items (상품 단위)
- t_marketing_funnel (리드 단위)
```

### 🔹 업로드 상태 점검

```
BigQuery olist-team-analysis.olist_analysis에 있는 테이블 목록이랑
각 행 수 알려줘. 원본 19개 + 통합 3개 총 22개가 맞는지 확인해줘.
```

### Claude Code 권한 매트릭스

| ✅ 해줄 수 있는 것 | ❌ 못하는 것 |
|-----------------|-----------|
| CSV 읽기/전처리 (pandas) | 루커 스튜디오 Web UI 클릭 |
| `bq` 명령 실행 (업로드·쿼리) | Google 계정 로그인 |
| BigQuery SQL 실행 | 신용카드 등록·결제 |
| 스키마 오류 자동 수정 | 브라우저 자동 조작 |
| 파일 읽기·쓰기 | 유료 API 호출 |

### 요청 시 팁

- **절대경로 사용**: `"C:/Users/본인계정/..."` 전체 경로
- **프로젝트 ID 명시**: `olist-team-analysis` (기본값이 다를 수 있음)
- **에러는 전문 그대로**: 빨간 메시지 전체 복붙 (`Location:`, `Line:` 포함)
- **스크린샷 공유**: 루커 화면에서 막히면 캡처 공유 시 정확 진단

---

## B-5. CSV 19개 업로드

### 🤖 Claude Code 방식 (추천, 5분)

위 B-4의 **"[1회 세팅] CSV 19개만 업로드"** 프롬프트 사용.

### 🔧 수동 방식

PowerShell에서:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
cd "C:/Users/본인계정/OneDrive/Desktop/fcicb7/project-2/guides"
.\upload_to_bigquery.ps1
```

`order_reviews`, `category_translation` 2개 CSV는 특수 처리 필요 → [부록 B](#부록-b-csv-업로드-이슈-2건) 참고.

### 업로드 확인

BigQuery 콘솔 → `olist_analysis` 펼치기 → 테이블 **19개** 확인.

---

## B-6. 통합 TABLE 3개 생성

### 왜 3개로 나누나?

- **행 폭발 방지**: 1:N 관계(주문-상품, 주문-결제, 주문-리뷰)를 한 테이블에 JOIN하면 금액이 중복 합산됨 → AOV·재구매율 숫자 왜곡
- **grain 분리**: 주문/상품/리드 단위 각각 독립 TABLE

### 왜 VIEW가 아니라 TABLE인가?

CSV가 1회 업로드 후 변하지 않는 **정적 데이터**. TABLE(결과 물리 저장)이 VIEW(매번 JOIN 재계산)보다 쿼리 비용 **10배 저렴**.

| 방식 | 쿼리 1회당 스캔 | 월 예상 (6명 × 13차트 × 5회/일 × 20일) |
|------|-------------|----------------------------------|
| VIEW | ~50MB | ~30GB |
| **TABLE** | **~5MB** | **~3GB** |

무료 한도(월 1TB) 대비 0.3% → 요금 걱정 불필요.

### 3개 TABLE 용도

| TABLE | 한 행 = | 대표 차트 | OKR 지표 |
|-------|--------|---------|---------|
| **`t_orders_summary`** | 주문 1건 | AOV, 재구매율, 배송 지연율, 저평점 비중 | G1·KR1, KR4, KR5 |
| **`t_order_items`** | 주문-상품 1건 | 카테고리 TOP, 셀러 매출, 베스트 상품 | G2 |
| **`t_marketing_funnel`** | MQL 1건 | MQL→계약 전환율, 채널별 유입 | Acquisition |

### 생성 방법

**🤖 Claude Code 방식 (추천)**: 위 B-4의 **"통합 TABLE 3개 생성"** 프롬프트 사용.

**🔧 수동 방식**: [부록 A](#부록-a-수동-실행-sql)의 SQL 3개를 BigQuery 쿼리 편집기에 붙여넣기.

### 검증

```sql
SELECT 't_orders_summary' AS t, COUNT(*) AS n FROM `olist-team-analysis.olist_analysis.t_orders_summary`
UNION ALL SELECT 't_order_items', COUNT(*) FROM `olist-team-analysis.olist_analysis.t_order_items`
UNION ALL SELECT 't_marketing_funnel', COUNT(*) FROM `olist-team-analysis.olist_analysis.t_marketing_funnel`;
```

기대값: `t_orders_summary=99,441` / `t_order_items=112,650` / `t_marketing_funnel=8,000`

---

## B-7. Looker Studio 연결 (수동)

> ⚠️ Web UI 구간 — Claude Code가 대신해줄 수 없음. 직접 클릭 필요.

### 3개 TABLE 모두 연결

1. https://lookerstudio.google.com → **만들기** → **보고서** (또는 기존 보고서 → **수정**)
2. **BigQuery** 선택 → `olist-team-analysis` → `olist_analysis` → `t_orders_summary` → **연결**
3. 추가: **리소스** → **추가된 데이터 소스 관리** → **⊕ 데이터 소스 추가**
4. `t_order_items`, `t_marketing_funnel` 차례로 연결 (총 3개)

### 차트에서 TABLE 선택

차트 클릭 → 우측 **데이터 패널** → **"데이터 소스"** 드롭다운에서 차트 용도에 맞는 TABLE 고르기.

### (옵션) 발표 전 쿼리 비용 0원화

**데이터 추출** 커넥터로 변환하면 BigQuery 쿼리가 아예 발생하지 않음. 차트 확정 후 발표 전날쯤 적용.

<details>
<summary>설정 방법 상세</summary>

**중요**: "데이터 추출"은 기존 소스 옵션이 아니라 **별도 커넥터**입니다.

1. 편집 화면 → **리소스** → **추가된 데이터 소스 관리** → **⊕ 데이터 소스 추가**
2. 커넥터 갤러리에서 **"데이터 추출(Extract Data)"** (📦 아이콘) 선택
3. 원본 데이터 소스로 `t_orders_summary` 선택
4. 필드 설정:
   - **측정기준**: 차트에 쓰는 컬럼 드래그
   - **측정항목**: 숫자 컬럼 드래그
   - **자동 업데이트**: 화면 **맨 아래** 라디오 버튼 → **`사용 안함`** 선택
5. **저장 및 추출** → 이름 입력 → 저장
6. 차트 → 데이터 소스 드롭다운에서 추출본으로 변경
7. `t_order_items`, `t_marketing_funnel`도 각각 동일하게 추출

</details>

---

---

# §C. 팀원 초대 발송 (팀 관리자용)

BigQuery·루커 세팅이 완료된 **팀 프로젝트**에 팀원 5명을 초대하는 절차. 팀당 1명(관리자)만 해당.

> ⚠️ **순서 중요**: BigQuery 먼저 → 루커 나중. 반대로 하면 팀원이 루커 열었을 때 데이터 안 보임.

## C-1. 사전 준비

팀원 5명의 Gmail 주소 수집 완료.

## C-2. BigQuery 데이터셋 공유 (먼저)

1. BigQuery 콘솔 → 왼쪽 패널 `olist_analysis` 데이터셋 클릭
2. 우측 상단 **공유** 버튼
3. 팀원 Gmail 입력
4. 역할: **BigQuery 데이터 뷰어**
5. **저장** → 팀원 이메일로 초대 메일 자동 발송

## C-3. 루커 보고서 공유 (그 다음)

1. 루커 보고서 우측 상단 **공유**
2. 팀원 Gmail 입력

| 역할 | 대상 |
|------|------|
| 편집자 | 차트 제작 팀원 5명 |
| 뷰어 | 발표 당일 관객, 멘토, 외부 |

3. **알림 보내기** 체크 → 초대 메일 자동 발송

## C-4. 팀원에게 §A 섹션 안내

팀원에게 이 가이드 링크 공유하면서 **"[§A. 팀원용 빠른 시작](#a-팀원용-빠른-시작-5분) 만 보면 됩니다"** 라고 공지.

---

# 📊 데이터 구조 (참고용)

**전체 흐름**:
```
CSV 19개 → BigQuery 원본 테이블 19개 → 통합 TABLE 3개 → Looker 대시보드
```

<details>
<summary>📁 CSV 파일 19개 세부 목록</summary>

#### olist_customers_dataset/ — Olist B2C (9개)

| CSV | 테이블 | 내용 |
|-----|-------|------|
| `olist_orders_dataset.csv` | `orders` | 주문 정보 |
| `olist_customers_dataset.csv` | `customers` | 고객 정보 |
| `olist_order_items_dataset.csv` | `order_items` | 주문 상품 |
| `olist_order_payments_dataset.csv` | `order_payments` | 결제 정보 |
| `olist_order_reviews_dataset.csv` | `order_reviews` | 리뷰 (⚠️ 따옴표 이슈) |
| `olist_products_dataset.csv` | `products` | 상품 카테고리 |
| `olist_sellers_dataset.csv` | `sellers` | 셀러 정보 |
| `olist_geolocation_dataset.csv` | `geolocation` | 위경도 |
| `product_category_name_translation.csv` | `category_translation` | 카테고리 번역 (⚠️ BOM 이슈) |

#### Olist Marketing Funnel/ — B2B (2개)

| CSV | 테이블 |
|-----|-------|
| `olist_marketing_qualified_leads_dataset.csv` | `marketing_qualified_leads` |
| `olist_closed_deals_dataset.csv` | `closed_deals` |

#### kaggle/ — Kaggle CRM (8개)

| CSV | 테이블 | 비고 |
|-----|-------|------|
| `hh_demographic.csv` | `hh_demographic` | |
| `transaction_data.csv` | `transaction_data` | |
| `product.csv` | `product` | |
| `campaign_desc.csv` | `campaign_desc` | |
| `campaign_table.csv` | `campaign_table` | |
| `coupon.csv` | `coupon` | |
| `coupon_redempt.csv` | `coupon_redempt` | |
| `causal_data.csv` | `causal_data` | ⚠️ 664MB 대용량 |

</details>

<details>
<summary>🔗 테이블 JOIN 관계</summary>

```
[B2B → B2C]
closed_deals.seller_id → sellers.seller_id

[B2C 내부]
customers → orders → order_items → products → category_translation
                  └→ order_payments
                  └→ order_reviews

[Kaggle 내부]
hh_demographic → transaction_data → product
              └→ campaign_table → campaign_desc
              └→ coupon_redempt → coupon
```

</details>

---

# 부록 A. 수동 실행 SQL

Claude Code 안 쓰고 직접 붙여넣어 실행할 때 사용. BigQuery 쿼리 편집기에 하나씩 복붙.

<details>
<summary>① t_orders_summary 생성 SQL</summary>

```sql
CREATE OR REPLACE TABLE `olist-team-analysis.olist_analysis.t_orders_summary` AS
WITH items_agg AS (
  SELECT order_id,
         COUNT(*) AS item_count,
         SUM(price) AS total_price,
         SUM(freight_value) AS total_freight
  FROM `olist-team-analysis.olist_analysis.order_items`
  GROUP BY order_id
),
payments_agg AS (
  SELECT order_id,
         SUM(payment_value) AS total_payment,
         STRING_AGG(DISTINCT payment_type) AS payment_types
  FROM `olist-team-analysis.olist_analysis.order_payments`
  GROUP BY order_id
),
reviews_agg AS (
  SELECT order_id, AVG(review_score) AS avg_review_score
  FROM `olist-team-analysis.olist_analysis.order_reviews`
  GROUP BY order_id
)
SELECT
  o.order_id, o.customer_id, o.order_status,
  o.order_purchase_timestamp, o.order_delivered_customer_date, o.order_estimated_delivery_date,
  c.customer_unique_id, c.customer_state, c.customer_city,
  i.item_count, i.total_price, i.total_freight,
  p.total_payment, p.payment_types,
  r.avg_review_score
FROM `olist-team-analysis.olist_analysis.orders` o
LEFT JOIN `olist-team-analysis.olist_analysis.customers` c ON o.customer_id = c.customer_id
LEFT JOIN items_agg i ON o.order_id = i.order_id
LEFT JOIN payments_agg p ON o.order_id = p.order_id
LEFT JOIN reviews_agg r ON o.order_id = r.order_id;
```

</details>

<details>
<summary>② t_order_items 생성 SQL</summary>

```sql
CREATE OR REPLACE TABLE `olist-team-analysis.olist_analysis.t_order_items` AS
SELECT
  oi.order_id, oi.order_item_id, oi.product_id, oi.seller_id,
  oi.price, oi.freight_value,
  p.product_category_name,
  ct.product_category_name_english AS category_en,
  o.order_purchase_timestamp, o.order_status
FROM `olist-team-analysis.olist_analysis.order_items` oi
LEFT JOIN `olist-team-analysis.olist_analysis.products` p ON oi.product_id = p.product_id
LEFT JOIN `olist-team-analysis.olist_analysis.category_translation` ct
  ON p.product_category_name = ct.product_category_name
LEFT JOIN `olist-team-analysis.olist_analysis.orders` o ON oi.order_id = o.order_id;
```

</details>

<details>
<summary>③ t_marketing_funnel 생성 SQL</summary>

```sql
CREATE OR REPLACE TABLE `olist-team-analysis.olist_analysis.t_marketing_funnel` AS
SELECT
  m.mql_id, m.first_contact_date, m.landing_page_id, m.origin AS lead_origin,
  d.seller_id, d.business_segment, d.lead_type, d.business_type, d.won_date,
  CASE WHEN d.seller_id IS NOT NULL THEN 1 ELSE 0 END AS is_converted
FROM `olist-team-analysis.olist_analysis.marketing_qualified_leads` m
LEFT JOIN `olist-team-analysis.olist_analysis.closed_deals` d ON m.mql_id = d.mql_id;
```

</details>

---

# 부록 B. CSV 업로드 이슈 2건

Claude Code에 맡기면 자동 처리되지만, 수동 업로드 시 참고.

### B-1. `olist_order_reviews_dataset.csv` — 따옴표 미종결

**증상**: `Missing close quote character (")` 에러로 업로드 실패
**원인**: 포르투갈어 리뷰에 따옴표 미종결 행 100여 건
**해결**: pandas 전처리 후 `--allow_quoted_newlines` 플래그로 재업로드

<details>
<summary>해결 명령어</summary>

```powershell
python -c "import pandas as pd; df=pd.read_csv(r'경로/olist_order_reviews_dataset.csv', engine='python', on_bad_lines='skip'); df.to_csv(r'경로/olist_order_reviews_CLEAN.csv', index=False, quoting=1, lineterminator='\n')"

bq load --source_format=CSV --autodetect --replace --skip_leading_rows=1 --allow_quoted_newlines --max_bad_records=100 olist-team-analysis:olist_analysis.order_reviews "경로/olist_order_reviews_CLEAN.csv"
```

결과: ~99,224행

</details>

### B-2. `product_category_name_translation.csv` — BOM 문자

**증상**: 업로드는 성공하지만 컬럼명이 `string_field_0/1`로 잡힘 → `t_order_items` 생성 시 `Name product_category_name not found` 에러
**원인**: 파일 맨 앞 BOM 문자로 헤더 인식 실패
**해결**: `encoding='utf-8-sig'`로 BOM 제거 + 명시적 스키마로 재업로드

<details>
<summary>해결 명령어</summary>

```powershell
python -c "import pandas as pd; df=pd.read_csv(r'경로/product_category_name_translation.csv', encoding='utf-8-sig'); df.to_csv(r'경로/category_translation_CLEAN.csv', index=False, lineterminator='\n')"

bq load --source_format=CSV --replace --skip_leading_rows=1 olist-team-analysis:olist_analysis.category_translation "경로/category_translation_CLEAN.csv" product_category_name:STRING,product_category_name_english:STRING
```

</details>

---

# 부록 C. 문제 해결 FAQ

| 증상 | 원인·해결 |
|------|---------|
| `Not found: Table ... was not found in location US` | 데이터셋 리전 불일치 또는 테이블 누락. 왼쪽 패널에서 테이블 존재 확인 |
| `Missing close quote character (")` | [부록 B-1](#b-1-olist_order_reviews_datasetcsv--따옴표-미종결) 참고 |
| `Name product_category_name not found inside ct` | [부록 B-2](#b-2-product_category_name_translationcsv--bom-문자) 참고 |
| `Already Exists: Table` | 정상. `CREATE OR REPLACE`라 재실행하면 덮어써짐 |
| `Permission denied` / 권한 없음 | 관리자에게 **BigQuery 데이터 뷰어** 권한 요청 |
| `Syntax error: Unexpected ...` | SQL 붙여넣기 중 일부 누락. 세미콜론(;)까지 전체 복사 재시도 |
| 루커에서 테이블 안 보임 | BigQuery 뷰어 권한 확인 + 브라우저 새로고침 |
| 루커 차트 느림 | 발표 전 B-7 "데이터 추출" 적용 |
| 쿼리 비용 걱정 | 정적 데이터 + TABLE 방식이라 월 ~3GB (무료 1TB의 0.3%) → 걱정 불필요 |
| `gcloud components update` 안내 | 무시 가능. SDK 업데이트 권유일 뿐 현재 작업에 영향 없음 |

---

# 부록 D. 개인 Google Cloud 프로젝트 생성 주의사항

§B(개인 연습용)를 본인 프로젝트에서 진행할 때 자주 걸리는 3가지.

<details>
<summary>세부 내용 펼치기</summary>

**① 샌드박스 모드 해제**: 신규 프로젝트는 `bq load` 실행 불가 → BigQuery 콘솔 상단 **"업그레이드"** 클릭 → 결제 계정 연결 (무료 한도 내 0원 청구)

**② 테이블 만료일 확인**: 샌드박스 해제 전 업로드한 테이블은 60일 후 자동 삭제. 각 테이블 → **세부정보** → **테이블 만료** → **없음**으로 변경

**③ 리전 불일치 방지**: `bq cp`로 팀(서울) → 개인(US) 복사 시 cross-region 오류. 로컬 CSV에서 직접 업로드 권장

</details>
