from github import Github,Auth
from github.Repository import Repository
from typing import List
import requests
import os, json, datetime, re,sys
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv
load_dotenv()



auth = Auth.Token(os.environ.get('GH_KEY', 'default'))
g = Github(auth=auth)



def getGithubPinned(username: str)-> List[str]:
    repos = []
    today = datetime.datetime.now()
    day_1 = today.replace(day=1)
    start_date, end_date  = day_1.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")
    
    url = f"https://github.com/{username}?tab=overview&from={start_date}&to={end_date}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pinned_items = soup.find_all('div', class_='pinned-item-list-item-content')
        
        repos = []
        for item in pinned_items:
            repo_name = item.find('span', class_='repo').text.strip()
            repos.append(repo_name)
    else:
        print(f"Failed to get pinned repos for {username}")
        
    return repos




def get_repositories(username: str)->List[Repository]:
    user = g.get_user(username)
    all_repos = [repo for repo in user.get_repos()]
    repo_dict = {repo.name: repo for repo in all_repos}
    pinned_repo_names = getGithubPinned(username)
    pinned_repos = []
    for name in pinned_repo_names:
        if name in repo_dict:
            pinned_repos.append(repo_dict.pop(name))
    sorted_repos = sorted(repo_dict.values(), key=lambda x: x.stargazers_count, reverse=True)
    final_repo_list = pinned_repos + sorted_repos

    return final_repo_list

