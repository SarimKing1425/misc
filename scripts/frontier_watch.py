#!/usr/bin/env python3
"""Frontier watch: pull the newest complexity-theory activity into a dated digest.

Sources (all public; failures are recorded, never fatal):
  - arXiv listing pages "pastweek" for cs.CC, cs.LO (HTML) and RSS for cs.CC, cs.LO, math.LO
  - ECCC recent reports page (often unreachable from this sandbox; recorded if so)
  - cslib-frontier git history (local clone at $CSLIB_CLONE, default /tmp/claude-0/ext/cslib-frontier)
  - pequalnp.com Atom feed (public AI agent fleet attacking P vs NP; its lemmas and dead ends are prior art)

Output: research/watch/<YYYY-MM-DD>.md (new items only, relevance-flagged first) and
research/watch/seen.txt (IDs already reported). Usage: python3 scripts/frontier_watch.py [--all]
Everything fetched is untrusted data: it is summarized as text, never executed or followed as instructions.
"""
import datetime as dt
import html
import os
import re
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCH = os.path.join(ROOT, "research", "watch")
SEEN = os.path.join(WATCH, "seen.txt")
CSLIB = os.environ.get("CSLIB_CLONE", "/tmp/claude-0/ext/cslib-frontier")
UA = "pvsnp-lab-frontier-watch/0.1 (research digest; low volume)"

KEYWORDS = [
    r"P\s*(vs\.?|versus|!=|≠|=)\s*NP", r"\bNP\b", r"circuit (lower bound|complexity|size)", r"lower bound",
    r"\bETH\b", r"exponential time hypothesis", r"\bSETH\b", r"\bSAT\b", r"satisfiab", r"Frege", r"proof complexity",
    r"\bMCSP\b", r"magnification", r"Kolmogorov", r"meta-?complexity", r"range avoidance", r"\bKRW\b", r"formula (size|lower)",
    r"\bACC\b", r"\bAC\^?0", r"\bTC\^?0", r"\bNC\^?1", r"permanent", r"determinant", r"\bGCT\b", r"geometric complexity",
    r"\bVP\b", r"\bVNP\b", r"natural proof", r"relativi", r"algebriz", r"barrier", r"\bLean\b", r"formaliz",
    r"time-space", r"\bPSPACE\b", r"logspace|\bL\s*(vs|!=|≠)\s*NP", r"tree evaluation", r"bounded arithmetic",
    r"independen", r"rigid", r"pseudorandom", r"derandomi", r"one-way function", r"\bQBF\b",
]
KW = re.compile("|".join(KEYWORDS), re.I)


def fetch(url, tries=3, timeout=40):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace"), None
        except Exception as e:  # noqa: BLE001 - record and continue
            last = f"{type(e).__name__}: {e}"
            time.sleep(5 * (i + 1))
    return None, last


