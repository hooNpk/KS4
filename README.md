# KS4

KS4는 Korea Short-term Stock Suggestion Serveice의 첫 글자들을 따왔습니다.
뜻 그대로 대한민국 단타 주식 추천 서비스입니다.
    
KS4 is acronym of Korea Short-term Stock Suggestion Service
As its name, This service recommend S.Korea's stock for short-term.(I used 'suggest' just for rhyme)
    
### 동작방식
  - 최초 실행 시 네이버 금융(finance.naver.com)에서 모든 종목 주식 데이터를 받아옵니다.
  - 주식 데이터를 가공하여 MySQL DB에 저장합니다.
  - 다음 실행 시 저번 실행 이후 주식 데이터를 업데이트합니다.
  - 특별한 알고리즘에 따라 종목을 추천합니다.

### 특별한 알고리즘
  - 특별한 거 없습니다.
  - 5일선 20일선 크로스가 발생한 종목
  - 20일선 주가 크로스가 발생한 종목
  - 이중 흔히 발생할 수 있는 경우를 제외합니다.
  - 기본적으로 펀더멘털이 갖춰져있고 기관 유입, 거래량에 뚜렷한 변화가 있는 종목을 추천합니다.

### 정확성
  - 실험 중

### 향후계획
  - 머신러닝을 접목하고 싶습니다.
     
     
     
### How KS4 runs
   - When its first run, she import every stock data for 60 days from "finance.naver.com"
   - After processing data, she stores the data in MySQL DB
   - On the next run, KS4 will update the stock data since the last run.
   - She recommends stocks under the special(?) algorithm.

### Special Algorithm
   - Nothing Special. It recommends two types of stock
   - Stocks in which a cross occurred in 5 days moving average line and 20 days moving average line.
   - Stocks in which a cross occurred in stock price line and 20 days moving average line.
   - Except where this may happen. ( I know. This is ambiguious expression. )
   - If the stocks equipped with fine fundamental and If there is meaningful change on volumes, institution's buy then, recommend it.

### How often KS4 predicts?
   - On experiments
  
### Future Plan
   - want to adopt machine-learnging
   
   
------
KS4는 업데이트 중 입니다.
자산을 자동으로 관리해주는 프로그램이 될 것 입니다.
