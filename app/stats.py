from collections import Counter


class DetectionStats:
    """Accumulate detection counts over a session."""

    def __init__(self) -> None:
        self.frames = 0
        self.counts: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def update(self, labels: list[str]) -> None:
        """Register the labels detected in one frame."""
        self.frames += 1
        self.counts.update(labels)

    def most_common(self, n: int = 5) -> list[tuple[str, int]]:
        return self.counts.most_common(n)

    def summary(self, top: int = 5) -> str:
        lines = [
            f"Frames processed: {self.frames}",
            f"Detections: {self.total}",
        ]

        if self.counts:
            lines.append("Most frequent:")
            for label, count in self.most_common(top):
                lines.append(f"  {label}: {count}")
        else:
            lines.append("No objects detected.")
        return "\n".join(lines)