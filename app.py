import io

import matplotlib
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


font_manager.fontManager.addfont("ipaexg.ttf")
matplotlib.rc("font", family="IPAexGothic")

st.title("時間感覚タイプテスト")

st.markdown("## テスト")

st.write("""\
まずは何も考えずに各項目を読み、できるだけ正直に答えてください。
それぞれの文章に「自分がどれぐらい当てはまるだろうか？」と考え、各問5点満点で採点しましょう。
全く当てはまらなければ1点、完全に当てはまれば5点です。\
""")

p2ja = {
    1: "完全に当てはまらない",
    2: "当てはまらない",
    3: "普通",
    4: "当てはまる",
    5: "完全に当てはまる",
}

questions = [
    # 予期が「濃い」または「薄い」
    "Q1. 何年過ぎても結果が出ない作業でも、重要だと思えば行動できる。",
    "Q2. 将来に問題が起きそうなときは、目の前の関心を忘れて対処できる。",
    "Q3. 将来の幸福を達成するためなら、目先の幸福を犠牲にするのにも抵抗がない。",
    "Q4. 過去にポジティブな経験をする機会を逃したことをよく後悔している。",
    "Q5. 魅力的な機会をうまく楽しめないことが多い。",
    # 予期が「多い」または「少ない」
    "Q6. 急な予定変更があると気が動転する。",
    "Q7. 作業に使える十分な時間がないとうろたえてしまう。",
    "Q8. 作業の優先順位をつけるのが苦手だ。",
    "Q9. 圧倒された気分のせいで、作業に取り組み始めるのに時間がかかる。",
    "Q10. やることは多いが、いまいち充実感を得られない。",
    # 想起が「正しい」または「誤り」
    "Q11. 課題に費やす時間を少なく見積もってしまうことはほとんどない。",
    "Q12. スケジュールを作るのがうまいと言われる。",
    "Q13. 計画を立てる際に、障害や不測の事態を必ず考える。",
    "Q14. 自分の願望だけをもとに計画を立てることはほとんどない。",
    "Q15. 作業の細かい手順を考えるのが得意だ。",
    # 想起が「肯定的」または「否定的」
    "Q16. 昔のことを考えていると充実した気分になる。",
    "Q17. 仕事や勉強ができる人だとは別に思われたくない。",
    "Q18. 過去のつらい体験が頭をよぎることはほとんどない。",
    "Q19. 決断を下すときに、周囲の人の考え方や環境には流されない。",
    "Q20. 作業前に「これは自分には無理だろう」と思うことはない。",
]
answers = []

for q in questions:
    a = st.select_slider(
        q, options=[1, 2, 3, 4, 5],  value=3,
        format_func=lambda x: p2ja[x],
        # help="1: 完全に当てはまらない、2: 当てはまらない、3: 普通、4: 当てはまる、5: 完全に当てはまる"
    )
    # st.write("あなたが選んだのは ", a, " です")
    answers.append(a)


st.markdown("## 結果")

# 予期が「濃い」または「薄い」
yoki_kosa = sum([a for a in answers[0:5]])
# st.write(f"{yoki_kosa=}")
# 予期が「多い」または「少ない」
yoki_osa = sum([a for a in answers[5:10]])
# st.write(f"{yoki_osa=}")
if yoki_kosa >= 13:
    if yoki_osa >= 13:
        yoki = "A: 容量超過"
    else:
        yoki = "B: 禁欲家"
else:
    if yoki_osa >= 13:
        yoki = "D: 浪費家"
    else:
        yoki = "C: 無気力"

# 想起が「正しい」または「誤り」
soki_tadashisa = sum([a for a in answers[10:15]])
# st.write(f"{soki_tadashisa=}")
# 想起が「肯定的」または「否定的」
soki_kouteisa = sum([a for a in answers[15:20]])
# st.write(f"{soki_kouteisa=}")
if soki_tadashisa >= 13:
    if soki_kouteisa >= 13:
        soki = "E: 自信家"
    else:
        soki = "F: 怖がり"
