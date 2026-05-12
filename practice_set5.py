# Scenario: Daily pipeline ke liye:

# Input files check karo
# Output folders create karo
# Processed files archive karo
# Old log files delete karo

from pathlib import Path
from datetime import datetime
import shutil

class PipeLineFileManager:

    def __init__(self, base_dir: str):
        # print('constructor load dir')
        self.base_dir = Path(base_dir)
        self.input_dir = self.base_dir / 'input'
        self.output_dir = self.base_dir / 'output'
        self.archive_dir = self.base_dir / 'archive'
        self.log_dir = self.base_dir / 'logs'
    
    def setup_directories(self):
        '''sari required directories'''
        for directory in [self.input_dir, self.output_dir, self.archive_dir, self.log_dir]:
            # print(directory)
            directory.mkdir(parents=True, exist_ok=True)
            print(f'Directory ready : {directory}')


    def get_pending_files(self) -> list:
        '''process hone wali csv files dhundho'''
        csv_files = list(self.input_dir.rglob('*.csv'))
        return csv_files
    
    def archive_processed_file(self, file_path: Path):
        '''process file ko archive me move kro'''
        today = datetime.now().strftime('%Y_%m_%d')
        archive_path = self.archive_dir / today
        archive_path.mkdir(parents=True, exist_ok=True)

        dest = archive_path / file_path.name
        shutil.move(str(file_path), str(dest))
        print(f'Archieve {file_path.name} -> {dest}')



manager = PipeLineFileManager('production/pipeline')

# manager.setup_directories()
files = manager.get_pending_files()
for file in files:
    # process karo...
    manager.archive_processed_file(file)