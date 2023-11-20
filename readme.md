# Cake study

Example tests with reporting to Qase.io using
[qase-pytest](https://github.com/qase-tms/qase-python/tree/master/qase-pytest)

Initialize a virtual environment and install dependencies

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To enable reporting to Qase.io, 
1.  Setup Pytest application and get an API key: https://app.qase.io/apps.
2.  Run pytest, providing the API key:

    ```bash
    pytest --qase-testops-api-token=<insert API key>
    ```

If the key is correct, pytest report will start with the following message:

```log
[Qase] TestOps: created test run https://app.qase.io/run/CAKES/dashboard/<run id>
```
