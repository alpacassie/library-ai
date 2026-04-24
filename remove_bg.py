"""Flood-fill the off-white backdrop of each flower PNG to transparent.

Run once after adding new flower images:
    python remove_bg.py
"""
from collections import deque
from pathlib import Path

from PIL import Image

FLOWER_DIR = Path(__file__).parent / "static" / "images" / "flowers"
TOLERANCE = 28  # per-channel distance from the sampled corner color


def near(a, b, tol=TOLERANCE):
    return all(abs(a[i] - b[i]) <= tol for i in range(3))


def strip_bg(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    px = img.load()

    # Sample corners, use the most common as the background color
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    bg = max(set(corners), key=corners.count)[:3]

    # Flood-fill from every edge pixel that matches the background
    visited = [[False] * h for _ in range(w)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if near(px[x, y][:3], bg):
                q.append((x, y))
                visited[x][y] = True
    for y in range(h):
        for x in (0, w - 1):
            if near(px[x, y][:3], bg) and not visited[x][y]:
                q.append((x, y))
                visited[x][y] = True

    while q:
        x, y = q.popleft()
        px[x, y] = (0, 0, 0, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                if near(px[nx, ny][:3], bg):
                    visited[nx][ny] = True
                    q.append((nx, ny))

    img.save(path, "PNG")
    print(f"  ✓ {path.name}")


def main() -> None:
    pngs = sorted(FLOWER_DIR.glob("*.png"))
    print(f"Stripping backgrounds from {len(pngs)} images…")
    for p in pngs:
        strip_bg(p)
    print("Done.")


if __name__ == "__main__":
    main()
