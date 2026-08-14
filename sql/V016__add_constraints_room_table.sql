-- Migration : V016
-- Description : Add Constraints to Room Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE room
    ALTER COLUMN room_name SET NOT NULL,
    ALTER COLUMN room_type SET NOT NULL,
    ALTER COLUMN department_id SET NOT NULL,
    ALTER COLUMN capacity SET NOT NULL,
    ALTER COLUMN location SET NOT NULL,
    ALTER COLUMN room_status SET NOT NULL;