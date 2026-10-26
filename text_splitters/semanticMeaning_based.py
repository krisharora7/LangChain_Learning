from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)
text =sample_text = """
The organic farmers in Punjab implemented a novel crop rotation strategy this season to naturally rejuvenate the nitrogen levels in the soil. By planting legumes immediately following the wheat harvest, they significantly reduced their dependency on synthetic chemical fertilizers while maintaining high crop yields despite erratic monsoon patterns. The local agricultural cooperative expects a record-breaking harvest of premium basmati rice by late autumn. Meanwhile, the national cricket team finalized their intensive training camp ahead of the upcoming boundary-heavy ICC tournament. Analysts are heavily debating whether the selectors should lean into a spin-heavy bowling attack or rely on raw pace to exploit the dry pitch conditions expected during the opening matches of the series. Fans are already queuing up overnight outside the stadium gates just to secure tickets for the highly anticipated weekend clash.

 Far away from sports and entertainment, infantry battalions deployed along the high-altitude mountainous border completed a grueling series of cold-weather combat readiness drills. These specialized tactical operations require soldiers to operate advanced thermal imaging systems and secure strategic vantage points under sub-zero visibility conditions to guarantee absolute territorial defense.
"""
splitter = SemanticChunker(
    embedding_model,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=80
)
result = splitter.split_text(text)
print(len(result))
print(result)