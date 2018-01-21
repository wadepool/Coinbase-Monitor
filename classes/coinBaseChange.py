import os
from colorama import *

if os.name == 'nt':
	init()

from classes.Discord import Discord
Discord = Discord()

class Change:

	def change(self, Crypto, currentPrice, hourlyChange):
		if hourlyChange < 0.0:
			return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL,  currentPrice, Style.BRIGHT, Fore.RED, hourlyChange, Style.RESET_ALL)

		if hourlyChange > 0.0:
			return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s+%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL, currentPrice, Style.BRIGHT, Fore.GREEN, hourlyChange, Style.RESET_ALL)

	def alertChange(self, Crypto, currentPrice, hourlyChange, config):

		alertUrl	= config['Discord']['Webhook']
		targetPrice = config['Discord']['Target']
		AlertMe		= config['Discord']['Alert']

		if AlertMe == "True":
			if float(currentPrice) < targetPrice:
				Discord.sendMessage(alertUrl, Crypto, currentPrice, hourlyChange)

			if hourlyChange < 0.0:
				return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL,  currentPrice, Style.BRIGHT, Fore.RED, hourlyChange, Style.RESET_ALL)

			if hourlyChange > 0.0:
				return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s+%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL, currentPrice, Style.BRIGHT, Fore.GREEN, hourlyChange, Style.RESET_ALL)

		else:
			if hourlyChange < 0.0:
				return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL,  currentPrice, Style.BRIGHT, Fore.RED, hourlyChange, Style.RESET_ALL)

			if hourlyChange > 0.0:
				return "%s%s%s%s Current Price: %10s | Hourly Change: %s%s+%f%s" % (Style.BRIGHT, Fore.CYAN, Crypto, Style.RESET_ALL, currentPrice, Style.BRIGHT, Fore.GREEN, hourlyChange, Style.RESET_ALL)
