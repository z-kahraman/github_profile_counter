def generate_svg_badge(page_id: str, count: int) -> str:
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="30">
      <rect width="150" height="30" fill="#24292e" rx="4"/>
      <text x="10" y="20" fill="#00ffcc" font-size="14" font-family="sans-serif">
        Views: {count}
      </text>
    </svg>
    """

