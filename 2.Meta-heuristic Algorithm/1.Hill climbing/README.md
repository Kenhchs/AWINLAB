## 目錄
- [虛擬碼](#虛擬碼)
- [程式流程](#程式流程)
- [函式介紹](#函式介紹)
  - [讀檔](#讀檔)
  - [初始解](#初始解)
  - [計算價值](#計算價值)
  - [尋找鄰近點](#尋找鄰近點)
  - [計算重量](#計算重量)
  - [初始變數設定](#初始變數設定)
  - [畫圖](#畫圖)
- [成果](#成果)
- [參考資料](#參考資料)

## 虛擬碼
```c
currentNode = startNode;
loop do
    L = NEIGHBORS(currentNode);
    nextEval = -INF;
    nextNode = NULL;
    for all x in L 
        if (EVAL(x) > nextEval)
            nextNode = x;
            nextEval = EVAL(x);
    if nextEval <= EVAL(currentNode)
        //Return current node since no better neighbors exist
        return currentNode;
    currentNode = nextNode;
```
## 程式流程
因為要有500個 iteration，有可能遇到的情況是找不到更好的 neighbor，與虛擬碼不同的是此時會啟動隨機重新啟動爬山([Random Restart Hill Climbing](https://en.wikibooks.org/wiki/Artificial_Intelligence/Search/Iterative_Improvement/Hill_Climbing#Random-Restart_Hill-Climbing))而不是回傳目前的點

https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L100-L107

## 函式介紹
### 讀檔
讀取儲存```背包容量```、```物品重量```、```物品價值```的檔案，並且分別存入變數```capcity```、```weights```、```profits```
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L4-L17

### 初始解
從```0```到```物品長度-1```在物品重量不超過背包容量的情況下，隨機挑選物品放入背包
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L19-L31

### 計算價值
依照挑選的物品計算出當前物品的總價值
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L33-L39

### 尋找鄰近點
尋找順序如下
1. 尋找可以放去的物品
2. 在不超出背包重量的情況下，將```選取的物品```與```未選取的物品```交換，即```選取的物品```設定成```未選取的物品```，```未選取的物品```設定成```選取的物品```
3. 背包清空，重新隨機選擇物品
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L41-L77

### 計算重量
依照挑選的物品計算出當前物品的總重量
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L79-L85

### 初始變數設定
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L89-L98

### 畫圖
```matplotlib```畫出收斂圖，```x_axis```和```iteration_score```分別為```x軸```及```y軸```
https://github.com/Kenhchs/AWINLAB/blob/de0b3d36a59725ae98d623e0c1eac042c4cd11eb/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/hill_climbing.py#L110-L113

## 成果
<img src="https://github.com/Kenhchs/AWINLAB/blob/main/2.Meta-heuristic%20Algorithm/1.Hill%20climbing/Hill%20climbing.png"/>

## 參考資料
[Knapsack problem using the hill climbing algorithm](https://ai.stackexchange.com/questions/3032/how-do-i-solve-the-knapsack-problem-using-the-hill-climbing-algorithm)
