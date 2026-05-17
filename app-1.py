from flask import Flask, request, render_template_string

app = Flask(__name__)

home_page = '''
<!DOCTYPE html>
<html>
<head>
<title>User Profile Generator</title>
<style>
body{
font-family:Arial,sans-serif;
background:#f4f4f4;
padding:40px;
text-align:center;
}
.container{
background:white;
padding:30px;
width:350px;
margin:auto;
border-radius:15px;
box-shadow:0 0 10px gray;
}
input,textarea{
width:90%;
padding:10px;
margin:10px;
border:1px solid #ccc;
border-radius:8px;
}
button{
background:pink;
padding:10px 20px;
border:none;
border-radius:8px;
font-size:18px;
cursor:pointer;
}
</style>
</head>
<body>
<div class="container">
<h1>User Profile Card Generator</h1>
<form action="/profile" method="POST">
<input type="text" name="name" placeholder="Enter name" required>
<textarea name="bio" placeholder="Enter bio" required></textarea>
<input type="text" name="image" placeholder="Paste image URL" required>
<br>
<button type="submit">Generate Card</button>
</form>
</div>
</body>
</html>
'''

profile_page='''
<!DOCTYPE html>
<html>
<head>
<title>Profile Card</title>
<style>
body{
font-family:Arial;
background:#f0f2f5;
text-align:center;
padding-top:50px;
}
.card{
width:320px;
background:white;
padding:20px;
margin:auto;
border-radius:15px;
box-shadow:0 0 12px gray;
}
img{
width:150px;
height:150px;
border-radius:50%;
object-fit:cover;
}
h2{color:#333;}
p{color:#666;}
a{
text-decoration:none;
background:pink;
padding:10px;
border-radius:8px;
color:black;
}
</style>
</head>
<body>
<div class="card">
<img src="{{image}}">
<h2>{{name}}</h2>
<p>{{bio}}</p>
<br>
<a href="/">Back</a>
</div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(home_page)

@app.route('/profile', methods=['POST'])
def profile():
    name=request.form['name']
    bio=request.form['bio']
    image=request.form['image']

    return render_template_string(
        profile_page,
        name=name,
        bio=bio,
        image=image
    )

if __name__=='__main__':
    app.run(debug=True)
