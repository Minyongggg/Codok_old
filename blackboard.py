from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def crawling(bbid, bbpassword):
    option = Options()

    option.add_argument("--headless")
    option.add_argument("start-maximised")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--window-size=1920x1080")


    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

    wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(3)
    driver.get('https://kulms.korea.ac.kr/ultra/course')
    driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a').click()


    driver.find_element_by_name('one_id').send_keys(bbid)
    driver.find_element_by_name('user_password').send_keys(bbpassword+'\n')

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='base_tools']/bb-base-navigation-button[4]/div/li/a"))
        )

    ####################################################################

    driver.get('https://kulms.korea.ac.kr/ultra/course')

    driver.execute_script("window.scrollTo(0, 900);")

    lec_list = driver.find_elements_by_class_name("course-id")

    def data(lec_list):
        final_result = []
        for lec in lec_list:
            course_id = lec.text
            subnum = course_id[10:-2]+"-"+course_id[-2:]
            semester = course_id[0:6]

            if(semester == "20211R"):
                final_result.append(subnum)

        return final_result

    final_result = data(lec_list)

    return final_result

# a = 'naminyong97'
# b = "dlalsdyd1!"
# lectures = []

# crawling(a, b, lectures)

# # print(lectures)


