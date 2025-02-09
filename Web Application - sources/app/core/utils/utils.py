import os
import uuid
import time
import asyncio
import pathlib
import subprocess
from datetime import datetime

from core.config import config


class Utils:
    def __init__(self):
        self.temp_folder = config.temp_folder.get_secret_value()
        self.templates_folder = config.templates_folder.get_secret_value()
    
    async def remove_pycache(self) -> None:
        try:
            [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]') if '.venv' not in p.parts]
            [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__') if '.venv' not in p.parts]
        except:
            pass
    
    async def save_file(self, file):
        data = bytes.fromhex(file)
        name = str(uuid.uuid4().hex)

        current_datetime = datetime.now()
        date = current_datetime.strftime("%Y-%m-%d_%H-%M")
        path = os.path.join(self.temp_folder, f'{name}_{date}')

        with open(path, 'wb') as f:
            f.write(data)

        return path

    async def extract_comment(self, text):
        try:
            res = text[text.find("Comment") + len("Comment") + 1 : text.find("Image Size")]
            if res and res != '':
                res = res[res.find(":") + 2 :]
                return res
            return None
        except:
            return None

    async def analyze_file(self, tool, path):
        try:
            full_path = os.path.abspath(path)
            result = subprocess.run([tool, full_path], capture_output=True, text=True)
            output = str(result.stdout)
            output2 = output.lower()
            if 'comment' in output2:
                output2 = 'The metadata of a file contains information that may be important. Please check it:' + '\n\n' + str(await self.extract_comment(output))
            else:
                output2 = 'No comments containing sensitive information were found in the file metadata.'

            response = {
                'status': 'ok',
                'tool': tool,
                'result': output,
                'result2': output2
            }

        except Exception as e:
            response = {
                'status': 'error',
                'tool': tool
            }

        finally:
            try:
                os.remove(full_path)
            except:
                pass

        return response

    async def render_template(self, template):
        with open(os.path.join(self.templates_folder, f'{template}.html'), 'r', encoding='utf8') as f:
            file = f.read()
        return file
