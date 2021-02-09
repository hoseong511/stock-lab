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
        self.html_table = """
        <html>
            <div class="aside_section">
                <table class="tbl">
            </div>
        </html>"""
