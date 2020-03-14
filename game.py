import view
import pygame as pg
import const

clock = pg.time.Clock()


# main function
def main():
    window = view.View(view.const.WIN_WIDTH, view.const.WIN_HEIGHT, view.const.WIN_NAME)

    # game loop
    while window.get_running():
        clock.tick(const.FPS)
        window.clear()
        window.ui()
        window.check_events()
        window.draw_shapes()
        window.update()


if __name__ == "__main__":
    main()
