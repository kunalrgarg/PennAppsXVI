from yahoo_finance import Share

def process_metric(stock_name):
    data = Share(stock_name)
    results = [metric(data) for metric in metrics]
    images = [make_img(result) for result in results]
    return images

def make_img(results):
