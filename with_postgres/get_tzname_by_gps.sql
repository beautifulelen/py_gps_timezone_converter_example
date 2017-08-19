CREATE OR REPLACE FUNCTION get_tzname_by_gps(longtitude DOUBLE PRECISION, latitude DOUBLE PRECISION)
RETURNS TEXT AS $$
DECLARE timezone_name TEXT;
BEGIN
    SELECT tzid INTO timezone_name
    FROM tz_world
    WHERE ST_Contains(geom, ST_MakePoint(longtitude, latitude)) LIMIT 1;
    RETURN timezone_name;
END;
$$  LANGUAGE plpgsql