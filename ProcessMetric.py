from yahoo_finance import Share
import inspect
import Metrics

def process_metric(stock_name):
    metrics = collect_metrics()
    data = Share(stock_name)
    results = [metric(data) for metric in metrics]
    images = [make_img(result) for result in results]
    return images

def collect_metrics():
    return [member[1] for member in inspect.getmembers(Metrics, predicate=inspect.ismethod())]

def make_img(results):
    pass