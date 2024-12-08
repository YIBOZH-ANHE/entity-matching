import pandas as pd
import numpy as np
import re

class DataPreprocessor:
    def __init__(self):
        self.amazon_df = None
        self.google_df = None
        
    def load_data(self, amazon_path: str, google_path: str) -> None:
        """加载数据集"""
        print("开始加载数据...")
        self.amazon_df = pd.read_csv(amazon_path, encoding='latin1')
        self.google_df = pd.read_csv(google_path, encoding='latin1')
        print(f"Amazon数据集大小: {self.amazon_df.shape}")
        print(f"Google数据集大小: {self.google_df.shape}")
    
    def clean_text(self, text: str) -> str:
        """清理文本数据"""
        if pd.isna(text):
            return ""
        # 转换为小写
        text = str(text).lower()
        # 移除特殊字符
        text = re.sub(r'[^\w\s]', ' ', text)
        # 移除多余空格
        text = ' '.join(text.split())
        return text
    
    def preprocess(self) -> None:
        """预处理数据"""
        print("\n开始数据预处理...")
        
        # 1. 统一列名
        print("1. 统一列名...")
        self.google_df.rename(columns={'name': 'title'}, inplace=True)
        
        # 2. 清理文本数据
        print("2. 清理文本数据...")
        for col in ['title', 'description', 'manufacturer']:
            print(f"   处理 {col}...")
            self.amazon_df[f'clean_{col}'] = self.amazon_df[col].apply(self.clean_text)
            self.google_df[f'clean_{col}'] = self.google_df[col].apply(self.clean_text)
        
        # 3. 统一价格格式
        print("3. 统一价格格式...")
        self.google_df['price'] = pd.to_numeric(self.google_df['price'], errors='coerce')
        
        # 4. 显示处理后的数据信息
        print("\n处理后的数据信息:")
        print("Amazon数据集大小:", self.amazon_df.shape)
        print("Google数据集大小:", self.google_df.shape)