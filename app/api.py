from sklearn.metrics.pairwise import cosine_similarity

def most_sim(title,data,title_dict) :
    try:
        title = title.get('Titles')
        to_match = data.loc[[title],:] #only getting first word of title
        poss = data.drop(title,axis=0)
        sims = zip(cosine_similarity(to_match,poss)[0],poss.index)
        final_return = []
        for book in sorted(sims,reverse=True)[:20] :
            book = book[1]
            final_return.append(title_dict[book])
        return final_return
    except :
        return ''

def very_topic(topic,data,title_dict) :
    try :
        topic = topic.get('Topics')
        percent = data.div(data.sum(axis=1), axis='index')
        percent = percent.sort_values(by=[topic],ascending=False)
        to_return = percent.index[:20]
        final_return = []
        for book in to_return :
            final_return.append(title_dict[book])
        return final_return
    except :
        return ''

