import gui
import mod_man

if __name__ == "__main__":
    modules, manifests = mod_man.load_modules()

    # separate args sets from manifests
    args_sets = {entry['name']: entry['args'] for entry in manifests.values()}

    gui.start(modules, args_sets)
