from datadog import initialize, statsd

# Initialize DogStatsD client
options = {
    'statsd_host': '127.0.0.1',  # DogStatsD server
    'statsd_port': 8125          # DogStatsD port
}

initialize(**options)

# Increment a counter
statsd.increment('custom.metric.counter')

# Record a gauge
statsd.gauge('custom.metric.gauge', 42)

# Record a histogram
statsd.histogram('custom.metric.histogram', 1.23)

print("Metrics sent successfully!")
