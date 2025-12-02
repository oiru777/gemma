import cv2
from ollama import chat

# カメラ初期化（0はデフォルトカメラ）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("カメラを開けませんでした")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("フレーム取得失敗")
            break

        # 取得したフレームを一時的に保存（Ollamaはファイルパス指定）
        image_path = "capture.png"
        cv2.imwrite(image_path, frame)

        # Gemmaに渡して説明生成
        response = chat(
            model="gemma3",  # マルチモーダル対応モデル
            messages=[
                {
                    "role": "user",
                    "content": "この画像を200文字以内で説明してください",
                    "images": [image_path]
                }
            ]
        )

        print("=== 説明 ===")
        print(response.message.content)
        print("============")

        # 続けるか聞く
        cont = input("もう1枚撮影しますか？ (y/n): ")
        if cont.lower() != "y":
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
