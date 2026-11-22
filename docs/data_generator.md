# Data Generator

Generates test data for the Hospital Management System, then injects controlled errors for data quality practice.

## Structure

- `config.py`: scale targets and `RANDOM_SEED`
- `database.py`: database connection (SQLAlchemy) and Python random seed
- `generators/`: one file per table, run in foreign key order
- `dirty_data.py`: injects errors into the clean data

## Generation order

department → patient → medicine → doctor → room → appointment → medical_record → prescription → prescription_item → invoice → payment

Parent tables come first because child tables need valid foreign keys (for example, an appointment needs an existing patient and doctor).

## Scale

| Table | Target |
|---|---|
| department | 55 |
| patient | 2000 |
| medicine | 200 |
| doctor | 30 |
| room | 60 |
| appointment | 10000 |

Medical records, prescriptions, items, invoices and payments are created from completed appointments, so their counts depend on the seed.

## Dirty data

Run last. It injects these errors and logs the exact counts:

| Error | Count |
|---|---|
| Corrupted patient phone numbers | 100 |
| Corrupted appointment times | 200 |
| Corrupted medical record dates | 156 |
| Corrupted payment dates | 133 |
| Corrupted appointment statuses | 200 |
| Duplicate patients | 20 |

## Reproducibility

`RANDOM_SEED` in `config.py` fixes Python randomness. `dirty_data.py` also calls PostgreSQL `setseed`, so SQL `RANDOM()` is fixed too. Running `python rebuild.py` twice gives identical data.

## How to run

```
python rebuild.py
```