else:
    if soki_kouteisa >= 13:
        soki = "H: 楽天家"
    else:
        soki = "G: 悲観主義"


# @st.cache
def plot(title, x, y, jiku, typea, typej):

    fontsize_title = 38
    labelsize_tick_params = 16
    pad_jiku = 0.6
    fontsize_jiku = 20
    pad_alphabet = 0.6
    fontsize_alphabet = 32
    pad_type = 0.4
    fontsize_type = 26

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title(title, fontsize=fontsize_title, y=1.12)
    # ax.set_xlim((-1, 26))
    # ax.set_ylim((-1, 26))
    ax.set_xlim((0, 25))
    ax.set_ylim((0, 25))
    ax.set_xticks(np.arange(0, 26, 5))
    ax.set_yticks(np.arange(0, 26, 5))
    ax.tick_params(
        direction="inout", length=10, labelsize=labelsize_tick_params)
    # 軸を真ん中に
    ax.spines["bottom"].set_position("center")
    ax.spines["left"].set_position("center")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    # 塗りつぶし
    ax.axvspan(0, 25, 0, 1, color="#e8e8e8")
    ax.axvspan(5, 20, 0.2, 0.8, color="#d0d0d0")
    ax.axvspan(10, 15, 0.4, 0.6, color="#b8b8b8")
    # a_0_25 = np.arange(0, 25, 0.1)
    # a_5_20 = np.arange(5, 20, 0.1)
    # a_10_15 = np.arange(10, 15, 0.1)
    # ax.scatter(
    #     np.tile(a_0_25, len(a_0_25)),
    #     np.array([[x for _ in range(len(a_0_25))] for x in a_0_25]).flatten(),
    #     marker="s", s=1, color="#e0e0e0"
    # )
    # ax.scatter(
    #     np.tile(a_5_20, len(a_5_20)),
    #     np.array([[x for _ in range(len(a_5_20))] for x in a_5_20]).flatten(),
    #     marker="s", s=1, color="#d0d0d0"
    # )
    # ax.scatter(
    #     np.tile(a_10_15, len(a_10_15)),
    #     np.array([[x for _ in range(len(a_10_15))]
    #              for x in a_10_15]).flatten(),
    #     marker="s", s=1, color="#c0c0c0"
    # )

    # 得点
    ax.scatter([x], [y], s=350, marker="*", color="yellow")
    # FIXME: 25点は見切れます

    # 軸の意味
    ax.text(
        25 + pad_jiku, 12.5, jiku[0],
        fontsize=fontsize_jiku,
        verticalalignment="center",
        horizontalalignment="left"
    )
    ax.text(
        0 - pad_jiku, 12.5, jiku[1],
        fontsize=fontsize_jiku,
        verticalalignment="center",
        horizontalalignment="right"
    )
    ax.text(
        12.5, 25 + pad_jiku, jiku[2],
        fontsize=fontsize_jiku,
        verticalalignment="bottom",
        horizontalalignment="center"
    )
    ax.text(
        12.5, 0 - pad_jiku, jiku[3],
        fontsize=fontsize_jiku,
        verticalalignment="top",
        horizontalalignment="center"
    )

    # タイプ（アルファベット）
    ax.text(
        20 - pad_alphabet, 20 - pad_alphabet, typea[0],
        fontsize=fontsize_alphabet,
        verticalalignment="top",
        horizontalalignment="right"
    )
    ax.text(
        5 + pad_alphabet, 20 - pad_alphabet, typea[1],
        fontsize=fontsize_alphabet,
        verticalalignment="top",
        horizontalalignment="left"
    )
    ax.text(
        5 + pad_alphabet, 5 + pad_alphabet, typea[2],
        fontsize=fontsize_alphabet,
        verticalalignment="bottom",
        horizontalalignment="left"
    )
    ax.text(
        20 - pad_alphabet, 5 + pad_alphabet, typea[3],
        fontsize=fontsize_alphabet,
        verticalalignment="bottom",
        horizontalalignment="right"
    )

    # タイプ
    ax.text(
        25 + pad_type, 25 + pad_type, typej[0],
        fontsize=fontsize_type,
        verticalalignment="bottom",
        horizontalalignment="left"
    )
    ax.text(
        0 - pad_type, 25 + pad_type, typej[1],
        fontsize=fontsize_type,
        verticalalignment="bottom",
        horizontalalignment="right"
    )
    ax.text(
        0 - pad_type, 0 - pad_type, typej[2],
        fontsize=fontsize_type,
        verticalalignment="top",
        horizontalalignment="right"
    )
    ax.text(
        25 + pad_type, 0 - pad_type, typej[3],
        fontsize=fontsize_type,
        verticalalignment="top",
        horizontalalignment="left"
    )

    # plt.tight_layout()
    return fig, ax


