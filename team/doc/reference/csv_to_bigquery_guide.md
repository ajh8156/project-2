# CSV → BigQuery 연동 가이드

**대상**: 데2터로말해조 팀원 전체  
**목적**: Olist CSV 파일을 BigQuery에 올리고 Looker Studio와 연결하기  
**작성일**: 2026-04-18 / **최종 수정**: 2026-04-21  
**완료 목표**: 4/21(화) 세션 전까지 개인 업로드 완료

---

## 운영 방식 안내

이 프로젝트는 BigQuery를 두 가지 용도로 운영합니다.

| 구분 | 프로젝트 | 용도 |
|------|---------|------|
| **개인 연습용** | `olist-practice-jh` 등 개인 프로젝트 | CSV → BigQuery 연동 실습, 쿼리 자유롭게 연습 |
| **팀 공용** | `olist-team-analysis` | 팀 전체가 함께 Looker Studio 대시보드 제작 |

**Looker Studio 공유 방식**

- Looker Studio 보고서는 링크로 팀원 전체와 공유 가능합니다.
- 역할은 **뷰어**(보기만)와 **편집자**(함께 제작) 두 가지로 나눌 수 있습니다.
- 단, 팀원이 데이터를 보려면 BigQuery 공용 프로젝트(`olist-team-analysis`) 접근 권한도 함께 있어야 합니다. → Step 6 참고

---

## 전체 흐름 한눈에 보기

```
CSV 파일                    BigQuery                  Looker Studio
(로컬 data 폴더)  ──────>  (테이블 생성)  ──────>  (대시보드 연결)
```

총 소요 시간: 약 15~20분 (스크립트 방식 기준)

---

## 업로드할 CSV 파일 목록

총 19개 CSV 파일, 3개 폴더로 나뉩니다.

### 📁 olist_customers_dataset/ — Olist B2C 거래 데이터 (9개)

| CSV 파일명 | BigQuery 테이블명 | 내용 |
|-----------|----------------|------|
| `olist_orders_dataset.csv` | `orders` | 주문 정보 (주문 상태, 날짜) |
| `olist_customers_dataset.csv` | `customers` | 고객 정보 (ID, 지역) |
| `olist_order_items_dataset.csv` | `order_items` | 주문 상품 정보 (가격, 수량) |
| `olist_order_payments_dataset.csv` | `order_payments` | 결제 정보 |
| `olist_order_reviews_dataset.csv` | `order_reviews` | 리뷰 점수 및 댓글 |
| `olist_products_dataset.csv` | `products` | 상품 카테고리 정보 |
| `olist_sellers_dataset.csv` | `sellers` | 셀러 정보 |
| `olist_geolocation_dataset.csv` | `geolocation` | 우편번호별 위경도 정보 |
| `product_category_name_translation.csv` | `category_translation` | 카테고리 영문 번역 |

### 📁 Olist Marketing Funnel/ — B2B 셀러 유치 데이터 (2개)

| CSV 파일명 | BigQuery 테이블명 | 내용 |
|-----------|----------------|------|
| `olist_marketing_qualified_leads_dataset.csv` | `marketing_qualified_leads` | 셀러 마케팅 리드 |
| `olist_closed_deals_dataset.csv` | `closed_deals` | 계약 완료 셀러 |

### 📁 kaggle/ — Kaggle CRM/쿠폰 데이터 (8개)

| CSV 파일명 | BigQuery 테이블명 | 내용 |
|-----------|----------------|------|
| `hh_demographic.csv` | `hh_demographic` | 가구 인구통계 (801가구) |
| `transaction_data.csv` | `transaction_data` | 구매 거래 내역 (약 260만건) |
| `product.csv` | `product` | 상품 마스터 |
| `campaign_desc.csv` | `campaign_desc` | 캠페인 정의 (30개) |
| `campaign_table.csv` | `campaign_table` | 캠페인 대상 가구 |
| `coupon.csv` | `coupon` | 쿠폰-상품 매핑 |
| `coupon_redempt.csv` | `coupon_redempt` | 쿠폰 사용 내역 |
| `causal_data.csv` | `causal_data` | 매장 프로모션 데이터 (664MB 대용량) |

---

## 왜 19개 전부 올려야 하는가?

우리 프로젝트의 전사 OKR 지표(재구매율, 배송 지연율, AOV 등)는 **3개 데이터 그룹이 AARRR 각 단계를 나눠서 담당**하고 있어서, 하나라도 빠지면 분석이 끊깁니다.

