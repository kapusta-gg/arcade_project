from entites.enemies.enemy_interface import EnemyInterface


class Butterfly(EnemyInterface):
    IMAGE_PATH_WALK = ["source/PNG/Enemies/Tiles/tile_0004.png",
                       "source/PNG/Enemies/Tiles/tile_0005.png", "source/PNG/Enemies/Tiles/tile_0006.png"]
    SPEED = 40
    TIMER_WALK_ANIM = 0.1
