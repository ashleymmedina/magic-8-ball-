from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

# @app.route('/')
# def hello ():
#     return render_template('index.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         return f'Thanks for submitting the response {request.form["response"]}!'
#     return render_template('signup.html', signup=url_for('response'))


# @app.route9('/8ball')
# def eightball():
#     return render_template('8ball.html, eightball={response}


# @app.route('/8ball')
# def eightball():
#     return render_template('8ball.html', eightball={random.choice('8ball')}

# @app.route('/gifs')
# def input():
#     myGifs = ["https://media1.giphy.com/media/ccLA75Is1P2by8Wx07/giphy.webp?cid=790b7611a8je0328b7iud4kiikl59lmp123p1ksr9srl999j&ep=v1_gifs_trending&rid=giphy.webp&ct=g",
#             "https://media0.giphy.com/media/fUQ4rhUZJYiQsas6WD/200.webp?cid=82a1493bw8vimalabjc82tlxg3rdgaf6ssaoqvg0bblwr89z&ep=v1_gifs_trending&rid=200.webp&ct=g",
#             "https://media2.giphy.com/media/3NtY188QaxDdC/giphy.webp?cid=82a1493bglhxix4lu59ygfjtihrnva94wuw5et2vo4ef7s4t&ep=v1_gifs_trending&rid=giphy.webp&ct=g",
#             "https://media1.giphy.com/media/xchUhdPj5IRyw/giphy.webp?cid=82a1493bh2tgpx4vnintztpbzh75r1oc6791cti1fowe8wsv&ep=v1_gifs_trending&rid=giphy.webp&ct=g"
#      ]
#     randomGif = random.choice(myGifs)
#     return render_template('gifs.html', random=randomGif, randomBool=False, myGifs=myGifs)

@app.route('/input', method=['GET', 'POST'])
def input():
    imgData = {
            "dog":["https://www.akc.org/wp-content/uploads/2017/11/Siberian-Husky-standing-outdoors-in-the-winter.jpg",
                   "https://miro.medium.com/v2/resize:fit:1024/1*VPra30HqtU1iPTkFaM2fow.png",
                   "https://www.akc.org/wp-content/uploads/2017/11/German-Shepherd-on-White-00.jpg",
                   "https://cdn.britannica.com/02/236302-050-E1F61BB1/Alaskan-Malamute-sled-dog.jpg",
                   ]
    }
    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "No data found for " + query # exit the function
        return render_template('gifs.html', imgData=imgData[query])

    return render_template('input.html', url=url_for('input'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
