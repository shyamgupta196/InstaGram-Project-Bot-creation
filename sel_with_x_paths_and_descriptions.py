from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import threading
from selenium.webdriver.common.action_chains import ActionChains as ac


class insta_logger():
    '''
    sets the driver and opens up the chrome;;;
    then it takes the username and password from the user and helps him log in 
    using the logger function
    '''
    
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password
        
    def login_in_func(self):

        self.browser.maximize_window();
        self.browser.get("https://instagram.com")
        sleep(2)


        login_key=self.browser.find_element_by_xpath('//input[@name="username"]')
        login_pass=self.browser.find_elements_by_css_selector('form input')[1]
        login_key.send_keys(self.username)
        login_pass.send_keys(self.password)
        login_pass.send_keys(Keys.ENTER)
        sleep(6)        # self.browser.fullscreen_window()
        
        # threading.Thread.start(logger)
        self.browser.find_element_by_xpath("//button[text()='Not Now']").click()
        '''
        you can use either tag method or xpath method 
        
        also either click() or send_keys(Keys.ENTER) can be used
        '''
        sleep(5)

        self.browser.find_element_by_xpath('//button[text()="Not Now"]').send_keys(Keys.ENTER)
        
        sleep(5)
        
    def follow_button(self,username_foll):
        ''' goes to a address and follows the 
                account'''
        self.browser.get("https://instagram.com/"+username_foll+'/')
        
        button_validator=self.browser.find_element_by_xpath('//button[text()="Follow"]')
        button_validator.click()
        if not button_validator:
            print("you are following this person")



    def unfollow(self,username):
        ''' 
        searches for button element with index and 
                completely unfollows the person
        '''
        self.browser.get("https://instagram.com/"+username+'/')
        
        try:
            self.browser.find_element_by_class_name('glyphsSpriteFriend_Follow u-__7').click()
            sleep(2)
            self.browser.find_elements_by_tag_name('button')[-2].send_keys(Keys.ENTER)
        except Exception:
            sleep(2)
            pass
        finally:
            sleep(1)


    def messenger(self,username):
        '''
        this sends messages to username provided automatically
        by using previous logger functions
        and makes the task possible
        '''
        self.browser.get('https:/instagram.com/'+username+'/')
        self.browser.find_element_by_xpath('//button[text()="Message"]').click()
        sleep(4)
        
        msg_search=self.browser.find_element_by_class_name("focus-visible")
        msg_search.send_keys('sorry but this process of experiment will go on for sometime ')
        msg_search.send_keys(Keys.RETURN)
        
        
    def liker(self,username,class_name):
        sleep(3)
        self.browser.get("https://instagram.com/"+username+'/')
        posts=self.browser.find_element_by_class_name(class_name)
        ac.send_keys(Keys.ARROW_DOWN).perform()
        # try: 
        #     # element = self.browser.find_element_by_class_name(class_name)
        #     for post in range(int(posts.text)):
        #         article=self.browser.find_element_by_tag_name('article')
        #         # article.find_element_by_xpath
                # self.browser.find_elements_by_class_name('wpO6b').click()[1]
                # sleep(2)
                # self.browser.find_elements_by_class_name('wpO6b').click()[-1]

        # except AttributeError as e:
        #     print(e)


bot=insta_logger('_shyamgupta','shyaminsta')
bot.login_in_func()

bot.liker('_shyamgupta','g47SY')







# bot.liker('_shyamgupta')
# bot.follow_button('robertdowneyjr')

# bot.unfollow('robertdowneyjr')
# for i in ['ishwarya_10','saakshi_reddy11']:
#     bot.messenger(i)
#     sleep(4)
    # continue
# session=ip('_shyamgupta','shyaminsta')
# session.login()
# session.like_by_tags(["fashion",'singing'], amount=1)
# session.set_dont_like(['porn','nude','boobs','bf'])

'''
if statements and custom inputs has to be used
then only it will be fully customisable


instapy still not used in the program its full selenium
'''


