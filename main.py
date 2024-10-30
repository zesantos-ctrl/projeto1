@namespace
class SpriteKind:
    OBJETO = SpriteKind.create()

def on_overlap_tile(sprite, location):
    info.change_life_by(2)
    tiles.set_tile_at(location, sprites.dungeon.dark_ground_south_east1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    info.change_score_by(100)
    tiles.set_tile_at(location2, sprites.dungeon.chest_open)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile2)

def on_b_pressed():
    global tiro
    tiro = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 2 2 . . . . . . . 
                    . . . 2 2 4 4 4 2 2 . . . . . . 
                    . . 2 4 4 5 5 5 4 2 2 2 . . . . 
                    . . 2 2 4 5 5 5 4 4 4 2 . . . . 
                    . . . 2 4 4 4 4 4 4 4 2 . . . . 
                    . . . 2 2 2 2 2 4 2 2 2 . . . . 
                    . . . . . . . 2 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        eu,
        controller.dx(8000),
        controller.dy(8000))
    music.play(music.create_sound_effect(WaveShape.TRIANGLE,
            1194,
            200,
            255,
            0,
            75,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile3(sprite3, location3):
    info.change_score_by(10)
    tiles.set_tile_at(location3, sprites.dungeon.dark_ground_south_east1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile3)

def on_a_pressed():
    if eu.is_hitting_tile(CollisionDirection.BOTTOM):
        eu.vy += -90
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(eu,
        [img("""
                ..............................
                        ..............................
                        ..............................
                        .............11...............
                        ............1.1...............
                        ..............1...............
                        ..............1...............
                        .............111..............
                        ..............................
                        ............ffff..............
                        ..........ff1111ff............
                        .........fb111111bf...........
                        .........f1111111df...........
                        ........fd1111111ddf..........
                        ........fd111111dddf..........
                        ........fd111ddddddf..........
                        ........fd1dfbddddbf..........
                        ........fbddfcdbbbcf..........
                        .........f11111bbcf...........
                        .........f1b1fffff............
                        .........fbfc111bf............
                        ..........ff1b1bff............
                        ...........fbfbfff.f..........
                        ............ffffffff..........
                        ..............fffff...........
                        ..............................
                        ..............................
                        ..............................
                        ..............................
                        ..............................
            """),
            img("""
                ..............................
                        ..............................
                        ............11................
                        ...........1.1................
                        .............1................
                        .............1................
                        .............1................
                        ............111...............
                        ..............................
                        ..........fffff...............
                        .........f11111ff.............
                        ........fb111111bf............
                        ........f1111111dbf...........
                        .......fd111111dddf...........
                        .......fd11111ddddf...........
                        .......fd11dddddddf...........
                        .......f111dddddddf...........
                        .......f11fcddddddf...........
                        ......fb1111bdddbf............
                        ......f1b1bdfcfff.............
                        ......fbfbffffffff............
                        .......fffffffffff.ff.........
                        ............ffffffff..........
                        .........f1b1bffffff..........
                        .........fbfbffffff...........
                        ..............................
                        ..............................
                        ..............................
                        ..............................
                        ..............................
            """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(eu,
        [img("""
                ........................
                        ........................
                        ............11..........
                        ............1.1.........
                        ............1...........
                        ............1...........
                        ...........111..........
                        ........................
                        ..........fffff.........
                        ........ff11111f........
                        .......fb111111bf.......
                        ......fbd1111111f.......
                        ......fddd111111df......
                        ......fdddd11111df......
                        ......fddddddd11df......
                        ......fddddddd111f......
                        ......fddddddcf11f......
                        .......fbdddb1111bf.....
                        ........fffcfdb1b1f.....
                        .......ffffffffbfbf.....
                        ....ff.fffffffffff......
                        .....ffffffff...........
                        .....ffffffb1b1f........
                        ......ffffffbfbf........
            """),
            img("""
                ............11..........
                        ............1.1.........
                        ............1...........
                        ............1...........
                        ...........111..........
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......fd1111111f.......
                        ......fdd1111111df......
                        ......fddd111111df......
                        ......fdddddd111df......
                        ......fbddddbfd1df......
                        ......fcbbbdcfddbf......
                        .......fcbb11111f.......
                        ........fffff1b1f.......
                        ........fb111cfbf.......
                        ........ffb1b1ff........
                        ......f.fffbfbf.........
                        ......ffffffff..........
                        .......fffff............
                        ........................
                        ........................
            """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile4(sprite4, location4):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile5)

def on_on_overlap(sprite6, otherSprite):
    global inimigo
    sprites.destroy(otherSprite)
    index = 0
    while index < 0:
        inimigo = sprites.create(img("""
                . . f f f . . . . . . . . f f f 
                            . f f c c . . . . . . f c b b c 
                            f f c c . . . . . . f c b b c . 
                            f c f c . . . . . . f b c c c . 
                            f f f c c . c c . f c b b c c . 
                            f f c 3 c c 3 c c f b c b b c . 
                            f f b 3 b c 3 b c f b c c b c . 
                            . c b b b b b b c b b c c c . . 
                            . c 1 b b b 1 b b c c c c . . . 
                            c b b b b b b b b b c c . . . . 
                            c b c b b b c b b b b f . . . . 
                            f b 1 f f f 1 b b b b f c . . . 
                            f b b b b b b b b b b f c c . . 
                            . f b b b b b b b b c f . . . . 
                            . . f b b b b b b c f . . . . . 
                            . . . f f f f f f f . . . . . .
            """),
            SpriteKind.enemy)
        inimigo.set_position(112, 31)
        index += 1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_overlap_tile6(sprite7, location6):
    tiles.place_on_random_tile(eu, sprites.dungeon.collectible_insignia)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile6)

tiro: Sprite = None
inimigo: Sprite = None
eu: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level2
"""))
eu = sprites.create(img("""
        ........................
            ........................
            ........................
            ..........11............
            .........1.1............
            ...........1............
            ...........1............
            ...........1............
            ...........1............
            ..........111...........
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
eu.set_stay_in_screen(True)
eu.ay = 120
inimigo = sprites.create(img("""
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c b b b b b b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b c b b b c b b b b f . . . . 
            f b 1 f f f 1 b b b b f c . . . 
            f b b b b b b b b b b f c c . . 
            . f b b b b b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.enemy)
inimigo.follow(eu, 40)
inimigo.set_position(116, 37)
info.set_life(3)
bau = sprites.create(img("""
        c c b b b b b b b b b b b b c c 
            c b e 4 4 4 4 4 4 4 4 4 4 e b c 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e e 4 4 4 4 4 4 4 4 4 4 e e b 
            b e e e e e e e e e e e e e e b 
            b e e e e e e e e e e e e e e b 
            b b b b b b b d d b b b b b b b 
            c b b b b b b c c b b b b b b c 
            c c c c c c b c c b c c c c c c 
            b e e e e e c b b c e e e e e b 
            b e e e e e e e e e e e e e e b 
            b c e e e e e e e e e e e e c b 
            b b b b b b b b b b b b b b b b 
            c b b c c c c c c c c c c b b c
    """),
    SpriteKind.OBJETO)
tiles.place_on_random_tile(eu, sprites.dungeon.stair_east)
controller.move_sprite(eu, 100, 0)
tiles.place_on_random_tile(bau, sprites.dungeon.chest_open)
scene.camera_follow_sprite(eu)
animation.run_image_animation(inimigo,
    [img("""
            . . f f f . . . . . . . . f f f 
                . f f c c . . . . . . f c b b c 
                f f c c . . . . . . f c b b c . 
                f c f c . . . . . . f b c c c . 
                f f f c c . c c . f c b b c c . 
                f f c 3 c c 3 c c f b c b b c . 
                f f b 3 b c 3 b c f b c c b c . 
                . c 1 b b b 1 b c b b c c c . . 
                . c 1 b b b 1 b b c c c c . . . 
                c b b b b b b b b b c c . . . . 
                c b 1 f f 1 c b b b b f . . . . 
                f f 1 f f 1 f b b b b f c . . . 
                f f 2 2 2 2 f b b b b f c c . . 
                . f 2 2 2 2 b b b b c f . . . . 
                . . f b b b b b b c f . . . . . 
                . . . f f f f f f f . . . . . .
        """),
        img("""
            . . f f f . . . . . . . . . . . 
                f f f c c . . . . . . . . f f f 
                f f c c c . c c . . . f c b b c 
                f f c 3 c c 3 c c f f b b b c . 
                f f c 3 b c 3 b c f b b c c c . 
                f c b b b b b b c f b c b c c . 
                c c 1 b b b 1 b c b b c b b c . 
                c b b b b b b b b b c c c b c . 
                c b 1 f f 1 c b b c c c c c . . 
                c f 1 f f 1 f b b b b f c . . . 
                f f f f f f f b b b b f c . . . 
                f f 2 2 2 2 f b b b b f c c . . 
                . f 2 2 2 2 2 b b b c f . . . . 
                . . f 2 2 2 b b b c f . . . . . 
                . . . f f f f f f f . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . c c . c c . . . . . . . . 
                . . f 3 c c 3 c c c . . . . . . 
                . f c 3 b c 3 b c c c . . . . . 
                f c b b b b b b b b f f . . . . 
                c c 1 b b b 1 b b b f f . . . . 
                c b b b b b b b b c f f f . . . 
                c b 1 f f 1 c b b f f f f . . . 
                f f 1 f f 1 f b c c b b b . . . 
                f f f f f f f b f c c c c . . . 
                f f 2 2 2 2 f b f b b c c c . . 
                . f 2 2 2 2 2 b c c b b c . . . 
                . . f 2 2 2 b f f c c b b c . . 
                . . . f f f f f f f c c c c c . 
                . . . . . . . . . . . . c c c c
        """),
        img("""
            . f f f . . . . . . . . f f f . 
                f f c . . . . . . . f c b b c . 
                f c c . . . . . . f c b b c . . 
                c f . . . . . . . f b c c c . . 
                c f f . . . . . f f b b c c . . 
                f f f c c . c c f b c b b c . . 
                f f f c c c c c f b c c b c . . 
                . f c 3 c c 3 b c b c c c . . . 
                . c b 3 b c 3 b b c c c c . . . 
                c c b b b b b b b b c c . . . . 
                c 1 1 b b b 1 1 b b b f c . . . 
                f b b b b b b b b b b f c c . . 
                f b c b b b c b b b b f . . . . 
                . f 1 f f f 1 b b b c f . . . . 
                . . f b b b b b b c f . . . . . 
                . . . f f f f f f f . . . . . .
        """),
        img("""
            . f f f . . . . . . . . f f f . 
                . c b b c f . . . . . . . c f f 
                . . c b b c f . . . . . . c c f 
                . . c c c b f . . . . . . . f c 
                . . c c b b f f . . . . . f f c 
                . . c b b c b f c c . c c f f f 
                . . c b c c b f c c c c c f f f 
                . . . c c c b c b 3 c c 3 c f . 
                . . . c c c c b b 3 c b 3 b c . 
                . . . . c c b b b b b b b b c c 
                . . . c f b b b 1 1 b b b 1 1 c 
                . . c c f b b b b b b b b b b f 
                . . . . f b b b b c b b b c b f 
                . . . . f c b b b 1 f f f 1 f . 
                . . . . . f c b b b b b b f . . 
                . . . . . . f f f f f f f . . .
        """),
        img("""
            f f f . . . . . . . . f f f . . 
                c b b c f . . . . . . c c f f . 
                . c b b c f . . . . . . c c f f 
                . c c c b f . . . . . . c f c f 
                . c c b b c f . c c . c c f f f 
                . c b b c b f c c 3 c c 3 c f f 
                . c b c c b f c b 3 c b 3 b f f 
                . . c c c b b c b 1 b b b 1 c . 
                . . . c c c c b b 1 b b b 1 c . 
                . . . . c c b b b b b b b b b c 
                . . . . f b b b b c 1 f f 1 b c 
                . . . c f b b b b f 1 f f 1 f f 
                . . c c f b b b b f 2 2 2 2 f f 
                . . . . f c b b b b 2 2 2 2 f . 
                . . . . . f c b b b b b b f . . 
                . . . . . . f f f f f f f . . .
        """)],
    500,
    True)

def on_forever():
    effects.star_field.start_screen_effect(5000)
forever(on_forever)