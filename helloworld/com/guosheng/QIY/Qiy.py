from selenium import webdriver
import time


class Aye:
    def __init__(self):
        self.start_url = "https://list.iqiyi.com/www/1/----------2---11-{}-1-iqiyi--.html"
        self.driver = webdriver.PhantomJS()
        self.flag = True
        pass

    def get_contList(self,x):
        li_list = self.driver.find_elements_by_xpath("//li[@class = 'qy-mod-li']")
        content_list = []
        #ele = self.driver.find_element_by_css_selector("[class = 'page a1']")
        ele = self.driver.find_elements_by_css_selector("[class = 'page a1 noPage']")
        print("第{}页".format(x),"noPage标签个数{}".format(len(ele)))
        if x>1 and len(ele)>=1:
            print("最后一页了")
            self.flag = False
        #page a1 noPage
        for li in li_list:
            item = {}
            item["name"] = li.find_element_by_xpath(".//div[@class='title-wrap']/p/a").get_attribute("title")
            # item["room"] = li.find_element_by_xpath(".//h3").get_attribute("title")
            # item["hot"] = li.find_elements_by_xpath(".//div[@class='DyListCover-info']")[1].find_element_by_xpath(
            #     "./span").text
            content_list.append(item)
            # print(li.get_attribute("class"))
            # time.sleep(1)
       # next_url = self.driver.find_elements_by_xpath("")
        #next_url = next_url[0] if len(next_url) > 0 else None
        return content_list
    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        # 3.提取数据，提取下一页的元素
        i = 1
        while self.flag:
            url = self.start_url.format(i);
            self.driver.get(url)
            content_list = self.get_contList(i)
            print(content_list)
            i = i+1
            # print(len(content_list))
        # list_url = [self.start_url.format(i) for i in range(1,10)]


        # 4.保存数据
        # 5.循环下一页
        pass


if __name__ == '__main__':
    douyu = Aye()
    douyu.run()
