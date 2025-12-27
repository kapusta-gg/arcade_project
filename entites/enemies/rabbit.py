from entites.enemies.enemy_interface import EnemyInterface


class Rabbit(EnemyInterface):
    IMAGE_PATH_WALK = ["source/PNG/Enemies/Tiles/tile_0007.png",
                       "source/PNG/Enemies/Tiles/tile_0009.png", "source/PNG/Enemies/Tiles/tile_0010.png"]
    SPEED = 40
    TIMER_WALK_ANIM = 0.1
