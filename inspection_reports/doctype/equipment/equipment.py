
import frappe
from frappe.model.document import Document


class Equipment(Document):
    def validate(self):
        self.validate_equipment_name()

    def validate_equipment_name(self):
        if not self.equipment_name or not self.equipment_name.strip():
            frappe.throw("Equipment Name is required.")
