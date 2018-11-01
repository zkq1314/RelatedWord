# coding:utf-8

from flask import jsonify
from flask import render_template
from flask import request

from app import app
import gensim


model_path = "data/GoogleNews-vectors-negative300.bin"  # model file
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True) #载入.bin 模型文件

@app.route("/", methods=['GET', ])
def getRelatedWords():
    word = request.values.get('query');
    if word:
        wordslist = get_similar_words_str(word, model)
        print(wordslist)
        return jsonify(RelatedWords=wordslist)
    else:
        res = {'message': 'query 不能为空'}
        return jsonify(res)


def get_similar_words_str(w, model, topn=10):
    result_words = get_similar_words_list(w, model)
    return str(result_words)


def get_similar_words_list(w, model, topn=10):
    result_words = []
    try:
        similary_words = model.most_similar(w, topn=10)
        print(similary_words)
        for (word, similarity) in similary_words:
            result_words.append(word)
        print(result_words)
    except:
        print("There are some errors!" + w)

    return result_words




