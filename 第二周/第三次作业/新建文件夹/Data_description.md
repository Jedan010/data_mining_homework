
## 1. 数据描述


```python
import pandas as pd
import scipy.stats as ss

```


```python
df = pd.read_excel('data.xlsx', index_col=0)
data = df.drop(df.columns[0], axis=1)
columns = data.columns

data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Salary income</th>
      <th>Household income</th>
      <th>Property income</th>
      <th>Transfer income</th>
    </tr>
    <tr>
      <th>No</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4524.25</td>
      <td>1778.33</td>
      <td>588.04</td>
      <td>455.64</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2720.85</td>
      <td>2626.46</td>
      <td>152.88</td>
      <td>79.64</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1293.50</td>
      <td>1988.58</td>
      <td>93.74</td>
      <td>105.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1177.94</td>
      <td>1563.52</td>
      <td>62.70</td>
      <td>86.49</td>
    </tr>
    <tr>
      <th>5</th>
      <td>504.46</td>
      <td>2223.26</td>
      <td>73.05</td>
      <td>188.10</td>
    </tr>
  </tbody>
</table>
</div>



### 统计数据基本情况
- 总数
- 均值
- 标准差
- 最小值
- 4分位数
- 最大值


```python
data.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Salary income</th>
      <th>Household income</th>
      <th>Property income</th>
      <th>Transfer income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1394.466452</td>
      <td>1822.891613</td>
      <td>115.492581</td>
      <td>178.723548</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1313.328388</td>
      <td>484.057977</td>
      <td>128.721523</td>
      <td>154.307114</td>
    </tr>
    <tr>
      <th>min</th>
      <td>195.510000</td>
      <td>774.600000</td>
      <td>16.810000</td>
      <td>52.660000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>574.230000</td>
      <td>1523.245000</td>
      <td>38.720000</td>
      <td>98.260000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>954.890000</td>
      <td>1778.330000</td>
      <td>62.700000</td>
      <td>129.830000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1365.535000</td>
      <td>2193.375000</td>
      <td>149.395000</td>
      <td>198.760000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6159.700000</td>
      <td>2789.400000</td>
      <td>588.040000</td>
      <td>855.950000</td>
    </tr>
  </tbody>
</table>
</div>



### 计算变异系数（偏差标准偏差与平均值的比值）


```python
ss.variation(data)
```




    array([ 0.92649919,  0.26122595,  1.09641978,  0.84934464])



### 计算偏度


```python
data.skew()
```




    Salary income       2.242446
    Household income   -0.047204
    Property income     2.419086
    Transfer income     3.206948
    dtype: float64



### 计算峰度


```python
df.kurt()
```




    Salary income        5.439312
    Household income    -0.546945
    Property income      6.348023
    Transfer income     12.388402
    dtype: float64



## 2. 关于SPSS箱线图胡须位置
 > 从箱图延伸出的 T 形条称为内围或细线。这些条延伸至箱图高度的 1.5 倍，或者如果个案/行有一个在该范围内的值，则延伸至最小或最大值。 <cite>SPSS官方教程[1]</cite>

[1]:https://www.ibm.com/support/knowledgecenter/zh/SS3RA7_15.0.0/com.ibm.spss.modeler.help/graphboard_creating_examples_boxplot.htm


所以spss的箱线图的胡须是从箱线图的顶部或底部向外延伸1.5倍的箱体长度。

