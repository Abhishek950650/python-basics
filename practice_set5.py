# परिदृश्य: दैनिक पाइपलाइन के लिए:
# Scenario: Daily pipeline ke liye:

# इनपुट फ़ाइलें जांचो / Input files check karo
# आउटपुट फ़ोल्डर बनाओ / Output folders create karo
# संसाधित फ़ाइलें संग्रहीत करो / Processed files archive karo
# पुरानी लॉग फ़ाइलें हटाओ / Old log files delete karo

from pathlib import Path
from datetime import datetime
import shutil
import logging

# लॉगिंग सेटअप करो / Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PipeLineFileManager:

    def __init__(self, base_dir: str):
        # कंस्ट्रक्टर में बेस डायरेक्टरी लोड करो / Load base directory in constructor
        try:
            self.base_dir = Path(base_dir)
            self.input_dir = self.base_dir / 'input'
            self.output_dir = self.base_dir / 'output'
            self.archive_dir = self.base_dir / 'archive'
            self.log_dir = self.base_dir / 'logs'
            logger.info(f"PipeLineFileManager initialized with base_dir: {base_dir}")
        except Exception as e:
            logger.error(f"Error initializing PipeLineFileManager: {e}")
            raise

    def setup_directories(self):
        '''सभी आवश्यक डायरेक्टरी बनाओ / Create all required directories'''
        try:
            for directory in [self.input_dir, self.output_dir, self.archive_dir, self.log_dir]:
                # डायरेक्टरी बनाओ अगर मौजूद नहीं है / Create directory if not exists
                directory.mkdir(parents=True, exist_ok=True)
                logger.info(f'Directory ready : {directory}')
                print(f'Directory ready : {directory}')
        except PermissionError as pe:
            logger.error(f"Permission denied while creating directories: {pe}")
            raise
        except OSError as oe:
            logger.error(f"OS error while creating directories: {oe}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while creating directories: {e}")
            raise


    def get_pending_files(self) -> list:
        '''प्रक्रिया के लिए CSV फ़ाइलें खोजो / Find CSV files for processing'''
        try:
            # इनपुट डायरेक्टरी मौजूद है या नहीं जांचो / Check if input directory exists
            if not self.input_dir.exists():
                logger.warning(f"Input directory does not exist: {self.input_dir}")
                return []

            # सभी CSV फ़ाइलें रिकर्सिवली खोजो / Search CSV files recursively
            csv_files = list(self.input_dir.rglob('*.csv'))
            logger.info(f"Found {len(csv_files)} CSV files in {self.input_dir}")
            return csv_files
        except PermissionError as pe:
            logger.error(f"Permission denied while searching for CSV files: {pe}")
            return []
        except Exception as e:
            logger.error(f"Error while searching for CSV files: {e}")
            return []

    def archive_processed_file(self, file_path: Path):
        '''प्रक्रिया की गई फ़ाइल को संग्रह में स्थानांतरित करो / Move processed file to archive'''
        try:
            # फ़ाइल का अस्तित्व जांचो / Check if file exists
            if not file_path.exists():
                logger.error(f"File does not exist: {file_path}")
                return False

            # आज की तारीख के साथ संग्रह पथ बनाओ / Create archive path with today's date
            today = datetime.now().strftime('%Y_%m_%d')
            archive_path = self.archive_dir / today

            # संग्रह डायरेक्टरी बनाओ / Create archive directory
            archive_path.mkdir(parents=True, exist_ok=True)

            dest = archive_path / file_path.name

            # गंतव्य में पहले से फ़ाइल है तो चेतावनी दो / Warn if file already exists at destination
            if dest.exists():
                logger.warning(f"File already exists at destination, overwriting: {dest}")

            # फ़ाइल को स्थानांतरित करो / Move file to archive
            shutil.move(str(file_path), str(dest))
            logger.info(f'Archived {file_path.name} -> {dest}')
            print(f'Archived {file_path.name} -> {dest}')
            return True

        except PermissionError as pe:
            logger.error(f"Permission denied while archiving file {file_path}: {pe}")
            return False
        except shutil.Error as se:
            logger.error(f"Error moving file {file_path}: {se}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error while archiving file {file_path}: {e}")
            return False


# मुख्य प्रोग्राम / Main program
if __name__ == '__main__':
    try:
        # पाइपलाइन फ़ाइल मैनेजर को इनिशियलाइज करो / Initialize pipeline file manager
        manager = PipeLineFileManager('production/pipeline')

        # अगर आवश्यक हो तो डायरेक्टरी सेटअप करो / Setup directories if needed
        try:
            manager.setup_directories()
        except Exception as setup_error:
            logger.error(f"Could not setup directories: {setup_error}")

        # प्रक्रिया के लिए लंबित फ़ाइलें प्राप्त करो / Get pending files for processing
        files = manager.get_pending_files()

        if not files:
            logger.warning("No CSV files found to process")
            print("No CSV files found to process")
        else:
            # प्रत्येक फ़ाइल को संग्रहीत करो / Archive each file
            for file in files:
                manager.archive_processed_file(file)
            logger.info(f"Successfully processed {len(files)} files")

    except Exception as e:
        logger.error(f"Fatal error in main program: {e}")