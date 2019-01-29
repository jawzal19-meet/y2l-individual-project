from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_account(first_name,last_name,username,password,gender):
    if check_user_exists(username)==False:
        print('adding account now')
        add_account = Account(
            first_name= first_name,
            last_name = last_name,
            username = username,         
            password = password,            
            gender = gender)
        print('00')
        session.add(add_account)
        print('11')
        session.commit()
        print('commited')
    else:
        print('user         exists')
        raise Exception("User already exists")


def check_user_exists(username):

    account = session.query(Account).filter_by(username=username).first()
    if account==None:

        return False
    else:
		return True


def get_all_posts():
	 all_posts = session.query(Post).all()
	 return all_posts


def check_user_and_pass(username, password):
    print("hello")
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Account).filter_by(username=username,password=password)
    print("check")
    result = query.first()
    if result is not None:
        return True
    else:
        print('wrong password!')
        return False

def commit_post(title,article,video,quiz):
	add_post=Post(
		title=title,
		article=article,
		video=video,
		quiz=quiz
		)

	session.add(add_post)
	session.commit()



def get_post_by_id (id):
    post = session.query(Post).filter_by(id=id).first()
    return post