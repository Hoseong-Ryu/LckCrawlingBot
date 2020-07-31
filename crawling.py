from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import bs4
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


def SearchMatching(teamName):
    # region 기본 크롤링 세팅
    URL = 'https://qwer.gg/teams/' + teamName
    driver.get(URL)
    time.sleep(2)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    first_div = soup.find('div', {'class': 'Team'})
    second_div = first_div.find_all('div', {'class': 'FluidContainer container-fluid'})
    third_div = second_div[3]
    a_find = third_div.find('a')
    # endregion

    home_team_find = a_find.find('div', {'class': 'MatchBar__column home'})
    away_team_find = a_find.find('div', {'class': 'MatchBar__column away'})

    score_find = a_find.find('div', {'class': 'MatchBar__column board'})
    score_find = score_find('div', {'class': 'ScoreBoard Gilroy MatchBar__column__score'})
    home = home_team_find.text.strip()
    away = away_team_find.text.strip()

    home = home.replace("WIN", "")
    away = away.replace("WIN", "")
    for i in score_find:
        score = i.text.strip()

    score1 = score[0]
    score2 = score[1]
    return_list = [home, score1, score2, away]
    return return_list


def SearchRank():
    URL = 'https://qwer.gg/leagues/LCK/2020/summer'
    driver.get(URL)
    time.sleep(2)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    first_div = soup.find('div', {'class': 'FluidContainer container-fluid'})
    second_div = first_div.find('div', {'class': 'League__tournament'})
    third_div = second_div.find('div', {'class': 'Tournament'})
    fourth = third_div.find('div', {'class': 'Ranks'})
    fifth = fourth.find('table', {'class': 'BorderedTable RankTable Ranks--desktop'})
    sixth = fifth.find('tbody')
    # endregion

    team_name_list = ["", "", "", "", "", "", "", "", "", ""]
    return_list = ["", "", "", "", "", "", "", "", "", ""]
    team = sixth.find_all('tr', {'class': 'RankTable__row'})
    for i in range(len(team)):
        team_info = team[i].find('td', {'class': 'RankTable__name Gilroy'})
        team_name = team_info.find('span', {'class': 'hidden-in-mobile'})
        team_name_list[i] = team_name.text.strip()

    return team_name_list


SearchMatching("SP")
