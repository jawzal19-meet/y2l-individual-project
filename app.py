from flask import Flask, render_template, url_for, redirect, request, session
from database import add_account, check_user_and_pass, check_user_exists, get_all_posts, commit_post, get_post_by_id

from flask import Flask
app = Flask(__name__)


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        if True:
            add_account(first_name, last_name, username, password, gender)
            return redirect(url_for('signin'))
        else: #except:
        	print('aaaaaaaaaaa')
        	return render_template("signup.html", error_message="Error: Username Taken")



@app.route('/', methods=['GET', 'POST'])
def signin():
    print("login")
    print(request.form)
    if request.method == 'POST':
        if check_user_and_pass(request.form['username'], request.form['password']) == True:
            print("success")
            return redirect(url_for('add_post'))
        else:
            print('error:username or password are incorrect!!')
            return render_template('login.html', incorrect_user_or_pass='error:username or password are incorrect!! ')

    return render_template('login.html')




@app.route('/courses', methods=['GET','POST'])
def courses():
	if request.method == 'GET':
		all_posts = get_all_posts()
		return render_template('postspage.html', all_posts = all_posts)


@app.route('/add-post', methods=['GET','POST'])
def add_post():
	if request.method == 'GET':
		return render_template('add_post.html')
	else:
		title = request.form['title']
		article = request.form['article']
		video = request.form['video']
		quiz = request.form['quiz']
		commit_post(title,article, video,quiz)
		return redirect(url_for('courses'))


@app.route('/postpage/<id>' , methods=['GET','POST'])
def postpage(id):
	print("bbb")
	if request.method == 'GET':
		print("aaa")
		post = get_post_by_id(id)
		print(post.title)
		return render_template('postpage.html' , post=post)


if __name__ == '__main__':
    app.run(debug=True)


