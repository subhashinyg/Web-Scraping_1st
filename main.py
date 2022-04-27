from bs4 import BeautifulSoup

with open('home.html', 'r')as html_file:
    content=html_file.read()
    #print(content)

    soup=BeautifulSoup(content, 'lxml')
    # print(soup.prettify()) ...............disply the html file
    # for grap some specific information from a html
    #tag = soup.find('h4') # find method search for the 1st element the stop the execution to find all the h4 tage use find_all method
    # h4_tag = soup.find_all('h4')
    # print(h4_tag)
    # for tag in h4_tag():
    #     print(tag.text)

    #......finding div class with character fluid

    product = soup.find_all('div', class_='card') # class_ her use _ because it is a build in keyword
    #print(product)
    for cake in product:
        #print(cake.h4)
        product_name = cake.h4.text
        product_descption = cake.p.text


        print(product_name)
        print(product_descption)