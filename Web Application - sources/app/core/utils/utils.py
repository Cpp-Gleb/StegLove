import os
import uuid
import pathlib
import subprocess

from datetime import datetime
from core.config import config
from core.db import sql_connector


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
    
    async def check_session(self, session: str) -> bool:
        try:
            value = await sql_connector.db(f'SELECT id FROM sessions WHERE user_id="{session}"')
            if value in [None, "", "-"]:
                return False
            return True
        except:
            return False
        
    async def check_file_analyze_session(self, user_session: str, analyze_session: str) -> bool:
        try:
            value = await sql_connector.db(f'SELECT result FROM analyzes WHERE id="{analyze_session}" AND user_id="{user_session}"')
            if value in [None, "", "-"]:
                return False
            return True
        except:
            return False
        
    async def get_analyze_results(self, user_session: str, analyze_session: str) -> dict | None:
        try:
            result1 = await sql_connector.db(f'SELECT result, tool FROM analyzes WHERE id="{analyze_session}" AND user_id="{user_session}"')
            result2 = await sql_connector.db(f'SELECT result2, tool FROM analyzes WHERE id="{analyze_session}" AND user_id="{user_session}"')
            return [result1, result2]
        except:
            return None
        
    async def add_analyze_results(self, result: dict, user_session: str) -> None:
        try:
            records_count = await sql_connector.db(f'SELECT COUNT(id) FROM analyzes WHERE user_id="{user_session}"')
            if records_count >= 5:
                mid = await sql_connector.db(f'SELECT MAX(id) FROM analyzes WHERE user_id="{user_session}"')
                await sql_connector.db(f'DELETE FROM analyzes WHERE id={mid} AND user_id="{user_session}"')
            timestamp = str(round(datetime.now().astimezone().timestamp()))
            await sql_connector.db(f'INSERT OR IGNORE INTO analyzes (user_id, timestamp, result, result2, tool) VALUES("{user_session}", "{timestamp}", "{result['result']}", "{result['result2']}", "{result['tool']}")')
        except:
            pass

    async def create_session(self, ip: str) -> str | None:
        try:
            idd = await sql_connector.db(f'SELECT MAX(id) FROM sessions')
            idd = idd if idd not in [ None, "" ] else 0
            uid = subprocess.check_output(f"cd core/uuid-generator && ./uuid-list-exe nth {idd}", shell=True, universal_newlines=True)
            await sql_connector.db(f'INSERT OR IGNORE INTO sessions (ip, user_id) VALUES("{ip}", "{uid}")')
            return uid
        except:
            return None
        
    async def get_analyze_sessions(self, session) -> dict | None:
        try:
            sessions = await sql_connector.db(f'SELECT id, tool FROM analyzes WHERE user_id="{session}"', fetchall=True)
            if sessions not in [None, "", "-", []]:
                result = {}
                for analyze_session in sessions:
                    session_id, tool = analyze_session
                    result[session_id] = tool
                new_result = dict(sorted(result.items(), key=lambda x: x[0]))
                return new_result
                    
            return None
        except:
            return None

    async def save_file(self, file: str) -> str | None:
        try:
            data = bytes.fromhex(file)
            name = str(uuid.uuid4().hex)

            current_datetime = datetime.now()
            date = current_datetime.strftime("%Y-%m-%d_%H-%M")
            path = os.path.join(self.temp_folder, f'{name}_{date}')

            with open(path, 'wb') as f:
                f.write(data)

            return path
        except:
            return None

    async def extract_comment(self, text: str) -> str | None:
        try:
            res = text[text.find("Comment") + len("Comment") + 1 : text.find("Image Size")]
            if res and res != '':
                res = res[res.find(":") + 2 :]
                return res
            return None
        except:
            return None

    async def analyze_file(self, tool: str, path: str) -> str:
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

        except:
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

    async def render_template(self, template: str) -> str | None:
        try:
            with open(os.path.join(self.templates_folder, f'{template}.html'), 'r', encoding='utf8') as f:
                file = f.read()
            return file
        except:
            return None
