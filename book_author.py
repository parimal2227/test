from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

#making connection to the server

db_string="postgres://postgres:parimal@localhost:5432/test" #"postgres://username:password@hostname:port(by default-5432)/dbname"
db=create_engine(db_string)
base=declarative_base()

#creating 1st model class for Books table

class Books(base):
    __tablename__='Books'

    id=Column(Integer,primary_key=True)
    Name=Column(String)
    Author_id=Column(Integer,ForeignKey('Author.id'))

#creating 2nd model class for Author table

class Author(base):
    __tablename__='Author'

    id=Column(Integer,primary_key=True)
    Name=Column(String)
    psuedo=relationship('Books',backref='book') #this is vitual column for Author table to make connection with Books table


Session=sessionmaker(db)
session=Session()

base.metadata.create_all(db) #both tables are created now in our database

#inerting data into the table Books

terry_pratchitt=Author(id='1',Name='terry pratchitt')
session.add(terry_pratchitt)
session.commit()

neil=Author(id='2',Name='neil gaiman')
session.add(neil)
session.commit()

dorothy=Author(id='3',Name='dorothy l sayers')
session.add(dorothy)
session.commit()

nicci=Author(id='4',Name='nicci french')
session.add(nicci)
session.commit()

camp=Author(id='5',Name='l spargue de camp')
session.add(camp)
session.commit()

david=Author(id='6',Name='david drake')
session.add(david)
session.commit()

king=Author(id='7',Name='stephen king')
session.add(king)
session.commit()

#inserting data into the books table

good= Books(id='1',Name='Good Omwns', book=terry_pratchitt)
session.add(good)
session.commit()

case=Books(id='2',Name='The Document in the case',book=dorothy)
session.add(case)
session.commit()

killing=Books(id='3',Name='Killing me softly',book=nicci)
session.add(killing)
session.commit()

bunny=Books(id='4',Name='The Undesired Princess and Enchanted Bunny',book=camp)
session.add(bunny)
session.commit()

blue=Books(id='5',Name='Blue Monday',book=nicci)
session.add(blue)
session.commit()

the=Books(id='6',Name='The Talisman',book=king)
session.add(the)
session.commit()

god=Books(id='7',Name='American God',book=neil)
session.add(god)
session.commit()


caroline=Books(id='8',Name='Caroline',book=neil)
session.add(caroline)
session.commit()

hammer=Books(id='9',Name='Hammer\'s Slummer',book=david)
session.add(hammer)
session.commit()

price=Books(id='10',Name='At Any Price',book=david)
session.add(price)
session.commit()



#function to get the author name and all books written by that author as output:


print ("kindly type the name of author from the list:")
names=session.query(Author)
for i in names:
    print(i.Name)

while True:  #infinite loop


 def get_book(author_name):
   oAuthor=session.query(Author).filter_by(Name=author_name).first()
   oBook=oAuthor.psuedo  #now oBook is an instance for Author table
   for i in oBook:
        print(i.Name)



 entered=input('Enter the author you are interested in(case insensitive): ')
 get_entered=entered.lower()  #converting the input string to lowercase to make the input case insensitive
 get_book(get_entered)        #calling the function

