import frappe


def _run_quality_checking_setup():
    # Run latest schema setup in an idempotent way for cloud updates.
    from quality_gsm_app.patches.v1_0 import create_gsm_quality_setup
    from quality_gsm_app.patches.v1_1 import ensure_quality_checking_schema
    from quality_gsm_app.patches.v1_2 import make_quality_checking_main_doctype

    create_gsm_quality_setup.execute()
    ensure_quality_checking_schema.execute()
    make_quality_checking_main_doctype.execute()
    frappe.db.commit()


def after_install():
    _run_quality_checking_setup()


def after_migrate():
    _run_quality_checking_setup()

