url = "http://naver.com"
site=url.replace("http://","")
site = site[:site.find(".")]
password = site[:3]+str(len(site))+str(site.count("e"))+"!"
print(password)

