import markdown
from weasyprint import HTML

with open("SHARK_TANK_DUBAI_PLAYBOOK.md") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html>
<head>
<style>
  @page {{ margin: 2cm; size: A4; }}
  body {{ font-family: Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #1a1a1a; }}
  h1 {{ font-size: 22pt; color: #0d1b2a; border-bottom: 3px solid #e63946; padding-bottom: 8px; margin-top: 0; }}
  h2 {{ font-size: 16pt; color: #1d3557; margin-top: 30px; }}
  h3 {{ font-size: 13pt; color: #457b9d; margin-top: 24px; }}
  blockquote {{ background: #f1faee; border-left: 4px solid #e63946; padding: 12px 16px; margin: 16px 0; font-style: italic; color: #2b2b2b; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 10pt; }}
  th {{ background: #1d3557; color: white; padding: 10px 12px; text-align: left; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid #ddd; }}
  tr:nth-child(even) {{ background: #f8f9fa; }}
  strong {{ color: #e63946; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 30px 0; }}
  ul, ol {{ padding-left: 20px; }}
  li {{ margin-bottom: 4px; }}
</style>
</head>
<body>{html_body}</body>
</html>"""

HTML(string=html).write_pdf("SHARK_TANK_DUBAI_PLAYBOOK.pdf")
print("PDF created successfully")
