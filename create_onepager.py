import markdown
from weasyprint import HTML

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: A4;
    margin: 1.5cm 2cm;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}

/* Header bar */
.header {
    background-color: #0d7c5f;
    color: white;
    padding: 20px 25px;
    margin: -1.5cm -2cm 20px -2cm;
    width: calc(100% + 4cm);
}
.header h1 {
    margin: 0;
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.header .subtitle {
    font-size: 11px;
    opacity: 0.85;
    margin-top: 4px;
}

/* Section titles */
.section-label {
    font-size: 9px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #0d7c5f;
    margin-bottom: 6px;
    margin-top: 22px;
    border-bottom: 2px solid #0d7c5f;
    padding-bottom: 4px;
}

/* Purpose box */
.purpose-box {
    background: #f0f9f6;
    border-left: 4px solid #0d7c5f;
    padding: 14px 18px;
    margin: 10px 0 16px 0;
    font-size: 12.5px;
    line-height: 1.5;
    font-weight: 500;
}

/* Two column layout */
.two-col {
    display: flex;
    gap: 20px;
    margin-top: 8px;
}
.two-col .col {
    flex: 1;
}

/* Narrative block */
.narrative p {
    font-size: 10.5px;
    line-height: 1.55;
    margin: 0 0 8px 0;
}
.narrative strong {
    color: #0d7c5f;
}

/* Strategy items */
.strategy-item {
    margin-bottom: 10px;
}
.strategy-item .num {
    display: inline-block;
    background: #0d7c5f;
    color: white;
    font-size: 9px;
    font-weight: 700;
    width: 18px;
    height: 18px;
    line-height: 18px;
    text-align: center;
    border-radius: 50%;
    margin-right: 6px;
}
.strategy-item .title {
    font-size: 11px;
    font-weight: 700;
    color: #1a1a1a;
}
.strategy-item .desc {
    font-size: 10px;
    color: #444;
    margin-left: 26px;
    margin-top: 2px;
    line-height: 1.45;
}

/* KPI grid */
.kpi-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
}
.kpi-box {
    background: #f7faf9;
    border: 1px solid #d4e8e0;
    padding: 10px 14px;
    width: calc(33.33% - 6px);
    box-sizing: border-box;
}
.kpi-box .number {
    font-size: 22px;
    font-weight: 700;
    color: #0d7c5f;
    margin: 0;
    line-height: 1.1;
}
.kpi-box .label {
    font-size: 8.5px;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 3px;
}

/* Bottom bar */
.bottom-bar {
    margin-top: 18px;
    padding-top: 10px;
    border-top: 2px solid #0d7c5f;
    display: flex;
    justify-content: space-between;
    font-size: 8.5px;
    color: #888;
}
.bottom-bar strong {
    color: #0d7c5f;
}

.one-liner {
    text-align: center;
    font-size: 11px;
    font-style: italic;
    color: #555;
    margin: 12px 0 0 0;
    padding: 10px;
    border-top: 1px solid #e0e0e0;
    border-bottom: 1px solid #e0e0e0;
}
</style>
</head>
<body>

<div class="header">
    <h1>MAL CFO FOUNDING CIRCLE</h1>
    <div class="subtitle">Executive One-Pager &middot; Internal Use Only &middot; Co-hosted with Bluefive Capital</div>
</div>

<!-- PURPOSE -->
<div class="section-label">PURPOSE</div>
<div class="purpose-box">
    Acquire <strong>80 SME CFOs</strong> as signed Mal customers before official launch by recruiting them as <strong>Founding Members</strong> who co-create the product &mdash; not as attendees who watch a demo. Every CFO who walks in should walk out on the waitlist, with their company on a path to banking with Mal.
</div>

<div class="one-liner">"We're selecting 80 CFOs to shape the future of SME finance in the GCC. You're one of them."</div>

<!-- TWO COLUMNS: NARRATIVE + STRATEGY -->
<div class="two-col">

