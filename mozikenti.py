# 暴言を検出する関数
def detect_profanity(text):
    # 検出された暴言を格納するリスト
    detected_profanity = []
    # テキストを小文字に変換
    text_lower = text.lower()
    # 暴言のリスト
    profanity_words = ["あああ", "badword2", "badword3"]  # 暴言のリストを適切に設定する
    # テキスト内の各単語をチェックし、暴言を検出する
    for word in profanity_words:
        if word in text_lower:
            detected_profanity.append(word)
    return detected_profanity

# テキストを入力
text = input("テキストを入力してください: ")

# 暴言を検出
detected_profanity = detect_profanity(text)

if detected_profanity:
    print("暴言が検知されました！")
    # ここでLINE Notifyを呼び出して通知を送信するコードを追加する
else:
    print("暴言は検知されませんでした。")
