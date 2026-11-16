"""把 README + 32 個案例合成一份 PDF（Chrome headless 列印）。
用法：python3 scripts/build_pdf.py → 輸出 事件交易案例集_2021-2026.pdf
"""
import re, glob, pathlib, subprocess, markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT_HTML = ROOT / "build" / "casebook.html"
OUT_PDF = ROOT / "事件交易案例集_2021-2026.pdf"

cases = sorted(glob.glob(str(ROOT / "cases" / "*.md")))
anchor = {pathlib.Path(c).name: "case-" + pathlib.Path(c).stem for c in cases}

def fix_links(md: str, base: pathlib.Path) -> str:
    # 案例互連 → 內部錨點；圖片 → 絕對路徑
    md = re.sub(r"\]\((?:\.\./)?cases/([^)#]+\.md)\)", lambda m: f"](#{anchor.get(m.group(1), '')})", md)
    md = re.sub(r"\]\(([0-9]{2}_[^)#/]+\.md)\)", lambda m: f"](#{anchor.get(m.group(1), '')})", md)
    md = re.sub(r"\]\((?:\.\./)?figures/([^)]+)\)", lambda m: f"]({(ROOT / 'figures' / m.group(1)).as_uri()})", md)
    return md

def render(path: pathlib.Path) -> str:
    md = fix_links(path.read_text(encoding="utf-8"), path.parent)
    return markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])

parts = [f'<section class="readme">{render(ROOT / "README.md")}</section>']
for c in cases:
    p = pathlib.Path(c)
    parts.append(f'<section class="case" id="{anchor[p.name]}">{render(p)}</section>')

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }
body { font-family: "PingFang TC", "Heiti TC", "Noto Sans TC", sans-serif; font-size: 10.2pt; line-height: 1.65; color: #1a1a1a; }
h1 { font-size: 19pt; border-bottom: 2px solid #2a78d6; padding-bottom: 6px; margin: 0 0 12px; }
h2 { font-size: 13.5pt; margin: 20px 0 8px; color: #184f95; }
h3 { font-size: 11.5pt; margin: 14px 0 6px; }
section.case { page-break-before: always; }
blockquote { margin: 10px 0; padding: 8px 12px; background: #f0f5fc; border-left: 4px solid #2a78d6; color: #222; }
blockquote p { margin: 0; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 8.8pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #d5d4cf; padding: 4px 6px; vertical-align: top; word-break: break-word; }
th { background: #f3f2ee; }
img { max-width: 100%; display: block; margin: 8px auto; page-break-inside: avoid; }
code { font-family: Menlo, monospace; font-size: 8.6pt; background: #f3f2ee; padding: 0 3px; }
pre { background: #f6f6f4; padding: 8px; font-size: 8.4pt; white-space: pre-wrap; }
a { color: #1c5cab; text-decoration: none; word-break: break-all; }
hr { border: none; border-top: 1px solid #ddd; margin: 14px 0; }
"""
html = f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>事件交易案例集 2021–2026</title><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'
OUT_HTML.parent.mkdir(exist_ok=True)
OUT_HTML.write_text(html, encoding="utf-8")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri()], check=True, capture_output=True)
print(OUT_PDF, OUT_PDF.stat().st_size // 1024, "KB")
