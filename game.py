import view

# main function
def main():
    window = view.View(view.const.WIN_WIDTH, view.const.WIN_HEIGHT, view.const.WIN_NAME)

    # game loop
    while window.get_running():
        window.clear()
        window.ui()
        window.check_close()
        window.update()


if __name__ == "__main__":
    main()
