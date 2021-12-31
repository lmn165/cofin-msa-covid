import datetime
import os

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from icecream import ic
from common.models import ValueObject
from sqlalchemy import create_engine
import pymysql
from datetime import datetime






def covid_scraper():
    vo = ValueObject()

    '''chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1200x600')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
    url = "http://ncov.mohw.go.kr/"
    driver.implicitly_wait(3)
    driver.get(url)'''
    pymysql.install_as_MySQLdb()
    #engine = create_engine("mysql+mysqldb://root:" + "password" + "@localhost/mariadb", encoding='utf-8')
    #conn = engine.connect()

    vo.context = 'data/'
    vo.url = 'http://ncov.mohw.go.kr/'
    driver = webdriver.Chrome(f'{vo.context}chromedriver')
    driver.get(vo.url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tables = soup.select('table')
    table = tables[0]
    table_html = str(table)
    table_df_list = pd.read_html(table_html)
    # ic(table_df_list)
    table_df = table_df_list[0]
    table_df['날짜'] = datetime.today()


    ic(table_df)
    table_df = table_df.loc[:, ['구분', '사망', '재원 위중증', '신규 입원', '확진','날짜']]
    #ic(table_df)
    today = table_df.iloc[0:1,1:]
    week = table_df.iloc[1:2,1:]
    ic(today)
    ic(week)
    week.rename(columns={'구분':'sortation','사망':'death','재원 위중증':'serious','신규 입원':'new_hospitalization','확진':'confirmed','날짜':'update_at'},inplace=True)
    today.rename(columns={'구분': 'sortation', '사망': 'death', '재원 위중증': 'serious', '신규 입원': 'new_hospitalization',
                         '확진': 'confirmed','날짜':'update_at'}, inplace=True)
    week.to_csv(vo.context + 'week_case.csv', index=False)
    today.to_csv(vo.context + 'today_case.csv', index=False)


    #db_connection_str = 'mysql+pymysql://root:root@127.0.0.1:3306/mariadb'
    #db_connection = create_engine(db_connection_str)
    #conn = db_connection.connect()
    #week.to_sql(name='week', con=db_connection, if_exists='append', index=False)
    #today.to_sql(name='today', con=db_connection, if_exists='append', index=False)
    # 위 커넥션 정보와 동일하게 입력
    #table_df.to_sql(name=table, con=engine, if_exists='append')
    driver.close()

if __name__ == '__main__':
    covid_scraper()

