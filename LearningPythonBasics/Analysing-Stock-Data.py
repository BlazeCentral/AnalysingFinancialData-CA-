from math import log, sqrt


# Calculate Log Return
def calculate_log_return(start_price, end_price):
  return log(end_price / start_price)


# Calculate Variance
def calculate_variance(dataset):
  mean = sum(dataset) / len(dataset)

  numerator = 0

  for data in dataset:
    numerator += (data - mean) ** 2

  return numerator / len(dataset)


# Calculate Standard Deviation
def calculate_stddev(dataset):
  variance = calculate_variance(dataset)
  return sqrt(variance)


# Calculate Correlation Coefficient
def calculate_correlation(set_x, set_y):
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])

  n = len(set_x)

  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# rate of return
def get_returns(prices):
  returns = []
  for i in range(len(prices) - 2):
    start_price = prices[i]
    end_price = prices[i + 1]
    x = calculate_log_return(start_price, end_price)
    returns.append(x)
  return returns

# calculate stock return as %
amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

amazon_returns_per = [display_as_percentage(amazon_returns[i]) for i in range(len(amazon_returns))]
ebay_returns_per = [display_as_percentage(ebay_returns[i]) for i in range(len(ebay_returns))]

print(amazon_returns_per)
print(ebay_returns_per)

# annual error
annual_amazon = sum(float(value) for value in amazon_returns)
print('The annual return of amazon is', display_as_percentage(annual_amazon))
annual_ebay = sum(float(value) for value in ebay_returns)
print('The annual return of ebay is', display_as_percentage(annual_ebay))

# var
am_var = calculate_variance(amazon_returns)
print('The variance of amazon is', am_var)
eb_var = calculate_variance(ebay_returns)
print('The variance of amazon is', eb_var)

# std
am_std = calculate_stddev(amazon_returns)
print('The std of amazon is', display_as_percentage(am_std))
eb_std = calculate_stddev(ebay_returns)
print('The std of ebay is', display_as_percentage(eb_std))

# correllation
corx = calculate_correlation(amazon_returns, ebay_returns)
print('The correlation between Ebay and Amazon is ', corx)
