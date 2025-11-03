import os

from dotenv import load_dotenv
from pydantic_core import ValidationError

load_dotenv()

CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.dirname(CURRENT_DIR)

DAL_PATH = os.path.join(APP_DIR, os.getenv('DAL_PATH', 'app/dal'))
SERVICES_PATH = os.path.join(APP_DIR, os.getenv('SERVICES_PATH', 'app/services'))

def find_file(name, path):
    found_file = None
    extension = ".py" # Пускай остается,
                      # на случай если потребуется переиспользовать
                      # поиск файлов, можно будет создать ENUM и искать файл

    if path == DAL_PATH:
        filename = f"{name}_dal"
    elif path == SERVICES_PATH:
        filename = f"{name}_service"
    else:
        return -1

    if filename is not None:
        filename = filename + extension

        for root, dirs, files in os.walk(path):
            if filename in files:
                found_file = os.path.join(root, filename)
                break

    return found_file

def select_dal(name: str):
    """Accepts the name of an entity or interaction object from DAL;
    var name must match: <name>_dal
    :return: Type"""

    dal_class  =  find_file(name, DAL_PATH)

    return dal_class

def select_service(name: str):
    """Accepts the name of an entity or interaction object from Services BLL;
    var name must match: <name>_service
    :return: Type"""

    service_class = find_file(name, SERVICES_PATH)

    return service_class

def get_layers_from_utils(name: str):
    service_class = select_service(name)
    dal_class = select_dal(name)

    if service_class is None or dal_class is None:
        # if anyone entity is not founded return -1 code
        # because is error
        return -1, -1

    return service_class, dal_class

def build_response(**kwargs) -> dict:
    """Создает JSON ответ, исключая None значения"""
    return {k: v for k, v in kwargs.items() if v is not None}

def pydantic_errors(validation_error: ValidationError):
    """Formate pydantic e.errors() return to comfort"""
    errors = {}

    for error in validation_error.errors():
        field = error["loc"][0]
        errors[field] = error["msg"]

    return errors






