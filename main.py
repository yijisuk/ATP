from s1_technical_analysis.main_processor import get_technical_analysis_score


if __name__ == "__main__":

    ticker = "BTC"
    decision = get_technical_analysis_score(ticker)

    if decision is None:
        print(f"Could not get technical analysis score for {ticker}")
    else:
        print(decision)