def plot2(ax, title, x, y, jiku, typea, typej):

    fontsize_title = 38
    labelsize_tick_params = 16
    pad_jiku = 0.6
    fontsize_jiku = 20
    pad_alphabet = 0.6
    fontsize_alphabet = 32
    pad_type = 0.4
    fontsize_type = 26

    ax.set_title(title, fontsize=fontsize_title, y=1.12)
    ax.set_xlim((0, 25))
    ax.set_ylim((0, 25))
    ax.set_xticks(np.arange(0, 26, 5))
    ax.set_yticks(np.arange(0, 26, 5))
    ax.tick_params(
        direction="inout", length=10, labelsize=labelsize_tick_params)
    # 軸を真ん中に
    ax.spines["bottom"].set_position("center")
    ax.spines["left"].set_position("center")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    # 塗りつぶし
    ax.axvspan(0, 25, 0, 1, color="#e8e8e8", alpha=0.5)
    ax.axvspan(5, 20, 0.2, 0.8, color="#d0d0d0", alpha=0.5)
    ax.axvspan(10, 15, 0.4, 0.6, color="#b8b8b8", alpha=0.5)

    # 得点
    ax.scatter([x], [y], s=400, marker="*", color="b")
    # FIXME: 25点は見切れます

    # 軸の意味
    ax.text(
        25 + pad_jiku, 12.5, jiku[0],
        fontsize=fontsize_jiku,
        verticalalignment="center",
        horizontalalignment="left"
    )
    ax.text(
        0 - pad_jiku, 12.5, jiku[1],
        fontsize=fontsize_jiku,
        verticalalignment="center",
        horizontalalignment="right"
    )
    ax.text(
        12.5, 25 + pad_jiku, jiku[2],
        fontsize=fontsize_jiku,
        verticalalignment="bottom",
        horizontalalignment="center"
    )
    ax.text(
        12.5, 0 - pad_jiku, jiku[3],
        fontsize=fontsize_jiku,
        verticalalignment="top",
        horizontalalignment="center"
    )

    # タイプ（アルファベット）
    ax.text(
        20 - pad_alphabet, 20 - pad_alphabet, typea[0],
        fontsize=fontsize_alphabet,
        verticalalignment="top",
        horizontalalignment="right"
    )
    ax.text(
        5 + pad_alphabet, 20 - pad_alphabet, typea[1],
        fontsize=fontsize_alphabet,
        verticalalignment="top",
        horizontalalignment="left"
    )
    ax.text(
        5 + pad_alphabet, 5 + pad_alphabet, typea[2],
        fontsize=fontsize_alphabet,
        verticalalignment="bottom",
        horizontalalignment="left"
    )
    ax.text(
        20 - pad_alphabet, 5 + pad_alphabet, typea[3],
        fontsize=fontsize_alphabet,
        verticalalignment="bottom",
        horizontalalignment="right"
    )

    # タイプ
    ax.text(
        25 + pad_type, 25 + pad_type, typej[0],
        fontsize=fontsize_type,
        verticalalignment="bottom",
        horizontalalignment="left"
    )
    ax.text(
        0 - pad_type, 25 + pad_type, typej[1],
        fontsize=fontsize_type,
        verticalalignment="bottom",
        horizontalalignment="right"
    )
    ax.text(
        0 - pad_type, 0 - pad_type, typej[2],
        fontsize=fontsize_type,
        verticalalignment="top",
        horizontalalignment="right"
    )
    ax.text(
        25 + pad_type, 0 - pad_type, typej[3],
        fontsize=fontsize_type,
        verticalalignment="top",
        horizontalalignment="left"
    )

    return ax


