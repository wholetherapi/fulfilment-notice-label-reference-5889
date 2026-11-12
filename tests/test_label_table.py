import json
import pathlib


def test_label_table_is_current_edition():
    table = json.loads((pathlib.Path(__file__).parent.parent / "label_table.json").read_text())
    assert table["edition"] == 3
    assert set(table["labels"]) == {"Swiftline Standard", "Northwind Economy", "Kestrel Express"}


def test_renderer_uses_registered_label():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
    from render_notice import render

    body = render(512, "Brenda Clark", "Swiftline Freightways Ltd.")
    assert "HRX-512" in body
    assert "Swiftline Freightways Ltd." in body
