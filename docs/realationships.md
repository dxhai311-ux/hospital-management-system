# Relationships

## Overview

Relationship describes how entities are associated with each other according to business requirements.

---

## 1. Patient ↔ Appointment

### Business Rule

A patient can have multiple appointments.
Each appointment belongs to one patient.

### Relationship

One-to-Many (1:N)

### Cardinality

- Patient → Appointment: 0..N
- Appointment → Patient: 1

### Participation

- Patient: Optional
- Appointment: Mandatory

### Reason

A patient may exist without any appointment.

An appointment cannot exist without a patient because every appointment must be associated with exactly one patient.

## 2. Doctor ↔ Appointment

### Business Rule

A doctor can have multiple appointments.
Each appointment is assigned to one doctor.

### Relationship

One-to-Many (1:N)

### Cardinality

- Doctor → Appointment: 0..N
- Appointment → Doctor: 1

### Participation

- Doctor: Optional
- Appointment: Mandatory

### Reason

A doctor may exist without any appointment.

An appointment cannot exist without a doctor because every appointment must be assigned to exactly one doctor.

## 3. Department ↔ Doctor

### Business Rule

A department can have multiple doctors.
Each doctor belongs to one department.

### Relationship

One-to-Many (1:N)

### Cardinality

- Department → Doctor: 0..N
- Doctor → Department: 1

### Participation

- Department: Optional
- Doctor: Mandatory

### Reason

A department may exist without any doctors.

A doctor cannot exist without belonging to a department because each doctor must be assigned to exactly one department.

## 4. Department ↔ Room

### Business Rule

A department can have multiple rooms.

Each room belongs to one department.

### Relationship

One-to-Many (1:N)

### Cardinality

- Department → Room: 0..N
- Room → Department: 1

### Participation

- Department: Optional
- Room: Mandatory

### Reason

A department may exist without any rooms.

A room cannot exist without belonging to a department because every room must be assigned to exactly one department.

## 5. Appointment ↔ Room

### Business Rule

A room can host multiple appointments.

Each appointment takes place in one room.

### Relationship

One-to-Many (1:N)

### Cardinality

- Room → Appointment: 0..N
- Appointment → Room: 1

### Participation

- Room: Optional
- Appointment: Mandatory

### Reason

A room may exist without any appointments.

An appointment cannot exist without a room because every appointment must take place in exactly one room.

## 6. Appointment ↔ Medical Record

### Business Rule

A medical record is created after an appointment.

Each medical record belongs to one appointment.

### Relationship

One-to-One (1:1)

### Cardinality

- Appointment → Medical Record: 0..1
- Medical Record → Appointment: 1

### Participation

- Appointment: Optional
- Medical Record: Mandatory

### Reason

An appointment may exist without a medical record because the patient may not have been examined yet.

A medical record cannot exist without an appointment because it is created as a result of a completed appointment.

## 7. Medical Record ↔ Prescription

### Business Rule

A medical record may contain multiple prescriptions.

Each prescription belongs to one medical record.

### Relationship

One-to-Many (1:N)

### Cardinality

- Medical Record → Prescription: 0..N
- Prescription → Medical Record: 1

### Participation

- Medical Record: Optional
- Prescription: Mandatory

### Reason

A medical record may exist without any prescriptions because the doctor may determine that medication is not required.

A prescription cannot exist without a medical record because every prescription must be issued based on a medical record.

## 8. Medical Record ↔ Invoice

### Business Rule

Each medical record has one invoice.

Each invoice belongs to one medical record.

### Relationship

One-to-One (1:1)

### Cardinality

- Medical Record → Invoice: 1
- Invoice → Medical Record: 1

### Participation

- Medical Record: Mandatory
- Invoice: Mandatory

### Reason

A medical record must have one invoice according to the business requirements.

An invoice cannot exist without a medical record because every invoice is generated from exactly one medical record.

## 9. Invoice ↔ Payment

### Business Rule

Each invoice has one payment.

Each payment belongs to one invoice.

### Relationship

One-to-One (1:1)

### Cardinality

- Invoice → Payment: 1
- Payment → Invoice: 1

### Participation

- Invoice: Mandatory
- Payment: Mandatory

### Reason

An invoice must have one payment according to the business requirements.

A payment cannot exist without an invoice because every payment is made for exactly one invoice.

## 10. Prescription ↔ Medicine

### Business Rule

A prescription may contain multiple medicines.

A medicine may appear in multiple prescriptions.

### Relationship

Many-to-Many (N:N)

### Cardinality

- Prescription → Medicine: 1..N
- Medicine → Prescription: 0..N

### Participation

- Prescription: Mandatory
- Medicine: Optional

### Reason

A prescription must contain at least one medicine.

A medicine may exist without being included in any prescription because it is managed independently by the hospital.