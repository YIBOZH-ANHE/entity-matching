# Entity Matching Project

这是一个实体匹配项目，主要目标是识别和匹配来自Amazon和Google两个数据源的相同商品。

## 环境配置

### 开发环境
- Python 3.8
- conda 环境管理

### 依赖包
- pandas >= 1.0.0
- numpy >= 1.18.0
- matplotlib
- ipython
- jupyter

### 环境安装
bash

# 创建conda环境
conda env create -f environment.yml

# 激活环境
conda activate entity_match 

## 项目结构
```
entity_matching/
├── data/
│ ├── Amazon.csv
│ ├── Google.csv
│ ├── Amazon_Google_perfectMapping.csv
│ └── stopwords.txt
├── code.ipynb
├── environment.yml
└── README.md
```     

## 实现方法

### 1. 文本预处理
- 读取Amazon.csv和Google.csv数据
- 对文本进行分词
- 去除停用词
- 构建token列表

### 2. 特征提取
- 计算TF (Term Frequency)
- 计算IDF (Inverse Document Frequency)
- 生成TF-IDF权重

### 3. 相似度计算
- 构建倒排索引
- 计算文档向量的点积
- 使用余弦相似度度量文档相似性

### 4. 评估方法
- 使用precision作为评估指标
- 通过阈值调节来优化匹配结果

## 遇到的问题及解决方案

### 1. 精确率曲线异常
**问题**: 在阈值0.84之后精确率急剧下降
- 阈值0.84时：85个匹配对，30个错误匹配
- 阈值0.85时：78个匹配对，28个错误匹配

**解决方案**:
- 优化相似度计算
- 确保向量归一化的正确性
- 添加数值保护措施

### 2. 环境配置问题
**问题**: 依赖包版本兼容性
**解决方案**: 使用conda环境管理，固定关键包版本

### 3. 数据预处理挑战
**问题**: 文本噪声和不规范数据
**解决方案**: 
- 规范化文本处理
- 去除停用词
- 统一大小写

## 结果分析

- 最佳阈值：0.84
- 最高精确率：约0.64
- 在高阈值区间（>0.84）性能下降明显

## 改进方向

1. 优化相似度计算
2. 改进特征提取方法
3. 考虑使用更多元的匹配策略

## 使用说明

1. 克隆项目
2. 配置环境：`conda env create -f environment.yml`
3. 激活环境：`conda activate entity_match`
4. 运行Jupyter notebook：`jupyter notebook`
5. 打开`code.ipynb`执行代码
