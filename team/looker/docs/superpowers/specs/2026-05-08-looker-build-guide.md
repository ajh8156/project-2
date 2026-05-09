# Looker Studio 대시보드 제작 가이드 — 팀원 공유용

> 작성일: 2026-05-08  
> 발표일: 2026-05-09  
> 연계 문서: `2026-05-08-looker-simplified-dashboard-design.md` (디자인 스펙)  
> 현재 상태: 헤더·KR3·KR4 완료 / KR5·BF·AARRR·차트·인사이트 박스 미완

---

## 레이아웃 한눈에 보기

```
[A]  헤더 텍스트                                              ✅ 완료
[B1] KR1  [B2] KR2  [B3] KR3  [B4] KR4  [B5] KR5  [B6] BF cohort
     ⏳팀장      ⏳팀장      ✅완료      ✅완료      ❌미완      ❌미완
[C]  AARRR 신호등 3개 (Healthy / Watch / Critical)            ❌미완
[D1] 평점별 재구매율 (막대)     [D2] 정시 vs 지연 재구매율 (막대)  ❌미완
[E]  인사이트 박스                                            ❌미완
```

---

## 데이터 소스 현황

| 소스 | 상태 | 비고 |
|------|------|------|
| `t_orders_summary` (커스텀 쿼리) | ✅ 연결됨 | is_delayed, is_low_rating, is_repeat_customer, customer_order_seq 포함 |
| `t_customer_summary` | ⏳ 팀장 BQ 권한 필요 | KR1·KR2용 |

---

## 디자인 시스템 색상 (팀 SSOT)

| 용도 | 색상 코드 |
|------|---------|
| 성공·목표 달성 지표 배경 | `#E6F4EA` |
| 경고·문제 지표 배경 | `#FCE8E6` |
| AARRR Watch 배경 | `#FEF7E0` |
| 인사이트 박스 배경 | `#E8F0FE` |
| 인사이트 제목 색 | `#1F4DDB` |
| 성공 강조 (막대 등) | `#34A853` |
| 경고 강조 (막대 등) | `#EA4335` |

---

## 남은 작업 순서

### ① KR3·KR4 필터 수정 (먼저 해야 함)

KR3, KR4 스코어카드는 만들어졌지만 필터가 빠져 있어서 값이 약간 다릅니다.  
각 스코어카드 클릭 → 우측 패널 `설정` → `+ 필터 추가` 클릭

| 스코어카드 | 필터 조건 | 예상 값 |
|---------|---------|-------|
| KR4 지연율 | `customer_order_seq` = `1` | ~8.16% |
| KR3 재구매 비중 | 필터 없음 (전체) | ~6.13% |

> KR3는 필터 불필요. KR4만 추가하면 됩니다.

---

### ② KR5 스코어카드 만들기

`차트 추가` → `스코어카드`

| 항목 | 설정값 |
|------|------|
| 데이터 소스 | `t_orders_summary` |
| 측정항목 | `kr5_pct` (= `AVG(is_low_rating) * 100`) |
| 형식 | `Number(2)` |
| 필터 | `customer_order_seq = 1` |
| 라벨 | `KR5 저평점 · 목표 10.5%` |
| 배경색 | `#FCE8E6` |
| 수치 폰트 | 36pt 이상 |

> `kr5_pct` 필드가 없으면: `리소스` → `데이터 소스 관리` → `t_orders_summary` 수정 → `+ 필드 추가` → 이름 `kr5_pct` / 공식 `AVG(is_low_rating) * 100`

---

### ③ BF cohort 카드 [B6] — 정적 텍스트

`삽입` → `텍스트` → KR 스코어카드 오른쪽에 배치

```
BF cohort 30일 재구매율
0.56%
참고: 평시 3.0%의 1/5
```

| 항목 | 설정값 |
|------|------|
| 배경색 | `#FCE8E6` |
| `0.56%` 폰트 | 36pt, 색상 `#EA4335` |
| 나머지 텍스트 | 12pt, 색상 `#5F6368` |

---

### ④ AARRR 신호등 [C] — 텍스트 박스 3개

