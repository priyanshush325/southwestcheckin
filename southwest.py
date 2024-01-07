import requests
import json
from playwright.sync_api import sync_playwright


def cookieGenerator():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://mobile.southwest.com/check-in")
        # page.get_by_text("Retrieve Reservation").click()
        # page.on("request", lambda request: print(request.headers))
        allCookies = context.cookies()
        # print(context)
        # print(context.cookies())
        # neededCookies = []
        # cookie1 = next(item for item in allCookies if item["name"] == "swa_FPID")
        # cookie2 = next(item for item in allCookies if item["name"] == "_up")
        # cookie3 = next(item for item in allCookies if item["name"] == "PIM-SESSION-ID")
        # cookie4 = next(item for item in allCookies if item["name"] == "_cc")
        # cookie5 = next(item for item in allCookies if item["name"] == "_cid_cc")
        cookie6 = next(item for item in allCookies if item["name"] == "sRpK8nqm_sc")
    
        # neededCookies.append(cookie1)
        # neededCookies.append(cookie2)
        # neededCookies.append(cookie3)
        # neededCookies.append(cookie4)
        # neededCookies.append(cookie5)
        # neededCookies.append(cookie6)


        # cookieString = ""
        # for cookie in neededCookies:
        #     cookieString = cookieString + cookie["name"] + "=" + cookie["value"] + "; "

        # return cookieString[:-2]
        cookieString = cookie6["name"] + "=" + cookie6["value"];
        return cookieString

