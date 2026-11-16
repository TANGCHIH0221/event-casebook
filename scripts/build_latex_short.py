"""精簡版 LaTeX（Overleaf 免費版可編）：導讀 + 每案「一句話 + 摘要表 + GitHub 詳細版連結」，依 README 分類分章。
用法：python3 scripts/build_latex_short.py → build/event-casebook-latex-short.zip
"""
import re, sys, shutil, zipfile, pathlib, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_latex as B

ROOT = B.ROOT
OUT = ROOT / "build" / "latex_short"
ZIP = ROOT / "build" / "event-casebook-latex-short.zip"
REPO = "https://github.com/TANGCHIH0221/event-casebook"
PDF_URL = REPO + "/blob/main/" + urllib.parse.quote("事件交易案例集_2021-2026.pdf")

def table_short(lines):
    """短表用 tabularx（單次編譯，比 xltabular 快）。"""
    t = B.table(lines)
    return t.replace(r"\begin{xltabular}", r"\begin{tabularx}").replace(r"\end{xltabular}", r"\end{tabularx}").replace("\\endhead\n", "")

def section_of_readme(md, title):
    m = re.search(r"^## " + re.escape(title) + r".*?$(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""

def conv_block(md):
    """README 片段轉 LaTeX，表格改 tabularx。"""
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"): j += 1
            out.append(table_short(lines[i:j])); i = j; continue
        j = i
        while j < len(lines) and not lines[j].startswith("|"): j += 1
        out.append(B.convert("\n".join(lines[i:j]), readme=True)); i = j
    return "\n".join(out)

def case_short(path):
    md = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
    quote = re.search(r"^> (.+)$", md, re.M).group(1).strip()
    tbl = re.search(r"^(\|.+\|\n\|[-| ]+\|\n(?:\|.+\|\n)+)", md, re.M).group(1).strip().split("\n")
    url = f"{REPO}/blob/main/cases/{path.name}"
    return "\n".join([
        r"\subsection*{" + B.inline(title) + "}",
        r"\addcontentsline{toc}{subsection}{" + B.inline(title) + "}",
        r"\begin{quote}" + B.inline(quote) + r"\end{quote}",
        r"{\small " + table_short(tbl) + "}",
        r"\par\noindent{\small 詳細版（時間軸、關鍵數字、解讀、勘誤）：\href{" + B.url_esc(url) + "}{" + B.esc(f"GitHub cases/{path.name}") + "}}",
        r"\bigskip",
    ])

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
% 用 XeLaTeX 編譯（Overleaf：Menu → Compiler → XeLaTeX）
\usepackage[fontset=none]{ctex}
\setCJKmainfont{Noto Sans CJK TC}
\usepackage[margin=2.2cm]{geometry}
\usepackage{amssymb,booktabs,tabularx,enumitem,textcomp}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.45em}
\setlist{itemsep=0.15em, topsep=0.3em}
\renewcommand{\arraystretch}{1.2}
\linespread{1.2}

\title{事件交易案例集（2021--2026）\\[0.3em]\large 規則的接縫與強制流（精簡版）}
\author{}  % 填入你的名字
\date{2026 年 11 月}

\begin{document}
\maketitle
\begin{center}\small
完整版（每案時間軸、關鍵數字、資料分析圖、解讀與勘誤）：\\
GitHub：\href{@REPOURL@}{@REPOTXT@}\quad
完整 PDF：\href{@PDFURL@}{事件交易案例集\_2021-2026.pdf}
\end{center}
\tableofcontents
\clearpage
"""

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    intro = readme.split("\n---", 1)[0].split("\n", 1)[1]            # H1 之後到第一條分隔線：開場白
    intro = "\n".join(l for l in intro.split("\n") if not l.startswith("**PDF 版**"))
    parts = [r"\section*{導讀}", r"\addcontentsline{toc}{section}{導讀}", conv_block(intro)]
    for t in ["我從 32 個案例看到的五件事", "框架：接縫理論", "我自己量化過的強制流", "怎麼查證"]:
        body = section_of_readme(readme, t)
        if body: parts += [r"\subsection*{" + B.inline(t) + "}", conv_block(body)]
    # 依 README 案例索引的分類分章
    idx = section_of_readme(readme, "案例索引")
    cats = re.split(r"^### ", idx, flags=re.M)[1:]
    for c in cats:
        name, rest = c.split("\n", 1)
        files = re.findall(r"\(cases/([0-9]{2}_[^)]+\.md)\)", rest)
        parts += [r"\bigskip", r"\section*{" + B.inline(name.strip()) + "}",
                  r"\addcontentsline{toc}{section}{" + B.inline(name.strip()) + "}"]
        parts += [case_short(ROOT / "cases" / f) for f in files]
    doc = PREAMBLE.replace("@REPOURL@", B.url_esc(REPO)).replace("@REPOTXT@", B.esc(REPO.replace("https://", ""))).replace("@PDFURL@", B.url_esc(PDF_URL)) + "\n".join(parts) + "\n\\end{document}\n"
    (OUT / "main.tex").write_text(doc, encoding="utf-8")
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(OUT / "main.tex", "main.tex")
    n = len(re.findall(r"\\subsection\*\{案例", doc))
    print(ZIP, ZIP.stat().st_size // 1024, "KB,", n, "cases")

if __name__ == "__main__":
    main()
