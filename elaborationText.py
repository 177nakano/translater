from textblob import TextBlob

def elaboration(text):
    blob = TextBlob(text)
    
    # 文を手動で分割
    sentences = str(blob).split('. ')
    
    corrected_sentences = []
    print(f"blob : {blob}")
    # 各文を修正
    for sentence in sentences:
        # 文を修正してリストに追加
        corrected_sentences.append(str(TextBlob(sentence).correct()))

    # 修正された文を結合して返す
    return '. '.join(corrected_sentences).strip() + ('.')