fig, axes = plt.subplots(2, 1, figsize=(12, 20))
_ = plot2(
    axes[0],
    "〈予期〉", yoki_osa, yoki_kosa,
    ["多い", "少ない", "濃い", "薄い"],
    ["A", "B", "C", "D"],
    ["容量超過", "禁欲家", "無気力", "浪費家"]
)
_ = plot2(
    axes[1],
    "〈想起〉", soki_kouteisa, soki_tadashisa,
    ["肯定的", "否定的", "正しい", "誤り"],
    ["E", "F", "G", "H"],
    ["自信家", "怖がり", "悲観主義", "楽天家"]
)
fig.tight_layout(pad=5.0)

fn = "time_sense.png"
img = io.BytesIO()
plt.savefig(img, format="png", bbox_inches="tight")

st.pyplot(fig)
btn = st.download_button(
    label="画像をダウンロード",
    data=img,
    file_name=fn,
    mime="image/png"
)


st.markdown("### 予期")
st.write("予期が「濃い」または「薄い」：" + str(yoki_kosa) + "点" +
         ("（濃い）" if yoki_kosa >= 13 else "（薄い）"))
st.write("予期が「多い」または「少ない」：" + str(yoki_osa) + "点" +
         ("（多い）" if yoki_osa >= 13 else "（少ない）"))
st.write(f"⇒ **{yoki}**")

# fig, _ax = plot(
#     "〈予期〉", yoki_osa, yoki_kosa,
#     ["多い", "少ない", "濃い", "薄い"],
#     ["A", "B", "C", "D"],
#     ["容量超過", "禁欲家", "無気力", "浪費家"]
# )
# st.pyplot(fig)

# fn = "yoki.png"
# img = io.BytesIO()
# plt.savefig(img, format="png", bbox_inches="tight")
# btn = st.download_button(
#     label="画像をダウンロード",
#     data=img,
#     file_name=fn,
#     mime="image/png"
# )

st.markdown("### 想起")
st.write("想起が「正しい」または「誤り」：" + str(soki_tadashisa) + "点" +
         ("（正しい）" if soki_tadashisa >= 13 else "（誤り）"))
st.write("想起が「肯定的」または「否定的」：" + str(soki_kouteisa) + "点" +
         ("（肯定的）" if soki_kouteisa >= 13 else "（否定的）"))
st.write(f"⇒ **{soki}**")

# fig, _ax = plot(
#     "〈想起〉", soki_kouteisa, soki_tadashisa,
#     ["肯定的", "否定的", "正しい", "誤り"],
#     ["E", "F", "G", "H"],
#     ["自信家", "怖がり", "悲観主義", "楽天家"]
# )
# st.pyplot(fig)

# fn = "soki.png"
# img = io.BytesIO()
# plt.savefig(img, format="png", bbox_inches="tight")
# btn = st.download_button(
#     label="画像をダウンロード",
#     data=img,
#     file_name=fn,
#     mime="image/png"
# )


st.markdown("## 参考")
st.markdown(
    "- [『YOUR TIME ユア・タイム: 4063の科学データで導き出した、あなたの人生を変える最後の時間術』](https://amzn.to/3Sx3d8m)、鈴木 祐、河出書房新社、978-4-309-30023-8")
st.markdown("- [時間感覚タイプテスト（河出書房新社Webページ）](https://www.kawade.co.jp/YOURTIME/)")
