# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "scrap"
app_title = "Erpnext Scrap Metal Recycling Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Scrap Metal Recycling Manager - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/scrap/css/scrap.bundle.css"
app_include_js = "/assets/scrap/js/scrap.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Scrap Metal Recycling Manager Entry": {
        "validate": "scrap.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "scrap.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "scrap.tasks.hourly_sync"
    ],
    "daily": [
        "scrap.tasks.daily_reconciliation"
    ],
    "weekly": [
        "scrap.tasks.weekly_digest"
    ]
}
