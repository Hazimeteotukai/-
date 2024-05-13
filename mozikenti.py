import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# NLTKのダウンロード
nltk.download('punkt')
nltk.download('stopwords')

# 暴言を含むかどうかを判定する関数
def detect_profanity(text):
    # 英語のストップワードを取得
    stop_words = set(stopwords.words('english'))
    # 文字列を単語に分割
    words = word_tokenize(text)
    # ストップワードを除外し、小文字に変換
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    # 暴言のリスト
    profanity_words = ["あああ", "badword2", "badword3"]  # 自分で暴言のリストを追加する
    # 暴言の検出
    detected_profanity = [word for word in filtered_words if word in profanity_words]
    return detected_profanity

# テキストを入力
text = input("テキストを入力してください: ")

# 暴言を検知
detected_profanity = detect_profanity(text)

if detected_profanity:
    print("暴言が検知されました！")
    # ここでLINE Notifyを呼び出して通知を送信するコードを追加する
else:
    print("暴言は検知されませんでした。")
