# Attributes

## Overview

Attribute represents a piece of information that describes an entity.

The purpose of attribute analysis is to determine what information the business needs to store for each entity before designing the database.

## 1. Patient

### Description

The Patient entity stores the personal and contact information required to identify and manage patients throughout their healthcare journey.

### Main Attributes

| Attribute | Description | Required | Notes |
|-----------|-------------|----------|-------|
| patient_id | Unique identifier assigned to each patient | Yes | Assigned by the hospital |
| full_name | Patient's full name | Yes | |
| date_of_birth | Patient's date of birth | Yes | Age is calculated, not stored |
| gender | Patient's gender | Yes | |
| phone_number | Primary contact number | Yes | One phone number per patient |
| address | Current residential address | Yes | |
| identity_number | National ID or passport number | No | Optional depending on patient eligibility |
| emergency_contact_name | Emergency contact person's name | No | |
| emergency_contact_phone | Emergency contact person's phone number | No | |

---

## 2. Doctor

### Description

Stores information required to identify, manage, and assign doctors within the hospital.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| doctor_id | Yes | Unique doctor identifier | Assigned by the hospital |
| full_name | Yes | Doctor's full name | |
| date_of_birth | Yes | Doctor's date of birth | Age is calculated from this value |
| gender | Yes | Doctor's gender | |
| phone_number | Yes | Primary contact number | One phone number per doctor |
| work_email | Yes | Official work email address | One work email per doctor |
| specialty | Yes | Doctor's primary medical specialty | One specialty per doctor |
| department | Yes | Department where the doctor works | One department per doctor |
| license_number | Yes | Medical practice license number | Issued by the medical authority |
| hire_date | Yes | Date the doctor joined the hospital | |
| employment_status | Yes | Current employment status | e.g. Active, On Leave, Resigned |

## 3. Department

### Description

Stores information required to identify and manage hospital departments.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| department_id | Yes | Unique department identifier | Assigned by the hospital |
| department_name | Yes | Department name | |
| description | No | Description of the department's function | Optional |
| location | Yes | Department location within the hospital | One location per department |
| phone_number | Yes | Department contact number | One phone number per department |
| department_status | Yes | Current operational status | e.g. Active, Inactive |

## 4. Room

### Description

Stores information required to identify and manage hospital rooms.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| room_id | Yes | Unique room identifier | Assigned by the hospital |
| room_name | Yes | Room name | |
| room_type | Yes | Type of room | e.g. Consultation Room, Operating Room, Emergency Room |
| department | Yes | Department responsible for the room | One department per room |
| capacity | Yes | Maximum number of patients the room can accommodate | |
| location | Yes | Room location within the hospital | Floor and building/area |
| room_status | Yes | Current room status | e.g. Available, Occupied, Maintenance, Closed |

## 5. Medicine

### Description

Stores information required to identify and manage medicines used in the hospital.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| medicine_id | Yes | Unique medicine identifier | Assigned by the hospital |
| medicine_name | Yes | Medicine name | |
| active_ingredient | Yes | Main active ingredient | |
| unit | Yes | Unit of measurement | e.g. Tablet, Bottle, Box |
| strength | Yes | Medicine strength | e.g. 500mg |
| manufacturer | Yes | Medicine manufacturer | |
| manufacture_date | Yes | Manufacture date | |
| expiry_date | Yes | Expiration date | |
| stock_quantity | Yes | Current stock quantity | Updated over time |
| medicine_status | Yes | Current medicine status | e.g. Active, Discontinued, Out of Stock |

## 6. Appointment

### Description

Stores information about appointments scheduled between patients and doctors.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| appointment_id | Yes | Unique appointment identifier | Assigned by the system |
| patient | Yes | Patient associated with the appointment | One patient per appointment |
| doctor | Yes | Doctor assigned to the appointment | One doctor per appointment |
| appointment_date | Yes | Scheduled appointment date | |
| appointment_time | Yes | Scheduled appointment time | |
| room | Yes | Room where the appointment takes place | One room per appointment |
| reason | No | Reason for the appointment | Optional |
| appointment_status | Yes | Current appointment status | e.g. Scheduled, Completed, Cancelled |

## 7. Medical Record

### Description

Stores examination and treatment information created after a patient appointment.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| medical_record_id | Yes | Unique medical record identifier | Assigned by the system |
| appointment | Yes | Appointment associated with the medical record | One medical record per appointment |
| diagnosis | Yes | Doctor's diagnosis | |
| symptoms | No | Patient's symptoms | Optional |
| treatment | No | Treatment provided | Optional |
| notes | No | Additional medical notes | Optional |
| record_date | Yes | Date the medical record was created | |

## 8. Prescription

### Description

Stores prescribed medicines issued by a doctor after a medical examination.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| prescription_id | Yes | Unique prescription identifier | Assigned by the system |
| medical_record | Yes | Medical record associated with the prescription | One prescription per medical record |
| prescribed_date | Yes | Date the prescription was issued | |
| instructions | No | Usage instructions for the medicines | Optional |
| prescription_status | Yes | Current prescription status | e.g. Issued, Cancelled |

## 9. Invoice

### Description

Stores billing information for medical services provided to patients.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| invoice_id | Yes | Unique invoice identifier | Assigned by the system |
| medical_record | Yes | Medical record associated with the invoice | One invoice per medical record |
| total_amount | Yes | Total amount to be paid | Calculated by the system |
| issued_date | Yes | Invoice issue date | |
| invoice_status | Yes | Current invoice status | e.g. Unpaid, Paid, Cancelled |

## 10. Payment

### Description

Stores payment transactions made by patients for hospital invoices.

### Main Attributes

| Attribute | Required | Description | Notes |
|-----------|----------|-------------|-------|
| payment_id | Yes | Unique payment identifier | Assigned by the system |
| invoice | Yes | Invoice associated with the payment | |
| payment_method | Yes | Payment method | e.g. Cash, Credit Card, Bank Transfer |
| payment_date | Yes | Date of payment | |
| payment_amount | Yes | Amount paid | |
| payment_status | Yes | Current payment status | e.g. Successful, Failed, Refunded |
| transaction_reference | No | External transaction reference | Optional |