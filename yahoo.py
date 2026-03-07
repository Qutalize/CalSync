# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import strip

# 出発駅の入力
departure_station = input("出発駅を入力してください：")
# 到着駅の入力
destination_station = input("到着駅を入力してください：")

# 経路の取得先URL
route_url = "https://transit.yahoo.co.jp/search/print?from="+departure_station+"&flatlon=&to="+ destination_station
print(route_url)
# Requestsを利用してWebページを取得する
route_response = requests.get(route_url)

# BeautifulSoupを利用してWebページを解析する
route_soup = BeautifulSoup(route_response.text, 'html.parser')

# 経路のサマリーを取得
route_summary = route_soup.find("div",class_ = "routeSummary")
# 所要時間を取得
required_time = route_summary.find("li",class_ = "time").get_text()
fare = route_summary.find("li", class_ = "fare").get_text()


print("======"+departure_station+"から"+destination_station+"=======")
print("所要時間："+required_time)
print("料金："+fare)
print("URL："+route_url)


