import frappe


@frappe.whitelist()
def get_unique_gsm_values(shaft_production_run: str):
    if not shaft_production_run:
        return []

    doc = frappe.get_doc("Shaft Production Run", shaft_production_run)
    rows = doc.get("roll_production_results") or []

    values = []
    for row in rows:
        gsm = row.get("gsm")
        if gsm is not None:
            values.append(float(gsm))

    return sorted(set(v for v in values if v > 0))

