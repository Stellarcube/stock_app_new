# Contains the validation logic:

def valid_interval(duration, time_period_duration, time_period_interval):
    return [
        k for k, v in time_period_interval.items() 
        if v < time_period_duration[duration]
    ]
