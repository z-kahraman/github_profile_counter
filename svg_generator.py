def generate_svg_badge(page_id: str, count: int) -> str:
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="200" height="40">
      <rect width="200" height="40" fill="#2d2d2d" rx="6" />
      <text x="12" y="25" fill="#00ffcc" font-size="16" font-family="Arial">
        👁️ {count} views
      </text>
    </svg>
    """

