#!/usr/bin/env python3
"""Generates the static pages. Run `python3 build.py`, then commit the .html files.
Edit copy here once; shared header/footer/meta stay consistent across pages."""
import html
SITE = "https://YOUR-USERNAME.github.io/delta-pharma"  # update after deploying
FORM = "https://formspree.io/f/YOUR_FORM_ID"           # update with your Formspree ID
PAGES = [("index.html", "Home"), ("about.html", "About"), ("products.html", "Products"),
         ("quality.html", "Manufacturing & Quality"), ("services.html", "Services"), ("contact.html", "Contact")]

def pack(n=12):
    return "".join('<i></i>' for _ in range(n))

def shell(fname, title, desc, body):
    nav = "".join(f'<li><a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{html.escape(t)}</a></li>' for f, t in PAGES)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Delta Pharma (Pvt.) Ltd.</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{fname}">
<meta property="og:type" content="website"><meta property="og:title" content="{title} | Delta Pharma">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}/{fname}">
<meta name="theme-color" content="#0f2a3a">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap">
<link rel="stylesheet" href="css/styles.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Delta Pharma (Pvt.) Ltd.","url":"{SITE}","address":{{"@type":"PostalAddress","addressLocality":"Nowshera","addressRegion":"Khyber Pakhtunkhwa","addressCountry":"PK"}}}}</script>
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap bar">
<a class="brand" href="index.html" aria-label="Delta Pharma home"><svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3 30 28H2z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><circle cx="16" cy="19" r="3.4" fill="#2bb391"/></svg><span>Delta Pharma<small>(Pvt.) Ltd.</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="wrap grid4">
<div><p class="brand-f">Delta Pharma (Pvt.) Ltd.</p><p>Pharmaceutical manufacturing in Nowshera, Khyber Pakhtunkhwa, Pakistan.</p></div>
<div><h2>Company</h2><ul><li><a href="about.html">About us</a></li><li><a href="quality.html">Manufacturing &amp; quality</a></li><li><a href="services.html">Services</a></li></ul></div>
<div><h2>Products</h2><ul><li><a href="products.html">Product categories</a></li><li><a href="contact.html">Request a catalogue</a></li></ul></div>
<div><h2>Contact</h2><p>Nowshera, Khyber Pakhtunkhwa<br><a href="mailto:info@example.com">info@example.com</a><br><a href="tel:+920000000000">+92 000 0000000</a></p></div>
</div><div class="wrap legal"><p>&copy; <span id="yr">2026</span> Delta Pharma (Pvt.) Ltd. All rights reserved.</p>
<p><a href="#">Privacy policy</a> &middot; <a href="#">Terms of use</a> &middot; <a href="#">Adverse event reporting</a></p>
<p class="disc">Product information on this site is for healthcare professionals and trade partners. It is not medical advice. Consult a physician or pharmacist before using any medicine.</p></div></footer>
<script src="js/main.js" defer></script></body></html>"""

def head(t, lead):
    return f'<section class="page-head"><div class="wrap"><h1>{t}</h1><p class="lead">{lead}</p></div></section>'

pages = {}

pages["index.html"] = ("Pharmaceutical manufacturer in Nowshera", "Delta Pharma (Pvt.) Ltd. manufactures quality-controlled medicines in Nowshera, Khyber Pakhtunkhwa, for patients and healthcare partners.", f"""
<section class="hero"><div class="wrap hero-grid"><div>
<h1>Medicines made with measured care, from Nowshera.</h1>
<p class="lead">Delta Pharma (Pvt.) Ltd. develops and manufactures pharmaceutical products under a documented quality system, so that every batch that leaves our plant can be traced and trusted.</p>
<p class="cta"><a class="btn" href="products.html">View product categories</a> <a class="btn ghost" href="contact.html">Contact our team</a></p></div>
<div class="blister" role="img" aria-label="Illustration of a tablet blister pack">{pack(12)}</div></div></section>
<section class="sec"><div class="wrap"><h2>What we stand for</h2><div class="grid3">
<article><h3>Quality in every step</h3><p>Raw material testing, in-process checks and finished-product release are documented and reviewed before a batch ships.</p></article>
<article><h3>Reliable supply</h3><p>Planned production and clear lead times help distributors, hospitals and pharmacies keep shelves stocked.</p></article>
<article><h3>Accountable partnership</h3><p>Our team answers technical, regulatory and supply questions directly and in writing.</p></article></div></div></section>
<section class="sec tint"><div class="wrap split"><div><h2>One site, one team, one standard</h2>
<p>From formulation to packing, work is done to written procedures by trained staff. Learn how our plant and laboratories are organised.</p>
<p><a class="btn" href="quality.html">Manufacturing &amp; quality</a></p></div>
<dl class="facts"><div><dt>Location</dt><dd>Nowshera, KP</dd></div><div><dt>Dosage forms</dt><dd>Solid and liquid oral</dd></div><div><dt>Focus</dt><dd>Quality and traceability</dd></div></dl></div></section>""")

pages["about.html"] = ("About us", "Delta Pharma (Pvt.) Ltd. is a Pakistani pharmaceutical manufacturer based in Nowshera.", head("About Delta Pharma", "A local manufacturer with a simple aim: dependable medicines, produced to documented standards.") + """
<section class="sec"><div class="wrap split"><div><h2>Our story</h2>
<p>Delta Pharma was established in Nowshera, Khyber Pakhtunkhwa, to supply affordable, consistent medicines to the region and beyond. We invest in people, equipment and procedures so that quality is built into manufacturing rather than checked in at the end.</p>
<p>[Add founding year, founders and key milestones here.]</p></div>
<div><h2>Mission</h2><p>To make safe, effective and affordable medicines available to the people who need them.</p><h2>Vision</h2><p>To be a trusted name in Pakistani pharmaceuticals, known for quality, integrity and reliable supply.</p></div></div></section>
<section class="sec tint"><div class="wrap"><h2>Facilities overview</h2><div class="grid3">
<article><h3>Production</h3><p>Separate areas for dispensing, processing and packing to limit mix-ups and contamination.</p></article>
<article><h3>Quality control laboratory</h3><p>Testing of raw materials, packaging components, in-process samples and finished goods.</p></article>
<article><h3>Warehouse</h3><p>Controlled storage with batch-wise records and first-expiry-first-out dispatch.</p></article></div></div></section>""")

cats = [("Tablets and capsules", "Oral solid dosage forms for common therapeutic needs."),
        ("Syrups and suspensions", "Liquid oral medicines, including paediatric-friendly formats."),
        ("Pain and fever", "Analgesic and antipyretic ranges."),
        ("Anti-infectives", "Antibacterial and related therapies, dispensed on prescription."),
        ("Gastrointestinal care", "Antacids, acid suppressants and digestive health."),
        ("Vitamins and supplements", "Nutritional support for adults and children.")]
pages["products.html"] = ("Products", "Browse Delta Pharma's pharmaceutical product categories, from oral solids to liquids.", head("Products", "Product categories we manufacture and supply. Ask for the full catalogue with strengths and pack sizes.") +
 '<section class="sec"><div class="wrap"><div class="grid3">' + "".join(f'<article class="prod"><h3>{a}</h3><p>{b}</p></article>' for a, b in cats) +
 '</div><p class="note">Category list is indicative. Individual products are registered and sold in line with applicable drug regulations. <a href="contact.html">Request the catalogue</a>.</p></div></section>')

pages["quality.html"] = ("Manufacturing and quality", "How Delta Pharma controls manufacturing and quality: GMP-based procedures, testing and traceability.", head("Manufacturing and quality", "Our quality system is built on current Good Manufacturing Practice (cGMP) principles.") + """
<section class="sec"><div class="wrap"><h2>From material to market</h2><ol class="steps">
<li><h3>Material approval</h3><p>Suppliers are qualified. Incoming materials are quarantined, sampled and tested before use.</p></li>
<li><h3>Controlled production</h3><p>Batches follow approved master formulas, with line clearance and in-process checks.</p></li>
<li><h3>Testing and release</h3><p>Finished products are tested against specifications. Only approved batches are released.</p></li>
<li><h3>Traceability</h3><p>Batch records and retained samples allow any product to be traced and, if needed, recalled.</p></li></ol></div></section>
<section class="sec tint"><div class="wrap"><h2>Licences and compliance</h2>
<p>Delta Pharma operates under the applicable drug manufacturing licensing framework in Pakistan.</p>
<ul class="ticks"><li>Manufacturing licence: [add number and issuing authority]</li><li>GMP inspection or certification: [add details and date]</li><li>Other certifications: [add, e.g. ISO standards, if held]</li></ul></div></section>""")

svc = [("Contract manufacturing", "Manufacture of your registered products to your specifications and quality agreement."),
       ("Private labelling", "Branded supply for distributors and institutions."),
       ("Product development support", "Formulation and technical dossier assistance for new products."),
       ("Institutional supply", "Planned supply to hospitals, pharmacies and distributors.")]
pages["services.html"] = ("Services", "Contract manufacturing, private label and supply services from Delta Pharma in Nowshera.", head("Services", "Ways we work with distributors, institutions and other pharmaceutical companies.") +
 '<section class="sec"><div class="wrap"><div class="grid2">' + "".join(f'<article><h3>{a}</h3><p>{b}</p></article>' for a, b in svc) +
 '</div><p><a class="btn" href="contact.html">Discuss your requirements</a></p></div></section>')

pages["contact.html"] = ("Contact", "Contact Delta Pharma (Pvt.) Ltd. in Nowshera, Khyber Pakhtunkhwa, for product, supply and partnership enquiries.", head("Contact us", "Send an enquiry and we will reply by email.") + f"""
<section class="sec"><div class="wrap split">
<form id="form" action="{FORM}" method="POST" novalidate>
<div class="f"><label for="n">Full name</label><input id="n" name="name" required autocomplete="name"></div>
<div class="f"><label for="e">Email</label><input id="e" name="email" type="email" required autocomplete="email"></div>
<div class="f"><label for="t">Enquiry type</label><select id="t" name="type"><option>Product information</option><option>Supply and distribution</option><option>Contract manufacturing</option><option>Careers</option><option>Other</option></select></div>
<div class="f"><label for="m">Message</label><textarea id="m" name="message" rows="5" required></textarea></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
<button class="btn" type="submit">Send enquiry</button><p id="status" role="status" aria-live="polite"></p></form>
<div><h2>Visit or write</h2><p><strong>Delta Pharma (Pvt.) Ltd.</strong><br>Nowshera, Khyber Pakhtunkhwa, Pakistan<br>[Add street address]</p>
<p>Email: <a href="mailto:info@example.com">info@example.com</a><br>Phone: <a href="tel:+920000000000">+92 000 0000000</a><br>Hours: Mon&ndash;Fri, 9:00&ndash;17:00</p>
<iframe title="Map of Nowshera" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=71.90%2C33.98%2C72.05%2C34.06&amp;layer=mapnik"></iframe></div></div></section>""")

for f, (t, d, b) in pages.items():
    open(f, "w", encoding="utf-8").write(shell(f, t, d, b))
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}/{f}</loc></url>" for f, _ in PAGES) + "</urlset>")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(pages), "pages")
