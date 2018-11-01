# RelatedWord
相关搜索推荐
使用 Flask 实现python 接口，之后的效果类似于 bing 的相关搜索推荐 api（ https://api.bing.com/osjson.aspx?query={搜索词} ）。
## word2vec
使用 word2vec 训练词向量，用gensim 工具包中的most_similar()方法找到 query 词的前十个近义词并返回json 格式结果。
## 训练语料
语料使用了维基百科中英文预料，训练参数使用默认参数，得到的模型大小为3.64G.
