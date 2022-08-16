from InternetSpeedTwitterBot_Class import InternetSpeedTwitterBot

your_google_email = 'your@email.here'
your_google_password = 'your_password_here'

bot_net = InternetSpeedTwitterBot()
up_down = bot_net.get_internet_speed()
bot_twitter = InternetSpeedTwitterBot()
bot_twitter.tweet_results(your_google_email, your_google_password, up_down[0], up_down[1])
