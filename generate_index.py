import os
import glob
import re
import wordninja

files = glob.glob('**/*.html', recursive=True)
files = [f for f in files if not f == 'index.html']
games = []
for f in files:
    name = os.path.basename(f)
    if name.startswith('cl') and name.endswith('.html'):
        game = name[2:-5]
        game_display = ' '.join(wordninja.split(game))
        rel_path = f.replace('\\', '/')  # in case
        games.append((game_display, rel_path))
games.sort(key=lambda x: x[0].lower())
# divide into 8 columns
num_cols = 8
cols = [[] for _ in range(num_cols)]
for i, (game_display, path) in enumerate(games):
    cols[i % num_cols].append((game_display, path))
# now generate HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .column {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        button {
            background: transparent;
            border: none;
            color: white;
            cursor: pointer;
            font-size: 16px;
            text-align: left;
            width: 100%;
            padding: 5px;
            border-radius: 5px;
            transition: background 0.3s;
        }
        button:hover {
            background: rgba(255, 255, 255, 0.2);
        }
    </style>
</head>
<body>
    <div class="container">
"""
for col in cols:
    html += '        <div class="column">\n            <ul>\n'
    for game, path in col:
        html += f'                <li><button onclick="openGame(\'{path}\')">{game}</button></li>\n'
    html += '            </ul>\n        </div>\n'
html += """    </div>
    <script>
        function openGame(file) {
            fetch(file)
                .then(response => response.text())
                .then(html => {
                    const win = window.open('about:blank');
                    win.document.write(html);
                    win.document.close();
                })
                .catch(err => console.error('Error loading game:', err));
        }
    </script>
</body>
</html>"""
with open('index.html', 'w') as f:
    f.write(html)