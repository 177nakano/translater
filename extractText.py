import pyautogui
import easyocr
import io

def extract_text(coordinates):
    # スクリーンショットを撮る
    screenshot = pyautogui.screenshot(region=coordinates)
    
    # PILの画像をバイトデータに変換
    buffered = io.BytesIO()
    screenshot.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    
    # EasyOCR のリーダーを作成
    reader = easyocr.Reader(['en'])
    
    # バイトデータをファイルに保存する
    with open("temp_image.png", "wb") as temp_file:
        temp_file.write(img_bytes)
    
    # 保存したファイルパスを使って OCR を実行
    result = reader.readtext("temp_image.png", detail=0)

    # 一時ファイルを削除する
    import os
    os.remove("temp_image.png")
    
    return " ".join(result)