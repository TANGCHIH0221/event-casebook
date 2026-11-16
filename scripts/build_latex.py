"""把 README + cases/*.md 轉成 Overleaf 可編譯的 LaTeX 專案（XeLaTeX + ctex），並打包成 zip。
用法：python3 scripts/build_latex.py [輸出 zip 路徑]
只處理本 repo 用到的 Markdown 子集：標題、引言、表格、清單（可巢狀）、粗體、行內程式碼、連結、圖片、程式碼區塊。
"""
import re, sys, glob, shutil, zipfile, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "latex"
ZIP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "event-casebook-latex.zip"

CASES = sorted(glob.glob(str(ROOT / "cases" / "*.md")))
LABEL = {pathlib.Path(c).name: "case:" + pathlib.Path(c).stem for c in CASES}

# ---------- 行內 ----------
SPECIAL = [("✅", r"$\checkmark$"), ("⚠️", r"\textbf{(!)}"), ("⚠", r"\textbf{(!)}"), ("★", r"$\star$"),
           ("−", r"$-$"), ("→", r"$\rightarrow$"), ("×", r"$\times$"), ("÷", r"$\div$"), ("≈", r"$\approx$"),
           ("≥", r"$\geq$"), ("≤", r"$\leq$"), ("±", r"$\pm$"), ("₹", r"Rs.\,"), ("¥", r"\textyen{}"),
           ("¶", r"\P{}"), ("‒", "--"), ("‑", "-"), ("…", r"\ldots{}"), ("️", "")]

def esc(s: str) -> str:
    out = []
    for ch in s:
        out.append({"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                    "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}.get(ch, ch))
    s = "".join(out)
    for a, b in SPECIAL:
        s = s.replace(a, b)
    return s

def url_esc(u: str) -> str:
    return u.replace("\\", "/").replace("%", r"\%").replace("#", r"\#")

PAT = re.compile(r"`([^`]+)`|\[([^\]]+)\]\(([^)\s]+)\)|\*\*(.+?)\*\*")

