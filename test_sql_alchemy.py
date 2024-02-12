from sqlalchemy import create_engine,String,text
# Database 
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session,session,sessionmaker,relationship
from sqlalchemy import String,Integer, Boolean,create_engine,ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

try:
    engine=create_engine('postgresql://postgres:123456789@127.0.0.1:5432/postgres',echo=False)
    print("connection okey for testing raw sql alchemy") 
    
except Exception as er:
    print(er)
    print("connction is not successful ")
    
with Session(engine) as session:
    Session = sessionmaker(bind=engine)
    session = Session()
    

# crud operation 

class Customer(Base):
    __tablename__='customers'
    
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_name:Mapped[str] = mapped_column(nullable=True)
    salary:Mapped[int] = mapped_column(nullable=True)
    department:Mapped[str] = mapped_column(nullable=True)
    
# select query for the sql alchemy
    # stmt=text('Select * from customers')
    # result=session.execute(stmt)
    
    # for row in result:
    #     print(row)
    
# insert into database using sql alchemy
    # insert_statement = text ("""INSERT INTO customers (customer_name,salary,department) VALUES ('Ganesh kunwar',15000,'It department')""")
    # result=session.execute(insert_statement)
    # session.commit()
    # for row_insert in result:
    #     print(row_insert)
    

    #update statement 
    # update_customer=text('''update customers set customer_name='Krishna budha',salary=4000 where id=1''') 
    # updated_customer=session.execute(update_customer)
    # session.commit()
    
    # delete operations
    delete_customer=text('''  delete from customers where id=1''')
    remove_delete=session.execute(delete_customer)
    session.commit()
    