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
create a random initial permutation
loop 500 times
  create an adjacent candidate solution
  if candidate is better than curr solution then
    curr solution = candidate (accept)
  else if candidate is worse then
    accept candidate anyway with small prob
  end-if
  
  decrease prob of accepting worse candidate
end-loop
return best solution found
```

## 程式流程

## 函式介紹

## 成果
<img src="https://github.com/Kenhchs/AWINLAB/blob/main/2.Meta-heuristic%20Algorithm/2.Simulated%20annealing/Simulated%20annealing.png">

## 參考資料
[Simulated Annealing](http://people.math.sfu.ca/~kyeats/teaching/math343/22-343.pdf)<br>
[Knapsack Problem Using Simulated Annealing](https://jamesmccaffrey.wordpress.com/2021/12/17/knapsack-problem-using-simulated-annealing-example/)
