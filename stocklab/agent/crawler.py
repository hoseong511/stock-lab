from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self):
        self.html_doc = """
                        <html>
                            <head>
                                <title>Home</title>
                            </head>
                            <body>
                                <div class="section">
                                    <h2>영역제목</h2>
                                    <ul>
                                        <li><a href="/news/news1"> 기사 제목1</a></li>
                                        <li><a href="/news/news2"> 기사 제목2</a></li>
                                        <li><a href="/news/news3"> 기사 제목3</a></li>
                                    </ul>
                                </div>
                            </body>
                        </html>
                        """
        # 샘플 코드!
        self.html_table = """
                        <html>
                            <div class="aside_section">
                                <table class="tbl">
                                    <thead>
                                        <tr>
                                            <th scope="col">컬럼1</th>
                                            <th scope="col">컬럼2</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <th><a href="/asdie1">항목1</a></th>
                                            <td>항목2값1</td>
                                            <td>항목2값2</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </html>"""
    def get_news_section(self):
        soup = BeautifulSoup(self.html_doc, 'html.parser')
        print(soup.prettify())
        print("title", soup.title)
        #<title>Home</title>
        print("title string", soup.title.string)
        #Home
        print("title parent name", soup.title.parent.name)
        #head
        print("div", soup.div)
        """
            <div class="section">
                <h2>영역제목</h2>
                <ul>
                    <li><a href="/news/news1"> 기사 제목1</a></li>
                    <li><a href="/news/news2"> 기사 제목2</a></li>
                    <li><a href="/news/news3"> 기사 제목3</a></li>
                </ul>
            </div>
        """
        print("div class", soup.div['class'])
        # ['section']
        print("li", soup.li)
        # <li><a href="/news/news1"> 기사 제목1</a></li>
        print("find li", soup.find_all('li'))
        # [<li><a href="/news/news1"> 기사 제목1</a></li>, <li><a href="/news/news2"> 기사 제목2</a></li>,
        #  <li><a href="/news/news3"> 기사 제목3</a></li>]
        print("find class section", soup.find_all(class_="setion"))
        # [ <div class="section">
        #                 <h2>영역제목</h2>
        #                 <ul>
        #                     <li><a href="/news/news1"> 기사 제목1</a></li>
        #                     <li><a href="/news/news2"> 기사 제목2</a></li>
        #                     <li><a href="/news/news3"> 기사 제목3</a></li>
        #                 </ul>
        #             </div> ]
        print("find href", soup.find_all(href=re.compile("/news")))
        # [<li><a href="/news/news1"> 기사 제목1</a></li>, <li><a href="/news/news2"> 기사 제목2</a></li>,
        #  <li><a href="/news/news3"> 기사 제목3</a></li>]
        news_list = soup.find_all(href=re.compile("/news"))
        for news in news_list:
            print(news["href"])
            print(news.string)
            """
            /news/news1
            기사제목1
            /news/news2
            기사제목2
            /news/news3
            기사제목3
            """

    def get_side(self):
        soup = BeautifulSoup(self.html_table, 'html.parser')
        print("table", soup.table)
        print("thead th", soup.thead.find_all(scope=re.compile("col")))
        # thead th [<th scope="col">컬럼1</th>, <th scope="col">컬럼2</th>]
        col_list = [ col.string for col in soup.thead.find_all(scope=re.compile("col")) ]
        print(col_list)
        #['컬럼1','컬럼2']
        tr_list = soup.tbody.find_all("tr")
        print("tr list", tr_list)

        for tr in tr_list:
            for td in tr.find_all("td"):
                print("tr dt", td.string)
        """
        tr td 항목1값1
        tr td 항목1값2
        tr td 항목2값1
        tr td 항목2값2
        """

if __name__ == "__main__":
    crawler = Crawler()
    crawler.get_news_section()
    crawler.get_side()


