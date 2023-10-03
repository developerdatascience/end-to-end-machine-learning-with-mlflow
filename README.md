# end-to-end-machine-learning-with-mlOps
End to End Machine Learning with  MLOPS


1. Install MLflow and DagsHub client
    pip3 install mlflow dagshub


2. Set DagsHub to track experiments with MLFlow
    import dagshub
    import mlflow

    dagshub.init("my-first-repo", "developerdatascience", mlflow=True)
    mlflow.start_run()


    mlflow.log_param("parameter name ", "value")
    mlflow.log_metric("metric name", 1)

    mlflow.end_run()


MLFlow Tracking remote:
https://dagshub.com/developerdatascience/end-to-end-machine-learning-with-mlflow.mlflow

Using MLFLOW Tracking:
MLFLOW_TRACKING_URI=https://dagshub.com/developerdatascience/end-to-end-machine-learning-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=developerdatascience \
MLFLOW_TRACKING_PASSWORD=3f1565218d6ec2d42985b700ffecee09de158b93 \
python script.py



export MLFLOW_TRACKING_URI=https://dagshub.com/developerdatascience/end-to-end-machine-learning-with-mlflow.mlflow
export MLFLOW_TRACKING_USERNAME=developerdatascience
export MLFLOW_TRACKING_PASSWORD=3f1565218d6ec2d42985b700ffecee09de158b93