`삽입` → `텍스트` 3개 만들어 가로로 나란히 배치

**박스 1**
```
● Healthy  ·  Acquisition
신규 고객 충분
```
배경색: `#E6F4EA`

**박스 2**
```
● Watch  ·  Activation
저평점 12.82%
```
배경색: `#FEF7E0`

**박스 3**
```
● Critical  ·  Retention
재구매율 3.0% ← 핵심 병목
```
배경색: `#FCE8E6`

---

### ⑤ 피크 차트 1 — 평점별 재구매율 [D1]

`차트 추가` → `세로 막대 차트`

| 항목 | 설정값 |
|------|------|
| 데이터 소스 | `t_orders_summary` |
| 차원 | `avg_review_score` |
| 측정항목 | `is_repeat_customer` → 집계 `평균` |
| 필터 1 | `customer_order_seq` = `1` |
| 필터 2 | `avg_review_score` IS NOT NULL |
| Y축 범위 | 0 ~ 0.04 고정 |
| 데이터 라벨 | 켜기 |

**색상 설정** (스타일 탭 → 막대 색상):
- `avg_review_score = 5` 막대: `#34A853`
- 나머지 막대: `#DADCE0`

---

### ⑥ 피크 차트 2 — 정시 vs 지연 재구매율 [D2]

먼저 계산된 필드 추가:  
`리소스` → `데이터 소스 관리` → `t_orders_summary` → `+ 필드 추가`
- 이름: `delivery_label`
- 공식: `CASE WHEN is_delayed = 1 THEN '지연 배송' ELSE '정시 배송' END`

`차트 추가` → `세로 막대 차트`

| 항목 | 설정값 |
|------|------|
| 데이터 소스 | `t_orders_summary` |
| 차원 | `delivery_label` |
| 측정항목 | `is_repeat_customer` → 집계 `평균` |
| 필터 | `customer_order_seq` = `1` |
| 데이터 라벨 | 켜기 (백분율 2자리) |

**색상**: `정시 배송` → `#34A853` / `지연 배송` → `#EA4335`

---

### ⑦ 인사이트 박스 [E]

`삽입` → `텍스트` → 페이지 맨 아래 가로 전체

```
→ 발견
  · 첫구매 후 97%가 이탈 (재구매율 3.0%)
  · BF 고객은 0.56%만 재구매 — 평시의 1/5
  · 재구매는 5점에서만 만들어지고 (3.12%), 5점은 배송이 결정
  · AARRR 병목: Retention 🚨 → TF 3개로 해결
```

| 항목 | 설정값 |
|------|------|
| 배경색 | `#E8F0FE` |
| `→ 발견` 폰트 | 16pt, 굵게, 색상 `#1F4DDB` |
| 본문 폰트 | 12pt, 색상 `#202124` |

---

## 팀장 권한 받은 후 추가 작업 (KR1·KR2)

BigQuery `olist_analysis` 데이터셋에 아래 SQL 실행 요청:

```sql
CREATE OR REPLACE TABLE `olist-team-analysis.olist_analysis.t_customer_summary` AS
SELECT
  customer_unique_id,
  COUNT(DISTINCT order_id) AS order_count,
  IF(COUNT(DISTINCT order_id) >= 2, 1, 0) AS is_repeat,
  MIN(DATE(purchase_timestamp)) AS first_purchase_date
FROM `olist-team-analysis.olist_analysis.t_orders_summary`
WHERE order_status = 'delivered'
GROUP BY customer_unique_id;
```

완료 후 Looker에서:
1. `데이터 추가` → `t_customer_summary` 연결
2. KR1 스코어카드: `is_repeat` 평균 × 100 → 목표 4.5%
3. KR2 스코어카드: `order_count` 평균 → 목표 1.06

현재 빈 스코어카드(Record Count 99,441) 2개를 교체하면 됩니다.

---

## 발표 전 최종 체크

- [ ] 모든 KR 수치가 슬라이드 본문 수치와 일치하는가
- [ ] 공유 권한 `보기 전용` 설정
- [ ] 슬27 슬라이드에 대시보드 URL + QR 코드 삽입
