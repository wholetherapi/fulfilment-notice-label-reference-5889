#!/usr/bin/env python3
"""Render a handover confirmation from the registered label table.

The current edition of the fulfilment notice standard requires the registered trading label
of the carrier service, not the internal service name printed on the order.
"""
import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent


def load_table(path=None):
    path = pathlib.Path(path) if path else ROOT / "label_table.json"
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def label_for(table, service):
    labels = table.get("labels", {})
    if service not in labels:
        raise KeyError(f"no registered label for service: {service}")
    return labels[service]


def render(order_number, contact, label, template_path=None):
    template_path = pathlib.Path(template_path) if template_path else ROOT / "templates" / "notice_template.txt"
    template = template_path.read_text(encoding="utf-8")
    return (template
            .replace("{{SHIPMENT_REFERENCE}}", f"HRX-{order_number}")
            .replace("{{CONTACT_NAME}}", contact)
            .replace("{{CARRIER_LABEL}}", label))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order-number", required=True)
    parser.add_argument("--contact", required=True)
    parser.add_argument("--service", required=True)
    args = parser.parse_args()
    table = load_table()
    if table.get("edition") != 3:
        raise SystemExit(f"refusing to render with non-current table edition: {table.get('edition')}")
    print(render(args.order_number, args.contact, label_for(table, args.service)))


if __name__ == "__main__":
    main()
