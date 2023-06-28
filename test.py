from s1_technical_analysis.main_processor import get_technical_analysis_score

ticker = "BTC"
decision = get_technical_analysis_score(ticker)

print(decision)