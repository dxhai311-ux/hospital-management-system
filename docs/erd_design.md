# Hospital Management System ERD Design

## 1. Purpose

This document describes the conceptual Entity Relationship Diagram (ERD) of the Hospital Management System.

The objective of this ERD is to identify the core business entities, define the relationships between them, and provide a clear data structure before the physical database implementation.

This document serves as the foundation for the Logical ERD and Physical Database Design in the next development phases.

---

# 2. Design Principles

The ERD is designed based on the following principles:

- Every relationship must be supported by a Business Requirement or Business Rule.
- Business Process is used to discover relationships but is not represented directly in the ERD.
- Each entity represents a real business object managed by the hospital.
- Layout is organized to maximize readability and minimize crossing relationships.
- Independent entities are separated from transactional entities.

---

# 3. Entity Groups

The entities are grouped according to their business responsibilities.

## 3.1 Human Management

- Patient
- Doctor

Responsible for managing people participating in the healthcare process.

---

## 3.2 Hospital Infrastructure

- Department
- Room

Responsible for managing hospital organizational structure and facilities.

---

## 3.3 Clinical Management

- Appointment
- Medical_Record

Core entities representing the diagnosis and treatment process.

---

## 3.4 Pharmacy Management

- Prescription
- Prescription_Item
- Medicine

Responsible for medication management and prescription details.

---

## 3.5 Financial Management

- Invoice
- Payment

Responsible for billing and payment processing.

---

# 4. Core Business Structure

The Appointment entity acts as the central transaction of the healthcare workflow.

Appointment connects:

- Patient
- Doctor
- Room
- Medical_Record

Medical_Record represents the result generated after an appointment.

Medical_Record branches into two independent business processes:

- Prescription
- Invoice

Prescription continues into:

Prescription → Prescription_Item → Medicine

Invoice continues into:

Invoice → Payment

---

# 5. Conceptual Relationship Overview

The conceptual relationships identified are:

- Patient ↔ Appointment
- Doctor ↔ Appointment
- Room ↔ Appointment
- Appointment ↔ Medical_Record
- Medical_Record ↔ Prescription
- Medical_Record ↔ Invoice
- Prescription ↔ Prescription_Item
- Prescription_Item ↔ Medicine
- Invoice ↔ Payment
- Department ↔ Doctor

Detailed cardinality will be documented in the Conceptual ER Diagram.

---

# 6. Deliverables

This phase produces:

- conceptual_erd.drawio
- conceptual_erd.png

These diagrams represent the Conceptual ER Diagram only.

Primary Keys, Foreign Keys, attributes, and data types will be introduced during the Logical ERD and Physical Database Design phases.