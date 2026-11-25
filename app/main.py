from fastapi import FastAPI
from typing import TypedDict, List

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Shot recipe data — sample clips for the AI video skill
# Each shot represents a recipe card with timing, transitions, and styling
class Shot(TypedDict):
    id: int
    title: str
    duration: int
    transition: str
    theme: str

SHOTS: List[Shot] = [
    {
        "id": 1,
        "title": "Opening Title",
        "duration": 3,
        "transition": "fade",
        "theme": "brand-ink-open",
    },
    {
        "id": 2,
        "title": "Paper Title Card",
        "duration": 5,
        "transition": "paper-title-card",
        "theme": "depth-layer-moves",
    },
    {
        "id": 3,
        "title": "Lead Word Zoom Assemble",
        "duration": 4,
        "transition": "lead-word-zoom-assemble",
        "theme": "steep-tilt-glide",
    },
    {
        "id": 4,
        "title": "Marker Underline Title",
        "duration": 6,
        "transition": "marker-underline-title",
        "theme": "card-stack",
    },
    {
        "id": 5,
        "title": "Crane Rise Reveal",
        "duration": 4,
        "transition": "crane-rise-reveal",
        "theme": "pill-chip-slot-cycle-handled",
    },
]


def validate_shots() -> None:
    """Validate that all SHOTS entries conform to the expected schema.

    Raises ValueError if any shot is missing required fields or has
    incorrect types, ensuring shot data consistency for the Remotion
    video skill pipeline.
    """
    required_fields = {"id", "title", "duration", "transition", "theme"}
    for i, shot in enumerate(SHOTS):
        missing = required_fields - set(shot.keys())
        if missing:
            raise ValueError(
                f"SHOTS[{i}] is missing required fields: {missing}"
            )
        type_checks = {
            "id": int,
            "title": str,
            "duration": int,
            "transition": str,
            "theme": str,
        }
        for field, expected_type in type_checks.items():
            if field in shot and not isinstance(shot[field], expected_type):
                raise ValueError(
                    f"SHOTS[{i}]['{field}'] expected {expected_type.__name__}, "
                    f"got {type(shot[field]).__name__}"
                )


@app.get("/api/shots")
def shots():
    validate_shots()
    return SHOTS
