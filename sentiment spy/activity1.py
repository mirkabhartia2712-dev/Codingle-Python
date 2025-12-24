import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print (f"{Fore.CYAN}🎉👏🤠 Welcome to Sentiment Spy!🤠{Style.RESET_ALL}")

user_name=input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()
if not user_name:

    user_name="cowboy cuz u didnt give a name"

conversation_history=[]

print (f"\n{Fore.CYAN}Hello, Agent {user_name}🤠.")
print(f"Type a sentance and I will analyse it with TextBlob to show you the sentiment.🤠🕵️‍♀️")
print (f"Type{Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW} 'history' {Fore.CYAN},{Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:

    user_input=(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
