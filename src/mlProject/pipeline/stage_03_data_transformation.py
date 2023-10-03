from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self) -> None:
        try:
            with open(Path("artifacts/data_validation/status.txt")) as f:
                status = f.read().split(" ")[-1]

            if status != "True":
                raise Exception("Your data schema is not valid")
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config= data_transformation_config)
            data_transformation.train_test_split()
        except Exception as e:
            logger.exception(e)
            raise e
    

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