def executeCheckIn(firstName, lastName, confirmation):
    url = "https://mobile.southwest.com/api/mobile-air-operations/v1/mobile-air-operations/page/check-in/" + str(confirmation)
    cookie = cookieGenerator()

    payload = json.dumps({
    "firstName": firstName,
    "lastName": lastName,
    "recordLocator": str(confirmation)
    })
    headers = {
    'content-type': 'application/json',
    'ee30zvqlwf-a': '6Sxcv94oXjwRTWBpjATEPH2LiO37p4P-GZUVelQO3=PKtWolGezhMGul86h_KwEI8wKM44z_K6xH7CFEmOIRVyz-ZtsCk=hDYeL_r2s2dv-eo0v85Ch31sxwYtJqc2kH1ybEqJ5ClaGWBjxWR3kUNNQP7UQ6yxuBycoaPy1Na34PZLrvLpWTyJpUdoSWxJiP9m=F0Qe33IOdt-LwZWnUv7piJ_Mn=Ml_0o8D-g7vmE-cA5vMmrq7hh01hW9jTK1FxjDVu2=xrVluGUrQR=VktxFdx9VmkndU7MrDWwW0QDpm=IzQ8MbFkzuBcRIB6LchNMU06nIBIrGc5HdxWMIHd2ZJLcEkAKPIekd7nAOK1PFSV2C_8ge72mvrCBdnLeN6i27u64mFIySiTSMWNc-rAtrWyKlGaswikekFNQV=5TmFFXv=6t1KICpHXh00BjFydboWKP5MuQYAAEo-byPE-mh=GHkXsO4K=zx12tbl-oW8tEaUklN4etpsej6BjQrJBxAiIx5sOFYttAho3nWahrQq3BeXBOEvRcMYa5GQpSKb4WlKvrkNe0ODAAM=0VGORv290Vvh6ibiZkYrEn9IBjAWYS8Tp0eFjTknNxtWUzJAAIDjeDZga-6MRPqU7H3gma3rxZ1A3ztIrc___SRc1N=I02vGCFke1p0s4osNCT9Dn42LbLismEIlQSMbUoeeFPvBeDJ_FeqiDaUtv_BPL0m4WH9mWJwJIVU2nFhBnpapYL5V9PEVrVopk=xrEVoWNxXkSVL21Swr82NLkxd-n0nWLq0lKEuo37obB4BdvRFZFsysZuhwhNYz9h4XZkDGjHU6d7b1=qNp0GqIQJA9q5LSVVMxE9McBhUBFlTI3xRunuuKdHeMFab4T_nv8Yi0hpkaFY9KLMSLwSjWcnQ5_a-VepagAuBdTdwRv0rjCzoUKdh-pmuVW8993irDe5SaxlhRCPP8O7LzAAbj_lwtCaxHbEdBGzGaxanBWL6=rwAoMsQzpD84mkINyd-_z2Br5h8mQ65mStQGTI-HBdaO4N_WIexrJL=qJXQP1GoUA6SnZ4XKc9a8SK7cqkqOzqQQdyUZ4PVKIc72bygQLT-_3BemVNcwEh_N_xN5TKmHhHiaADs2_Q6R0XO-SA3aOYnA_D-s3bPh2IuTp9EN9-oTnz6eqkl71ACy4uRVpOJyxTdlNnhwVZB-8-8i9ja7PArHubiJY2U4CrXZs7RAY1HgFW4iYR_zH_M_JS7CKh1tSCIEJTN4Bz0ejAUnHYpSlsuZesn8u2pNRtD0KNuXkbzv9OYIEpPtig_L8k_rW13Fb5B48FSOyNeyZqYo5BIQji1mWESIhvOh7JxvGck8Epa0umjWnM8mXGEohXzM3=6Xc3PYQVssMrARBAUY13pUp0mb7BnNOgNMo7gvN_AgJ5DiUFiGqS6Frh7bglVCNF4ZL2YzeS76HGG4JZEyFuN2GzwPRjw9wF-71aamW9IRyn5BUkrJXkTy5E4xV1lvUzncHWreYp-O6x-MLijG=3NRiQpySi0pZUqBtLD8HZoZnPvY2xLEga-tTnsjTqpKKgiQ2R2rgN9QRbpG_tEehOL50S6umB1p6vS5t-c3LeNNaMXql0lJMVJ5Cvhw3cEV=Q7o_M2E4a-U4mB0pexIUE7CT3GcTqFjLyZg-NIwUd58xCojZNgy-MhsG8MIeV-XK-ERmLiP3sIOE7Hg5p_9Bg2bP7PGyDXEJZKTwXQN9m8nvQvc-eLON917GWIv8oEdNEEu-jwe=l2Nix4v8BWDVaDZP7h62gh=8cS74Elvn=SUaoHBK_6cbJLGFa21it7mBP6dRnmPHaayrV3Qc83u6m_6v8kHFr925F_roxVISR4225ro_tl7Ct28mHrqa2NgqT5x4tA_pWEHopc1i0tgzQeGzHX=nGNu4btTYJuRETKhlOXEFcV1F-hRjtRrVdRkGgEFYLMp27qnuIHcFwpUXt1rRh7FR85I=_x3lIJPNmr5M7ulWNL7EzFpnDAL5ROWL4kPYBztYSL62_1OYJv6DNq1k3ZonSST_LLg=a3TPxp0iA0Y4X5p8r2YBcT-R65VK8KwuRKBkNa30sCp43300L_=Uw276l55BpeL1JYgJ2SHZT76M3KmYMINeWzgw50Zez7O57UCox4za3Ivk5qStuEdXs66wGH5JwWgAUK=gUKXnkdhtAqX82zHOXstAQ3Y6l_IVKmCBeu4XHcsSWjIQIUpr7-LQkuibUUwnKZP7XymHGMDgszDu=LCygjJtZSAWLJS2eQzVemV3b8I_yRIIRvibVKGLJP_ax=IX=cx3_NbLHA=4uxijktknDAGk-4FprsXHM1o4r3kvYyiNeZxP_w7CZ4DxuTU6HP2DpYLuaBNHNNVASbzhaJ2C3igh97CsL1vKSvWelxByuBiQbuZ0vmI6zwcsM2Yb9bIn9bT7kQS4=JWlnVMTOvDZd1jEumB7tbsUgu7KMwEpO53epInC7vPh4NF4zXVNPvo5eB1o93R17Fi4CzUzVt67s0RuSlA-FZeNW9j-L2OUPkO5Fzri6l3WpMwL69EeApmH_pMTh7Orz2tdUTeloFauUF0FqPniH7eBtyLNKtNqzalA-cuSOHFIeAViDKcVBk94pj=tz3ob_hXWCrV-WKQ=Ldvx3J2DNY9HE5jyCq2DURcJIYsF971cg0j9QzkN5TqjpRp_wUKVzvzZ90W4zv-=omQhjHz=CjUDYn5yqrH0uoq8qYWUpr5KVIqqvu1XntWPJeHLnOvbF7j1LQimzxdtcGbCl0Rq29oR0q0-z45OwzOElT6W-pY1tjsl1Ukzep=GrAiJZ0AOGo5U3wU6iJQS4-JgZFkzFga6eSV9QK60-BWrVs9VDQOsxIjH5MOGw877s_BiXpC-7xWuGGlCMu79glU1T9P36Hk6D5HvlGNvMrpDg94qiA7K4SnDwvxtnH84Mph0JOqGHp8sm6oENBXwSH5H6nhVsUhOmgarIOOHU80aIv8ig6YG0EaWqFgH6umx4s1mYM5H14-KxcDqF9to25spEo512cgs3w6pFCt_TBxkwcbHTd4M9_jIJ-kAvtsZlm0ZQZsg6lC1Ur=Rq3kYjsD=takLymuUFdp8Dm6WaKUvn5NJ1qhaqCHhz5th8MJiHwzILSvn3sMhFaU6OTTI53Ijo4V3B-TwHRJ8Xu0SG2EleWABucV=ZGh184rqBcck3CWMoldxuNnxlJn-DY-8sLPqgHdJPbnICIiMateSnUyVygX9QtQ5R2eyF9iwYr=XGpFKuOrtiW568JrQgoLdKdeJ9HFd83h7m2wKkW7NY4t2r=K2EH1RI4GwoQH0FudBi1G0DpEUp-EJrno6q6Rh3RU3==rXQMUJE6qqqhqems27cCGBz6PeSFg3_9SwBGLn1ueqtT7=DJtEcclyzmJCi6NA1hcrO5OR2inOP=RUOlhzUdA6w5auaeyh7mOoZyyihqsYui1kwgOmlAVb9vEnK=AhJTjP5S4Cy6EA8=wd4UVMCeeBu-pXkgG_Kp8kYYOYDXx3PiSiQxUnhi1GUeKuYXQnspyQraBRtLetyowKZkZzEKcs1gqeg47pluFpB4jiJi-NR8suA-22Sm3GWdXls3PiYe8in3IuOXOpmwiA0lcT-yYJtV8zCsLTkrST5oKu3=GxcUm4pjacZU3zdUXEIxLw9QYkyoWu4jtR89iGyL95qCVOO_ptb=1wz3BeIVuDnKhDjOAFY_ZZ0vzNpeegHTlyc=c1H5cZS1TDnol0AP01LAvvMwVX1eRsO6H3UtXsk8bOtLkHEREoeiM2iBaLELTTXvyX2DxUYRp_7VnwPoYXRmithUXSl--Fn2PKpHLG6o9o9kB8w7lyGSGk9u9ykAui1Q3y0hoYVFFB_bguxIHo4KcV4wmdt5h-vWQ3eM7eHXU7pk_4mUb9CIoh2o_U-mnd2_1vN4YDXY4M_Q24h1vq40JM=ZiGh96AQJkXH4IyMLqaw5zjsluah0YJFNCWTjGXP9UGL_zL-4H9mBHCu0RFIyvxrvO_DzWdJLAKSxXeth_yA8V4DGOEBPuhwhgR1MBZiv_tCdw2OMlj5GMkmVNKHvMtKdKHHk60beEx-V_s1a5DxUKG0BPoyRDzUxNH-5Chz80I2sRvIgdOoj7BUKg7vwq93EdbvbxokchnBoWPS_D=cly57mv-QYSWRiF0IlzKZI1nZMIVbrxDABorbOnIZOSNDob9JYoA6Rpb_=wco_peynnaOnVum-unWsDu5LJuSHghGoJbzWDSpWZlil_pKpi5-kh5H43i90XALrjjZz7hqDEMx77gsr9UrPxyWDA_ndUsDnJ-I3-xkxbd7S7u7AaCALQ7Eb-h6JAuC54scdR81ATFtATol9sTPEIxDdmneB6emFgT37Avh3XSHsarnpmR35t_3zgb2vCihVEQVWszPCY-gCTZ-_=sK6UhSXrxWGIN9oXGapi83qEoIP23jX=NX0GV2ovTnawUwdCldqVtTWiz0nyMZYZ0vTK7v97L8p2G7g6XU5eUJZJDVlBc847nKdm8R8n9k4u3nGFTNCzNZ7OJUGdrS5y96HhOxWRQNejZ-5d5WHN2lrKxadtPqDFduWSzT6sJyMueaTxS4wAtWBLUyhsYmRpEweMyo9c-r_N6cIjWl-iDS0uwBk3c3SAQwqGj9-oxK4AO4Gb-lvmjYQnzjG2gUyi=4OaTsLYq=wgDCAM3RgbU096BPYtVt9pc4EB3aKv4GuLezQuAerARmc42hI=N0_P5cMWvojvSA9ewdA-cA0WXxHkT7GuHdIdi-rgkEMJBjIY94YrBCkec1WdQEnHugoEtb-uORMNQz26XjGei0i7aWWV0XdgaK_zxFNqKEcmJVbwrgV971oSOnr-zpFgND4aU8Bi6kjWAI9865mYwjno8xbNGIibHMoBjbe4jC16KuSKwVjsairsXTD4mgUZP2PrdXppt-uCr35n8ica=2MJbrPFKwFawcXFpKu6ExNnAYIgjEdnc=5wGqNRte6vy=E1kHSnzVpkwyS5W8Yh0wug4YlRITvmJlyP=vzr-7M7KoQh8jR80pCqOlkezv=_bwS0vvDSoSAgacNqL9RAZ-NIaji4-wdwUPCbArt93q-CwBdjX-oLkKF8SMyXDDWGF1THZLzwBMde-zLeNEA0SUqPR5QnTJCTa4nMuuTHpENZ5FUFClRW6xJlcNrLj4u=g7dsWA=nJXziVQTytBFDC_hDF7gYWbbx4mchA7qT1i6ctDFe19oXAd-IrtGixSaZJsiNgTEiKsAnDeJTbMYXoO2l9hqwniOSZvEKvLVUA9vb4xzdr2Wyod=nvXeemAnozzCtPdQiQa8BV282c9HLE-3ioQB2=nTyNZ=-OKjPX1YlDoNsAQYeY_9JmSO1CL4tFJOomhz0m=xCiWM_6IyLZlwPkvKwhIbnDJOxu5jJ4mWpOKvZ5NTotPxdDcXeGyIeFLbO7-QpEh_T4ACHcMY7IwO_4khWQZOx=dWntI4hFMP_9_NFAmj-8RgRrj0sCCxyEasCPZcnVBYI7yBEYWVYBJFnTpHIzs=QvwmpVNbYVSohXxQW9LA_HMN6aqE-cKCWnjimdTwkQA79PaBq9NjydtJYDN_ElMCoYZT0YHCdFMz14QwT9t=BHBl4cKKQALXQziKthV82ArU3oigU41y24W53llTWvAUH55xpQhMlXuUuK7NTLb9H33kZwir9CYaKqclUHHBta6YTK6I4jTsp38Ija=eKpxADNWAvt25Vs14XKGguODXC=EZLF-cWgR-Mov9CE8rnu_j54a5InMGH74NM4KSJHLuKq2uRmcvRy4vwknnp48cXM0Y-wPJlimEi7mhomkhS6j7Vweo5jU7TZpdZGMlbOswFYb=dM2pYt9HJdtIDk6WF9AAWIm13HhTiw_xPFoizAKOF9dr-548pr6eoKYZGz231HlSoxL0aVUuqQopMAmWsG=RpnAGQ4a5l_h8Zq_m83SR568iLMys5gCVb7MtH=HgeENB=UNc3-22EeglihIgrxvyTIc-938VLTF5IZR=9aweUyYQKg3IW4_2=K7QCVYCHTyvGgcOXknuDbSGgExsnD2WAJTWEq1TVpdIH1X5zsaEULAPw2z_lHbMrndYDeVHvJoA16NvACLBlyZH1i5SQt3viTE8QRZ46Tw=nHqATx2YVXEZ35CekY42r1AOJPQRjyo=mzeIeE4tRV7Cx1QXkAHDKZkKxhOZG_lzuS0gGr5bC-PsV-KswWBN2T=Z5pnWjoCRiRYlaVi1nSkeOjn5YBbS32ijtEn1ANrV2F58-OrKVuGw7blp-h3jil5N3mMuBoDoX666ceJQIkVM0vO4G_6dYWOMnKb_d9Y_1FvEHN22tuWdz=MSBBC1LoHNVJv7LX54CnZcnZsz8OU0=OMuJxThHyWXWLp5XP2ZdR_JjSvho-=eUB8dj2NFYqDLhN-vViods2ubLs0cWE5P8ZGtqOMvhZUqNVt3OysbmL=CJEIt4xRM3WDC9hw05m9EcckG7XGJZSVF0YqW1HQolziCPOkCIOSuCvSSBkm75qjeAw=an7KMRH19UTcLbODr1Et8A_nhth8vs7TKGzOGSvqVCXN2heueQh2T8Wz8jE9zcVJ9LDgT6qvFGuDDppwPq6SOJ-erDG0roBSWIbD7cwJOWk2Ny8MDEAHAFPO6ZpVI66peXXRR5ODYet8q06TkyO0hJhj3cKt2q5CHuqT-jCCVZO5NLJwNjWzr4gQHG67Btum2xLvNZ7R1d8GQ2M8VsNR=V8t4z73MFp=itr2znO7JsgNhCeRQBZ4nCgrIqaasKgpCsv5gpIDq_0r55CHx4FjnNdNSqs1i3eWmoIjhQA=03xSTvFeSaUVsdQy8dtDp8q9iQ=DzNPxH4uyN1lNUQwgYKbqKYBZyjAxDtPY4gcD3=0KxmgNJ77qbtN4b8c0cSiwEJrQaTIPvi_4XUeChjGUqY4r-jLRR-20MWwK2TOzY-V0YVwGFUWP0D--kJ9jtqREWTmBtJDRaFN6qFLajp7Pkydn7ojxlpE9NH6RLp0dVAy74kanrw=14741ArLhUbnmbysztpiDHzAASJcTAD0o=dBJ3bu4wrExRVb1XYzDWYkiF6Tkdynn-m5S45iz8ltEOZM7_PkGNQ4KRlz3lNu=RN_9AJYIOgzvAPBj8hTz_AFmlkNXWNXqrFI1iB_mTs9iXVP61CSt5tTN7encWk8X9y3Sw3id1cPOjLh_HGlT8_CaTJkgo=jZlVG9EhPuNlwvyxAnYmAIVN=C5ZSES4FdLEeyv6k4TQkMCQQiI-auEe8=CTVaKDaGFZqhFWbwmgAPWEFOoVP3LOr2Eh3X8jKX92dEzJU1UO8-4zXqzwI5=KPDNSLAzh53Yuec1lo9ldYTQ=v6Nqqxm5oLBX-wl4FZXm6_i3Kq8owp6a5F_URwcMBOEBM3KvbEHXOVgC1rA9q-4aBUUx8yb-yAGp8a0N8vzezkWJv4hE6kOmcrYD-aJRUBI2pbYl4tE0SUxXuOBokbwColLORCYOMrQWS66BFopA4CbRR--9iW=lELiqDF-V6GGt-t_U=y5wUo6huvN3y1bZWJ_r2U45euHe5c2Skl5k61OQpYPIiwFEWpt3_DKdMKq0pchlG1l3U=v2J78A3K7LtbxHeCUl4Du6iXrtm3Q5p4EZgstSg1w==DAEL8n0N-ct65VBrIeK1-zTr_x06hDAobiO1PiA',
    'ee30zvqlwf-b': 'pqme4h',
    'ee30zvqlwf-c': 'AMAgr-GMAQAA8mxHnuZ_MdwtNRsuZCrQ5FeV_X8wt976Hw5rA2bQIf26iGyG',
    'ee30zvqlwf-d': 'ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpizi_33wdm0CH9uohshgAAAABnMdsJAFl3vokl0pS6WcajLplesdQ',
    'ee30zvqlwf-f': 'A7jlseGMAQAAa-Ntvs9T-ks5g0kfgfmL17eKXbEF7tN6J1_R0eC6nvawT7X_AUnKRMmcwm1wfMB9t4LqosJ9tw==',
    'ee30zvqlwf-z': 'q',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-api-key': 'l7xx2c186c1297274b828b1872e22edfe67a',
    'x-channel-id': 'MWEB',
    'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

