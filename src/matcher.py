from typing import Dict, List
import pandas as pd
import numpy as np

class ProductMatcher:
    def __init__(self, threshold: float = 0.5):
        """
        初始化匹配器
        threshold: 相似度阈值，高于此值的才认为是匹配
        """
        self.threshold = threshold
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """计算两个文本的相似度（使用简单的字符匹配）"""
        if pd.isna(text1) or pd.isna(text2):
            return 0.0
        if text1 == "" or text2 == "":
            return 0.0
            
        # 转换为集合
        set1 = set(text1.split())
        set2 = set(text2.split())
        
        # 计算 Jaccard 相似度
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def match_products(self, amazon_df: pd.DataFrame, google_df: pd.DataFrame) -> pd.DataFrame:
        """匹配产品"""
        matches = []
        total = len(amazon_df)
        
        print(f"开始匹配 {total} 个Amazon产品...")
        
        for idx, amazon_row in amazon_df.iterrows():
            if idx % 100 == 0:
                print(f"处理进度: {idx}/{total}")
            
            # 对每个Amazon产品，找到最佳匹配的Google产品
            best_match = None
            best_similarity = self.threshold
            
            for _, google_row in google_df.iterrows():
                # 计算标题相似度
                title_sim = self.calculate_similarity(
                    amazon_row['clean_title'],
                    google_row['clean_title']
                )
                
                # 如果标题相似度高于阈值，再计算其他特征
                if title_sim > best_similarity:
                    # 计算制造商相似度
                    manuf_sim = self.calculate_similarity(
                        amazon_row['clean_manufacturer'],
                        google_row['clean_manufacturer']
                    )
                    
                    # 综合相似度 (标题权重0.7，制造商权重0.3)
                    total_sim = title_sim * 0.7 + manuf_sim * 0.3
                    
                    if total_sim > best_similarity:
                        best_similarity = total_sim
                        best_match = {
                            'amazon_id': amazon_row['id'],
                            'google_id': google_row['id'],
                            'amazon_title': amazon_row['title'],
                            'google_title': google_row['title'],
                            'similarity': total_sim
                        }
            
            if best_match:
                matches.append(best_match)
        
        return pd.DataFrame(matches)