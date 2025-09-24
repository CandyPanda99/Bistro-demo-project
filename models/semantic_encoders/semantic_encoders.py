import os

from semantic_router import SemanticRouter
from semantic_router.encoders import CohereEncoder, OpenAIEncoder

from utils.routes import routes

encoder_type = os.getenv("ENCODER_TYPE", "openai")

encoder = None
if encoder_type == "cohere":
    encoder = CohereEncoder(
        name="embed-english-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY"),
    )
else:
    encoder = OpenAIEncoder(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_base_url=os.getenv("OPENAI_MODEL_ENDPOINT")
    )

router = SemanticRouter(encoder=encoder, routes=routes, auto_sync="local")