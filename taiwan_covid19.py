import cv2
import requests
from bs4 import BeautifulSoup
import re

taiwan = {'NewTaipei': '0',
          'Taipei': '0',
          'Taoyuan': '0',
          'Hsinchu': '0',
          'Miaoli': '0',
          'Taichung': '0',
          'Changhua': '0',
          'Yunlin': '0',
          'Chiayi': '0',
          'Tainan': '0',
          'Kaohsiung': '0',
          'Pingtung': '0',
          'Taitung': '0',
          'Hualien': '0',
          'Nantou': '0',
          'Yilan': '0',
          'Keelung': '0'
          }

r = requests.get("https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php?language=en",
                 verify=False)  # 將網頁資料GET下來
soup = BeautifulSoup(r.text, "html.parser")  # 將網頁資料以html.parser
# 取HTML標中的 <div class="col-lg-12.main a"></div> 中的<span>標籤存入sel
sel = soup.select("div.col-lg-12.main a")

for s in sel:
    data = s.text.replace("+", " ").replace("\n\xa0",
                                            "").replace("\xa0", " 0").split(" ")
    
    if data[0] == 'New':
        taiwan['NewTaipei'] = "+" + data[len(data) - 1]
    if data[0] == 'Taipei':
        taiwan['Taipei'] = "+" + data[len(data) - 1]
    if data[0] == 'Taoyuan':
        taiwan['Taoyuan'] = "+" + data[len(data) - 1]
    if data[0] == 'Miaoli':
        taiwan['Miaoli'] = "+" + data[len(data) - 1]
    if data[0] == 'Changhua':
        taiwan['Changhua'] = "+" + data[len(data) - 1]
    if data[0] == 'Keelung':
        taiwan['Keelung'] = "+" + data[len(data) - 1]
    if data[0] == 'Taichung':
        taiwan['Taichung'] = "+" + data[len(data) - 1]
    if data[0] == 'Yilan':
        taiwan['Yilan'] = "+" + data[len(data) - 1]
    if data[0] == 'Kaohsiung':
        taiwan['Kaohsiung'] = "+" + data[len(data) - 1]
    if data[0] == 'Hualien':
        taiwan['Hualien'] = "+" + data[len(data) - 1]
    if data[0] == 'Hsinchu':
        if data[1] == 'County':
            taiwan['Hsinchu'] = "+" + \
                str(int(taiwan['Hsinchu'].replace("+", "")) +
                    int(data[len(data) - 1]))
        elif data[1] == 'City':
            taiwan['Hsinchu'] = "+" + \
                str(int(taiwan['Hsinchu'].replace("+", "")) +
                    int(data[len(data) - 1]))
    if data[0] == 'Chiayi':
        if data[1] == 'County':
            taiwan['Chiayi'] = "+" + \
                str(int(taiwan['Chiayi'].replace("+", "")) +
                    int(data[len(data) - 1]))
        elif data[1] == 'City':
            taiwan['Chiayi'] = "+" + \
                str(int(taiwan['Chiayi'].replace("+", "")) +
                    int(data[len(data) - 1]))
    if data[0] == 'Tainan':
        taiwan['Tainan'] = "+" + data[len(data) - 1]
    if data[0] == 'Pingtung':
        taiwan['Pingtung'] = "+" + data[len(data) - 1]
    if data[0] == 'Nantou':
        taiwan['Nantou'] = "+" + data[len(data) - 1]
    if data[0] == 'Taitung':
        taiwan['Taitung'] = "+" + data[len(data) - 1]
    if data[0] == 'Yunlin':
        taiwan['Yunlin'] = "+" + data[len(data) - 1]
print(taiwan)

# 原始圖片
bk_img = cv2.imread("Taiwan.jpg")
# 在圖片上添加文字
cv2.putText(bk_img, "New Taipei:" + taiwan['NewTaipei'], (810, 170),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Taoyuan:" + taiwan['Taoyuan'], (200, 120), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Hsinchu:" + taiwan['Hsinchu'], (200, 175), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Miaoli:" + taiwan['Miaoli'], (185, 220), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Taichung:" + taiwan['Taichung'], (145, 280),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Changhua:" + taiwan['Changhua'], (100, 345),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Yunlin:" + taiwan['Yunlin'], (125, 400), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Chiayi:" + taiwan['Chiayi'], (105, 445), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Tainan:" + taiwan['Tainan'], (95, 515), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Kaohsiung:" + taiwan['Kaohsiung'], (85, 580),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Pingtung:" + taiwan['Pingtung'], (125, 670),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Taitung:" + taiwan['Taitung'], (715, 545),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Hualien:" + taiwan['Hualien'], (785, 320),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Nantou:" + taiwan['Nantou'], (775, 385),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Yilan:" + taiwan['Yilan'], (815, 215), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Keelung:" + taiwan['Keelung'], (820, 70),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(bk_img, "Taipei:" + taiwan['Taipei'], (255, 70), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 0, 0), 1, cv2.LINE_AA)


# 顯示圖片
cv2.imshow("Taiwan_COVID-19", bk_img)
cv2.waitKey()
# 保存圖片
# cv2.imwrite("add_text.jpg",bk_img)
