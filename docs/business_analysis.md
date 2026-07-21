# Business Analysis

## 1. Project Overview

The Hospital Management System is designed to improve operational efficiency, enhance data accuracy, and provide centralized access to hospital information.

The system addresses common operational challenges such as duplicate patient records, difficulties in tracking medical history, appointment scheduling conflicts, and slow report generation.

It supports the management of core hospital operations, including patient registration, doctor management, appointment scheduling, prescription management, billing, and payment processing.

The primary goal of the system is to streamline hospital workflows, reduce manual effort, improve service quality, and provide reliable information for daily operations and decision-making.

## 2. Actors

### Receptionist

**Responsibilities**
- Register new patients.
- Update patient information.
- Schedule appointments.
- View appointment schedules.

**Permissions**
- Create and update patient records.
- Create, modify, and cancel appointments.

**Restrictions**
- Cannot prescribe medicines.
- Cannot modify medical records.
- Cannot manage user accounts.

---

### Doctor

**Responsibilities**
- Examine patients.
- Review patient medical history.
- Diagnose diseases.
- Create prescriptions.
- Provide medical advice.

**Permissions**
- Create prescriptions.
- Update prescriptions before they are finalized.
- View patient medical history.

**Restrictions**
- Cannot manage user accounts.
- Cannot access financial management.
- Cannot permanently delete patient records.

### Administrator

**Responsibilities**
- Manage user accounts.
- Manage user roles and permissions.
- Monitor system activities.
- Maintain system configuration.

**Permissions**
- Create, update, disable, and enable user accounts.
- Assign roles and permissions.
- View system logs.
- Access all system modules.

**Restrictions**
- Cannot modify medical diagnoses for business purposes.
- Cannot create prescriptions on behalf of doctors.

### Cashier

**Responsibilities**
- Process patient payments.
- Generate invoices.
- Verify payment status.
- Issue payment receipts.

**Permissions**
- Create payment records.
- Update payment status.
- View invoices.

**Restrictions**
- Cannot modify patient medical records.
- Cannot prescribe medicines.
- Cannot manage user accounts.

### Pharmacist

**Responsibilities**
- View prescriptions.
- Dispense medicines.
- Verify prescribed medicines.
- Record medicine dispensing.

**Permissions**
- View approved prescriptions.
- Update dispensing status.
- Record dispensed medicines.

**Restrictions**
- Cannot create prescriptions.
- Cannot modify patient medical records.
- Cannot manage payments.

## 3. Business Process

### Patient Journey

1. Patient arrives at the hospital.
2. Patient goes to the reception desk.
3. Receptionist creates a patient record (if the patient is new).
4. Receptionist schedules an appointment.
5. Patient waits for the appointment.
6. Patient enters the assigned examination room.
7. Doctor examines the patient.
8. Doctor records the diagnosis.
9. Doctor creates a prescription (if required).
10. Patient collects medicine from the pharmacy.
11. Patient completes the payment.
12. Patient leaves the hospital.

## 4. Business Rules

- A patient can have multiple appointments.
- A doctor can examine multiple patients.
- Each doctor belongs to one department.
- A department can have multiple doctors.
- Each appointment is assigned to one doctor.
- Each appointment belongs to one patient.
- A medical record is created after an appointment.
- A prescription belongs to one medical record.
- A prescription may contain multiple medicines.
- A medicine may appear in multiple prescriptions.
- Each medical record has one invoice.
- Each room belongs to one department.
- A department can have multiple rooms.
- Each appointment takes place in one room.
- A room can host multiple appointments.