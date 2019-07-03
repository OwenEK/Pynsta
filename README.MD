## Pynsta is currently out of order due to changes in XPATHs on Instagrams Website.  This will be fixed eventually.


Welcome to Pynsta, a python module for doing cool things with websites.  Below you will find all of the information necessary for working with Pynsta.


## How to get started:
### In order to get started, type the three following commands into terminal in order to download selenium and pillow, two modules which are necessary for Pynsta to function, and of course Pynsta itself:
> pip install selenium

> pip install Pillow

> pip install pynsta
### Additionally, in order for Pynsta to operate, you will also need to install the ChromeDriver.
In order to do so goto [this page](https://chromedriver.storage.googleapis.com/index.html?path=2.40/) and download  the correct Driver for your operating system.

# Documentation:
Currently Pynsta can only be used with Instagram, but doing similar things with other sites is planned for the future.
## Instagram:

### The first step to working with Pynsta is to import the Instagram class from Pynsta.  In order to do so, write the following:

> from pynsta.pysta import Insta 
### After doing so, in order for any of Pynstas Instagrams functions to work, you must also login.  To do so type:
> Insta.login('yourusername', 'yourpassword')

### After doing both of the two above steps, you are now able to delve into Pynsta's current Instagram capabilities.

**If you want to bring the headless ChromeDriver back to the logged-in user's profile, type**
> Insta.to_profile()

**If you want to fully expand the dropdown that contains all of the logged-in user's followings, type**
> Insta.followings()

**If you want to utilize an array that contains all of the logged-in user's followings, type**
> Insta.get_followings()

**which will return an array with all of a users followings**

##

**If you want to fully expand the dropdown that contains all of the logged-in user's followers, type**
> Insta.followers()

**If you want to utilize an array that contains all of the logged-in user's followers, type**
> Insta.get_followers()

**which will return an array with all of a users followers**

##

**If you want to optionally unfollow users who don't follow you back, type**
> Insta.follow_unfollow()

**This will prompt you in console to decide whether or not you wish to unfollow a user who does not follow you back until the list of all users who don't follow you back has been cycled through.  Answers yes, Yes, ya or Ya will work for unfollowing the user, otherwise the user will stay followed.**
##
**If you want to unfollow every user that doesn't follow you back, type**
> Insta.follow_unfollow_all()

**If you want to deny all requests to follow you, type**
> Insta.deny_all_follow_requests()

**If you want to accept all requests to follow you, type**
> Insta.accept_all_follow_requests()

**If you want to get all of a user's images who: either you follow or has a public account, type**
> Insta.get_user_images('name_of_user', 'number_of_images', 'where_you_want_saved')

For the command to get a user's images, if there is a video, it will also count as an image(IE: the shown part of the video prior to it being played will be gotten).  Also, the number of images will go from 1-x, where x is the number you entered.  Be aware, large image quantities will cause this command to take a long time.  Finally, if you want the images to be saved to whatever directory you have open type None.  If the number of images you request is greater than their number of posts, the program will still operate and get the maximum amount of images.  If ran through terminal, the images will be saved in preview on mac.  To easily find the images, type the name of the user into finder as the images are named "{name_of_user}image{x}.png"

**If you want to like a user's posts, with the user being either someone you follow or someone with a public account, in bulk, type**
> Insta.like_user_posts('username', 'number_of_posts')

Much like the get_user_images command, this will go from post 1-x, where x is the chosen number.  Another thing similar to the get_user_images is that if the inputted number of posts to like is greater than the number of posts on the account, the program will like the maximum amount possible and then simply progress.

**Finally, if you want to unlike all of a users posts that you had previously liked, type**
> Instagram.unlike_user_posts('username', 'number_of_posts')

unlike_user_posts operates in the same manner that like_user_posts, except instead of liking posts it unlikes them if they had previously been liked by you.


## Still confused by how it works?
### Below is an example of some code to help you get a better idea of how it works!

> from pynsta.pysta import Insta

> Insta.login('username', 'hunter2')

> Insta.get_followings()

> Insta.like_user_posts('github', '50')