def inline(s: str) -> str:
    out, pos = [], 0
    for m in PAT.finditer(s):
        out.append(esc(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(r"\texttt{" + esc(m.group(1)) + "}")
        elif m.group(2) is not None:
            text, url = m.group(2), m.group(3)
            name = url.split("/")[-1]
            if name in LABEL and not url.startswith("http"):
                out.append(r"\hyperref[" + LABEL[name] + "]{" + inline(text) + "}")
            elif url.startswith("http"):
                out.append(r"\href{" + url_esc(url) + "}{" + inline(text) + "}")
            else:
                out.append(inline(text))
        else:
            out.append(r"\textbf{" + inline(m.group(4)) + "}")
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out)

# ---------- 區塊 ----------
def table(lines):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    head, body = rows[0], [r for r in rows[2:]]
    n = len(head)
    body = [r + [""] * (n - len(r)) if len(r) < n else r[:n] for r in body]
    lens = [max(len(r[i]) for r in [head] + body) for i in range(n)]
    spec = "".join("l" if L <= 10 else r">{\raggedright\arraybackslash}X" for L in lens)
    if "X" not in spec:
        spec = r">{\raggedright\arraybackslash}X" * n
    t = [r"\begin{xltabular}{\linewidth}{" + spec + "}", r"\toprule",
         " & ".join(r"\textbf{" + inline(h) + "}" for h in head) + r" \\", r"\midrule", r"\endhead"]
    for r in body:
        t.append(" & ".join(inline(c) for c in r) + r" \\")
    t += [r"\bottomrule", r"\end{xltabular}"]
    return "\n".join(t)

LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")

def lists(lines):
    out, stack = [], []          # stack: (indent, env)
    for l in lines:
        m = LIST_RE.match(l)
        if not m:                 # 續行
            out[-1] += " " + inline(l.strip()); continue
        ind, mark, text = len(m.group(1)), m.group(2), m.group(3)
        env = "enumerate" if mark[0].isdigit() else "itemize"
        while stack and ind < stack[-1][0]:
            out.append(r"\end{" + stack.pop()[1] + "}")
        if not stack or ind > stack[-1][0]:
            out.append(r"\begin{" + env + "}"); stack.append((ind, env))
        out.append(r"\item " + inline(text))
    while stack:
        out.append(r"\end{" + stack.pop()[1] + "}")
    return "\n".join(out)

def convert(md, label=None, readme=False):
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"): j += 1
            out.append(r"\begin{verbatim}" + "\n" + "\n".join(lines[i + 1:j]).replace("→", "->") + "\n" + r"\end{verbatim}")
            i = j + 1; continue
        if l.startswith("# "):
            title = l[2:].strip()
            if readme:
                out.append(r"\section*{" + inline(title) + "}")
            else:
                out.append(r"\clearpage" + "\n" + r"\section*{" + inline(title) + "}\n"
                           + r"\addcontentsline{toc}{section}{" + inline(title) + "}\n" + r"\label{" + label + "}")
        elif l.startswith("### "):
            out.append(r"\subsubsection*{" + inline(l[4:].strip()) + "}")
        elif l.startswith("## "):
            out.append(r"\subsection*{" + inline(l[3:].strip()) + "}")
        elif l.startswith(">"):
            j = i
            buf = []
            while j < len(lines) and lines[j].startswith(">"):
                buf.append(lines[j].lstrip(">").strip()); j += 1
            paras = "\n".join(buf).split("\n\n")
            out.append(r"\begin{quote}" + "\n" + "\n\n".join(inline(" ".join(p.split("\n"))) for p in paras if p.strip()) + "\n" + r"\end{quote}")
            i = j; continue
        elif l.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"): j += 1
            out.append(table(lines[i:j])); i = j; continue
        elif LIST_RE.match(l):
            j = i + 1
            while j < len(lines) and lines[j].strip() and (LIST_RE.match(lines[j]) or lines[j].startswith("   ")):
                j += 1
            out.append(lists(lines[i:j])); i = j; continue
        elif l.startswith("!["):
            m = re.match(r"!\[[^\]]*\]\(([^)]+)\)", l)
            fig = m.group(1).split("/")[-1]
            out.append(r"\begin{figure}[H]\centering\includegraphics[width=\linewidth]{figures/" + fig + r"}\end{figure}")
        elif l.strip() == "---" or l.startswith("**PDF 版**"):
            pass
        elif l.strip():
            out.append(inline(l))
        else:
            out.append("")
        i += 1
    return "\n".join(out)

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
% 用 XeLaTeX 編譯（Overleaf：Menu → Compiler → XeLaTeX）
\usepackage[fontset=none]{ctex}
\setCJKmainfont{Noto Serif CJK TC}[BoldFont=Noto Sans CJK TC]
\setCJKsansfont{Noto Sans CJK TC}
\usepackage[margin=2.2cm]{geometry}
\usepackage{amssymb,graphicx,float,booktabs,xltabular,enumitem,textcomp}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}
\setlist{itemsep=0.2em, topsep=0.3em}
\renewcommand{\arraystretch}{1.25}
\linespread{1.25}

\title{事件交易案例集（2021--2026）\\[0.3em]\large 規則的接縫與強制流}
\author{}  % 填入你的名字
\date{2026 年 11 月}

\begin{document}
\maketitle
\tableofcontents
\clearpage
"""

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / "cases").mkdir(parents=True); (OUT / "figures").mkdir()
    for f in (ROOT / "figures").glob("*.png"): shutil.copy(f, OUT / "figures" / f.name)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = readme.split("\n", 1)[1]           # 去掉 README 的 H1（用 \maketitle）
    (OUT / "intro.tex").write_text(r"\section*{導讀}" + "\n" + r"\addcontentsline{toc}{section}{導讀}" + "\n" + convert(readme, readme=True), encoding="utf-8")
    body = [PREAMBLE, r"\input{intro}"]
    for c in CASES:
        p = pathlib.Path(c)
        (OUT / "cases" / (p.stem + ".tex")).write_text(convert(p.read_text(encoding="utf-8"), label=LABEL[p.name]), encoding="utf-8")
        body.append(r"\input{cases/" + p.stem + "}")
    body.append(r"\end{document}")
    (OUT / "main.tex").write_text("\n".join(body) + "\n", encoding="utf-8")
    ZIP.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in OUT.rglob("*"):
            if f.is_file(): z.write(f, f.relative_to(OUT))
    print(ZIP, ZIP.stat().st_size // 1024, "KB,", len(CASES), "cases")

if __name__ == "__main__":
    main()
