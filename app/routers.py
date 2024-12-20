from fastapi import APIRouter
from modules.v1.health import routers as health_routers
from modules.v1.tasks import routers as tasks_routers
from modules.v1.games import routers as games_routers
from modules.v1.games import socket as games_socket
from modules.v1.moves import routers as moves_routers
from modules.v1.histories import routers as histories_routers
from users import routers as users_routers
from modules.v1.leaderboard import routers as leaderboard_routers

api_routers = APIRouter()

# Healthy check
api_routers.include_router(health_routers.router)

# Users
api_routers.include_router(users_routers.router)

# Modules
api_routers.include_router(tasks_routers.router)

# Modules
api_routers.include_router(games_routers.router)
api_routers.include_router(games_socket.router)


# Modules
api_routers.include_router(moves_routers.router)

# Modules
api_routers.include_router(histories_routers.router)

# Modules
api_routers.include_router(leaderboard_routers.router)