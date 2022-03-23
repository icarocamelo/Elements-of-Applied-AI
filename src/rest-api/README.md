## REST API
> REST API written in Python/Flask that forecasts CPU usage from dataset

### Curl request
```
{
 "dataset": "http://github.com/your_repo/dataset/dummy-dataset.csv",
 "start_date": "2016-01-01",
 "end_date": "2020-12-31"
}
```
### API call to forecast values
```\
curl -X POST http://localhost:5000/forecast
   -H 'Content-Type: application/json'
   -d '{
 "dataset": "http://github.com/your_repo/dataset/dummy-dataset.csv",
 "start_date": "2016-01-01",
 "end_date": "2020-12-31"
}'
```

### API response
```\
"DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04', '2016-01-05', '2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10', ... '2020-12-22', '2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26', '2020-12-27', '2020-12-28', '2020-12-29', '2020-12-30', '2020-12-31'], dtype='datetime64[ns]', length=1827, freq='D')"}'
```