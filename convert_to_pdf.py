import markdown
from weasyprint import HTML

with open("MAL_CFO_Founding_Circle_Master_Plan.md", "r") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {{
    size: A4;
    margin: 2cm 2.5cm;
}}
body {{
    font-family: Helvetica, Arial, sans-serif;
    font-size: 11px;
    line-height: 1.6;
    color: #1a1a1a;
}}
h1 {{
    font-size: 22px;
    color: #0d7c5f;
    border-bottom: 3px solid #0d7c5f;
    padding-bottom: 8px;
    margin-top: 30px;
}}
h2 {{
    font-size: 16px;
    color: #0d7c5f;
    margin-top: 25px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
}}
h3 {{
    font-size: 13px;
    color: #333;
    margin-top: 18px;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10px;
}}
th {{
    background-color: #0d7c5f;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
}}
td {{
    padding: 7px 10px;
    border-bottom: 1px solid #e0e0e0;
}}
tr:nth-child(even) td {{
    background-color: #f7faf9;
}}
strong {{
    color: #0d7c5f;
}}
hr {{
    border: none;
    border-top: 2px solid #0d7c5f;
    margin: 30px 0;
}}
blockquote {{
    border-left: 4px solid #0d7c5f;
    margin: 15px 0;
    padding: 10px 15px;
    background: #f7faf9;
    font-style: italic;
}}
p, li {{
    margin-bottom: 6px;
}}
ul, ol {{
    padding-left: 20px;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf("MAL_CFO_Founding_Circle_Master_Plan.pdf")
print("PDF created successfully")
