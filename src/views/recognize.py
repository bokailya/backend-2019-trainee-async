from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import response_schema

from integrations import GoogleSpeechToText
from schemas import RecognizeResponseSchema


@docs(
    tags=['Speech-To-Text'],
    summary='Распознать речь',
    description='Распознование речи через Google Speech-To-Text',
)
@response_schema(RecognizeResponseSchema)
async def recognize(request):
    """Распознать речь"""
    responce = await GoogleSpeechToText.recognize(await request.read(), request.app['persistent_session'])
    return web.json_response(dict(recognizedText=responce,))