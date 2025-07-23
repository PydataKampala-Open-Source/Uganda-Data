# 2021 Presidential Election Polling Station Results


## Option 1: Read data using polars
```bash
pip install polars
```

```python
import polars as pl

data = pl.read_parquet("polling-station-results.parquet")
```

## Option 2: Read data using polars

```bash
pip install "pandas[pyarrow]"
```

```python
import pandas as pd

data = pd.read_parquet("polling-station-results.parquet")
```
