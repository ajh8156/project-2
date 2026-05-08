"""
슬6 RFM 산점도 차트 생성 — Python matplotlib
디자인 토큰 색(블루 단색) 적용 + Pretendard 폰트
출력: team/발표자료/exports/rfm-scatter.png (3200x1800 @2x)
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 디자인 토큰
OLIST_BLUE = "#1E40FF"
BLUE_TINT  = "#EEF2FF"
GRAY_400   = "#9CA3AF"
GRAY_200   = "#E5E7EB"
GRAY_600   = "#5A5A5A"
NEAR_BLACK = "#080808"

# 폰트
mpl.rcParams["font.family"] = ["Pretendard", "sans-serif"]
mpl.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(8, 4.4), dpi=200)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

np.random.seed(42)

# 좌상 — 이탈재구매 2,562명 ★ (강조)
n_churn_repeat = 80
ax.scatter(np.random.uniform(0.05, 0.45, n_churn_repeat),
           np.random.uniform(0.55, 0.95, n_churn_repeat),
           color=OLIST_BLUE, s=42, alpha=0.78,
           edgecolors="white", linewidths=0.6, zorder=3)

# 우상 — 충성 고객
ax.scatter(np.random.uniform(0.55, 0.95, 110),
           np.random.uniform(0.55, 0.95, 110),
           color=GRAY_400, s=20, alpha=0.55, zorder=2)

# 우하 — 신규
ax.scatter(np.random.uniform(0.55, 0.95, 160),
           np.random.uniform(0.05, 0.45, 160),
           color=GRAY_400, s=18, alpha=0.5, zorder=2)

# 좌하 — 이탈 (포기)
ax.scatter(np.random.uniform(0.05, 0.45, 320),
           np.random.uniform(0.05, 0.45, 320),
           color=GRAY_200, s=12, alpha=0.5, zorder=1)

# 4분면 십자선
ax.axvline(0.5, color=GRAY_400, lw=0.8, alpha=0.4, zorder=0)
ax.axhline(0.5, color=GRAY_400, lw=0.8, alpha=0.4, zorder=0)

# 강조 영역 박스 (좌상)
from matplotlib.patches import Rectangle
ax.add_patch(Rectangle((0.02, 0.52), 0.46, 0.46,
                        linewidth=1.8, edgecolor=OLIST_BLUE,
                        facecolor=BLUE_TINT, alpha=0.25, zorder=0.5))

# 라벨
ax.text(0.25, 0.96, "이탈재구매 2,562명 ★",
        fontsize=15, fontweight="900", ha="center", va="top", color=OLIST_BLUE)
ax.text(0.25, 0.91, "회복 1순위 타겟",
        fontsize=10, ha="center", va="top", color=OLIST_BLUE)

ax.text(0.75, 0.96, "충성 고객",
        fontsize=12, fontweight="700", ha="center", va="top", color=GRAY_600)
ax.text(0.75, 0.91, "유지", fontsize=9, ha="center", va="top", color=GRAY_600)

ax.text(0.75, 0.04, "신규", fontsize=12, fontweight="700",
        ha="center", va="bottom", color=GRAY_600)
ax.text(0.75, 0.09, "양육", fontsize=9, ha="center", va="bottom", color=GRAY_600)

ax.text(0.25, 0.04, "이탈", fontsize=12, fontweight="700",
        ha="center", va="bottom", color=GRAY_400)
ax.text(0.25, 0.09, "포기", fontsize=9, ha="center", va="bottom", color=GRAY_400)

# 축
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("← Recency (구매 최근성) →",
              fontsize=10, color=GRAY_600, labelpad=8)
ax.set_ylabel("Frequency (구매 빈도) →",
              fontsize=10, color=GRAY_600, labelpad=8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color(GRAY_200)
ax.spines["left"].set_color(GRAY_200)
ax.set_xticks([])
ax.set_yticks([])
ax.tick_params(left=False, bottom=False)

plt.tight_layout()
out = Path(__file__).resolve().parent.parent / "exports" / "rfm-scatter.png"
out.parent.mkdir(exist_ok=True)
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved -> {out}  ({out.stat().st_size:,} bytes)")
