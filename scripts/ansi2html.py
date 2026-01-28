#!/usr/bin/env python3
"""Convert ANSI terminal output to HTML."""
import html
import re
import sys

COLORS = {
    "30": "black", "31": "red", "32": "green", "33": "yellow",
    "34": "blue", "35": "magenta", "36": "cyan", "37": "white",
    "90": "bright-black", "91": "bright-red", "92": "bright-green",
    "93": "bright-yellow", "94": "bright-blue", "95": "bright-magenta",
    "96": "bright-cyan", "97": "bright-white",
}

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zalgoctl showcase</title>
    <style>
        :root {{
            --bg: #0d1117;
            --fg: #c9d1d9;
            --black: #484f58;
            --red: #ff7b72;
            --green: #7ee787;
            --yellow: #d29922;
            --blue: #79c0ff;
            --magenta: #d2a8ff;
            --cyan: #a5d6ff;
            --white: #c9d1d9;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            padding: 2rem;
            background: var(--bg);
            color: var(--fg);
            font-family: "SF Mono", "Menlo", "Monaco", "Consolas", monospace;
            font-size: 14px;
            line-height: 1.5;
        }}
        pre {{
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        .bold {{ font-weight: bold; }}
        .dim {{ opacity: 0.6; }}
        .fg-black {{ color: var(--black); }}
        .fg-red {{ color: var(--red); }}
        .fg-green {{ color: var(--green); }}
        .fg-yellow {{ color: var(--yellow); }}
        .fg-blue {{ color: var(--blue); }}
        .fg-magenta {{ color: var(--magenta); }}
        .fg-cyan {{ color: var(--cyan); }}
        .fg-white {{ color: var(--white); }}
        .fg-bright-black {{ color: #6e7681; }}
        .fg-bright-red {{ color: #ffa198; }}
        .fg-bright-green {{ color: #56d364; }}
        .fg-bright-yellow {{ color: #e3b341; }}
        .fg-bright-blue {{ color: #79c0ff; }}
        .fg-bright-magenta {{ color: #d2a8ff; }}
        .fg-bright-cyan {{ color: #a5d6ff; }}
        .fg-bright-white {{ color: #ffffff; }}
        footer {{
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #30363d;
            opacity: 0.7;
        }}
        footer a {{ color: var(--cyan); }}
    </style>
</head>
<body>
    <pre>{content}</pre>
    <footer>
        <a href="https://github.com/possibilities/zalgoctl">github.com/possibilities/zalgoctl</a>
    </footer>
</body>
</html>
'''


def ansi_to_html(text: str) -> str:
    result = []
    pos = 0
    open_spans = 0
    pattern = re.compile(r"\x1b\[([0-9;]*)m")

    for match in pattern.finditer(text):
        result.append(html.escape(text[pos:match.start()]))
        pos = match.end()
        codes = match.group(1).split(";") if match.group(1) else ["0"]
        classes = []

        for code in codes:
            if code == "0":
                result.append("</span>" * open_spans)
                open_spans = 0
            elif code == "1":
                classes.append("bold")
            elif code == "2":
                classes.append("dim")
            elif code in COLORS:
                classes.append("fg-" + COLORS[code])

        if classes:
            result.append('<span class="' + " ".join(classes) + '">')
            open_spans += 1

    result.append(html.escape(text[pos:]))
    result.append("</span>" * open_spans)
    return "".join(result)


def main():
    content = sys.stdin.read()
    converted = ansi_to_html(content)
    print(HTML_TEMPLATE.format(content=converted))


if __name__ == "__main__":
    main()
