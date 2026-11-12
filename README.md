# Fulfilment notice label reference

Reference implementation maintained by dispatch systems. It holds the machine-readable table of
registered trading labels for carrier services and a small renderer that fills the plain-text
handover notice template.

## Layout
- `label_table.json` - registered trading label table (current edition 3)
- `render_notice.py` - renders a handover notice from an order number, a contact and a service
- `templates/notice_template.txt` - notice template
- `tests/test_label_table.py` - sanity checks for the table and renderer

## Usage
```
python render_notice.py --order-number 512 --contact "Brenda Clark" --service "Swiftline Standard"
```
