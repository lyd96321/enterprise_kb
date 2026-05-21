import ffmpeg
import whisper
import tempfile
from adapter.base_adapter import BaseAdapter
from entity.document_entity import DocumentEntity
from common.utils import clean_text, md5_hash
from config.settings import settings

class VideoAdapter(BaseAdapter):
    def __init__(self):
        self.whisper_model = whisper.load_model(settings.WHISPER_MODEL)

    def _video2mp3(self, video_path: str, temp_mp3: str):
        (
            ffmpeg
            .input(video_path)
            .output(temp_mp3, format="mp3", ar=settings.FFMPEG_SAMPLE_RATE)
            .run(overwrite_output=True, quiet=True)
        )

    def parse(self, file_path: str) -> DocumentEntity:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            self._video2mp3(file_path, tmp.name)
            res = self.whisper_model.transcribe(tmp.name, language="zh")
            content = res["text"]
        clean_content = clean_text(content)
        file_id = md5_hash(file_path)
        return DocumentEntity(
            file_id=file_id,
            title=file_path.split("/")[-1],
            raw_content=clean_content,
            file_type="mp4",
            file_path=file_path
        )