import requests
from bs4 import BeautifulSoup

URL = "https://store.musinsa.com/app/items/lists/001"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select("div.list-box ul.snap-article-list li.li_box")

for r in result:
    #print(r)
    print("브랜드 : ", r.select("p.item_title")[0].text.replace("\n","").replace("[패밀리세일]",""))
    print("제품명 : ", r.select("p.list_info")[0].text.replace("\n","").strip())
    print("가격 : ", r.select("p.price")[0].text.replace("\n","").strip().split("\t")[-1])
    print("")

# \n: 다음 줄로 이동하며 개행이라고도 부릅니다.
# \t: 탭 문자, 키보드의 Tab 키와 같으며 여러 칸을 띄웁니다.
# strip() 문자열에서 공백을 제거