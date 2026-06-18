from stock import stock_system

def test_real_time_data():
    assert stock_system("DATA") == "REAL-TIME DATA RECEIVED"

def test_transaction_validation():
    assert stock_system("TRANSACTION") == "TRANSACTION VALIDATED"

def test_performance_testing():
    assert stock_system("PERFORMANCE") == "LOW LATENCY PERFORMANCE"