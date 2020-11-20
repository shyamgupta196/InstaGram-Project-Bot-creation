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
        sleep(6)
        
        '''this is basically the info buttons about 
        you want to save passwords or not 
        
        and whether you want to recieve the notifications or not 
        
        !!!warning this is case with chrome do have a check with other drivers too
        '''
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
        sleep(2)
        self.browser.find_element_by_xpath('//button[text()="Message"]').click()
        sleep(3)
        
        msg_search=self.browser.find_element_by_class_name("focus-visible")
        
        ##$$$ ENTER THE MESSAGE YOU WANT TO SEND IN THE SEND_KEYS METHOD BELOW
        
        msg_search.send_keys('this is a trial msg from bot')
        msg_search.send_keys(Keys.RETURN)


def main():
   '''
   this executes all the main commands of the program
   
   username n password should be placed in place of 
   
   ##your_username## , ##your_password## 
   
   '''  
    bot=insta_logger('your_username',"your_password")
    bot.login_in_func()
'''
    for iron man fans
'''
    bot.follow_button('robertdowneyjr')
'''
also if you want then to unfollow in the same run you can un comment this piece of code 
'''

    bot.unfollow('robertdowneyjr')
##$$$ ENTER THE MESSAGE YOU WANT TO SEND IN THE SEND_KEYS OF THE MESSENGER  FUNCTION OF THE CLASS 


#### inlist of people insert the ids of the people you  want to message
    
    for i in ['list of people']:
        bot.messenger(i)
        sleep(4)


main()
