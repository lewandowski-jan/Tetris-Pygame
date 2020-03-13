import view


def main():
    window = view.View(view.const.WIN_WIDTH, view.const.WIN_HEIGHT, view.const.WIN_NAME)

    while window.get_running():
        window.clear()
        window.check_events()
        window.update()



if __name__ == "__main__":
    main()
