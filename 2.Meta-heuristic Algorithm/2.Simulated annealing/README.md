## 目錄

```c
create a random initial permutation
loop many times
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
