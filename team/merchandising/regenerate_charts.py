"""
MD팀 차트 재생성 스크립트
- md_okr_01_current_state.png (리뷰 불만 카테고리 분류)
- md_okr_06_option_a_logic.png (다품목 구매 시 배송비 절감)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── 한글 폰트 설정 ──────────────────────────────────────────
plt.rcParams['font.family'] = 'Apple SD Gothic Neo'
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = "images"


# ════════════════════════════════════════════════════════════
# Chart 1: 리뷰 불만 카테고리 분류 (DL 분석 결과)
# ════════════════════════════════════════════════════════════
def chart_review_complaints():
    # DL(딥러닝) 공식 수치 — review_tfidf_analysis.md 기준
    categories = [
        "미배송\n(42.0%)",
        "환불/CS\n무응답 (19.8%)",
        "제품 불량\n(9.2%)",
        "배송 지연\n(8.7%)",
        "기대 불일치\n(8.5%)",
        "가격/배송비\n(6.3%)",
        "포장 불량\n(5.5%)",
    ]
    values = [42.0, 19.8, 9.2, 8.7, 8.5, 6.3, 5.5]
    # 배송 관련(미배송+배송지연) 강조, 신규 발견(가격/배송비) 강조
    colors = ['#C0392B', '#E74C3C', '#E67E22', '#E67E22',
              '#F39C12', '#2980B9', '#BDC3C7']

    fig, ax = plt.subplots(figsize=(9, 5.5))
    bars = ax.bar(range(len(categories)), values, color=colors,
                  width=0.6, zorder=3)

    # 바 위 수치 레이블
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.4,
                f'{val}%', ha='center', va='bottom',
                fontsize=9, fontweight='bold', color='#333333')

    # ── "679건 신규 발견" annotation — 가격/배송비(index 5) ──
    bar_x = 5
    bar_top = values[5]
    ax.annotate(
        "679건 신규 발견\n다품목 구매의 숨겨진 장벽",
        xy=(bar_x, bar_top),
        xytext=(bar_x - 1.6, bar_top + 14),
        fontsize=8.5,
        color='#1A5276',
        fontweight='bold',
        ha='center',
        va='bottom',
        bbox=dict(
            boxstyle='round,pad=0.45',
            facecolor='#EBF5FB',
            edgecolor='#2980B9',
            linewidth=1.5,
        ),
        arrowprops=dict(
            arrowstyle='-|>',
            color='#2980B9',
            lw=1.5,
            connectionstyle='arc3,rad=0.2',
        ),
    )

    # ── 배송 관련 합계 브래킷 annotation (미배송+배송지연 = 50.7%) ──
    y_bracket = 47
    ax.annotate(
        '', xy=(3, y_bracket), xytext=(0, y_bracket),
        arrowprops=dict(arrowstyle='-', color='#7F8C8D', lw=1.2),
    )
    ax.text(1.5, y_bracket + 0.8, '배송 관련 합계 50.7%',
            ha='center', va='bottom', fontsize=8,
            color='#7F8C8D', style='italic')

    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontsize=8.5)
    ax.set_ylabel('비중 (%)', fontsize=10)
    ax.set_ylim(0, 53)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_title('저평점 리뷰 불만 원인 분류\n(딥러닝 분석 결과, 10,611건)', fontsize=13, fontweight='bold', pad=14)

    # 출처 주석
    fig.text(0.5, -0.02,
             '출처: review_tfidf_analysis.md — paraphrase-multilingual-MiniLM-L12-v2, Zero-shot 분류, 신뢰도 80.8%',
             ha='center', fontsize=7, color='#999999')

    plt.tight_layout()
    path = f"{OUTPUT_DIR}/md_okr_01_current_state.png"
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ 저장: {path}")


# ════════════════════════════════════════════════════════════
# Chart 2: 다품목 구매 시 고객이 체감하는 배송비 절감
# ════════════════════════════════════════════════════════════
def chart_shipping_saving():
    labels = ["단품 구매\n(현재 90%)", "2개 이상 구매\n(번들/묶음)"]
    values = [6926, 3900]
    colors = ['#BDC3C7', '#E74C3C']

    fig, ax = plt.subplots(figsize=(6, 5.5))
    bars = ax.bar(range(len(labels)), values, color=colors,
                  width=0.45, zorder=3)

    # 바 위 수치 레이블
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 60,
                f'₩{val:,}', ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='#333333')

    # ── "-44% 절약" annotation (깔끔한 버전) ──────────────
    # 두 바의 상단 중간 지점에 브래킷 스타일 annotation
    x_mid = 0.5
    y_high = values[0]
    y_low  = values[1]

    # 수평 비교선 (두 바 상단 연결)
    ax.annotate(
        '',
        xy=(1, y_low + 200),
        xytext=(0, y_high - 200),
        arrowprops=dict(
            arrowstyle='-|>',
            color='#27AE60',
            lw=1.8,
            connectionstyle='arc3,rad=0',
        ),
    )

    # "-44% 절약" 텍스트 박스 (선 중간)
    ax.text(
        x_mid + 0.22,
        (y_high + y_low) / 2 + 300,
        "-44%\n절약",
        ha='center', va='center',
        fontsize=11, fontweight='bold', color='#27AE60',
        bbox=dict(
            boxstyle='round,pad=0.5',
            facecolor='#EAFAF1',
            edgecolor='#27AE60',
            linewidth=1.8,
        ),
    )

    # 절감 금액 보조 텍스트
    saving = values[0] - values[1]
    ax.text(
        x_mid + 0.22,
        (y_high + y_low) / 2 - 450,
        f"(₩{saving:,} 절감)",
        ha='center', va='center',
        fontsize=8.5, color='#27AE60',
    )

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylabel('개별 상품 배송비 (원)', fontsize=10)
    ax.set_ylim(0, 9200)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_title('다품목 구매 시\n고객이 체감하는 배송비 절감', fontsize=13, fontweight='bold', pad=14)

    # 주석: 합포장 가능 구조 전제
    fig.text(0.5, -0.03,
             '※ 합포장 가능 구조 전제 수치. Olist 현행(합포장 불가) 구조에는 적용 불가.',
             ha='center', fontsize=7.5, color='#888888', style='italic')

    plt.tight_layout()
    path = f"{OUTPUT_DIR}/md_okr_06_option_a_logic.png"
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ 저장: {path}")


if __name__ == '__main__':
    chart_review_complaints()
    chart_shipping_saving()