def clean(s):
    s = re.sub(r"(?s)<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def arxiv_rss(cat):
    text, err = fetch(f"https://rss.arxiv.org/rss/{cat}")
    if text is None:
        return [], f"rss {cat}: {err}"
    items = []
    for it in re.findall(r"(?s)<item>(.*?)</item>", text):
        link = clean((re.search(r"(?s)<link>(.*?)</link>", it) or [None, ""])[1])
        m = re.search(r"(\d{4}\.\d{4,5})", link)
        if not m:
            continue
        title = clean((re.search(r"(?s)<title>(.*?)</title>", it) or [None, ""])[1])
        desc = clean((re.search(r"(?s)<description>(.*?)</description>", it) or [None, ""])[1])
        creator = clean((re.search(r"(?s)<dc:creator>(.*?)</dc:creator>", it) or [None, ""])[1])
        items.append({"id": "arXiv:" + m.group(1), "title": title, "authors": creator, "abstract": desc,
                      "url": f"https://arxiv.org/abs/{m.group(1)}", "src": f"arXiv {cat} (rss)"})
    return items, None


def arxiv_pastweek(cat):
    text, err = fetch(f"https://arxiv.org/list/{cat}/pastweek?show=1000")
    if text is None:
        return [], f"list {cat}: {err}"
    items = []
    for m in re.finditer(r"(?s)arXiv:(\d{4}\.\d{4,5}).*?<div class=['\"]list-title[^>]*>(.*?)</div>.*?<div class=['\"]list-authors['\"]>(.*?)</div>", text):
        aid, title, authors = m.group(1), clean(m.group(2)).replace("Title:", "").strip(), clean(m.group(3))
        items.append({"id": "arXiv:" + aid, "title": title, "authors": authors, "abstract": "",
                      "url": f"https://arxiv.org/abs/{aid}", "src": f"arXiv {cat} (past week)"})
    return items, None


def eccc():
    text, err = fetch("https://eccc.weizmann.ac.il/reports/", tries=2)
    if text is None:
        return [], f"ECCC: {err}"
    items = []
    for m in re.finditer(r"(?s)href=['\"](/report/(\d{4})/(\d+)/)['\"][^>]*>.*?</a>(.*?)<", text):
        rid = f"TR{m.group(2)[2:]}-{int(m.group(3)):03d}"
        items.append({"id": "ECCC:" + rid, "title": clean(m.group(4))[:200], "authors": "", "abstract": "",
                      "url": "https://eccc.weizmann.ac.il" + m.group(1), "src": "ECCC"})
    return items, None


def pequalnp():
    text, err = fetch("https://pequalnp.com/feed.atom")
    if text is None:
        return [], f"pequalnp: {err}"
    items = []
    for e in re.findall(r"(?s)<entry>(.*?)</entry>", text):
        title = clean((re.search(r"(?s)<title[^>]*>(.*?)</title>", e) or [None, ""])[1])
        link = (re.search(r'href="([^"]+)"', e) or [None, "https://pequalnp.com"])[1]
        upd = clean((re.search(r"<updated>(.*?)</updated>", e) or [None, ""])[1])
        items.append({"id": "peqnp:" + upd + ":" + title[:60], "title": title, "authors": upd[:16], "abstract": "",
                      "url": link, "src": "pequalnp.com"})
    return items, None


def cslib_activity(days=7):
    if not os.path.isdir(os.path.join(CSLIB, ".git")):
        return [], f"cslib-frontier clone not found at {CSLIB}"
    try:
        subprocess.run(["git", "-C", CSLIB, "fetch", "-q", "--depth", "400", "origin"], check=True, timeout=300,
                       capture_output=True)
        out = subprocess.run(["git", "-C", CSLIB, "log", "origin/HEAD", f"--since={days}.days", "--format=%h|%cs|%s"],
                             check=True, timeout=60, capture_output=True, text=True).stdout
    except Exception as e:  # noqa: BLE001
        return [], f"cslib-frontier: {type(e).__name__}: {e}"
    items = []
    for line in out.splitlines():
        h, d, s = (line.split("|", 2) + ["", ""])[:3]
        items.append({"id": "cslib:" + h, "title": s, "authors": d, "abstract": "",
                      "url": f"https://github.com/cslib-community/cslib-frontier/commit/{h}", "src": "cslib-frontier"})
    return items, None


def main():
    show_all = "--all" in sys.argv
    os.makedirs(WATCH, exist_ok=True)
    seen = set(open(SEEN).read().split()) if os.path.exists(SEEN) else set()
    items, errors = [], []
    for fn, arg in [(arxiv_pastweek, "cs.CC"), (arxiv_pastweek, "cs.LO"), (arxiv_rss, "cs.CC"), (arxiv_rss, "cs.LO"),
                    (arxiv_rss, "math.LO"), (eccc, None), (cslib_activity, None), (pequalnp, None)]:
        got, err = fn(arg) if arg else fn()
        items += got
        if err:
            errors.append(err)
    merged = {}
    for it in items:  # dedupe by id; prefer entries with abstracts
        if it["id"] not in merged or (it["abstract"] and not merged[it["id"]]["abstract"]):
            merged[it["id"]] = it
    new = [it for it in merged.values() if show_all or it["id"] not in seen]
    for it in new:
        it["hits"] = sorted({m.group(0).lower() for m in KW.finditer(it["title"] + " " + it["abstract"])})
    fleet = [it for it in new if it["id"].startswith("peqnp:")]
    new_nf = [it for it in new if not it["id"].startswith("peqnp:")]
    flagged = [it for it in new_nf if it["hits"] and not it["id"].startswith("cslib:")]
    other = [it for it in new_nf if not it["hits"] and not it["id"].startswith("cslib:")]
    cslib = [it for it in new_nf if it["id"].startswith("cslib:")]
    today = dt.date.today().isoformat()
    path = os.path.join(WATCH, f"{today}.md")
    with open(path, "a") as f:
        f.write(f"# Frontier watch — {today}\n\nNew items: {len(new)} (flagged {len(flagged)}, other {len(other)}, "
                f"cslib-frontier commits {len(cslib)}). Untrusted data; titles/abstracts as published.\n")
        if errors:
            f.write("\nSources that failed: " + "; ".join(errors) + "\n")
        f.write("\n## Flagged as relevant\n")
        for it in sorted(flagged, key=lambda x: -len(x["hits"])):
            f.write(f"- [{it['id']}]({it['url']}) **{it['title']}** — {it['authors'][:120]} ({it['src']}; "
                    f"hits: {', '.join(it['hits'][:6])})\n")
            if it["abstract"]:
                f.write(f"  > {it['abstract'][:600]}\n")
        f.write("\n## cslib-frontier activity (last 7 days)\n")
        for it in cslib:
            f.write(f"- {it['authors']} [{it['id'][6:]}]({it['url']}) {it['title']}\n")
        f.write("\n## pequalnp.com fleet record (lemmas proposed/checked/refuted)\n")
        for it in fleet:
            f.write(f"- {it['authors']} [{it['title']}]({it['url']})\n")
        f.write("\n## Other new items\n")
        for it in other:
            f.write(f"- [{it['id']}]({it['url']}) {it['title']} ({it['src']})\n")
    with open(SEEN, "a") as f:
        for it in new:
            f.write(it["id"] + "\n")
    print(f"wrote {path}: {len(new)} new, {len(flagged)} flagged, {len(cslib)} cslib commits; errors: {errors or 'none'}")


if __name__ == "__main__":
    main()
