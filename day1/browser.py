import webbrowser


keywords = ["아이유", "수지", "설현"]
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
for name in keywords:
    webbrowser.open(url + name)
