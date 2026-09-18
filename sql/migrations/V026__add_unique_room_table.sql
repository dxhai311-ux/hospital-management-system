-- Migration : V026
-- Description : Add Unique Constraint to Room Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE room
    ADD CONSTRAINT uq_room_name_department UNIQUE (room_name, department_id);