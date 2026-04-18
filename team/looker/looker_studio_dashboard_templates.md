# Looker Studio 대시보드 템플릿 추천

> 목적: Olist 이커머스 데이터 분석 프로젝트에 활용할 Looker Studio 대시보드 템플릿 정리  
> 작성일: 2026-04-14  
> 기준: project-2 커리큘럼 (AARRR, KPI Tree, 코호트, 퍼널, RFM 분석)

---

## 프로젝트 핵심 요약

| 항목 | 내용 |
|------|------|
| 데이터 | Olist 브라질 이커머스 (주문 9.9만건, 고객 9.3만명) |
| 핵심 문제 | 재구매율 3% → 재구매 구조 개선 |
| 프레임워크 | AARRR, KPI Tree, OKR |
| 팀 | CX, Logistics + 기획/마케팅 관점 |
| 시각화 도구 | Looker Studio (커리큘럼 지정) |

---

## 1. 무료 템플릿

| 템플릿 | 적합한 분석 | 링크 |
|--------|------------|------|
| Supermetrics Ecommerce Dashboard | 매출 트렌드, AOV, 전환율 | https://supermetrics.com/template-gallery/looker-studio-ecommerce-dashboard |
| Porter Metrics Funnel Templates | AARRR 퍼널 전환율 시각화 | https://portermetrics.com/en/dashboard-templates/funnels/ |
| Porter Ecommerce Templates | 이커머스 종합 대시보드 | https://portermetrics.com/en/templates/e-commerce/ |
| Dashboard Design Lab GA4 Templates | 사용자 행동, 코호트 분석 | https://dashboarddesignlab.com/blog/ga4-report-templates-looker-studio/ |

---

## 2. 유료 템플릿 (프로젝트에 적합)

| 템플릿 | 적합한 분석 | 링크 |
|--------|------------|------|
| Gaille Reports 코호트 분석 | LTV, 리텐션, 코호트 | https://gaillereports.com/cohort-analysis-in-looker-studio-and-google-sheets-template-overview-ltv-and-customer-retention/ |
| Gaille Reports 이커머스 3종 팩 | 코호트 + RFM + 이탈 분석 | https://gaillereports.com/product-category/all-templates/ecommerce/ |
| Datmark CRO Funnel | 전환율 최적화 퍼널 | https://datmark.gumroad.com/l/cro-looker-studio |

---

## 3. GitHub 참고용

| 리포지토리 | 설명 |
|---|---|
| Ishansingh438/Google-Analytics-Looker-Studio | 퍼널 + 코호트 분석 포함, 구조 참고용 |
| 링크 | https://github.com/Ishansingh438/Google-Analytics-Looker-Studio |

### LookML 블록 (Looker Enterprise 참고용)

| 리포지토리 | 설명 |
|---|---|
| llooker/improvado | AdWords, Facebook, Twitter, YouTube 등 다수 플랫폼 대시보드 |
| looker-open-source/dashboard-summarization | AI 기반 대시보드 요약 확장 |
| pipeline-looker-blocks/facebookads | Facebook Ads 대시보드 LookML 블록 |
| kustomer/looker | 고객 대화/유저 분석 대시보드 블록 |
| snowplow/looker-snowplow-web | 웹 트래킹 데이터 분석 대시보드 |
| appomni/looker-dashboard | SaaS 보안 대시보드 |

---

## 4. 팀별 추천 조합

| 팀/관점 | 필요한 대시보드 | 추천 템플릿 참고 |
|---------|----------------|-----------------|
| 전사 OKR | 재구매율, AOV, GMV 트렌드 | Supermetrics Ecommerce |
| 마케터 | AARRR 퍼널, 채널별 전환율 | Porter Funnel + CRO Funnel |
| 기획자 | 코호트 리텐션, RFM 세그먼트 | Gaille 코호트/RFM 팩 |
| CX | 리뷰 점수, 저평점 분석 | 커스텀 (기본 차트로 충분) |
| Logistics | 배송 지연율, 지역별 분포 | 커스텀 (지도 차트 활용) |

---

## 5. 데이터 연결 방법

Olist 데이터는 CSV 기반이므로 아래 방법으로 Looker Studio에 연결 가능:

1. **Google Sheets 연결** — CSV를 Google Sheets에 업로드 후 Looker Studio 데이터 소스로 연결
2. **BigQuery 연결** — CSV를 BigQuery에 로드 후 연결 (대용량 처리에 유리)
3. **CSV 직접 업로드** — Looker Studio의 파일 업로드 커넥터 사용 (소규모 데이터)

### 연결 시 참고사항

- `olist_geolocation_dataset.csv`는 100만 행 → Google Sheets 한도(500만 셀) 주의, BigQuery 권장
- 테이블 간 JOIN은 Looker Studio 블렌딩 또는 사전 처리(Python/SQL) 후 업로드 권장
- 날짜 필드(`order_purchase_timestamp` 등)는 Looker Studio에서 날짜 타입으로 변환 필요
