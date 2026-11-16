# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "scrap"
app_title = "Erpnext Scrap Metal Recycling Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Scrap Metal Recycling Manager for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/scrap/css/scrap.bundle.css"
app_include_js = "/assets/scrap/js/scrap.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "scrap.engine.on_document_submit",
        "on_cancel": "scrap.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "scrap.engine.daily_scheduled_sync"
    ]
}
