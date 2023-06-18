from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

result = requests.get('https://auto.ria.com/uk/search/?&region.id[0]=10&city.id[0]=10&categories.main.id=1&abroad.not=0&custom.not=1')


soup = BeautifulSoup(result.text,'html.parser')


for i in range(10):
    name = soup.find('span',{'class':'blue bold'}).next_element
print(name)







# # def show_info(request,type_city,city):
#     url = f'https://ua.sinoptik.ua/погода-{type_city}/2023-05-27'
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, 'html.parser')

#     mini = soup.find('div', {'class': 'min'})
#     max = soup.find('div', {'class': 'max'})

#     context = {
#         'city':city,
#         'type_city':type_city,
#         'min_temp': mini.text.strip(),
#         'max_temp': max.text.strip(),
#     }

#     return render(request, 'app/info.html', context)
