-- Migration : V032
-- Description : Add check room table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE room 
    ADD CONSTRAINT chk_room_capacity CHECK (capacity > 0);