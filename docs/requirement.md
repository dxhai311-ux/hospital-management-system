# Software Requirement Specification (SRS)

## Project Information

**Project Name:** Hospital Management System

**Version:** 1.0

**Status:** Draft

**Prepared By:** Client

---

# 1. Project Background

ABC Hospital is currently managing its daily operations using multiple Excel files and paper-based records. This approach has caused several issues, including duplicate patient information, difficulty tracking medical history, scheduling conflicts, and slow reporting.

The hospital management has decided to develop a centralized Hospital Management System to improve operational efficiency, data accuracy, and information accessibility.

---

# 2. Project Objectives

The system aims to:

- Store and manage patient information.
- Manage doctor information.
- Organize hospital departments.
- Schedule patient appointments.
- Record medical examinations.
- Manage medicines and prescriptions.
- Generate invoices for medical services.
- Allow staff to search and review patient medical history.

---

# 3. Project Scope

The first version of the system includes only the core hospital management functions.

The following features are included:

- Patient Management
- Doctor Management
- Department Management
- Appointment Management
- Medical Record Management
- Prescription Management
- Medicine Management
- Invoice Management

The following features are NOT included:

- Online payment
- Health insurance integration
- SMS notification
- Email notification
- Mobile application
- Online appointment booking by patients

---

# 4. System Users

The system will be used internally by hospital staff.

The user roles include:

- Receptionist
- Doctor
- Pharmacist
- Accountant
- Administrator

Patients do not directly access the system.

---

# 5. Functional Requirements

The system shall allow hospital staff to:

### Patient Management

- Register a new patient.
- Update patient information.
- Search patient information.
- View patient medical history.

### Doctor Management

- Add doctor information.
- Update doctor information.
- Assign doctors to departments.

### Department Management

- Manage hospital departments.

### Appointment Management

- Create appointments.
- Update appointment schedules.
- Cancel appointments.

### Medical Record Management

- Record diagnoses.
- Record symptoms.
- Record treatment notes.

### Prescription Management

- Create prescriptions.
- Add multiple medicines to one prescription.

### Medicine Management

- Manage medicine information.
- Update medicine stock information.

### Invoice Management

- Generate invoices.
- Calculate total medical costs.

---

# 6. Business Rules

The following business rules apply:

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

---

# 7. Non-functional Requirements

The system should:

- Store data securely.
- Prevent duplicate records whenever possible.
- Support future system expansion.
- Maintain data consistency.
- Provide acceptable query performance.

---

# 8. Assumptions

The first version assumes:

- One hospital only.
- One branch only.
- One doctor belongs to one department.
- One appointment is for one patient only.

---

# 9. Out of Scope

The following features are outside the scope of Version 1.0:

- Multi-branch hospitals
- Online payment gateway
- Insurance claim processing
- Laboratory management
- Medical imaging management
- Patient mobile application

---

**End of Requirement Specification**