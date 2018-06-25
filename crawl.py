import requests
from bs4 import BeautifulSoup

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "piro.settings"
                      )
django.setup()
from graph.models import Member, Contrib


def update_data(mem_list=None):
    if not mem_list:
        mem_list = Member.objects.filter()
    url = "https://github.com/users/{user_name}/contributions"

    levels = {
        '#ebedf0': 0,
        '#c6e48b': 1,
        '#7bc96f': 2,
        '#239a3b': 3,
        '#196127': 4,
    }

    for member in mem_list:
        user_url = url.format(user_name=member.git_user_name)
        req = requests.get(user_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        tags = soup.find_all("rect")
        index = 1
        contrib_list = []
        while index < len(tags):
            contrib = tags[-index]
            contrib_level = levels.get(contrib.get('fill'))
            contrib_date = contrib.get('data-date')
            print(contrib_date, contrib_level)

            if not Contrib.objects.filter(
                    member=member,
                    date=contrib_date).exists():
                contrib = Contrib(member=member, date=contrib_date, level=contrib_level)
                contrib_list.append(contrib)
                index += 1

            else:
                break
        if contrib_list:
            Contrib.objects.bulk_create(contrib_list)


if __name__ == '__main__':
    update_data()
