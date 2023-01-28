import requests
#dasein 24794195
url = 'https://soz6.com/sds-sentbox.php?id=1080449'
vocaroo_url = 'https://upload1.vocaroo.com/apps/main-api/upload/62xq87ewqPLLegRipFBjWI/chunk/0'
header_data = {
	'authority': 'soz6.com',
	'method': 'GET',
	'path': '/sds-sentbox.php?id=1080449',
	'scheme': 'https',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'cache-control': 'max-age=0',
	'cookie': 'PHPSESSID=4l8r3o5la2lja475irr3lgoa9f; _ga=GA1.2.1260927010.1667205694; __gads=ID=06ecd78b3320f1bd-22e2cd365fce00da:T=1667205694:RT=1667205694:S=ALNI_MZW81b29XaHTRTGib32puUIbeRHsg; pid=24794195; postlar_k=hamisi; _gid=GA1.2.701683543.1673446055; username=dasein; user_id=24794195; auth=09db0d327b0222c041fc19560ce76ebbd9bb0cd7; __gpi=UID=00000b7a9924216a:T=1667205694:RT=1673549676:S=ALNI_MaBAYKe8Nwqb_SU_3dGaiNnemddnw; __cf_bm=jNM1BJ3RrzVbslWZkCMWj0YKgxDa7NP9HgWcjNK7o8I-1673553129-0-AR4FAJTDte+IIQCLf7TtUev8R0s/5y3v4nbYMuu14lkfhjRRh9c7DfssZowSSXgCjI1U4lPvIyltAjbo8EI0Nb4kRWBSkHRBjJNx7XtuJEXowRUHcZL8uDFKWXwR0td0p417tlxDHzjz0B78MJko/ww=; _gat=1',
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Linux"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}



vocaroo_data = {'chunk': 349382}
#use the 'headers' parameter to set the HTTP headers:
# x = requests.get(url, headers = header_data)


# print(x.text)
# f = open('result.html', 'w')
# f.write(x.text)
# f.close()

#the 'demopage.asp' prints all HTTP Headers

####################################################################################################

delete_id = 361228;
delete_url = 'https://soz6.com/sds-entrydel.php?id=%d' % delete_id
delete_data = {'entryid' : str(delete_id)}

username = 'grammarnazi'
user_id = 24796413
# 24798743 derek id

delete_header = {
	'authority': 'soz6.com',
	'method': 'POST',
	'path': '/sds-entrydel.php?id=%d' % delete_id,
	'scheme': 'https',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'cache-control': 'max-age=0',
	'content-length': '14',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'PHPSESSID=4l8r3o5la2lja475irr3lgoa9f; _ga=GA1.2.1260927010.1667205694; __gads=ID=06ecd78b3320f1bd-22e2cd365fce00da:T=1667205694:RT=1667205694:S=ALNI_MZW81b29XaHTRTGib32puUIbeRHsg; pid=24794195; postlar_k=hamisi; _gid=GA1.2.701683543.1673446055; username=%s; user_id=%d; auth=09db0d327b0222c041fc19560ce76ebbd9bb0cd7; __gpi=UID=00000b7a9924216a:T=1667205694:RT=1673549676:S=ALNI_MaBAYKe8Nwqb_SU_3dGaiNnemddnw; __cf_bm=KY90Pv6dGkp6IQVS6SVAzAkQm0.CnP6ovoZD6A_kvqM-1673554125-0-AfrMCheUPeW87+4EcAKqdx96FQg1zOlLop+32FjxESfWhAkooVyeX5Wi0DyrNB6hSzQ1d6RTiFSO/wvgAajbfDJATpWlkLTrvGPg+vbtFf0BHGCamyF5SeTlNYozREMFpUiDv4AgZ+x3gTWbTKW0Lmg=' % (username, user_id),
	'origin': 'https://soz6.com',
	'referer': 'https://soz6.com/sds-entrydel.php?id=%d' % delete_id,
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Linux"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-or,igin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

}

d = requests.post(delete_url, data=delete_data, headers = delete_header)


print(d.text)