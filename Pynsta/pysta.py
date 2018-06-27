import re
import time
from io import BytesIO
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image

URL = "https://www.instagram.com/"

headless = webdriver.ChromeOptions()
headless.add_argument('headless')

DRIVER = webdriver.Chrome(chrome_options=headless)

class Insta:

    DRIVER.get(URL)
    global user
    global secret

    @staticmethod
    def login(username, password):
        global user
        global secret
        user = username
        secret = password

        try:
            # below finds the login button in initial instagram page
            log = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/accounts/login/']")))
            log.click()
        except TimeoutException:
            pass


        try:
            # below finds textbox entry for username
            username_entry = WebDriverWait(DRIVER, 5).until(ec.presence_of_element_located((By.NAME, "username")))
            # below finds textbox entry for password
            password_entry = DRIVER.find_element_by_name("password")
            password_entry.send_keys(password, Keys.ARROW_DOWN)
            time.sleep(.05)
            username_entry.send_keys(username, Keys.ARROW_DOWN)
        except StaleElementReferenceException:
            time.sleep(.05)
            # below finds textbox entry for username
            username_entry = WebDriverWait(DRIVER, 5).until(ec.presence_of_element_located((By.NAME, "username")))
            # below finds textbox entry for password
            password_entry = DRIVER.find_element_by_name("password")
            password_entry.send_keys(password, Keys.ARROW_DOWN)
            time.sleep(.05)
            username_entry.send_keys(username, Keys.ARROW_DOWN)

        # below two lines finds the login button and then clicks on it
        login_button = DRIVER.find_element_by_css_selector("button._5f5mN.jIbKX.KUBKM.yZn4P")
        login_button.click()

        try:
            if WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.ID, "slfErrorAlert"))):
                text_error = DRIVER.find_element_by_id("slfErrorAlert").__getattribute__('text').split('.')
                raise ValueError (text_error[0] + '.')

        except TimeoutException:
            pass


    @staticmethod
    def to_profile():
        DRIVER.get(f'{URL}{user}/')


    def followings(self):
        self.to_profile()
        x = 0
        # Below finds the following subtag in the users profile page
        try:
            following_sub = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "following")))
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('button._5f5mN.-fzfL._6VtSN.yZn4P')
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        following_count = following_sub.__getattribute__('text')
        following_count = int(re.search(r'\d+', following_count).group())
        use_following_count = following_count/12
        following_sub.click()
        bottom = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.PdwC2.HYpXt')))
        actions = webdriver.ActionChains(DRIVER)
        actions.move_to_element(bottom)
        actions.click()
        while x < use_following_count:
            # When in doubt brute force it out? I'm pretty sure that the actual way to scroll to the bottom doesn't work on mac or at least not for popups.
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.perform()
            x += 1


    def get_followings(self):
        self.followings()
        followingzz = []
        following_list = DRIVER.find_elements_by_css_selector("a.FPmhX.notranslate.zsYNt")
        for x in following_list:
            followingzz.append(x.__getattribute__('text'))
        return followingzz


    def followers(self):
        self.to_profile()
        x = 0
        # finds the followers element on the users profile page
        try:
            followers_sub = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('button._5f5mN.-fzfL._6VtSN.yZn4P')
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")


        total_followers = followers_sub.__getattribute__('text')
        total_followers = int(re.search(r'\d+', total_followers).group())
        use_follower_total = total_followers/12

        followers_sub.click()
        # pop up window
        pop_up = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.PdwC2.HYpXt')))

        actions = webdriver.ActionChains(DRIVER)
        actions.move_to_element(pop_up)
        actions.click()

        while x < use_follower_total:
            # Same thing as in followings
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.send_keys(Keys.END)
            actions.perform()
            x += 1


    def get_followers(self):
        self.followers()
        followzz = []
        followings_list = DRIVER.find_elements_by_css_selector('a.FPmhX.notranslate.zsYNt')
        for x in followings_list:
            followzz.append(x.__getattribute__('text'))
        return followzz


    def follow_unfollow(self):
        z = 0
        followz = self.get_followers()
        followingz = self.get_followings()
        # Below finds all unfollow buttons in a scroll list.
        unfollow = DRIVER.find_elements_by_css_selector('button._5f5mN.-fzfL.KUBKM.yZn4P')
        for user in followingz:
            if user not in followz:
                yes_or_no = input("You follow Instagram user " + user.strip() + ", but they do not follow you back. Would you like to unfollow them?\n")
                pattern = re.compile(r'(ya|Ya|Yes|yes)')
                if pattern.search(yes_or_no):
                    unfollow[z].click()
                    print("You have unfollowed user" + user.strip())
                else:
                    print('You have not unfollowed user ' + user.strip() + ".\n")
            z += 1
        print("The list of people who don't follow you back has been cycled through.")


    def follow_unfollow_all(self):
        z = 0
        rude_people = []
        followz = self.get_followers()
        followingz = self.get_followings()
        # Below finds all unfollow buttons in a scroll list.
        unfollow = DRIVER.find_elements_by_css_selector('button._5f5mN.-fzfL.KUBKM.yZn4P')
        for user in followingz:
            if user not in followz:
                unfollow[z].click()
                rude_people.append(user)
            z += 1
        print(f'You have unfollowed {rude_people}')
        return rude_people


    def deny_all_follow_requests(self):
        self.to_profile()
        try:
            follow_requests = WebDriverWait(DRIVER, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a._0ZPOP.kIKUG.coreSpriteDesktopNavActivity")))
            follow_requests.click()
            WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR,'a.M_9ka'))).click()
        except StaleElementReferenceException:
            # finds the activity button
            follow_requests = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a._0ZPOP.kIKUG.coreSpriteDesktopNavActivity")))
            follow_requests.click()
            WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR,'a.M_9ka'))).click()
        except TimeoutException:
            try:
                #login button when you got users porifle page and you are not logged in due to flagging.
                DRIVER.find_element_by_css_selector('span.Szr5J')
                print("There are no pending follow requests to deny.")
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        for _ in DRIVER.find_elements_by_css_selector('button._5f5mN.-fzfL.KUBKM.yZn4P'):
            time.sleep(.5)
            try:
                WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
            except StaleElementReferenceException:
                WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
            except TimeoutException:
                pass
            try:
                DRIVER.find_element_by_css_selector('button._5f5mN.-fzfL.KUBKM.yZn4P')[0].click()
            except StaleElementReferenceException:
                DRIVER.find_element_by_css_selector('button._5f5mN.-fzfL.KUBKM.yZn4P')[0].click()

        print("All users requests to follow you have been denied.")


    def accept_all_follow_requests(self):
        self.to_profile()
        try:
            follow_requests = WebDriverWait(DRIVER, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a._0ZPOP.kIKUG.coreSpriteDesktopNavActivity")))
            follow_requests.click()
            WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
        except StaleElementReferenceException:
            # finds the activity button
            follow_requests = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a._0ZPOP.kIKUG.coreSpriteDesktopNavActivity")))
            follow_requests.click()
            WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('span.Szr5J')
                print("There are no pending follow requests to accept.")
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        for _ in DRIVER.find_elements_by_css_selector('button._5f5mN.jIbKX.KUBKM.yZn4P'):
            time.sleep(.5)
            try:
                WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
            except StaleElementReferenceException:
                WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.M_9ka'))).click()
            except TimeoutException:
                pass
            try:
                DRIVER.find_elements_by_css_selector('button._5f5mN.jIbKX.KUBKM.yZn4P')[0].click()
            except StaleElementReferenceException:
                DRIVER.find_elements_by_css_selector('button._5f5mN.jIbKX.KUBKM.yZn4P')[0].click()

    @staticmethod
    def get_user_images(name, number, location):
        count=1
        DRIVER.get(f'https://www.Instagram.com/{name}/')
        # finds images
        try:
            images = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.v1Nh3.kIKUG._bz0w')))
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('span.Szr5J')
                print(f'Instagram user {name} has no images to get.')
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        try:
            images.click()
        except WebDriverException:
            raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        time.sleep(1)
        while  count <= int(number):
            png = DRIVER.get_screenshot_as_png()
            im = Image.open(BytesIO(png))
            im = im.crop((40, 108, 425, 493))
            nombre = f'{name}image{count}.png'
            if location is None:
                im.save(nombre, 'png')
            else:
                im.save(f'{location}/{nombre}','png', optimize= True, quality = 100)
            count+=1
            try:
                DRIVER.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()
            except NoSuchElementException:
                break

            time.sleep(.5)


    @staticmethod
    def like_user_posts(name, number):
        count = 0
        DRIVER.get(f'https://www.Instagram.com/{name}/')
        # finds images
        try:
            images = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.v1Nh3.kIKUG._bz0w')))
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('span.Szr5J')
                print("The user has no posts to like.")
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")
        try:
            images.click()
        except WebDriverException:
            raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")
        while  count <= int(number):
            time.sleep(.5)
            if WebDriverWait(DRIVER,3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.fr66n.tiVCN'))).__getattribute__('text') == 'Like':
                DRIVER.find_element_by_css_selector('a.fr66n.tiVCN').click()
            try:
                # finds the arrow when you click on image page
                DRIVER.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()
            except NoSuchElementException:
                break
            count+=1


    @staticmethod
    def unlike_user_posts(name, number):
        count = 0
        DRIVER.get(f'https://www.Instagram.com/{name}/')
        # finds images
        try:
            images = WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.v1Nh3.kIKUG._bz0w')))
        except TimeoutException:
            try:
                DRIVER.find_element_by_css_selector('span.Szr5J')
                print("The user has no posts to unlike.")
                return
            except NoSuchElementException:
                raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")
        try:
            images.click()
        except WebDriverException:
            raise RuntimeError("If you are logged in and recieving this error, you'll need to manually log into Instagram as your account has been flagged for suspicious behavior.  Otherwise, you'll need to call the login function.")

        while count <= int(number):
            time.sleep(.5)
            if WebDriverWait(DRIVER, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.fr66n.tiVCN'))).__getattribute__('text') == 'Unlike':
                DRIVER.find_element_by_css_selector('a.fr66n.tiVCN').click()
            try:
                # finds the arrow when you click on image page
                DRIVER.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()
            except NoSuchElementException:
                break
            count += 1

Insta = Insta()


