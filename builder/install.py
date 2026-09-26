from frappe.core.api.file import create_new_folder

from builder.export_import_standard_page import sync_standard_builder_pages
from builder.setup import setup_builder_desktop_icon
from builder.utils import (
	add_composite_index_to_web_page_view,
	sync_block_templates,
	sync_builder_variables,
	sync_page_templates,
)


def after_install():
	create_new_folder("Builder Uploads", "Home")
	create_new_folder("Fonts", "Home/Builder Uploads")
	sync_page_templates()
	sync_block_templates()
	sync_builder_variables()
	add_composite_index_to_web_page_view()
	sync_standard_builder_pages()
	setup_builder_desktop_icon()


def after_migrate():
	sync_page_templates()
	sync_block_templates()
	sync_builder_variables()
	sync_standard_builder_pages()
	setup_builder_desktop_icon()


def after_app_install(app_name=None):
	sync_standard_builder_pages(app_name)
