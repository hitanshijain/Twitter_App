import botometer
consumer_key = 'XXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXX'
twitter_app_auth = {
                    'consumer_key': consumer_key,
                    'consumer_secret': consumer_secret,
                    'access_token': access_token,
                    'access_token_secret': access_token_secret
                   }
botometer_api_url = "https://botometer-pro.p.rapidapi.com"

bom = botometer.Botometer(
                wait_on_ratelimit = True,
                botometer_api_url='botometer-pro.p.rapidapi.com',
                rapidapi_key = 'e6a69c18acmshd6f3c48867ff26ap10d09cjsn6c8996a54d5f',
                **twitter_app_auth)
result = bom.check_account("hitanshijain27")
