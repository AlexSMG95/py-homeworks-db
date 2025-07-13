import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale

engine = create_engine('postgresql://postgres:root@localhost/hw_db')
Session = sessionmaker(bind=engine)
session = Session()

with open('data/data_for_db.json', 'r') as file:
    data = json.load(file)

for item in data:
    model_name = item['model']
    fields = item['fields']
    pk = item['pk']

    if model_name == 'publisher':
        publisher = Publisher(id=pk, name=fields['name'])
        session.add(publisher)

    elif model_name == 'book':
        book = Book(id=pk, title=fields['title'], id_publisher=fields['id_publisher'])
        session.add(book)

    elif model_name == 'shop':
        shop = Shop(id=pk, name=fields['name'])
        session.add(shop)

    elif model_name == 'stock':
        stock = Stock(id=pk, id_shop=fields['id_shop'], id_book=fields['id_book'], count=fields['count'])
        session.add(stock)

    elif model_name == 'sale':
        sale = Sale(id=pk, price=fields['price'], date_sale=fields['date_sale'], count=fields['count'], id_stock=fields['id_stock'])
        session.add(sale)

session.commit()