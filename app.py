from flask import Flask, render_template, abort

app = Flask(__name__)


CATEGORIES = [
    {"slug": "everything", "label": "Everything"},
    {"slug": "flowers",    "label": "Flowers"},
    {"slug": "sake",       "label": "Sake"},
    {"slug": "bags",       "label": "Bags"},
]


FLOWERS = [
    {
        "slug": "cherry-blossom",
        "name": "Cherry Blossom",
        "latin": "Prunus serrulata",
        "note": "collected in bloom, early spring",
        "date": "April 08, 2026",
        "tone": "blush",
    },
    {
        "slug": "magnolia",
        "name": "Magnolia",
        "latin": "Magnolia × soulangeana",
        "note": "saucer variety, pale pink edges",
        "date": "April 11, 2026",
        "tone": "cream",
    },
    {
        "slug": "plum-blossom",
        "name": "Plum Blossom",
        "latin": "Prunus mume",
        "note": "found on a morning walk",
        "date": "April 12, 2026",
        "tone": "rose",
    },
    {
        "slug": "camellia",
        "name": "Camellia",
        "latin": "Camellia japonica",
        "note": "deep red, yellow stamen",
        "date": "April 14, 2026",
        "tone": "rust",
    },
    {
        "slug": "iris",
        "name": "Iris",
        "latin": "Iris germanica",
        "note": "bearded iris, velvet petals",
        "date": "April 16, 2026",
        "tone": "violet",
    },
    {
        "slug": "wisteria",
        "name": "Wisteria",
        "latin": "Wisteria sinensis",
        "note": "hanging cluster, trellised",
        "date": "April 18, 2026",
        "tone": "lilac",
    },
    {
        "slug": "hydrangea",
        "name": "Hydrangea",
        "latin": "Hydrangea macrophylla",
        "note": "blue-to-violet gradient",
        "date": "April 19, 2026",
        "tone": "slate",
    },
    {
        "slug": "daffodil",
        "name": "Daffodil",
        "latin": "Narcissus pseudonarcissus",
        "note": "sunlight yellow, six petals",
        "date": "April 20, 2026",
        "tone": "sun",
    },
    {
        "slug": "tulip",
        "name": "Tulip",
        "latin": "Tulipa gesneriana",
        "note": "single bloom, dusty pink",
        "date": "April 21, 2026",
        "tone": "blush",
    },
    {
        "slug": "peony",
        "name": "Peony",
        "latin": "Paeonia lactiflora",
        "note": "petals layered, early blooming",
        "date": "April 22, 2026",
        "tone": "pink",
    },
]


def items_for(category_slug):
    if category_slug in ("everything", "flowers"):
        return [dict(item, category="Flowers") for item in FLOWERS]
    return []


@app.route("/")
def index():
    return render_template(
        "index.html",
        categories=CATEGORIES,
        active="everything",
        items=items_for("everything"),
    )


@app.route("/c/<slug>")
def category(slug):
    if slug not in {c["slug"] for c in CATEGORIES}:
        abort(404)
    return render_template(
        "index.html",
        categories=CATEGORIES,
        active=slug,
        items=items_for(slug),
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        categories=CATEGORIES,
        active=None,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
