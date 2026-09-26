import frappe
import json
import os

def setup_builder_desktop_icon():
    icon_name = "Builder"
    icon_data = {
        "label": "Builder",
        "icon": "layout",
        "icon_type": "Link",
        "link_type": "Workspace Sidebar",
        "link_to": "Builder",
        "parent_icon": "",
        "hidden": 0,
        "standard": 1,
        "app": "builder",
        "idx": 26
    }

    if frappe.db.exists("Desktop Icon", icon_name):
        frappe.db.set_value("Desktop Icon", icon_name, icon_data)
    else:
        doc = frappe.new_doc("Desktop Icon")
        doc.name = icon_name
        doc.update(icon_data)
        doc.insert(ignore_permissions=True)

    # Sync Workspace Sidebar if file exists
    sb_file = "/home/frappe/frappe-bench/apps/builder/builder/workspace_sidebar/builder.json"
    if os.path.exists(sb_file):
        try:
            with open(sb_file, "r", encoding="utf-8") as fp:
                sb_data = json.load(fp)
            if frappe.db.exists("Workspace Sidebar", "Builder"):
                sb = frappe.get_doc("Workspace Sidebar", "Builder")
                sb.items = []
                for it in sb_data.get("items", []):
                    sb.append("items", it)
                sb.save(ignore_permissions=True)
            else:
                sb = frappe.new_doc("Workspace Sidebar")
                sb.update(sb_data)
                sb.insert(ignore_permissions=True)
        except Exception:
            pass

    if frappe.db.table_exists("Desktop Layout"):
        layouts = frappe.get_all("Desktop Layout", fields=["name", "layout"])
        for l in layouts:
            if not l.layout:
                continue
            try:
                items = json.loads(l.layout)
                has_it = False
                for item in items:
                    if item.get("name") in ["Builder", "Frappe Builder"] or item.get("label") in ["Builder", "Frappe Builder"]:
                        item["name"] = "Builder"
                        item["label"] = "Builder"
                        item["link_type"] = "Workspace Sidebar"
                        item["link_to"] = "Builder"
                        item["icon"] = "layout"
                        item["app"] = "builder"
                        has_it = True
                        break
                if not has_it:
                    c_item = {
                        "label": "Builder",
                        "bg_color": "blue",
                        "link": None,
                        "link_type": "Workspace Sidebar",
                        "app": "builder",
                        "icon_type": "Link",
                        "parent_icon": "",
                        "icon": "layout",
                        "link_to": "Builder",
                        "idx": 26,
                        "standard": 1,
                        "logo_url": None,
                        "hidden": 0,
                        "name": "Builder",
                        "restrict_removal": 0,
                        "icon_image": None
                    }
                    items.append(c_item)
                doc_l = frappe.get_doc("Desktop Layout", l.name)
                doc_l.layout = json.dumps(items)
                doc_l.save(ignore_permissions=True)
            except Exception:
                pass

def after_install():
    setup_builder_desktop_icon()
    frappe.db.commit()

def after_migrate():
    setup_builder_desktop_icon()
    frappe.db.commit()
