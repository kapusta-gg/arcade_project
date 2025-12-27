from entites.enemies.enemy_interface import EnemyInterface


class Bigrabbit(EnemyInterface):
    IMAGE_PATH_WALK = ["source/PNG/Enemies/Tiles/tile_0012.png",
                       "source/PNG/Enemies/Tiles/tile_0013.png", "source/PNG/Enemies/Tiles/tile_0014.png"]
    SPEED = 40
    TIMER_WALK_ANIM = 0.1
