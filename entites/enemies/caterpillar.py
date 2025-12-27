from entites.enemies.enemy_interface import EnemyInterface


class Caterpillar(EnemyInterface):
    IMAGE_PATH_WALK = ["source/PNG/Enemies/Tiles/tile_0000.png",
                       "source/PNG/Enemies/Tiles/tile_0001.png", "source/PNG/Enemies/Tiles/tile_0002.png"]
    SPEED = 40
    TIMER_WALK_ANIM = 0.1
