import psycopg2
import pandas.io.sql as psql

conn = psycopg2.connect(database="dvdrental", user = "postgres", password = 
"ABCabc123", host = "127.0.0.1", port = "5432")
cur = conn.cursor()


def get_data():
    data = psql.read_sql('''
    select json_agg(t) from ( select concat_ws(' ', first_name, last_name) as 
    customer_name, email, address.address as address, 
    json_agg((payment.customer_id, staff_id, rental_id)) as payment from customer 
    join payment on payment.customer_id = customer.customer_id 
    left join address on address.address_id = customer.address_id
    group by first_name, last_name, email, address
    )t ;''', conn)
    return data.json_agg[0]