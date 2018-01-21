import requests

class Discord:

    def initiate(self, url):

        discordUrl = url + '/slack'
        payload = {
            "attachments": [{
                "fallback": "Update message for the Crypto monitor.",
                "color": "#2AA198",
                "author_name": "Coinbase-Monitor",
                "author_icon": "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png",
                "text": "Price monitor started.",
                "footer": "Price Monitor",
                "footer_icon": "https://www.coinbase.com/assets/logos/logo@2x-facc8a78d7aa50ec2df3f7b1dd646105ccfc29991397499cd26f5aa8c781a9bb.png"
            }]
        }
        r = requests.post(discordUrl, json=payload, headers={'content-type':'application/json'})
        if r.status_code != 200:
            return 'error initializing discord'

    def sendMessage(self, url, name, price, change):

        discordUrl = url + '/slack'
        payload = {
            "attachments": [{
                "fallback": "Update message for the Crypto monitor.",
                "color": "#2AA198",
                "author_name": "Coinbase-Monitor",
                "author_icon": "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png",
                "text": "%s is below your target price to buy" % name,
                "fields": [{
                    "title": "%s" % name,
                    "value": "%s" % price,
                    "short": True
                }, {
                    "title": "Hourly Change",
                    "value": "%s" % change,
                    "short": True
                }],
                "footer": "Price Monitor",
                "footer_icon": "https://www.coinbase.com/assets/logos/logo@2x-facc8a78d7aa50ec2df3f7b1dd646105ccfc29991397499cd26f5aa8c781a9bb.png"
            }]
        }
        discHeaders = { 'content-type': 'application/json' }
        r = requests.post(discordUrl, json=payload, headers=discHeaders)
        if (r.status_code != 200):
            return r.text
        return 'Successfully sent Discord alert update for %s' % name
