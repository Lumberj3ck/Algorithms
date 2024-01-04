select company_name, contact_name, phone, country
from customers
where country = 'USA';

select count(*) from products where unit_price > 20;


select count(*) from products where discontinued <> 1;


select * from orders where order_date > '1998-03-01';


select * from orders where freight between 20 and 40;


select min(order_date)
from orders
where ship_city = 'London';



select ship_country, count(*) from orders where freight > 50 group by ship_country;

select country, count(customer_id) as amount from Customers group by country order by amount asc limit 10;


select company_name, count(*)
from orders
inner join shippers on ship_via = shipper_id
group by company_name
;

select count(*) from orders;

select category_name, sum(unit_price) from products natural join categories group by category_name;

select category_id, sum(unit_price * units_in_stock) as overall_amount from products where discontinued = 0 group by category_id ;

