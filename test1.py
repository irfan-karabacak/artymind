import yake
kw_extractor = yake.KeywordExtractor()
text = """
Schmidt had had several years of psychotherapy and was not without some perspective on himself, and he knew that a certain percentage of his reaction to the way these older men coolly inspected their cuticles or pinched at the crease in the trouser of the topmost leg as they sat back on the coccyx joggling the foot of their crossed leg was just his insecurity, that he felt somewhat sullied and implicated by the whole enterprise of contemporary marketing and that this sometimes manifested via projection as the feeling that people he was trying to talk as candidly as possible to always believed he was making a sales pitch or trying to manipulate them in some way, as if merely being employed, however ephemerally, in the great grinding US marketing machine had somehow colored his whole being  and that something essentially shifty or pleading in his expression now always seemed inherently false or manipulative and turned people off, and not just in his career – which was not his whole existence, unlike so many at Team Δy, or even that terribly important to him; he had a vivid and complex inner life, and introspected a great deal – but in his personal affairs as well, and that somewhere along the line his professional marketing skills had metastasized through his whole character so that he was now the sort of man who, if he were to screw up his courage and ask a female colleague out for drinks and over drinks open his heart to her and reveal that he respected her enormously, that his feelings for her involved elements of both professional and highly personal regard, and that he spent a great deal more time thinking about her than she probably had any idea he did, and that if there were anything at all he could ever do to make
"""
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 1
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)
for kw in keywords:
    print(kw)