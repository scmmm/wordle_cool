# 程序怎么运行的

## 输入

每次输入一个单词(仅包含小写字母)以及一个仅包含 `012` 的序列，对应顺序可以看下面的demo

然后程序会返回不超过 30 个建议你扩大猜测范围的单词以及不超过 30 个可能的正确答案

# DEMO

例如我猜测一个长度为 11 的单词

首先随便输入一个单词，例如 transformer

[![piZJ2o4.png](https://z1.ax1x.com/2023/10/26/piZJ2o4.png)](https://imgse.com/i/piZJ2o4)

然后向代码中输入这样一行序列

```
1
11
transformer
10111010000
```
程序会建议你猜测这些单词
```
当前建议猜测的单词
['bushwalking', 16]
['jackpudding', 16]
['oxysulphide', 15]
['xylographic', 15]
['acidophilus', 14]
['bivouacking', 14]
['bloodguilty', 14]
['buckpassing', 14]
['chickabiddy', 14]
['clodhopping', 14]
['conjugality', 14]
...
```
选一个顺眼的,我选了 conjugality

然后

[![piZJWFJ.png](https://z1.ax1x.com/2023/10/26/piZJWFJ.png)](https://imgse.com/i/piZJWFJ)

接着输入

```
conjugality
01100220210
```

此时已经有很多黄的了，不妨直接猜
对于正确答案，程序预测如下

```
当前可能的单词
['instigation', 29]
['astrogation', 28]
['castigation', 28]
['fustigation', 27]
['subrogation', 27]
['entorganism', 26]
['propagation', 26]
['segregation', 26]
['subjugation', 26]
['aggregation', 25]
['disorganize', 25]
['prorogation', 25]
['variegation', 25]
['assignation', 24]
['expurgation', 24]
['objurgation', 24]
['colligation', 23]
['designation', 23]
```

然后输入第一个，发现的确是答案。

[![piZJgwF.png](https://z1.ax1x.com/2023/10/26/piZJgwF.png)](https://imgse.com/i/piZJgwF)

# 只是做着玩的

 本程序用猜测wordle要的单词，还不够完善，但是够用了，以后有空再更新

## this code is just for fun
## DO NOT CHEAT

# 因为此程序产生的法律后果概不负责

 Not responsible for the consequences

# 单词表来自
[这里](https://github.com/1eez/103976)

