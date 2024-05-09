from main import app
from . import IndicesRouter, DocumentsRouter, SearchRouter

app.include_router(IndicesRouter.router, prefix='/elastic/indices', tags=['Elastic/Indices'])
app.include_router(DocumentsRouter.router, prefix='/elastic/documents', tags=['Elastic/Documents'])
app.include_router(SearchRouter.router, prefix='/elastic/search', tags=['Elastic/Search'])
