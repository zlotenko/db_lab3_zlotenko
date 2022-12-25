--SELECT * FROM countries

DO $$
DECLARE 
	country_id 	 countries.country_id%TYPE;
	country_name countries.country_name%TYPE;
	
BEGIN
	country_id :=10;
	country_name := 'CountryName';
	FOR counter IN 1..10
		LOOP
			INSERT INTO countries(country_id, country_name)
			VALUES (country_id + counter, country_name || counter);
		END LOOP;
END;
$$
	