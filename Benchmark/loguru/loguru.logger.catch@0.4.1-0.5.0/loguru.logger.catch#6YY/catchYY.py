from loguru import logger
logger.catch(reraise=False, message='An exception occurred!', level='ERROR')
