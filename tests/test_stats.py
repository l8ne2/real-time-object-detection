from app.stats import DetectionStats


def test_update_counts_labels():
    stats = DetectionStats()

    stats.update(["person", "person", "car"])
    stats.update(["person"])

    assert stats.frames == 2
    assert stats.total == 4
    assert stats.most_common(1) == [("person", 3)]


def test_summary_without_detections():
    stats = DetectionStats()
    stats.update([])

    assert "No objects detected" in stats.summary()