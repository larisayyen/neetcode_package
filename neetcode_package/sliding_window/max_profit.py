
def maxProfit(prices):
    '''
    given an array of prices
    output the maximum profit
    '''

    res = 0
    low = prices[0]

    for p in prices:
        if p < low:
            low = p
        res = max(res,p - low)

    return res

def maxProfit_singlePass(prices):

    n = len(prices)
    # only buy and sell once
    if n < 2:
        return 0

    maxprofit,minstock = float('-inf'),prices[0]

    for p in prices:
        maxprofit = max(maxprofit, p - minstock)
        minstock = min(minstock, p)

    return maxprofit

# medium link: https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImFmYzRmYmE2NTk5ZmY1ZjYzYjcyZGM1MjI0MjgyNzg2ODJmM2E3ZjEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NzQyODEyNDIsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNjEzOTUxMDA2NDAyNDU2MzY0MCIsImVtYWlsIjoibGlzYXllbjEyMjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiJsaXNhIHllbiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA1dVNDMzhkQ3lLeTY1V1BHQWJ5VE5oMENVb2JwY1ZpTmVIQTZIQz1zOTYtYyIsImdpdmVuX25hbWUiOiJsaXNhIiwiZmFtaWx5X25hbWUiOiJ5ZW4iLCJpYXQiOjE2NzQyODE1NDIsImV4cCI6MTY3NDI4NTE0MiwianRpIjoiNWM4MDNkZjlmNTVjM2UyM2NiODVhYzdhMDJjYjQzY2U3NDM4Y2ZmMyJ9.ofRJngZhmsnLG_yh7alJ9MdnSm6m0beqM5oqBFEA13l0TdaT-ctJM6fx-_OflxVuCxT1k4YTnUEac2HFwAJN-W_TJYS2egp3Z_1seG4K7pvD48vmvnPLZ0lun10PsoJ7gPrmaOYsTPH0ve3znbfl35zlHALMg8DeUOfkw77Z3SJwm4dk5pW1sLW22NXz0KsqMLTPuFV9B55kMT1GDTlKib58kuYoG5zKFMN2wnlsM1StHjW2Ug3U3XnxFIfLIA7Qcbm0w8wwZWO1lZZVpFOG8zzMpO6AabLCc_0in508gROlBvULxGu2Uo830rEd_d6Sa65zU98a4wXDno-1V4rqcQ
