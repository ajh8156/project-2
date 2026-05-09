# Looker Studio 간소화 대시보드 — 디자인 스펙

> 작성일: 2026-05-08  
> 발표일: 2026-05-09  
> 목적: 슬27 참고 슬라이드 링크용 · Q&A·후속 접근용  
> 범위: 단일 페이지, 차트 7개 + 정적 요소 3개

---

## 배경 및 결정 사항

- 기존 스펙 (28개 차트, 3페이지)은 오늘 하루 안에 완성 불가
- 루커는 발표 본문에서 패스(슬27)되는 참고 자료 → 완성도 높은 1페이지가 더 효과적
- 사용 가능 시간: 2~3시간
- 연결된 데이터 소스: `t_orders_summary`, `t_order_items`, `t_marketing_funnel`
- 추가 BQ 작업: `t_customer_summary` 1개 생성 필요 (KR1·KR2용)

---

## 디자인 시스템 (팀 SSOT 기준)

### 색상

| 역할 | 색상 코드 | 사용처 |
|------|---------|------|
| Brand · CTA | `#1F4DDB` | 헤더, 인사이트 박스 강조, 목표값 |
| Blue Border | `#BAD2F5` | 구분선 |
| Blue BG | `#E8F0FE` | 강조 배경 |
| Text | `#202124` | 본문 |
| Muted | `#5F6368` | 보조 텍스트, 캡션 |
| Surface | `#F9FAFB` | 카드 배경 |
| Success | `#34A853` | TF3·정시배송·5점 막대 강조 |
| Success Soft | `#E6F4EA` | Success 카드 배경 |
| Alert | `#EA4335` | KR4·KR5·지연배송·BF cohort 카드 |
| Alert Soft | `#FCE8E6` | Alert 카드 배경 |

### 타이포그래피

| 레벨 | 크기/굵기 | 용도 |
|------|---------|------|
| Heading | 32 / 700 | 페이지 제목 |
| Body | 18 / 400 | 스코어카드 수치, 본문 |
| Caption | 12 / 400 | 보조 텍스트, 목표값 비교 |

폰트: Pretendard (Looker 미지원 시 Noto Sans KR 대체)

### 컴포넌트

**KPI 카드**: 왼쪽 컬러 보더 + 수치(Body) + "+X%p vs 현재 Y%" (Caption, Muted)  
**신호등 배지**: Critical(적신호) · Watch(주의) · Healthy(정상)

---

## 단일 페이지 레이아웃

```
┌─────────────────────────────────────────────────────────────────┐
│ [A] 헤더 텍스트                                                  │
│  Olist 재구매 구조 진단 · 2018년 컨설팅 보고서                    │
│  분석 기간: 2016.09~2018.08 · 주문 99,441건 · 고객 96,096명      │
├──────┬──────┬──────┬──────┬──────┬──────────────────────────────┤
│ [B1] │ [B2] │ [B3] │ [B4] │ [B5] │  [B6] BF cohort 30일 재구매  │
│  KR1 │  KR2 │  KR3 │  KR4 │  KR5 │        0.56%                 │
│ 3.0% │1.033 │6.13% │8.16% │12.82%│  (평시 3.0%의 1/5) ★충격수치 │
│      │      │      │      │      │  배경: Alert Soft             │
├──────┴──────┴──────┴──────┴──────┴──────────────────────────────┤
│ [C] AARRR 신호등 (3개 배지 가로 배치)                            │
│  ● Healthy · Acquisition — 신규 충분                             │
│  ● Watch   · Activation  — 저평점 12.82%                        │
│  ● Critical · Retention  — 재구매 3.0% ← 핵심 병목              │
├──────────────────────────────┬──────────────────────────────────┤
│ [D1] 평점별 재구매율 (막대)   │ [D2] 정시 vs 지연 재구매율 (막대) │
│  1~4점: ~2.5% (회색)         │  정시 3.04% (Success)            │
│  5점: 3.12% ★ (Success)      │  지연 2.51% (Alert)              │
│  → "재구매는 5점에서만"       │  → "5점은 배송이 결정"           │
├──────────────────────────────┴──────────────────────────────────┤
│ [E] 인사이트 박스 (Surface 배경, 왼쪽 Brand 보더)                │
│  · 첫구매 후 97%가 이탈 (재구매율 3.0%)                          │
│  · BF 고객은 0.56%만 재구매 — 평시의 1/5                         │
│  · 재구매는 5점에서만 만들어지고 (3.12%), 5점은 배송이 결정      │
│  · AARRR 병목: Retention 🚨 → TF 3개로 해결                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 요소별 상세

### [A] 헤더 (텍스트 박스)
- 상단 전체 너비
- 텍스트: `Heading(32/700)` + `Caption(12/400)`
- 색상: 제목 `#202124` / 서브 `#5F6368`

### [B1~B5] KR 스코어카드 5개

