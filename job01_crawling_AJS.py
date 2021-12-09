from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('lang=ko_KR')
options.add_argument('disable_gpu')

# 'headless'라고 주면 크롤링하는 웹브라우저가 안떠.

driver = webdriver.Chrome('./chromedriver', options=options)

# titles = []
# reviews = []
#
# # https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=1
# # https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=2
#
# # 37페이지까지 있고, 36페이지까지는 20개씩, 마지막 페이지는 10개. 총 730개
#
# # 영화제목 Xpath
# # 1번째: //*[@id="old_content"]/ul/li[1]/a
# # 2번째: //*[@id="old_content"]/ul/li[2]/a
# # 20번쨰: //*[@id="old_content"]/ul/li[20]/a
# # //*[@id="movieEndTabMenu"]/li[6]/a/em 리뷰 버튼
# # //*[@id="reviewTab"]/div/div/div[2]/span/em 리뷰 건수
#
# # //*[@id="pagerTagAnchor1"]  리뷰 페이지 버튼
# # //*[@id="pagerTagAnchor19"]/em 리뷰 다음 페이지 버튼
# # //*[@id="reviewTab"]/div/div/ul/li[1]/a/strong 리뷰 제목
# # //*[@id="content"]/div[1]/div[4]/div[1]/div[4] # class: user_tx_area
#
# review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'  # 리뷰버튼
# # 나중에 href에서도 써먹어야하니까 em 없는애로다가.
# review_number_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em'  # 리뷰건수
#
# try:  # driver.close
#     for i in range(1, 38):      # 2020년도 페이지가 37페이지까지 있음
#         url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page={}'.format(i)
#         titles = []
#         reviews = []
#         for j in range(1, 21):  # 페이지 별로 20개의 title들이 들어있음
#             print(j+((i-1)*20), '번째 영화 크롤링 중')
#             try:
#                 driver.get(url)
#                 movie_title_xpath ='//*[@id="old_content"]/ul/li[{}]/a'.format(j)
#                 title = driver.find_element_by_xpath(movie_title_xpath).text            # 타이틀 따오기
#                 driver.find_element_by_xpath(movie_title_xpath).click()                 # 타이틀 눌러서 개별 영화로 들어가기
#
#                 # 영화의 리뷰페이지로 가기. click 은 종종 문제가 있으니 대신에 아래 두 줄(driver.get)로 받자.
#                 # driver.find_element_by_xpath(review_button_xpath).click()
#                 review_page_url = driver.find_element_by_xpath(review_button_xpath).get_attribute('href')
#                 driver.get(review_page_url)
#
#                 review_range = driver.find_element_by_xpath(review_number_xpath).text.replace(',','')
#                 review_range = int(review_range)
#                 review_range = review_range // 10 + 2
#                 # 1000건이 넘는 경우 1,000으로 들어오므로 replace로 ',' 없애기
#                 # 리뷰가 1페이지당 10개씩 있으므로 10으로 나눈 몫(정수로 받게) + 1(나머지)
#                 # review_range 에다 더하므로 +1을 더 더해서 + 2
#
#                 if review_range > 6: review_range == 6     # 리뷰가 그렇게 많을 필요 없어. 그러니 50개까지만 가져오자.(range로 받으니까 5+1)
#                 for k in range(1, review_range):           # 리뷰 1페이지~ 5페이지까지만
#                     driver.get(review_page_url + '&page={}'.format(k))    # 페이지의 주소를 열기
#                     time.sleep(0.3)
#                     for l in range(1,11):  # 리뷰페이지 별 각각의 리뷰
#                         review_title_xpath = '//*[@id="reviewTab"]/div/div/ul/li[{}]/a/strong'.format(l)
#                         try:
#                             driver.find_element_by_xpath(review_title_xpath).click()   # 리뷰 하나 클릭
#                             time.sleep(0.3)
#                             review = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div[4]').text    # 리뷰 다 따오기
#                             # print('=========================================')
#                             # print(title)
#                             # print(review)
#                             titles.append(title)   # 타이틀을 리뷰랑 맞춰서 저장해야하니 여기서 저장
#                             reviews.append(review) # append하는 애들은 가능한 몰아서 놓자. 짝맞춰야하니
#                             driver.back()
#                         except:
#                             # print(l, '번째 리뷰가 없다')
#                             break
#                         # 5번째 리뷰를 눌러야되는데 영화가 없어. 그럴 때 오류나는걸 방지하기 위한 try문
#                         # back을 두 번 눌러야 그 다음 영화를 누를 수 있게돼
#                         # 아니면 아예 driver.get(url)을 해주면 돼 > 근데 driver.get을 넣어줬으니 없애자그냥
#
#             except:
#                   print('error')
#         df_review_20 = pd.DataFrame({'title': titles, 'reviews': reviews})  # 전처리는 나중에. 여기서는 그대로 저장
#         df_review_20.to_csv('./crawling_data/reviews_{}_{}.csv'.format(2020, i), index=False)
# except: print('totally error')
# finally: driver.close() # 크롤링 끝나면 브라우저 닫히게. 어떻게 되더라도 하게끔 하는 것이 finally.
#
#
# # df_review = pd.DataFrame({'title':titles,reviews':reviews}, index=False)
# # df_review.to_csv("./crawling_data/reviews_{}.csv".format(2020))
# # 전처리는 나중에. 여기서는 그대로 저장
# # 마지막에 한번에 저장하는 코드. 위험이 있으니 페이지 돌 때마다 저장
# # 페이지 돌 때마다 저장하니까 titles, review의 빈 리스트를 for문 안으로 집어넣자.
# //*[@id="container"]/div[5]/ul/li[3]/a
review_button_xpath = '//*[@id="container"]/div[5]/ul/li[3]/strong/a'
review_number_xpath = '//*[@id="reviewList"]/li[1]/dl/dt/a'
# //*[@id="reviewList"]/li[1]/dl/dt/a
# //*[@id="post-view222588927949"]/div/div[3]
# //*[@id="reviewList"]/li[1]/dl/dt/a

driver.get('https://book.naver.com/bookdb/book_detail.naver?bid=9743475')
driver.find_element_by_xpath('//*[@id="container"]/div[5]/ul/li[3]/a').click()
time.sleep(1)
review_url = driver.find_element_by_xpath('//*[@id="reviewList"]/li[1]/dl/dt/a').get_attribute('href')
driver.get(review_url)
time.sleep(1)
driver.switch_to.frame('mainFrame')
review = driver.find_element_by_xpath('//*[@id="post-view222588927949"]/div/div[3]').text
print(review)
driver.close()



#//*[@id="reviewList"]/li[1]/dl/dt/a








