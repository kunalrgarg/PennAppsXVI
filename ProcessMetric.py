from yahoo_finance import Share
import inspect

def process_metric(stock_name):
    metrics = collect_metrics()
    data = Share(stock_name)
    results = [metric(data) for metric in metrics]
    images = [make_img(result) for result in results]
    return images

def collect_metrics():
    return [member[1] for member in inspect.members()]

def make_img(results):
