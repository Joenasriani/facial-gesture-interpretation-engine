from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

old_title = "    <title>AEON / Signal Observation Interface</title>"
new_title = "    <title>AEON | Browser Signal Observation Interface</title>"
if old_title in s:
    s = s.replace(old_title, new_title, 1)

marker = "<!-- A3: AEON canonical search metadata -->"
if marker not in s:
    block = '''
    <!-- A3: AEON canonical search metadata -->
    <meta name="author" content="Joe Nasr">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
    <link rel="canonical" href="https://facial-gesture-interpretation-engin.vercel.app/">
    <link rel="author" href="https://joe-nasr-signals.vercel.app/v2/">
    <meta property="og:type" content="website">
    <meta property="og:title" content="AEON | Browser Signal Observation Interface">
    <meta property="og:description" content="Experimental browser interface for camera landmarks, expression-model probabilities, orientation proxies, pitch, audio level and session variability. It does not infer deception, intent, personality, cognition, mental state or truthfulness.">
    <meta property="og:url" content="https://facial-gesture-interpretation-engin.vercel.app/">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="AEON | Browser Signal Observation Interface">
    <meta name="twitter:description" content="Camera, landmark, expression-model and microphone signal observation without psychological or deception inference.">
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"WebApplication","@id":"https://facial-gesture-interpretation-engin.vercel.app/#application","name":"AEON","alternateName":"AEON Signal Observation Interface","url":"https://facial-gesture-interpretation-engin.vercel.app/","description":"Experimental browser interface for observing camera landmarks, expression-model probabilities, orientation proxies, pitch, audio level and session variability without inferring deception, intent, personality, cognition, mental state or truthfulness.","applicationCategory":"MultimediaApplication","operatingSystem":"Web browser","creator":{"@type":"Person","@id":"https://joe-nasr-signals.vercel.app/v2/#joe-nasr","name":"Joe Nasr","url":"https://joe-nasr-signals.vercel.app/v2/"},"sameAs":"https://github.com/Joenasriani/facial-gesture-interpretation-engine"}
    </script>
    <!-- /A3: AEON canonical search metadata -->'''
    s = s.replace(new_title, new_title + block, 1)

p.write_text(s, encoding="utf-8")

Path("robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nSitemap: https://facial-gesture-interpretation-engin.vercel.app/sitemap.xml\n",
    encoding="utf-8",
)
Path("sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    '  <url>\n'
    '    <loc>https://facial-gesture-interpretation-engin.vercel.app/</loc>\n'
    '    <lastmod>2026-09-16</lastmod>\n'
    '  </url>\n'
    '</urlset>\n',
    encoding="utf-8",
)
