from yahoo_finance import Share
import inspect
import Metrics

def process_metric(stock_name):
    metrics = collect_metrics()
    data = Share(stock_name)
    results = [metric(data) for metric in metrics]
    return results
    #images = [make_img(result) for result in results]
    #return images

def collect_metrics():
    return [member[1] for member in inspect.getmembers(Metrics, predicate=inspect.isfunction)]

def make_img(results):
    pass

if __name__ == "__main__":
    import sys
    print(Share("'" + sys.argv[1]).get_name() + "':")
    print(process_metric(sys.argv[1]))
    #print(Metrics.EarningsPerShare(sys.argv[1]))