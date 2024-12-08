from data_preprocessor import DataPreprocessor
from matcher import ProductMatcher
import os

def main():
    """
    主程序：执行完整的实体匹配流程
    """
    # 获取数据文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    amazon_path = os.path.join(os.path.dirname(current_dir), 'data', 'Amazon.csv')
    google_path = os.path.join(os.path.dirname(current_dir), 'data', 'Google.csv')
    
    print("=== 实体匹配系统启动 ===")
    
    # 1. 预处理数据
    preprocessor = DataPreprocessor()
    preprocessor.load_data(amazon_path, google_path)
    preprocessor.preprocess()
    
    # 2. 执行匹配
    matcher = ProductMatcher(threshold=0.5)
    matches = matcher.match_products(preprocessor.amazon_df, preprocessor.google_df)
    
    # 3. 保存结果
    output_path = os.path.join(os.path.dirname(current_dir), 'results', 'matches.csv')
    matches.to_csv(output_path, index=False)
    
    # 4. 输出统计信息
    print("\n=== 匹配结果统计 ===")
    print(f"找到的匹配数量: {len(matches)}")
    print(f"匹配率: {len(matches)/len(preprocessor.amazon_df):.2%}")
    print(f"平均相似度: {matches['similarity'].mean():.3f}")
    
    # 5. 显示示例匹配
    print("\n=== 匹配示例 ===")
    for _, match in matches.head().iterrows():
        print(f"\n相似度: {match['similarity']:.3f}")
        print(f"Amazon: {match['amazon_title']}")
        print(f"Google: {match['google_title']}")
    
    print("\n=== 处理完成 ===")
    print(f"结果已保存至: {output_path}")

if __name__ == "__main__":
    main() 