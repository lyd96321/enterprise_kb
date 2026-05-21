import re
class CleanStrategy:
    @staticmethod
    def deep_clean(text: str) -> str:
        text = re.sub(r"第[\d]+页/共[\d]+页", "", text)
        text = re.sub(r"©.*?版权所有", "", text)
        text = re.sub(r"www\..*?.com", "", text)
        text = re.sub(r"[-=]{5,}", "", text)
        return text.strip()