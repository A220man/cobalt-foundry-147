from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Shot recipe data — sample clips for the AI video skill
# Each shot represents a recipe card with timing, transitions, and styling
SHOTS = [
    {
        "id": 1,
        "title": "Opening Title",
        "duration": 3,
        "transition": "fade",
        "theme": "brand-ink-open",
    },
    {
        "id": 2,
        "duration": 5,
        "transition": "paper-title-card",
        "theme": "depth-layer-moves",
    },
    {
        "id": 3,
        "duration": 4,
        "transition": "lead-word-zoom-assemble",
        "theme": "steep-tilt-glide",
    },
    {
        "id": 4,
        "duration": 6,
        "transition": "marker-underline-title",
        "theme": "card-stack",
    },
    {
        "id": 5,
        "duration": 4,
        "transition": "crane-rise-reveal",
        "theme": "pill-chip-slot-cycle-handled",
    },
]

@app.get("/api/shots")
def shots():
    return SHOTS
