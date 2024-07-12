from aiogram import Router

import handlers.user_commands
import handlers.business_messages


def setup_routers() -> Router:
    router = Router()

    router.include_router(handlers.user_commands.router)
    router.include_router(handlers.business_messages.router)
    return router
