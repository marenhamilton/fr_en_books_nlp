import flask
from flask import request,redirect,url_for
import pandas as pd
from api import very_topic, most_sim
import pickle

app = flask.Flask(__name__)

en_topics = pd.read_csv('static/data/topic_en_hyper.csv',index_col=0)
fr_topics = pd.read_csv('static/data/topic_fr_hyper.csv',index_col=0)

top_trans_en = ['Romantic Drama','Science','War','Religion','Outdoors',
             'Boats (adventure)','Literature','Boats (living on)',
             'Crime','People and Folk','Politics','Native Worlds','Knights']
top_trans_fr = ['Drame Romantique','Guerre','Révolution','Campagne','Espionnage et Détectives','Politique et Economie',
             'Bateaux','Drame de Vie',"Exploration à l'Etranger",'Business et Commerce','Religion','La Guerre Franco-Prussienne',
             'Contes de Fées','Des Arts et la Bohème','Chevaliers','Loi et Crime','Romains "Philosophiques"']

topics_en = dict(sorted(list(zip(en_topics,top_trans_en)),key=lambda x : x[1]))
topics_fr = dict(sorted(list(zip(fr_topics,top_trans_fr)),key=lambda x : x[1]))

books_en = pickle.load(open('static/data/en_title_dictionary.pkl','rb'))
books_fr = pickle.load(open('static/data/fr_title_dictionary.pkl','rb'))

@app.route('/')
def welcome():
    return redirect("/en", code=302)

@app.route('/en')
def welcome_en():
    return flask.render_template('en_homepage.html')

@app.route('/en/by_book',methods=['POST','GET'])
def by_book():
    recom = most_sim(request.args,en_topics,books_en)
    return flask.render_template('by_book.html',
                                books = books_en,
                                rec_book = recom)

@app.route('/en/by_topic',methods=['POST','GET'])
def by_topic():
    books = very_topic(request.args,en_topics,books_en)
    return flask.render_template('by_topic.html',
                                topics = topics_en,
                                chosen_topic = books)

@app.route('/en/about')
def about() :
    return flask.render_template('about.html')

@app.route('/en/contact')
def contact_en() :
    return flask.render_template('contact_en.html')

@app.route('/fr')
def acceuil() :
    return flask.render_template('acceuil.html')

@app.route('/fr/par_livre')
def par_livre() :
    recom = most_sim(request.args,fr_topics,books_fr)
    return flask.render_template('par_livre.html',
                                books = books_fr,
                                rec_book = recom)

@app.route('/fr/par_topique',methods=['POST','GET'])
def par_topique():
    books = very_topic(request.args,fr_topics,books_fr)
    return flask.render_template('par_topique.html',
                                topics = topics_fr,
                                chosen_topic = books)

@app.route('/fr/contact')
def contact_fr() :
    return flask.render_template('contact_fr.html')

@app.route('/fr/a_propos')
def a_propos() :
    return flask.render_template('a_propos.html')

if __name__=="__main__" :
    app.run(debug=True)