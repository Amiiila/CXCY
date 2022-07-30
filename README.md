# SM3_birthday_attack
Implement the naïve birthday attack of reduced SM3
## 生日攻击
生日攻击利用概率论中生日问题的数学原理，通过找到Hash函数输出值相同的两个不同输入，伪造报文的攻击方法。
## 实验过程
SM3算法可以调用python中的gmssl库实现。
根据生日攻击原理，可以随机生成两个数并比较其hash‘函数的输出值，直到两个输出值相等。
## 运行结果
<img width="415" alt="image" src="https://user-images.githubusercontent.com/110109750/181868516-79031da3-a2cc-41cb-b63a-6f80c53e40ca.png">

## 参考文献
[MD5的生日攻击](https://gist.github.com/BenFranzi/087ba57ecdc4c6eb7c52ba485242762f)
