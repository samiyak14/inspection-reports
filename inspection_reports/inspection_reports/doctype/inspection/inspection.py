
import frappe
from frappe.model.document import Document


class Inspection(Document):
    def validate(self):
        self.validate_measurements()
        self.calculate_overall_result()

    def validate_measurements(self):
        for row in self.measurements:
            measured_value = row.get("measured_value")
            reference_min = row.get("reference_min")
            reference_max = row.get("reference_max")

            # Check that the reference range is valid.
            if (
                reference_min is not None
                and reference_max is not None
                and reference_min != ""
                and reference_max != ""
                and reference_min > reference_max
            ):
                frappe.throw(
                    f"Reference Min cannot exceed Reference Max "
                    f"for '{row.parameter}'."
                )

            # Missing values or incomplete reference ranges
            # must not be evaluated as zero.
            if (
                measured_value is None
                or measured_value == ""
                or reference_min is None
                or reference_min == ""
                or reference_max is None
                or reference_max == ""
            ):
                row.evaluation = "Not Evaluated"
                continue

            # Evaluate the measurement against the reference range.
            if reference_min <= measured_value <= reference_max:
                row.evaluation = "OK"
            else:
                row.evaluation = "Not OK"

    def calculate_overall_result(self):
        if not self.measurements:
            self.overall_result = "Not Evaluated"
            return

        evaluations = [row.evaluation for row in self.measurements]

        if any(result == "Not OK" for result in evaluations):
            self.overall_result = "Not OK"
        elif all(result == "OK" for result in evaluations):
            self.overall_result = "OK"
        else:
            self.overall_result = "Not Evaluated"