| 카드 | 데이터 소스 | 필드 | 집계 | 목표 | 보더 색 |
|------|-----------|------|------|------|---------|
| KR1 재구매율 | `t_customer_summary` | `is_repeat` | 평균 | 4.5% | Success |
| KR2 주문수/인 | `t_customer_summary` | `order_count` | 평균 | 1.06 | Success |
| KR3 재구매 비중 | `t_orders_summary` | `is_repeat_customer` | 평균 | 9.0% | Success |
| KR4 지연율 | `t_orders_summary` | `is_delayed` | 평균 (필터: seq=1) | 6.0% | Alert |
| KR5 저평점 | `t_orders_summary` | `is_low_rating` | 평균 (필터: seq=1) | 10.5% | Alert |

- 수치 폰트: 36pt 이상 (뒷자리에서 가독)
- KR4·KR5: 카드 배경 `#FCE8E6`
- KR1·KR2·KR3: 카드 배경 `#E6F4EA`
- 캡션: "현재 X% → 목표 Y%"

### [B6] BF cohort 카드 (정적 텍스트 박스)
- 배경: `#FCE8E6`
- 수치: `0.56%` (36pt 이상, Alert 색)
- 서브: "참고: 평시 3.00%의 1/5"
- BigQuery SQL로 미리 계산 후 고정값 입력

### [C] AARRR 신호등 (정적 텍스트 박스 3개 가로)
- 팀 배지 컴포넌트 스타일
- Healthy(녹): `#E6F4EA` / Watch(노): `#FEF7E0` / Critical(적): `#FCE8E6`
- 각 배지에 단계명 + 한 줄 설명

### [D1] 평점별 재구매율
- 차트: 세로 막대
- 데이터: `t_orders_summary`
- 차원: `review_score` / 측정항목: `is_repeat_customer` 평균
- 필터: `customer_order_seq = 1` AND `review_score IS NOT NULL`
- 5점 막대만 `#34A853`, 나머지 `#DADCE0`
- Y축: 0~4% 고정 / 데이터 라벨 표시

### [D2] 정시 vs 지연 재구매율
- 차트: 세로 막대 (2개)
- 데이터: `t_orders_summary`
- 계산된 필드: `CASE WHEN is_delayed = 1 THEN '지연 배송' ELSE '정시 배송' END`
- 측정항목: `is_repeat_customer` 평균 / 필터: `customer_order_seq = 1`
- 정시: `#34A853` / 지연: `#EA4335`
- 데이터 라벨: 백분율 2자리

### [E] 인사이트 박스 (텍스트 박스)
- 배경: `#E8F0FE` (Blue BG — Looker는 왼쪽 보더 미지원, 배경색으로 Brand 느낌 대체)
- 폰트: Body 18pt / Caption 12pt
- 제목 텍스트 색: `#1F4DDB` (Brand)

---

## BigQuery 사전 작업

### t_customer_summary 생성 SQL

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

### BF cohort 30일 재구매율 확인 SQL (결과값 B6 카드에 직접 입력용)

```sql
WITH bf_buyers AS (
  SELECT customer_unique_id, MIN(DATE(purchase_timestamp)) AS first_bf_date
  FROM `olist-team-analysis.olist_analysis.t_orders_summary`
  WHERE DATE(purchase_timestamp) BETWEEN '2017-11-24' AND '2017-11-26'
    AND order_status = 'delivered'
  GROUP BY customer_unique_id
),
re_buyers AS (
  SELECT bf.customer_unique_id
  FROM bf_buyers bf
  JOIN `olist-team-analysis.olist_analysis.t_orders_summary` o
    ON bf.customer_unique_id = o.customer_unique_id
  WHERE DATE(o.purchase_timestamp) > bf.first_bf_date
    AND DATE(o.purchase_timestamp) <= DATE_ADD(bf.first_bf_date, INTERVAL 30 DAY)
  GROUP BY bf.customer_unique_id
)
SELECT
  ROUND(COUNT(DISTINCT re_buyers.customer_unique_id) /
        COUNT(DISTINCT bf_buyers.customer_unique_id) * 100, 2) AS bf_cohort_30d_pct
FROM bf_buyers
LEFT JOIN re_buyers USING (customer_unique_id);
```

---

## 작업 순서 및 시간 계획 (총 2~2.5시간)

| 단계 | 작업 | 예상 시간 |
|------|------|---------|
| 1 | BigQuery `t_customer_summary` 생성 + BF cohort SQL 실행 | 15분 |
| 2 | Looker에 `t_customer_summary` 데이터 소스 추가 | 5분 |
| 3 | 헤더 텍스트 박스 배치 | 5분 |
| 4 | KR1~KR5 스코어카드 5개 + BF cohort 카드 | 35분 |
| 5 | AARRR 신호등 텍스트 박스 3개 | 15분 |
| 6 | 피크 차트 D1 (평점별 재구매율) | 20분 |
| 7 | 피크 차트 D2 (정시 vs 지연) | 20분 |
| 8 | 인사이트 박스 | 10분 |
| 9 | 색상·정렬·폰트 마무리 점검 | 15분 |
| **합계** | | **약 2시간 20분** |

---

## 발표 전 최종 체크 (5/8 완료 후)

- [ ] 모든 스코어카드 수치가 슬라이드 본문 수치와 일치하는가
- [ ] BF cohort 0.56% 카드 수치 검증
- [ ] 5점 막대 녹색 강조 잘 보이는가
- [ ] 공유 권한 `보기 전용` 설정
- [ ] 슬27 슬라이드에 URL + QR 코드 삽입
