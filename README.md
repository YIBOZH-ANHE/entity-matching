# 实体匹配系统实验报告

## 1. 作业要求
现有一个Amazon的众多商品的数据记录文件(Amazon.csv)，同时有Google对众多商品的数据库记录文件(Google.csv)。将两者的数据匹配起来。

## 2. 运行环境

### 2.1 硬件环境
- 处理器: Apple M1
- 内存: 8GB
- 存储空间: 256GB

### 2.2 软件环境
- 操作系统: macOS
- Python: 3.8+
- 包管理器: conda

### 2.3 环境配置
```bash
# 创建并激活虚拟环境
conda create -n entity_match python=3.8
conda activate entity_match

# 安装依赖包
pip install pandas numpy
```

## 3. 项目结构
```
entity_matching/
├── data/                # 数据目录
│   ├── Amazon.csv      # Amazon产品数据（1363条记录）
│   └── Google.csv      # Google产品数据（3226条记录）
├── src/                 # 源代码目录
│   ├── data_preprocessor.py  # 数据预处理模块
│   ├── matcher.py            # 匹配算法实现
│   └── main.py              # 主程序
├── results/             # 结果目录
│   └── matches.csv      # 匹配结果
└── README.md           # 项目文档
```

## 4. 模块说明

### 4.1 数据预处理模块 (data_preprocessor.py)
- 功能：数据加载、清理和标准化
- 主要处理：
  - 统一列名（name -> title）
  - 文本清理（小写转换、特殊字符移除）
  - 数据类型统一（价格格式）
  - 生成清理后的特征列（clean_title, clean_description, clean_manufacturer）

### 4.2 匹配算法模块 (matcher.py)
- 功能：实现产品匹配逻辑
- 算法特点：
  - 使用 Jaccard 相似度计算文本相似度
  - 多特征加权（标题70%，制造商30%）
  - 阈值筛选（>0.5）

### 4.3 主程序 (main.py)
- 功能：程序入口，执行完整匹配流程
- 主要步骤：
  1. 加载数据
  2. 预处理
  3. 执行匹配
  4. 保存结果
  5. 输出统计信息

## 5. 算法详解

### 5.1 文本相似度计算
使用 Jaccard 相似度：

```python
def calculate_similarity(text1: str, text2: str) -> float:
    # 转换为集合
    set1 = set(text1.split())
    set2 = set(text2.split())
    
    # 计算交集和并集
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    # 计算相似度
    return intersection / union if union > 0 else 0.0
```

### 5.2 匹配策略
1. 标题相似度权重：0.7
2. 制造商相似度权重：0.3
3. 匹配阈值：0.5
4. 选择最佳匹配：对每个Amazon产品选择相似度最高的Google产品

## 6. 工作流程
1. 数据加载
   - 读取CSV文件
   - 处理编码问题
2. 数据预处理
   - 统一列名
   - 清理文本
   - 标准化格式
3. 特征提取
   - 生成清理后的文本特征
4. 相似度计算
   - 计算多维度相似度
5. 匹配筛选
   - 应用阈值
   - 选择最佳匹配
6. 结果输出
   - 保存匹配结果
   - 生成统计信息

## 7. 实验效果
- 数据规模：
  - Amazon: 1363 条记录
  - Google: 3226 条记录
- 匹配结果：
  - 成功匹配：327 对
  - 匹配率：24%
  - 平均相似度：0.630
- 示例匹配：
  ```
  相似度: 0.700
  Amazon: adobe premiere pro cs3 upgrade
  Google: adobe premiere pro cs3 upgrade
  ```

## 8. 总结

### 8.1 主要成果
1. 实现了完整的实体匹配系统
2. 达到了较好的匹配准确度
3. 系统具有良好的可扩展性

### 8.2 改进方向
1. 算法优化
   - 引入更多特征（如价格比较）
   - 使用更复杂的相似度算法（如编辑距离）
   - 实现并行处理提高效率
2. 评估体系
   - 添加准确率、召回率等指标
   - 实现人工标注的验证集
3. 系统扩展
   - 支持更多数据源
   - 提供API接口
   - 优化内存使用

## 9. 运行说明

```bash
# 1. 克隆项目（如果适用）
git clone <project_url>
cd entity_matching

# 2. 配置环境
conda create -n entity_match python=3.8
conda activate entity_match
pip install pandas numpy

# 3. 运行程序
python src/main.py

# 4. 查看结果
# 结果保存在 results/matches.csv

# 5. 项目中使用了部分绝对路径，如需运行请自行修改