| 데이터 그룹 | AARRR 담당 | 이 데이터로 보는 지표 |
|------------|-----------|-------------------|
| **Olist B2C** (9개) | Activation / Retention / Revenue / Referral | 재구매율(KR1), 배송 지연율(KR4), 저평점 비중(KR5), AOV(G2) |
| **Marketing Funnel** (2개) | Acquisition | MQL → 계약 전환율, 셀러 유치 채널 분석 |
| **Kaggle CRM** (8개) | Retention / Revenue | 쿠폰 효과, 캠페인 전환율, 가구별 구매 패턴 (CRM Lifecycle 설계 근거) |

**테이블 간 연결 관계 (BigQuery에서 JOIN할 때 필요):**

```
[B2B → B2C 연결]
closed_deals.seller_id ──→ sellers.seller_id
  (셀러 유치 후 실제 판매까지 추적 가능)

[B2C 내부 연결]
customers → orders → order_items → products → category_translation
                  └→ order_payments
                  └→ order_reviews
customers/sellers → geolocation (지역별 분석)

[Kaggle 내부 연결]
hh_demographic → transaction_data → product
              └→ campaign_table → campaign_desc
              └→ coupon_redempt → coupon
```

> 결론: Looker Studio에서 전사 OKR 대시보드를 하나로 만들려면 19개 전부 필요합니다.

---

## Step 1: 사전 준비

### 1-1. Google Cloud SDK 설치 확인

PowerShell에서 아래 입력:

```
bq version
```

