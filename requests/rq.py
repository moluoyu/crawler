import requests

headers = {
    'Cookie': '_ga=GA1.2.1327816022.1553740125; _octo=GH1.1.378491643.1553740135; _device_id=4e1a7e1ccec6925b184f7f9a2fe1b46b; user_session=PJMnffggySVAZntu0LWNqWdcKiUYUngvZebVAn8qCx_DvkzH; __Host-user_session_same_site=PJMnffggySVAZntu0LWNqWdcKiUYUngvZebVAn8qCx_DvkzH; logged_in=yes; dotcom_user=moluoyu; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=oywnsmptqU%2Fj2Zq8l1wfUAagzp9PUD7bkXrd1TpCaTSZOT4QhQu05qUGfBBUkZkWCtM0T8aEz%2BJOzr%2Fh3uekLG3izU171cjVtjjhmZukpU9rjiGv78bTXEv%2Fm%2Fh%2BU8Z6vOUYg7csEIXU%2Fujl0whASZTMUci9dwLaedOz3%2Fy4lbgyQFU5pWjCFX9nV9W%2BDNOWyg7fq0jT19tKv2sgJRtZllTrOsg6TxkXTyzNFedMVbEfeCirn%2BjHlePNcl2WUu3dYCjjBaZWBzLbbhzr55n7ubEEyr7BnqroSrz%2BaqKzsufwSKlvRmn90YPFKz0iW2RxD6pTMsV0%2BG6Amo9GWwbrhS6NxMUwgWaOmi9mtHbeK1CGievHY%2BpKDVSZdDpGT0YTPJELRsASBfdv7CgBR5y%2Fpoqju0RwS9tDstFuhF8km4D1chbzbu3xeMFMJNuJC%2BAgIDs3HQgyAbAesgrTSteXPwlN164WOk3jlPg0E91W19O1MSf2BF13H76t68VrcckkzvVFga5tHFO1NpqqFrIfDtgGqVGaMnjJHbmrsnMzqyQOCF00JCQEm%2BtTIaAgd66VhtmkOAe%2FS0u7iZPfVseSFdmV00vAVAmO7wm%2B3AOGhDkpM7gSP9%2FJvHmiUqhK7IuhezWZTmkw5kaNI6RZm22n0GD3F3wO6nZtPU8liWg85cFrWAmYRWPhFbOELeTYXaNYWu%2FnaZawH%2Fu81e0DlQJjiEZgNVRVGHtpgaUUFGaRyB9ag6xSj7sENOAGOPRTE978CSsGUYs%2FZmVgbc1UZhyyidc04rem1qEhrq3Eh1tycvIUTQRo%2Fc6HTgV%2F89Ul%2B3LBLTBBo6mx%2BJeNJAynuali%2F1vfHdQK%2Bmoiugf4kYeZmSOx2l40updb1rTZQN%2BmcptWKn57yXdn0hS6iMnzoUoO%2FHs1Pt2WjbFjdR24lxxAL083llLsUafr65LhLUPb1Ndl5bLc3BDt2jyjDqIqrs08VYJb8L61T30u%2F9kAT2PmrlzAkP4gEF38dI%2BWh%2FWLRBEtFePdHob5n%2F94ZJvhua7hnAsGy%2BoyrXZ0z0hNbdgXyw9w6fgPJ8V6TCnuWw1zNLmyUhpmA0LFCGjW2feFqQ1Cl0tljN2paUdz7qSr2FzRhQROzCHts92eF8P6dFW6JjN33hEqI5jTZhSn4it2YgrPvwNU5bORJsaod7XdS5Rl8vq%2F760rAXK7T9PeFiHL5c0R4eXld8IEzaG3usoyuUVRR3eUYEVVoxkP89Us9m2Z%2FhNvIUySFyRr7Dj2iDYuRVJf%2FVv2%2BxPjyDoTdcPWm8%2Bfis83LA9IAQNpxfCPlJCPG%2BeIsV3W9XTTNluAJ5xy%2FvOwjen7OOr76i6WfUQrbaFKCsvh5Ho8palDEsmrdRnsxIgdVlZAmSXKQN9u6FX9FiwZlbXM8Ud3lh7BAkPSdTGo3fGYlLRx6MQHEBkwwe6Mo%2FGKlyu%2BuqV4ybrBOyrfnFkJtRMGLEvEn%2FYUsosfvjPKUhe%2FjohCUIFUROMBlWxXd1BDGjl8kRktkZi50CClD%2FSwzxK9Qo6uPeztvs6DNacmCFI4eWJ4w3cAqztXDmhazCGUcJ%2F19cD6Cch7cDMpDXzza1PyJ30X4xXFbgfiaTK%2BmacTCoMKz4el1ZZoUqivcpLhNsBvXWmDc3v7F3QRhxYR7I6AFGmHOXMot5PRZCgsy9H2P1emcnoC%2FrijBfuTwnP4WJAfTjewoGQstx2SEVeZfXiMrIi7hq%2Fzx43mU2bYbFpzIOmQkE1rwTWL6zhOtTUfsTODRm8PqJjsZ%2BOm0fPpR196kQgKnyz9gnVMBG2x1Sxl4AF7Wh2K2DbJiLNO909lfVolz%2Bt3655%2BaROAXKsqPS%2FZwX2AXCotuDbp4kZWV888FAupE6xpP0D1RhrYJvdXROTqF7eFTqkL3sjNn56m6gLWv58yQFrHsNh6If6z4ViSXZINUo7e7dkrIuy85Fjp0cTUKi8IGjE187dopATDLimG7oxQIdHrEEHueBI94oO9etOWtl9Ik0MsB%2FdGfI6Im8ryHmUCM%2BuxiRK6LBU0BGGl8Yppl%2BV7Fs12oqmCub%2Fmc%2F%2BBFyJgmYLkWd0VCWNHfpEYcs%2BDHika0jTy2%2FQKCZH4FM4vj0MzvCANiAoPWChH3X3qDHC57JNoiaCkauhZdmsFiaSPV%2FYwpBnMizA7oBm9R7hygFXF%2BdSTCgRvDzwp2N8%3D--kCI5nrB%2FLz%2FYGMp0--82gtIHGdWRj8voQWD1nk0g%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://github.com/', headers=headers)
print(r.text)
with open('1.html', 'wt') as f:
    f.write(r.text)


