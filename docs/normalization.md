# Normalization Analysis

## Overview

Normalization is the process of verifying that each entity in the Logical ERD conforms to the standard normal forms (1NF, 2NF, 3NF). The goal is to eliminate data redundancy and avoid update, insert, and delete anomalies before moving into Physical Database Design.

This analysis checks all 11 entities defined in `attributes.md` and confirmed in `logical_erd.drawio`.

---

## Normalization Rules Applied

**1NF (First Normal Form)**
- Every column must hold a single, atomic value.
- No repeating groups (e.g. no `medicine_1`, `medicine_2` columns).

**2NF (Second Normal Form)**
- Must already satisfy 1NF.
- Every non-key column must depend on the **entire** primary key, not just part of it.
- Only relevant when the primary key is composite (more than one column). Tables with a single-column primary key automatically satisfy 2NF.

**3NF (Third Normal Form)**
- Must already satisfy 2NF.
- No non-key column may depend on another non-key column (no transitive dependency). Every non-key column must depend directly on the primary key only.

---

## 1. Patient

**PK:** `patient_id` (single column) → 2NF automatically satisfied.

**3NF check:** All attributes (`full_name`, `date_of_birth`, `gender`, `phone_number`, `address`, `identity_number`, `emergency_contact_name`, `emergency_contact_phone`) describe the patient directly. No attribute can be derived from another non-key attribute.

**Result:** ✅ 3NF

---

## 2. Doctor

**PK:** `doctor_id` (single column) → 2NF automatically satisfied.

**3NF check:** Considered whether `consultation_fee` depends on `specialty` instead of `doctor_id` directly. Rejected — two doctors with the same specialty can charge different consultation fees (e.g. seniority, experience). `consultation_fee` depends only on `doctor_id`. All other attributes are directly descriptive of the individual doctor.

**Result:** ✅ 3NF

---

## 3. Department

**PK:** `department_id` (single column) → 2NF automatically satisfied.

**3NF check:** `department_name`, `description`, `location`, `phone_number`, `department_status` are all independent attributes of the department. No transitive dependency found.

**Result:** ✅ 3NF

---

## 4. Room

**PK:** `room_id` (single column) → 2NF automatically satisfied.

**3NF check:** Considered whether `capacity` depends on `room_type` instead of `room_id` directly. Rejected — two rooms of the same type (e.g. "Operating Room") can have different capacities depending on physical size. `capacity` depends only on `room_id`.

**Result:** ✅ 3NF

---

## 5. Appointment

**PK:** `appointment_id` (single column) → 2NF automatically satisfied.

**3NF check:** Considered whether `reason` depends on `patient_id` instead of `appointment_id` directly. Rejected — the same patient can have different reasons across different appointments (e.g. headache in one visit, follow-up in another). `reason` depends only on `appointment_id`.

**Result:** ✅ 3NF

---

## 6. Medical_Record

**PK:** `medical_record_id` (single column) → 2NF automatically satisfied.

**3NF check:** Considered whether `treatment` depends on `diagnosis` instead of `medical_record_id` directly. Rejected — patients with the same diagnosis can require different treatments depending on age, gender, pre-existing conditions, and individual health status. `treatment` depends only on `medical_record_id`.

**Result:** ✅ 3NF

---

## 7. Prescription

**PK:** `prescription_id` (single column) → 2NF automatically satisfied.

**3NF check:** `prescribed_date`, `instructions`, `prescription_status` are independent attributes of the prescription as a whole. No transitive dependency found.

**Result:** ✅ 3NF

---

## 8. Prescription_Item

**PK:** `prescription_item_id` (single column) → 2NF automatically satisfied. (Note: PK is a surrogate key rather than a composite of `prescription_id` + `medicine_id`, which correctly allows the same medicine to appear more than once in the same prescription with different dosage/frequency, e.g. morning and evening doses.)

**3NF check:** Considered whether `dosage` depends on `frequency` instead of `prescription_item_id` directly. Rejected — items with the same frequency (e.g. "2 times/day") can still have different dosages depending on the medicine and treatment plan. `dosage` depends only on `prescription_item_id`.

**Result:** ✅ 3NF

---

## 9. Medicine

**PK:** `medicine_id` (single column) → 2NF automatically satisfied.

**3NF check:**
- Considered whether `manufacturer` depends on `active_ingredient`. Rejected — multiple manufacturers can produce medicine with the same active ingredient (e.g. multiple companies producing Paracetamol).
- Considered whether `manufacture_date` depends on `manufacturer`. Rejected — a single manufacturer produces multiple batches on different dates; the manufacturer alone does not determine a specific manufacture date.

**Result:** ✅ 3NF

---

## 10. Invoice

**PK:** `invoice_id` (single column) → 2NF automatically satisfied.

**3NF check:** `total_amount`, `issued_date`, `invoice_status` are independent attributes of the specific invoice. No transitive dependency found.

**Result:** ✅ 3NF

---

## 11. Payment

**PK:** `payment_id` (single column) → 2NF automatically satisfied.

**3NF check:** Considered whether `transaction_reference` depends on `payment_method` instead of `payment_id` directly. Rejected — each payment generates its own unique transaction reference, even when the payment method is the same (e.g. two Credit Card payments have two different reference codes). `transaction_reference` depends only on `payment_id`.

**Result:** ✅ 3NF

---

## Summary Table

| # | Entity | 1NF | 2NF | 3NF |
|---|--------|-----|-----|-----|
| 1 | Patient | ✅ | ✅ | ✅ |
| 2 | Doctor | ✅ | ✅ | ✅ |
| 3 | Department | ✅ | ✅ | ✅ |
| 4 | Room | ✅ | ✅ | ✅ |
| 5 | Appointment | ✅ | ✅ | ✅ |
| 6 | Medical_Record | ✅ | ✅ | ✅ |
| 7 | Prescription | ✅ | ✅ | ✅ |
| 8 | Prescription_Item | ✅ | ✅ | ✅ |
| 9 | Medicine | ✅ | ✅ | ✅ |
| 10 | Invoice | ✅ | ✅ | ✅ |
| 11 | Payment | ✅ | ✅ | ✅ |

## Conclusion

All 11 entities in the Logical ERD satisfy 1NF, 2NF, and 3NF. No structural changes to `logical_erd.drawio` are required as a result of this analysis.

This is expected rather than coincidental: the schema already separated repeating/variable data into dedicated tables at design time (e.g. `Prescription_Item` as a junction table, `Department`/`Room` as independent entities), which avoided most common normalization violations from the start.

The design is ready to proceed to Phase 3 — Physical Database Design.