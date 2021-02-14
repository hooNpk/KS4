from get_fund_from_naver import return_fundamental, str_tidy

def sales_increase(y3, y2, y1):
    sales = y2[0] > y3[0]
    if(y1[0]=='-777'):
        return sales
    else:
        return ( sales and y1[0] > y2[0] )

def positive_profit(y3, y2, y1):
    profit = float(str_tidy(y3[1])) > 0
    profit = profit and (float(str_tidy(y2[1])) > 0)
    if(y1[1]=='-777'):
        return profit
    else:
        return profit and (float(str_tidy(y1[1])) > 0)

def quick_ratio(y3, y2, y1):
    if(y3[4]=='-777'):
        return False
    quick = float(str_tidy(y3[4])) > 80
    quick = quick and (float(str_tidy(y2[4])) > 80)
    if(y1[4]=='-777'):
        return quick
    else:
        return quick and (float(str_tidy(f1[4])) > 80)

def check_per(q2):
    return float(str_tidy(q2[5])) < 50

def is_candidate(fund):
    """
        1) 이전 3년 연간영업이익 > 0
        2) 이전 3년 연간 매출 증가
        4) 이전 3년 연간 당좌비율 > 80%
        5) 마지막 분기 PER < 50
    """
    #fund = return_fundamental('락앤락')
    
    y3, y2, y1 = fund[8], fund[9], fund[10]
    q4, q3, q2, q1 = fund[11], fund[12], fund[13], fund[14]

    sales = sales_increase(y3, y2, y1)
    profit = positive_profit(y3, y2, y1)
    quick = quick_ratio(y3, y2, y1)
    per = check_per(q2)
    
    return sales and profit and quick and per

#is_candidate()
