from paralleldots import set_api_key,get_api_key
import tweepy
con067='2B6pHocLD1WCyDyfFLiuKqLis'
con_sc='g0wFoRQUJ9vCvQ1yPrUGjYJPkF0fdh7mbOLcFxbHYcLehyfTsW'
access_token='1011132698407026688-EghMoE3WnBv38tlLNTzczoAStZNTXv'
Access_Token_Secret='0PvAQsDxkA72jifmLtnpT7x0ZV77avNlzzpMdM1qtpYQ6'
auth=tweepy.OAuthHandler(con067,con_sc)
auth.set_access_token(access_token,Access_Token_Secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)
def menu():
    print("\n\t\t\t\t\t TwitterBot\n\n")
    print("\t\t\4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\tWELCOME TO OUR YOU Twitter Bot   \t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4\t\t\t\t\t\t\t\t\t\t\t\t\4\n")
    print("\t\t\4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4 \4\n")
    print("\t\n Choose your option form 1-to-6\n")
    print("\t1.Retrieve Tweets\n")
    print("\t2.Count the followers\n ")
    print("\t3.Determine the sentiment\n")
    print("\t4.Determine location,language and time zone.\n")

    print("\t5.Compare tweets \n")
    print("\t6. Analyze top usage \n")
    print("\t7. Tweet a message \n")
    print("\t 8. Exit \n")
    me = int(input())
    if (me == 1):
        retrieve()
		
	elif(me==2):
       followers()
    elif (me == 3):
        sentiment()
    elif (me == 4):
        loc()
    elif (me == 5):
        comp()
    elif(me==6):
        analyze()
    elif(me==7):
        mess()
    else :
        exit()
def retrieve():
    user=input("Enter any Hash Tag or Search:-")
    tweets = api.search(user, lang='en', count=10, tweet_mode="extended")

    for tweet in tweets:
        print("-----------------------")
        print(tweet.full_text)
    print("-----------------------")
def followers():
    us=input("Enter Any twitter id for Serch Number of follower:-")
    targets = [us]  # All your targets here
#@SahilGo52134462
    for target in targets:
        user = api.get_user(target)
        print(user.name, user.followers_count)
def loc():
    user_id=input("Enter ani id to see location:-")
    user=api.get_user(user_id)
    print("loction of user:-",user.location)
    print("Time Zone :-",user.time_zone)
    print("language:- :-", user.lang)
def sentiment():
    set_api_key()
def mess():
    user_id=input("Enter any id to send msg:-")
    msg=input("Enetr any msg:-")
    api.send_direct_message(user=user_id,text=msg)
menu()

	


	