import re, pexpect, time

SUCCESS = 0
file = open("decrypted_password.csv")
data_lines = file.readlines()
file.close()


def get_domain(site_url: str) -> str | None:
    match = re.search(r"(?<=\/\/)[\w\.\-\d\:]+(?=\/)", site_url)
    if match:
        return match.group()
    else:
        return None


def pass_del_pw(pass_name):
    command = f"pass rm {pass_name}"
    child = pexpect.spawn(command)
    child.sendline("y")
    print("Password removed successfully")
    child.close()


def pass_insert_pw(password, site_domain):
    ''' Problems occured:
        1. Didn't use expect method to find exact string 
        2. Didn't wait long enough, therefoure sent second password 
        too early pass've been waiting for second password which'll never
        come
        
        Use expect and time.sleep
    '''
    command = f"pass insert {site_domain}"
    print(command)
    global child
    child = pexpect.spawn(command)
    expected = ["Enter password", "Retype password"]
    for expec in expected:
        try:
            resp = child.expect(expec, timeout=1)
        except:
            return
        if resp == SUCCESS:
            print("Sended password")
            child.sendline(password)
    print(child.isalive())
    time.sleep(0.3)
    child.close()


domains = [
    "www.alditalk-kundenbetreuung.de",
    "www.bath.ac.uk",
    "www.codewars.com",
    "www.deepl.com",
    "www.epicgames.com",
    "www.fastly.com",
    "www.hoyolab.com",
    "www.instagram.com",
    "www.mangalove.site",
    "www.michaelpage.de",
    "www.namecheap.com",
    "www.oed.com",
    "www.oreilly.com",
    "www.upwork.com",
    "www.wg-gesucht.de",
    "www.workwise.io",
]


def move_www(site_domain):
    domain = re.search(r"(?<=www.)[\w\.\-\d\:]+", site_domain).group()
    command = f"pass mv {site_domain} www/{domain}"
    print(command)
    child = pexpect.spawn(command)
    time.sleep(0.3)
    child.close()


def get_collumns(row):
    splited_line = row.split(",")
    username = splited_line[2]
    password = splited_line[3]
    site_url = splited_line[1]
    return username, password, site_url

def main():
    for line in data_lines:
        line = line.strip()
        username, password, site_url = get_collumns(line)
        site_domain = get_domain(site_url)
        if not site_domain:
            continue
        print(username, site_domain, password)
        pass_insert_pw(password, site_domain)

if __name__ == "__main__":
    for domain in domains:
        move_www(domain)