버전 숫자(`BigQuery CLI 2.x.x`)가 나오면 설치된 것.  
오류가 나면 [Google Cloud SDK 설치](https://cloud.google.com/sdk/docs/install) 후 다시 진행.

### 1-2. Google 계정 로그인

```
gcloud auth login
```

브라우저가 열리면 팀 Google 계정으로 로그인.

### 1-3. 프로젝트 설정

```
gcloud config set project olist-team-analysis
```

`Updated property [core/project].` 메시지가 나오면 완료.

---

## Step 2: 데이터셋 확인

BigQuery 콘솔(https://console.cloud.google.com/bigquery)에서  
왼쪽 패널에 `olist_analysis` 데이터셋이 보이면 이미 생성된 것 → Step 3으로 바로 이동.

없으면 PowerShell에서 실행:

```
bq mk --dataset --location=asia-northeast3 olist-team-analysis:olist_analysis
```

---

## Step 3: CSV 파일을 BigQuery 테이블로 업로드

> **스크립트 파일을 실행해서 19개를 한 번에 올립니다.**  
> 스크립트 파일 위치: `project-2/guides/upload_to_bigquery.ps1`

### 실행 방법 (3단계)

**① 스크립트 실행 허용 설정**

PowerShell에서 입력:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**② 스크립트 폴더로 이동**

```
cd "C:/Users/본인계정/OneDrive/Desktop/fcicb7/project-2/guides"
```

> `본인계정` 부분은 본인 Windows 사용자명으로 변경하세요.  
> 예: `ajh81` → `C:/Users/ajh81/OneDrive/...`

**③ 스크립트 실행**

```
.\upload_to_bigquery.ps1
```

### 진행 상황 확인

실행하면 아래처럼 번호가 표시되며 자동으로 순서대로 올라갑니다:

```
===== Olist B2C 업로드 시작 (9개) =====
[1/19] orders 완료
[2/19] customers 완료
...
===== causal_data 업로드 (664MB, 수분 소요) =====
[19/19] causal_data 완료
===== 전체 업로드 완료! =====
```

> `causal_data.csv`는 664MB로 수 분이 걸립니다. 터미널이 멈춘 것처럼 보여도 정상입니다.

---

## Step 4: 업로드 확인

1. BigQuery 콘솔 접속 → 왼쪽 패널에서 `olist_analysis` 클릭
2. 테이블 19개가 목록에 보이는지 확인
3. 아무 테이블 클릭 → **"미리보기"** 탭에서 데이터 확인

**정상 완료 시 테이블 목록:**

```
campaign_desc / campaign_table / category_translation / causal_data /
closed_deals / coupon / coupon_redempt / customers / geolocation /
hh_demographic / marketing_qualified_leads / order_items / order_payments /
orders / product / products / sellers / transaction_data / order_reviews
```

테스트 쿼리 (쿼리 편집기에서 실행):

```sql
-- 주문 건수 확인
SELECT COUNT(*) AS total_orders
FROM `olist-team-analysis.olist_analysis.orders`;

-- 재구매 고객 수 확인 (Quick Check)
SELECT
  customer_unique_id,
  COUNT(order_id) AS order_count
FROM `olist-team-analysis.olist_analysis.orders` o
JOIN `olist-team-analysis.olist_analysis.customers` c
  ON o.customer_id = c.customer_id
GROUP BY customer_unique_id
HAVING order_count > 1
LIMIT 10;
```

정상이면 결과가 표 형태로 출력됩니다.

---

## Step 5: Looker Studio 연결

1. https://lookerstudio.google.com 접속
2. **"만들기"** → **"보고서"** 클릭
3. 데이터 소스 추가 창에서 **"BigQuery"** 선택
4. 아래 경로로 테이블 선택:
   ```
   olist-team-analysis → olist_analysis → orders (또는 원하는 테이블)
   ```
5. **"연결"** → **"보고서에 추가"** 클릭
6. 차트 생성 시작

> **팀 공유 설정 필요**: Looker Studio 보고서 공유 링크 → "편집자" 권한으로 팀원 Gmail 추가

---

## Step 6: 팀원 BigQuery 권한 공유

BigQuery 프로젝트 관리자가 아래 작업 진행:

1. BigQuery 콘솔 → `olist_analysis` 데이터셋 클릭
2. 우측 상단 **"공유"** 클릭
3. 팀원 Gmail 주소 입력
4. 역할 설정:

| 역할 | 권한 |
|------|------|
| BigQuery 데이터 뷰어 | 조회만 가능 |
| BigQuery 데이터 편집자 | 조회 + 데이터 수정 |
| BigQuery 데이터 오너 | 모든 권한 |

5. **"저장"** 클릭 → 팀원 이메일로 초대 메일 발송됨

---

## 개인 연습용 프로젝트 주의사항

개인 프로젝트(`olist-practice-jh` 등)를 처음 만들 때 아래 사항을 확인하세요.

**① 샌드박스 모드 해제 필요**

신규 Google Cloud 프로젝트는 기본적으로 샌드박스 모드로 시작합니다.  
샌드박스 상태에서는 `bq load`(로컬 파일 업로드)가 실행되지 않습니다.

> 해결: BigQuery 콘솔 상단 배너의 **"업그레이드"** 클릭 → 기존 결제 계정 선택  
> 카드 등록만 하면 되며, **무료 한도(월 1TB 쿼리 + 10GB 저장) 안에서 비용은 발생하지 않습니다.**

**② 테이블 만료일 확인**

업로드 후 테이블 목록에 만료 시간이 표시될 수 있습니다 (약 60일).  
만료일이 지나면 테이블이 자동 삭제됩니다.

> 해결: 만료일을 제거하려면 각 테이블 클릭 → **"세부정보"** 탭 → **"테이블 만료"** → **"없음"** 으로 변경

**③ 프로젝트 간 복사(bq cp)는 리전이 같아야 함**

공용 프로젝트(서울 리전)에서 개인 프로젝트로 `bq cp`로 복사할 경우,  
개인 프로젝트 리전이 다르면 cross-region 오류가 발생합니다.

> 해결: `bq cp` 대신 `upload_to_personal_bq.ps1` 스크립트로 로컬 파일에서 직접 업로드

---

## 문제 해결

| 증상 | 해결 방법 |
|------|---------|
| "권한이 없습니다" 오류 | BigQuery 프로젝트 관리자에게 접근 권한 요청 |
| `bq` 명령어가 실행 안 됨 | Google Cloud SDK 설치 후 `gcloud auth login` 실행 |
| 스크립트 실행 오류 | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` 먼저 실행 |
| CSV 업로드 중 스키마 오류 | 스크립트의 `--autodetect` 옵션이 자동 처리함 |
| 날짜 컬럼 타입이 STRING으로 잡힘 | 쿼리에서 `PARSE_DATE` 또는 `CAST(... AS DATE)` 사용 |
| Looker에서 테이블이 안 보임 | BigQuery 뷰어 권한 재확인 / 브라우저 새로고침 |
| 쿼리 실행 비용 걱정 | BigQuery 무료 티어: 월 1TB 쿼리 무료 (Olist 데이터는 충분히 무료 범위) |
