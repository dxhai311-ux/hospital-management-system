# Entities

## Overview

Based on the business requirements and business analysis, the Hospital Management System manages the following core entities:

- Patient
- Doctor
- Department
- Appointment
- Medical Record
- Prescription
- Medicine
- Invoice
- Payment
- Room

## Entity Analysis 

### 1. Patient

#### Description

Patient represents a person who receives medical services from the hospital. The system stores and manages patient information throughout the patient's medical lifecycle, from registration to treatment and follow-up care.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a real-world business object that the hospital needs to manage.
- Has a unique identity (`patient_id`).
- Exists independently of appointments, invoices, prescriptions, or other business events.
- Contains multiple business-related attributes.
- Has its own lifecycle (registered, active, inactive, archived, etc.).
- Serves as a core entity referenced by multiple other entities within the system.

### 2. Doctor

#### Description

Doctor represents a medical professional who provides healthcare services to patients. The system stores and manages doctor information throughout their employment lifecycle.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a real-world business object managed by the hospital.
- Has a unique identity.
- Exists independently of appointments or patients.
- Has its own lifecycle.
- Is referenced by multiple business events.

### 3. Department

#### Description

Department represents a specialized medical unit within the hospital. It is responsible for organizing doctors and providing specific healthcare services.

#### Why is it an Entity?

- Required by the business requirements.
- Represents an organizational unit managed by the hospital.
- Exists independently of doctors or patients.
- Has its own lifecycle.
- Is referenced by multiple business entities.

### 4. Room

#### Description

Room represents a physical space within the hospital where healthcare services or hospital operations take place. The system stores and manages room information to support daily hospital operations.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a physical business object managed by the hospital.
- Exists independently of patients, doctors, or appointments.
- Has its own lifecycle (available, occupied, under maintenance, retired, etc.).
- Is referenced by multiple business activities within the hospital.

### 5. Medicine

#### Description

Medicine represents a pharmaceutical product used by the hospital to treat patients. The system stores and manages medicine information for prescription and inventory purposes.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a business object managed by the hospital.
- Different medicines are used for different medical conditions.
- Exists independently of prescriptions or patients.
- Has its own lifecycle (available, out of stock, expired, discontinued, etc.).

### 6. Appointment

#### Description

Appointment represents a scheduled medical visit between a patient and a doctor. The system stores appointment information to organize and manage medical consultations.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a business transaction managed by the hospital.
- Records a scheduled interaction between a patient and a doctor.
- Has its own timeframe and business status.
- Has its own lifecycle (scheduled, confirmed, completed, cancelled, etc.).

### 7. Medical Record

#### Description

Medical Record represents the clinical information generated during a patient's medical examination and treatment. The system stores medical records to maintain the patient's healthcare history.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a business record created after a medical examination.
- Stores diagnosis, treatment, and clinical information.
- Maintains the patient's medical history.
- Has its own lifecycle throughout the healthcare process.

### 8. Prescription

#### Description

Prescription represents a doctor's medication order created after a medical examination. The system stores prescription information to support patient treatment and medication dispensing.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a medical document created during the treatment process.
- Stores prescribed medicines and dosage instructions.
- Supports medication dispensing and treatment tracking.
- Has its own lifecycle (issued, dispensed, completed, cancelled, etc.).

### 9. Invoice

#### Description

Invoice represents the billing information for medical services and products provided to a patient. The system stores invoices to calculate and manage hospital charges.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a financial business document managed by the hospital.
- Records charges for medical services and products.
- Supports hospital billing and financial management.
- Has its own lifecycle (draft, issued, paid, cancelled, etc.).

### 10. Payment

#### Description

Payment represents a financial transaction made by a patient to settle an invoice. The system stores payment information to track and confirm hospital payments.

#### Why is it an Entity?

- Required by the business requirements.
- Represents a financial transaction managed by the hospital.
- Records payment information for invoices.
- Supports payment tracking and financial management.
- Has its own lifecycle (pending, completed, failed, refunded, etc.).