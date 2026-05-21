import jieba
from collections import Counter

class TagService:
    INDUSTRY_WORDS = {
        "行政":["制度","流程","审批","公告"],
        "技术":["代码","部署","运维","接口"],
        "财务":["报表","账单","费用","报销"]
    }

    @staticmethod
    def generate_tags(text: str, top_n=5) -> list:
        stop = {"的","了","是","我","你","他","在"}
        words = [w for w in jieba.lcut(text) if len(w)>1 and w not in stop]
        count = Counter(words)
        hot_tags = [x[0] for x in count.most_common(top_n)]
        for industry, keywords in TagService.INDUSTRY_WORDS.items():
            if any(k in text for k in keywords):
                hot_tags.append(industry)
        return list(set(hot_tags))
