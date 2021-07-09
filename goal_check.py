from bs4 import BeautifulSoup
from urllib.request import urlopen

def soccer():
    '''
    Parses page with soccer info
    '''
    text = 'SOCCER⚽️\n'
    html_text = urlopen('https://www.sfstats.net/soccer/')
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find_all('div', class_ = "item")[1]
    matches = table.find_all('tr', class_ = 'tsor1')
    for match in matches:
        text += '\n-----------------\n'
        stats = match.find_all('td')
        time = 'Time: ' + stats[0].text + '\n'
        result = stats[1].text + ' -> ' + stats[2].text + ' <- ' + stats[3].text + '\n'
        if stats[4].text == '-':
            odds = 'ODDS: -'
        else:
            odds = 'ODDS:\n\tFirst: ' + stats[4].text + '\n\tSecond: ' + stats[6].text + '\n\tDraw: ' + stats[5].text
        
        text += time + result + odds
    return text


def basketball():
    '''
    Parses page with basketball info
    '''
    text = 'BASKETBALL🏀\n'
    html_text = urlopen('https://www.sfstats.net/basketball/leagues/1_NBA')
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('tbody')
    games = table.find_all('tr')
    for game in games:
        if '@' in game.text:
            text += '\n-----------------\n'
            text += 'Date:' + game.text
        else:
            stats = game.find_all('td')
            result = stats[0].text + ' : ' + stats[1].text + '\n'
            if stats[2].text == '-':
                odds = 'ODDS: -'
            else:
                odds = 'ODDS:\n\tFirst: ' + stats[2].text + '\n\tSecond: ' + stats[3].text + '\n\tDraw: ' + stats[4].text
            
            text += result + odds
    return text
