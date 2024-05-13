#!/bin/bash

# 暴言を検出する関数
detect_profanity() {
    # 検出された暴言を格納する変数
    detected_profanity=""
    # 暴言のリスト
    profanity_words=("badword1" "badword2" "badword3")  # 暴言のリストを適切に設定する
    # 入力されたテキストを小文字に変換
    text_lower=$(echo "$1" | tr '[:upper:]' '[:lower:]')
    # テキスト内の各単語をチェックし、暴言を検出する
    for word in "${profanity_words[@]}"; do
        if [[ "$text_lower" == *"$word"* ]]; then
            detected_profanity="$word"
            break
        fi
    done
    echo "$detected_profanity"
}

# メインの処理
main() {
    # テキストを入力
    echo "テキストを入力してください: "
    read -r text

    # 暴言を検出
    detected_word=$(detect_profanity "$text")

    if [ -n "$detected_word" ]; then
        echo "暴言が検知されました！($detected_word)"
        # ここでLINE Notifyを呼び出して通知を送信するコードを追加する
    else
        echo "暴言は検知されませんでした。"
    fi
}

# メインの処理を呼び出す
main
