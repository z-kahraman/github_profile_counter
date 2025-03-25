def generate_svg_badge(page_id: str, count: int) -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20" role="img" aria-label="views: {count}">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#444" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="150" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <rect width="70" height="20" fill="#555"/>
    <rect x="70" width="80" height="20" fill="#4c1"/>
    <rect width="150" height="20" fill="url(#b)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11">
    <text x="35" y="14">views</text>
    <text x="110" y="14">{count}</text>
  </g>
</svg>
"""

