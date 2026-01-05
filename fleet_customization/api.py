import frappe, json
@frappe.whitelist(allow_guest=True)
def export_fixtures():  
    doctypes = frappe.get_all("DocType", filter=[['module'],'=','VSD Fleet MS'])
    for dt in doctypes:
        try:
            records = frappe.get_all(dt.name)
            with open(f"{dt.name}.json", "w") as f:
                f.write(json.dumps(records, indent=2, default=str))
            print(f"Exported {dt.name} ({len(records)} records)")
        except Exception as e:
            print(f"Skipping {dt.name}: {e}")