<div class="col">
<div class="section-label">THE NARRATIVE</div>
<div class="narrative">
    <p><strong>The problem:</strong> CFOs at UAE SMEs are duct-taping 10 tools together &mdash; one for banking, one for payroll, one for invoicing, one for compliance. Their bank doesn't know their business. When they need credit, they fill forms and wait days. If they want Sharia compliance, they compromise on technology.</p>
    <p><strong>The villain:</strong> Legacy banks that treat every SME the same and force CFOs into systems designed for corporates or consumers &mdash; never for them.</p>
    <p><strong>The shift:</strong> Mal is the first Islamic-native, all-in-one SME operating system. Banking + credit + payroll + compliance + AI &mdash; one platform that already knows your business. No other player in the GCC has built this.</p>
    <p><strong>The hook:</strong> We don't launch Mal <em>at</em> CFOs. We launch it <em>with</em> them. 80 hand-selected CFOs get Founding Member status, co-design input, and their name attached to infrastructure 10,000 businesses will use. This is recognition, not a sales pitch.</p>
    <p><strong>The flywheel:</strong> Each CFO signs their company &rarr; their employees get Mal personal accounts (retail bridge) &rarr; they refer peers to the community &rarr; the community grows the product &rarr; the product grows Mal.</p>
</div>
</div>

<div class="col">
<div class="section-label">THE STRATEGY</div>

<div class="strategy-item">
    <span class="num">1</span><span class="title">5 Cohorts, Not 1 Conference</span>
    <div class="desc">80 CFOs split into 5 groups of 16, by sector. One cohort every 2 weeks over 10 weeks (Aug&ndash;Oct). Intimate sessions convert; conferences don't.</div>
</div>

<div class="strategy-item">
    <span class="num">2</span><span class="title">Pre-Qualify Every Invite</span>
    <div class="desc">No awareness attendees. Every CFO is screened for a real pain point Mal solves (AED 5M&ndash;500M revenue, 10&ndash;500 employees, UAE ops). 120 names sourced, 80 invited.</div>
</div>

<div class="strategy-item">
    <span class="num">3</span><span class="title">Convert in the Room</span>
    <div class="desc">Crisis Simulation using Mal tools &rarr; hands-on product experience. iPads at every seat. Live "Founding CFOs" wall fills in real time. Social proof + zero friction = sign-up.</div>
</div>

<div class="strategy-item">
    <span class="num">4</span><span class="title">E-Invoicing as the Urgency Lever</span>
    <div class="desc">UAE e-invoicing mandate hits SMEs by July 2027. Position Mal as "compliance + financing in one platform." Fear of penalties accelerates decisions.</div>
</div>

<div class="strategy-item">
    <span class="num">5</span><span class="title">Content Engine Warms the Funnel</span>
    <div class="desc">5-episode "Mal Show" podcast (ft. Youssef Salem, ADNOC Drilling CFO) drops weekly through August. Every episode ends with a waitlist CTA. Every guest gets a Founding Circle invite.</div>
</div>

<div class="strategy-item">
    <span class="num">6</span><span class="title">Lock In Long-Term via Community</span>
    <div class="desc">CFO Advisory Council (10&ndash;15 seats, design partners). Startup Grant Program (USD 10&ndash;15K/quarter, zero cost to Mal via Hub71/Bluefive). Quarterly dinners. This is a membership, not a one-off event.</div>
</div>

</div>
</div>

<!-- KPIs -->
<div class="section-label">KPIs THAT MATTER</div>
<div class="kpi-grid">
    <div class="kpi-box">
        <div class="number">80</div>
        <div class="label">Founding CFOs signed across 5 cohorts</div>
    </div>
    <div class="kpi-box">
        <div class="number">90%+</div>
        <div class="label">Waitlist sign-up rate per session</div>
    </div>
    <div class="kpi-box">
        <div class="number">10&ndash;15</div>
        <div class="label">Advisory Council seats filled</div>
    </div>
    <div class="kpi-box">
        <div class="number">5&ndash;8</div>
        <div class="label">Design partnerships signed</div>
    </div>
    <div class="kpi-box">
        <div class="number">60%+</div>
        <div class="label">Founding CFOs &rarr; active accounts within 90 days</div>
    </div>
    <div class="kpi-box">
        <div class="number">4,000+</div>
        <div class="label">Retail accounts via payroll bridge (employees)</div>
    </div>
</div>

<div class="bottom-bar">
    <div><strong>Owners:</strong> Vishnu (commercial) &middot; Manar (logistics) &middot; Amine (content) &middot; Abdallah (keynote + relationships)</div>
    <div><strong>Mal</strong> &middot; Internal use only</div>
</div>

</body>
</html>"""

HTML(string=html).write_pdf("MAL_CFO_Founding_Circle_OnePager.pdf")
print("One-pager PDF created")
