def create_example_trade():
    trade = Trade(
        tradeDate={"value": "2025-04-01"},
        product={"economicTerms": {}}
    )
    return trade