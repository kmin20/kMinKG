template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Map {map_number} - Lava Cave</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=DynaPuff:wght@400..700&display=swap');
    body {{
      background-color: #ffeeee;
      font-family: 'Comic Sans MS', cursive, sans-serif;
      margin: 0;
      padding: 0;
      text-align: center;
    }}
    header {{
      background-color: #4a3b3b;
      color: white;
      padding: 20px;
      font-size: 5vw;
      font-weight: bold;
    }}
    .map-row {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
      padding: 20px 10px;
    }}
    .map-image {{
      width: 100%;
      max-width: 400px;
      height: auto;
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    h2 {{
      font-size: 20px;
      margin: 20px 0 10px;
      color: #333;
    }}
    .map-list {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin: 20px auto 40px;
      padding: 0 10px;
      max-width: 90vw;
    }}
    .map-tile {{
      width: 64px;
      aspect-ratio: 1 / 1;
      background-image: url('../img/null.png');
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      position: relative;
      text-decoration: none;
      display: inline-block;
      transition: transform 0.2s ease, filter 0.2s ease;
    }}
    .map-tile span {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -70%);
      font-size: 20px;
      color: black;
      font-family: 'DynaPuff', cursive;
      font-weight: 700;
    }}
    .map-tile:hover {{
      filter: brightness(1.1);
      transform: scale(1.05);
    }}
    #map-nav {{
      margin: 10px 0;
      font-size: 16px;
    }}
    #map-nav a {{
      color: #333;
      text-decoration: underline;
      margin: 0 20px;
    }}
    footer {{
      background-color: #4a3b3b;
      color: white;
      font-size: 13px;
      padding: 10px;
    }}
    @media (max-width: 768px) {{
      header {{ font-size: 6vw; }}
      .map-tile span {{ font-size: 16px; }}
    }}
  </style>
</head>
<body>
  <header>
    MAP {map_number} - LAVA CAVE
  </header>

  <!-- MAP -->
  <div class="map-row">
    {images}
  </div>

  <!-- Prev / Next -->
  <div id="map-nav"></div>

  <!-- LIST MAP -->
  <h2>Next Maps</h2>
  <div class="map-list" id="map-list"></div>

  <footer>
    <em>Created by kMin. Inspired by Kadaver</br>
      <a href="https://kmin20.site" target="_blank" style="color: #fff; text-decoration: underline;">kMin20.Site</a>.</em>
  </footer>

  <script>
    const currentMap = {map_number};
    const totalMaps = 50;

    const mapList = document.getElementById('map-list');
    const mapNav = document.getElementById('map-nav');

    const prevMap = currentMap - 1 >= 1 ? currentMap - 1 : null;
    const nextMap = currentMap + 1 <= totalMaps ? currentMap + 1 : null;

    if (prevMap || nextMap) {{
      const navWrapper = document.createElement('div');
      if (prevMap) {{
        const prev = document.createElement('a');
        prev.href = `${{prevMap}}.html`;
        prev.textContent = `<< Prev (${{prevMap}})`;
        navWrapper.appendChild(prev);
      }}
      if (nextMap) {{
        const next = document.createElement('a');
        next.href = `${{nextMap}}.html`;
        next.textContent = `Next (${{nextMap}}) >>`;
        navWrapper.appendChild(next);
      }}
      mapNav.appendChild(navWrapper);
    }}

    const range = 2;
    for (let i = currentMap - range; i <= currentMap + range; i++) {{
      if (i < 1 || i > totalMaps || i === currentMap) continue;

      const a = document.createElement('a');
      a.className = 'map-tile';
      a.href = `${{i}}.html`;

      const span = document.createElement('span');
      span.textContent = i;

      a.appendChild(span);
      mapList.appendChild(a);
    }}
  </script>
</body>
</html>
"""

# ✅ Sinh 50 file HTML
for i in range(1, 51):
    images = '\n    '.join([
        f'<img src="img/{i}_{j}.png" alt="Map {i}-{j}" class="map-image">' for j in range(1, 6)
    ])
    html_content = template.format(map_number=i, images=images)

    with open(f"{i}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

print("✅ Đã tạo xong 50 file HTML: 1.html → 50.html")
