# 介紹
這是一個可以輸出台灣各縣市當日covid-19新增確診個數的分佈地圖

# 建構過程

## 安裝opencv
`pip install opencv-python`

## 安裝Python Requests套件
`pip install requests`

## 安裝Python Beautifulsoup4套件
`pip install beautifulsoup4`

# 方法
利用Requests套件與Beautifulsoup4套件撰寫爬蟲程式抓取當日的確診個數，
再利用opencv套件針對圖片進行編輯，將抓取到的各縣市新增個數加入圖片

# 參考資料
https://blog.csdn.net/sinat_29957455/article/details/88071078
https://ithelp.ithome.com.tw/articles/10202121?sc=hot

# 數據資料來源
https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php?language=zh-tw

# Taiwan_covid-19
