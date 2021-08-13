CREATE TRIGGER insert_farmer_to_billing
AFTER INSERT ON dataapp_farmer
FOR EACH ROW
BEGIN
	INSERT INTO dataapp_billing(farmer_id, quantity, unit_price, total_amount_owed, year, recorded_by_id)
	VALUES(NEW.id_number, 0, 0, 0, 2021, NULL);
END

CREATE TRIGGER add_farmer_to_billing
AFTER INSERT ON dataapp_farmer
FOR EACH ROW
BEGIN
	INSERT INTO dataapp_billing(farmer_id, total_quantity_delivered, total_cumulative_amount, amount_paid, balance, year)
	VALUES(NEW.id_number, 0, 0, 0, 0, NEW.join_year);
END

CREATE TRIGGER update_farmer_payment
AFTER INSERT ON dataapp_payfarmer
FOR EACH ROW
BEGIN
	UPDATE dataapp_billing
	SET amount_paid = amount_paid + NEW.amount
	WHERE farmer_id = NEW.farmer_id AND year = NEW.year;
END

CREATE TRIGGER update_billing_after_delivery
AFTER INSERT ON dataapp_delivery
FOR EACH ROW
BEGIN
	UPDATE dataapp_billing
	SET total_quantity_delivered = total_quantity_delivered + NEW.quantity, total_cumulative_amount = total_cumulative_amount + (NEW.quantity * NEW.unit_price)
	WHERE farmer_id = NEW.farmer_id AND year = NEW.year;
END