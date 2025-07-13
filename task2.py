from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, Shop, Sale, Stock, Publisher

engine = create_engine('postgresql://postgres:root@localhost/hw_db')

Session = sessionmaker(bind=engine)
session = Session()

publisher_input = input("Введите имя или идентификатор издателя: ")

if publisher_input.isdigit():
    publisher_id = int(publisher_input)
    filter_condition = Publisher.id == publisher_id
else:
    publisher_name = publisher_input
    filter_condition = Publisher.name == publisher_name

query = (
    session.query(
        Book.title.label('Название книги'),
        Shop.name.label('Название магазина'),
        Sale.price.label('Стоимость покупки'),
        Sale.date_sale.label('Дата покупки')
    )
    .join(Stock, Stock.id_book == Book.id)
    .join(Sale, Sale.id_stock == Stock.id)
    .join(Shop, Stock.id_shop == Shop.id)
    .join(Publisher, Book.id_publisher == Publisher.id)
    .filter(filter_condition)
    .order_by(Sale.date_sale.desc())
)

for row in query:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3].strftime('%d-%m-%Y')}")