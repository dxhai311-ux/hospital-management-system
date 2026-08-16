-- Migration : V042 
-- Description : Add default room table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE room
    ALTER COLUMN room_status SET DEFAULT 'Available';