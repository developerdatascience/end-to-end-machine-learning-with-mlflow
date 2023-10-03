from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValiationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline 


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj= DataValiationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj= DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj= ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj= ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e